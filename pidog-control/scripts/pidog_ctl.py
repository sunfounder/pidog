#!/usr/bin/env python3
import argparse
import importlib
import json
import os
import shutil
import signal
import socket
import subprocess
import sys
import time
from pathlib import Path

EXPECTED_DIRS = [
    Path.home() / "pidog",
    Path.home() / "robot-hat",
    Path.home() / "vilib",
]

STATE_DIR = Path.home() / ".openclaw" / "pidog-control"
HOLD_PID_FILE = STATE_DIR / "hold.pid"
DAEMON_PID_FILE = STATE_DIR / "controller.pid"
SOCKET_PATH = STATE_DIR / "controller.sock"
LOG_FILE = STATE_DIR / "controller.log"

COLOR_MAP = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 255),
    "pink": (255, 0, 128),
    "cyan": (0, 255, 255),
    "white": (255, 255, 255),
    "orange": (255, 128, 0),
    "black": (0, 0, 0),
    "off": (0, 0, 0),
}

ACTION_MAP = {
    "stand": "stand",
    "sit": "sit",
    "lie": "lie",
    "wag-tail": "wag_tail",
    "forward": "forward",
    "backward": "backward",
    "turn-left": "turn_left",
    "turn-right": "turn_right",
}

DEFAULT_BARK_SOUND = "single_bark_1"

LIGHT_MODE_MAP = {
    "off": ("breath", (0, 0, 0), 0.5, 0.0),
    "solid": ("boom", None, 1.0, 0.8),
    "breath": ("breath", None, 1.0, 0.8),
    "listen": ("listen", None, 0.6, 0.8),
    "boom": ("boom", None, 1.0, 0.8),
}

EXPERIMENTAL_LIGHT_MODES = {"solid"}


class PiDogRuntime:
    def __init__(self, controller_mode=False, lazy=False):
        self.module = None
        self.cls = None
        self.instance = None
        self.import_error = None
        self.controller_mode = controller_mode
        self.lazy = lazy
        if not self.lazy:
            self._load()

    def _load(self):
        try:
            mod = importlib.import_module("pidog")
            cls = getattr(mod, "Pidog", None)
            if cls is None:
                raise AttributeError("pidog.Pidog not found")
            self.module = mod
            self.cls = cls
        except Exception as exc:
            self.import_error = exc

    @property
    def available(self):
        if self.cls is None and self.import_error is None:
            self._load()
        return self.cls is not None

    def connect(self, *, head_init_angles=None):
        if not self.available:
            raise RuntimeError(f"PiDog Python module unavailable: {self.import_error}")
        if self.instance is None:
            kwargs = {}
            if head_init_angles is not None:
                kwargs["head_init_angles"] = head_init_angles
            if self.controller_mode:
                original_sensory = getattr(self.cls, "sensory_process_start", None)
                original_close = getattr(self.cls, "close", None)

                def patched_sensory_process_start(_self):
                    _self.sensory_process = None
                    return None

                def patched_close(_self):
                    try:
                        _self.close_all_thread()
                    except Exception:
                        pass
                    try:
                        if hasattr(_self, 'dual_touch') and _self.dual_touch:
                            _self.dual_touch.close()
                    except Exception:
                        pass
                    try:
                        if hasattr(_self, 'ears') and _self.ears:
                            _self.ears.close()
                    except Exception:
                        pass
                    try:
                        if hasattr(_self, 'legs_thread'):
                            _self.legs_thread.join(timeout=1)
                    except Exception:
                        pass
                    try:
                        if hasattr(_self, 'head_thread'):
                            _self.head_thread.join(timeout=1)
                    except Exception:
                        pass
                    try:
                        if hasattr(_self, 'tail_thread'):
                            _self.tail_thread.join(timeout=1)
                    except Exception:
                        pass
                    try:
                        if hasattr(_self, 'rgb_thread_run'):
                            _self.rgb_thread_run = False
                        if hasattr(_self, 'rgb_strip_thread'):
                            _self.rgb_strip_thread.join(timeout=1)
                        if hasattr(_self, 'rgb_strip') and _self.rgb_strip:
                            _self.rgb_strip.close()
                    except Exception:
                        pass
                    try:
                        if hasattr(_self, 'imu_thread'):
                            _self.imu_thread.join(timeout=1)
                    except Exception:
                        pass

                try:
                    if original_sensory is not None:
                        setattr(self.cls, "sensory_process_start", patched_sensory_process_start)
                    if original_close is not None:
                        setattr(self.cls, "close", patched_close)
                    self.instance = self.cls(**kwargs)
                finally:
                    if original_sensory is not None:
                        setattr(self.cls, "sensory_process_start", original_sensory)
                    if original_close is not None:
                        setattr(self.cls, "close", original_close)
            else:
                self.instance = self.cls(**kwargs)
        return self.instance

    def close(self):
        if self.instance is None:
            return
        try:
            self.instance.close()
        except Exception:
            pass

    def release(self):
        self.instance = None


def parse_color(value):
    value = value.strip().lower()
    if value in COLOR_MAP:
        return COLOR_MAP[value]
    if value.startswith("#"):
        value = value[1:]
    if len(value) == 6:
        try:
            return tuple(int(value[i:i+2], 16) for i in (0, 2, 4))
        except ValueError:
            pass
    raise argparse.ArgumentTypeError("Color must be a known name or hex like #00aaff")


def json_ready(obj):
    if isinstance(obj, tuple):
        return list(obj)
    if isinstance(obj, dict):
        return {k: json_ready(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [json_ready(v) for v in obj]
    return obj


def print_expected_dirs():
    for p in EXPECTED_DIRS:
        print(f"path:{p}={'yes' if p.exists() else 'no'}")


def ensure_state_dir():
    STATE_DIR.mkdir(parents=True, exist_ok=True)


def read_pid(path):
    try:
        return int(path.read_text().strip())
    except Exception:
        return None


def write_pid(path, pid):
    ensure_state_dir()
    path.write_text(str(pid))


def clear_pid(path):
    try:
        path.unlink()
    except FileNotFoundError:
        pass


def read_hold_pid():
    return read_pid(HOLD_PID_FILE)


def write_hold_pid(pid):
    write_pid(HOLD_PID_FILE, pid)


def clear_hold_pid():
    clear_pid(HOLD_PID_FILE)


def read_daemon_pid():
    return read_pid(DAEMON_PID_FILE)


def write_daemon_pid(pid):
    write_pid(DAEMON_PID_FILE, pid)


def clear_daemon_pid():
    clear_pid(DAEMON_PID_FILE)


def pid_alive(pid):
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def daemon_running():
    pid = read_daemon_pid()
    return bool(pid and pid_alive(pid))


def stop_previous_hold(timeout=5.0):
    pid = read_hold_pid()
    if not pid:
        return False, "no previous hold pid"
    if pid == os.getpid():
        return False, "current process already owns hold pid"
    if not pid_alive(pid):
        clear_hold_pid()
        return False, "stale hold pid removed"
    os.kill(pid, signal.SIGTERM)
    deadline = time.time() + timeout
    while time.time() < deadline:
        if not pid_alive(pid):
            clear_hold_pid()
            return True, f"stopped previous hold pid {pid}"
        time.sleep(0.1)
    return False, f"previous hold pid {pid} did not exit after SIGTERM"


class PiDogController:
    def __init__(self):
        self.runtime = PiDogRuntime(controller_mode=True, lazy=True)
        self.started_at = time.time()
        self.request_count = 0
        self.current_posture = None
        self.last_action = None
        self.last_light = None
        self.should_stop = False
        self.server = None

    def close(self):
        self.runtime.close()
        if self.server is not None:
            try:
                self.server.close()
            except Exception:
                pass
        try:
            SOCKET_PATH.unlink()
        except FileNotFoundError:
            pass
        clear_daemon_pid()

    def _connect(self):
        return self.runtime.connect()

    def action(self, name, speed=60, hold=False):
        dog = self._connect()
        if name == "bark":
            result = dog.speak(DEFAULT_BARK_SOUND)
            if result is False:
                raise RuntimeError(f"PiDog sound '{DEFAULT_BARK_SOUND}' was not found in the installed sounds directory")
            self.last_action = {"name": name, "speed": speed, "hold": hold, "sound": DEFAULT_BARK_SOUND}
            return {"message": f"action 'bark' ok via speak('{DEFAULT_BARK_SOUND}')"}

        action_name = ACTION_MAP[name]
        dog.do_action(action_name, speed=speed)
        self.current_posture = name if hold and name in {"stand", "sit", "lie"} else None
        self.last_action = {"name": name, "mapped": action_name, "speed": speed, "hold": hold}
        return {
            "message": f"action '{name}' dispatched via do_action('{action_name}')",
            "hold": hold,
            "posture": self.current_posture,
            "dispatched": True,
        }

    def light(self, mode, color, bps=None, brightness=None):
        dog = self._connect()
        mode_name, default_color, default_bps, default_brightness = LIGHT_MODE_MAP[mode]
        color = default_color if default_color is not None else color
        bps = bps if bps is not None else default_bps
        brightness = brightness if brightness is not None else default_brightness
        dog.rgb_strip.set_mode(mode_name, color=color, bps=bps, brightness=brightness)
        self.last_light = {
            "mode": mode,
            "mapped": mode_name,
            "color": list(color),
            "bps": bps,
            "brightness": brightness,
        }
        data = {
            "message": f"light '{mode}' ok via rgb_strip.set_mode('{mode_name}', color={list(color)}, bps={bps}, brightness={brightness})",
            "mode": mode,
            "mapped": mode_name,
            "color": list(color),
            "bps": bps,
            "brightness": brightness,
        }
        if mode in EXPERIMENTAL_LIGHT_MODES:
            data["note"] = "experimental mode mapped to tested 'boom' effect"
        return data

    def status(self):
        return {
            "running": True,
            "pid": os.getpid(),
            "socket": str(SOCKET_PATH),
            "uptime_s": round(time.time() - self.started_at, 1),
            "request_count": self.request_count,
            "runtime_available": self.runtime.available,
            "import_error": None if self.runtime.available else str(self.runtime.import_error),
            "connected": self.runtime.instance is not None,
            "current_posture": self.current_posture,
            "last_action": self.last_action,
            "last_light": self.last_light,
        }

    def shutdown(self):
        self.should_stop = True
        return {"message": "shutdown requested"}

    def handle(self, req):
        cmd = req.get("cmd")
        self.request_count += 1
        if cmd == "ping":
            return self.status()
        if cmd == "action":
            return self.action(req["name"], speed=req.get("speed", 60), hold=req.get("hold", False))
        if cmd == "light":
            return self.light(
                req["mode"],
                tuple(req.get("color", COLOR_MAP["white"])),
                bps=req.get("bps"),
                brightness=req.get("brightness"),
            )
        if cmd == "shutdown":
            return self.shutdown()
        raise RuntimeError(f"unknown controller command: {cmd}")

    def serve(self):
        ensure_state_dir()
        if SOCKET_PATH.exists():
            SOCKET_PATH.unlink()
        self.server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server.bind(str(SOCKET_PATH))
        os.chmod(SOCKET_PATH, 0o600)
        self.server.listen(4)
        write_daemon_pid(os.getpid())

        def _handle_signal(signum, frame):
            self.should_stop = True

        signal.signal(signal.SIGTERM, _handle_signal)
        signal.signal(signal.SIGINT, _handle_signal)

        while not self.should_stop:
            try:
                self.server.settimeout(1.0)
                conn, _ = self.server.accept()
            except socket.timeout:
                continue
            except OSError:
                break
            with conn:
                try:
                    raw = conn.recv(65536)
                    req = json.loads(raw.decode("utf-8"))
                    resp = {"ok": True, "data": json_ready(self.handle(req))}
                except Exception as exc:
                    resp = {"ok": False, "error": str(exc)}
                conn.sendall((json.dumps(resp) + "\n").encode("utf-8"))
        self.close()


def controller_request(payload, timeout=5.0):
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect(str(SOCKET_PATH))
        sock.sendall(json.dumps(json_ready(payload)).encode("utf-8"))
        raw = sock.recv(65536)
    finally:
        sock.close()
    if not raw:
        raise RuntimeError("controller returned no data")
    resp = json.loads(raw.decode("utf-8"))
    if not resp.get("ok"):
        raise RuntimeError(resp.get("error", "controller request failed"))
    return resp["data"]


def wait_for_controller(timeout=8.0):
    deadline = time.time() + timeout
    last_error = "controller did not start"
    while time.time() < deadline:
        if SOCKET_PATH.exists():
            try:
                return controller_request({"cmd": "ping"}, timeout=1.0)
            except Exception as exc:
                last_error = str(exc)
        time.sleep(0.2)
    raise RuntimeError(last_error)


def start_controller_process(force_restart=False):
    ensure_state_dir()
    if daemon_running():
        if force_restart:
            stop_controller_process(timeout=8.0)
        else:
            return {"started": False, "message": "controller already running", "pid": read_daemon_pid()}

    try:
        SOCKET_PATH.unlink()
    except FileNotFoundError:
        pass

    with LOG_FILE.open("ab") as log_handle:
        proc = subprocess.Popen(
            [sys.executable, str(Path(__file__).resolve()), "serve"],
            stdin=subprocess.DEVNULL,
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            start_new_session=True,
            close_fds=True,
        )
    status = wait_for_controller()
    return {
        "started": True,
        "message": "controller started",
        "pid": status["pid"],
        "socket": status["socket"],
        "spawn_pid": proc.pid,
    }


def stop_controller_process(timeout=8.0):
    pid = read_daemon_pid()
    if not pid:
        return {"stopped": False, "message": "controller not running"}
    if not pid_alive(pid):
        clear_daemon_pid()
        try:
            SOCKET_PATH.unlink()
        except FileNotFoundError:
            pass
        return {"stopped": False, "message": f"stale controller pid {pid} removed"}

    try:
        result = controller_request({"cmd": "shutdown"}, timeout=2.0)
    except Exception:
        os.kill(pid, signal.SIGTERM)
        result = {"message": "SIGTERM sent to controller"}

    deadline = time.time() + timeout
    while time.time() < deadline:
        if not pid_alive(pid):
            clear_daemon_pid()
            try:
                SOCKET_PATH.unlink()
            except FileNotFoundError:
                pass
            return {"stopped": True, "message": result["message"], "pid": pid}
        time.sleep(0.1)
    return {"stopped": False, "message": f"controller pid {pid} did not exit", "pid": pid}


def print_json_or_text(data):
    print(json.dumps(json_ready(data), ensure_ascii=False, indent=2, sort_keys=True))


def cmd_status(args):
    runtime = PiDogRuntime()
    data = {
        "python": sys.executable,
        "expected_dirs": {str(p): p.exists() for p in EXPECTED_DIRS},
        "runtime_available": runtime.available,
        "import_error": None if runtime.available else str(runtime.import_error),
        "tools": {cmd: bool(shutil.which(cmd)) for cmd in ["espeak", "pico2wave", "aplay"]},
        "controller_pid": read_daemon_pid(),
        "controller_socket": str(SOCKET_PATH),
        "controller_socket_exists": SOCKET_PATH.exists(),
    }
    if daemon_running():
        try:
            data["controller"] = controller_request({"cmd": "ping"}, timeout=1.0)
        except Exception as exc:
            data["controller_error"] = str(exc)
    print_json_or_text(data)


def cmd_safe_test(args):
    runtime = PiDogRuntime()
    if not runtime.available:
        raise SystemExit(f"PiDog runtime unavailable: {runtime.import_error}")
    dog = runtime.connect()
    print("Running safe test: stand -> sit")
    try:
        dog.do_action("stand", speed=60)
        dog.wait_all_done()
        print("stand: ok via do_action('stand')")
        dog.do_action("sit", speed=60)
        dog.wait_all_done()
        print("sit: ok via do_action('sit')")
    finally:
        runtime.close()


def cmd_action(args):
    if daemon_running() and not args.direct:
        payload = {"cmd": "action", "name": args.name, "speed": args.speed, "hold": args.hold}
        print_json_or_text(controller_request(payload))
        return

    if args.hold:
        stopped, note = stop_previous_hold()
        print(f"hold-switch: {note}")
    runtime = PiDogRuntime()
    if not runtime.available:
        raise SystemExit(f"PiDog runtime unavailable: {runtime.import_error}")
    dog = runtime.connect()
    try:
        if args.name == "bark":
            result = dog.speak(DEFAULT_BARK_SOUND)
            if result is False:
                raise SystemExit(f"PiDog sound '{DEFAULT_BARK_SOUND}' was not found in the installed sounds directory")
            print(f"action 'bark' ok via speak('{DEFAULT_BARK_SOUND}')")
            if args.hold:
                print("hold: bark has no persistent posture to keep; leaving runtime active briefly is unnecessary")
            return
        action_name = ACTION_MAP[args.name]
        dog.do_action(action_name, speed=args.speed)
        dog.wait_all_done()
        print(f"action '{args.name}' ok via do_action('{action_name}')")
        if args.hold:
            write_hold_pid(os.getpid())
            print(f"hold: keeping PiDog in '{args.name}' posture; registered hold pid {os.getpid()}")
            runtime.release()
            return
    finally:
        runtime.close()
        if args.hold and read_hold_pid() == os.getpid():
            clear_hold_pid()


def cmd_light(args):
    if daemon_running() and not args.direct:
        payload = {
            "cmd": "light",
            "mode": args.mode,
            "color": list(args.color),
            "bps": args.bps,
            "brightness": args.brightness,
        }
        print_json_or_text(controller_request(payload))
        return

    runtime = PiDogRuntime()
    if not runtime.available:
        raise SystemExit(f"PiDog runtime unavailable: {runtime.import_error}")
    dog = runtime.connect()
    try:
        mode_name, default_color, default_bps, default_brightness = LIGHT_MODE_MAP[args.mode]
        color = default_color if default_color is not None else args.color
        bps = args.bps if args.bps is not None else default_bps
        brightness = args.brightness if args.brightness is not None else default_brightness
        dog.rgb_strip.set_mode(mode_name, color=color, bps=bps, brightness=brightness)
        print(
            f"light '{args.mode}' ok via rgb_strip.set_mode('{mode_name}', color={list(color)}, bps={bps}, brightness={brightness})"
        )
        if args.mode in EXPERIMENTAL_LIGHT_MODES:
            print("note: this light mode is experimental on current PiDog releases and is implemented via the tested 'boom' RGB mode, not a true steady solid mode")
    finally:
        runtime.close()


def cmd_say(args):
    runtime = PiDogRuntime()
    if runtime.available:
        dog = runtime.connect()
        try:
            result = dog.speak(args.name, volume=args.volume)
            if result is False:
                raise SystemExit(f"PiDog sound '{args.name}' was not found in the installed sounds directory")
            print(f"spoken via dog.speak('{args.name}', volume={args.volume})")
            return
        finally:
            runtime.close()

    if shutil.which("espeak"):
        subprocess.run(["espeak", args.name], check=True)
        print("spoken via espeak fallback")
        return

    if shutil.which("pico2wave") and shutil.which("aplay"):
        wav = "/tmp/pidog_tts.wav"
        subprocess.run(["pico2wave", "-w", wav, args.name], check=True)
        subprocess.run(["aplay", wav], check=True)
        print("spoken via pico2wave fallback")
        return

    print(args.name)
    raise SystemExit("No PiDog runtime or local TTS backend found")


def cmd_demo(args):
    path = Path(args.path).expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"Demo file not found: {path}")
    if path.suffix != ".py":
        raise SystemExit("Demo path must be a .py file")
    proc = subprocess.run([sys.executable, str(path)])
    raise SystemExit(proc.returncode)


def cmd_start(args):
    print_json_or_text(start_controller_process(force_restart=args.force))


def cmd_stop(args):
    print_json_or_text(stop_controller_process())


def cmd_send_action(args):
    print_json_or_text(
        controller_request({"cmd": "action", "name": args.name, "speed": args.speed, "hold": args.hold})
    )


def cmd_send_light(args):
    print_json_or_text(
        controller_request(
            {
                "cmd": "light",
                "mode": args.mode,
                "color": list(args.color),
                "bps": args.bps,
                "brightness": args.brightness,
            }
        )
    )


def cmd_serve(args):
    controller = PiDogController()
    if not controller.runtime.available:
        raise SystemExit(f"PiDog runtime unavailable: {controller.runtime.import_error}")
    controller.serve()


def main():
    parser = argparse.ArgumentParser(description="Generic PiDog V2 control helper")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("status", help="Inspect PiDog runtime and controller status")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("start", help="Start the persistent PiDog controller")
    p.add_argument("--force", action="store_true", help="Restart the controller if already running")
    p.set_defaults(func=cmd_start)

    p = sub.add_parser("stop", help="Stop the persistent PiDog controller")
    p.set_defaults(func=cmd_stop)

    p = sub.add_parser("send-action", help="Send an action to the persistent controller")
    p.add_argument("name", choices=["stand", "sit", "lie", "bark", "wag-tail", "forward", "backward", "turn-left", "turn-right"])
    p.add_argument("--speed", type=int, default=60)
    p.add_argument("--hold", action="store_true")
    p.set_defaults(func=cmd_send_action)

    p = sub.add_parser("send-light", help="Send a light command to the persistent controller")
    p.add_argument("mode", choices=["off", "solid", "breath", "listen", "boom"])
    p.add_argument("--color", type=parse_color, default=COLOR_MAP["white"])
    p.add_argument("--bps", type=float)
    p.add_argument("--brightness", type=float)
    p.set_defaults(func=cmd_send_light)

    p = sub.add_parser("serve", help="Run the persistent PiDog controller server")
    p.set_defaults(func=cmd_serve)

    p = sub.add_parser("safe-test", help="Run a minimal stand/sit motion test")
    p.set_defaults(func=cmd_safe_test)

    p = sub.add_parser("action", help="Run a named basic action (uses controller if running unless --direct)")
    p.add_argument("name", choices=["stand", "sit", "lie", "bark", "wag-tail", "forward", "backward", "turn-left", "turn-right"])
    p.add_argument("--speed", type=int, default=60)
    p.add_argument("--hold", action="store_true", help="Keep the resulting posture instead of calling close() at the end")
    p.add_argument("--direct", action="store_true", help="Bypass the persistent controller and talk to hardware directly")
    p.set_defaults(func=cmd_action)

    p = sub.add_parser("light", help="Control the light board (uses controller if running unless --direct)")
    p.add_argument("mode", choices=["off", "solid", "breath", "listen", "boom"])
    p.add_argument("--color", type=parse_color, default=COLOR_MAP["white"])
    p.add_argument("--bps", type=float)
    p.add_argument("--brightness", type=float)
    p.add_argument("--direct", action="store_true", help="Bypass the persistent controller and talk to hardware directly")
    p.set_defaults(func=cmd_light)

    p = sub.add_parser("say", help="Play a PiDog sound name or fallback local TTS")
    p.add_argument("name")
    p.add_argument("--volume", type=int, default=80)
    p.set_defaults(func=cmd_say)

    p = sub.add_parser("demo", help="Run an installed PiDog demo .py file")
    p.add_argument("path")
    p.set_defaults(func=cmd_demo)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
