# `pidog/pidog.py` — Detailed Documentation

This document explains `pidog/pidog.py` in depth: every module-level construct,
every attribute and method of the `Pidog` class, the threading/IPC model, the
kinematics maths, and the sharp edges / latent bugs in the current
implementation.

Companion document: [`action_flow.md`](./action_flow.md), which documents the
behaviour scheduler layered on top of this driver.

---

## 1. Purpose and place in the codebase

`pidog.py` defines **`Pidog`** — the *hardware abstraction layer* for the
SunFounder Pidog robot. It is the single object that owns every peripheral and
every background thread, and it is what every other module in the package is
ultimately talking to.

```
examples/*.py, pidog-control            <- applications
        |
        v
pidog/action_flow.py (ActionFlow)       <- named behaviours, queueing, postures
        |
        v
pidog/preset_actions.py                 <- composite animations (bark, stretch, …)
        |
        v
pidog/pidog.py  (Pidog)   <<< THIS FILE >>>
   |     |        |
   |     |        +-- pidog/actions_dictionary.py (ActionDict) -> walk.py / trot.py
   |     |                 raw joint-angle frames per named action
   |     +-- pidog/sh3001.py (IMU), rgb_strip.py, sound_direction.py, dual_touch.py
   +-- robot_hat (Robot, Pin, Ultrasonic, Music, utils, I2C)  -> servos / I²C / audio
```

Responsibilities of `Pidog`:

1. **Initialise all hardware** — 12 servos in three groups (legs/head/tail),
   IMU, RGB chest strip, dual touch sensors, sound-direction sensor, audio,
   ultrasonic.
2. **Provide non-blocking motion primitives** — `legs_move`, `head_move`,
   `tail_move`, `do_action`. These *append frames to buffers*; dedicated
   threads drain the buffers into servo writes.
3. **Provide the synchronisation primitives** callers use to make that
   asynchronous model look sequential — `wait_all_done`, `is_all_done`,
   `body_stop`.
4. **Kinematics** — convert body pose (x, y, z + roll/pitch/yaw) into eight leg
   joint angles, and convert head yaw/roll/pitch into three head servo angles.
5. **Sensors** — expose ultrasonic distance, IMU-derived `pitch`/`roll`, battery
   voltage.
6. **Audio** — `speak` / `speak_block`.
7. **Calibration** — persist servo offsets to `~/.config/pidog/pidog.conf`.

---

## 2. Module header

### 2.1 Imports (lines 1–15)

```python
import os, sys
from time import sleep, time
from multiprocessing import Process, Value, Lock
import threading
import numpy as np
from math import pi, sin, cos, sqrt, acos, atan2, atan
from robot_hat import Robot, Pin, Ultrasonic, utils, Music, I2C
from .sh3001 import Sh3001
from .rgb_strip import RGBStrip
from .sound_direction import SoundDirection
from .dual_touch import DualTouch
import warnings
warnings.filterwarnings("ignore")  # ignore warnings for pygame # not work
```

| Import | Used for |
| --- | --- |
| `multiprocessing.Value`, `Lock` | Shared ultrasonic distance (`Value('f', -1.0)`) and its lock. `Process` is imported but **no longer used** — the "sensory process" is now a `threading.Thread` (see §9). The shared-memory `Value` is a leftover from the process-based design; it still works fine as a plain float holder. |
| `robot_hat.Robot` | Servo group driver: holds pins, offsets, speed limiting (`max_dps`) and the config DB. |
| `robot_hat.Pin` | GPIO for the ultrasonic trigger/echo (`D0`/`D1`) and touch pins. |
| `robot_hat.Ultrasonic` | HC-SR04-style distance sensor. |
| `robot_hat.Music` | Audio playback (pygame based). |
| `robot_hat.utils` | `reset_mcu()`, `run_command()`, `get_battery_voltage()`. |
| `robot_hat.I2C` | Imported, **unused** in this file. |
| `Sh3001` | 6-axis IMU driver. |
| `RGBStrip` | 11-LED chest strip (IS31FL-style controller at I²C `0x74`). |
| `SoundDirection` | Sound-direction-of-arrival sensor. |
| `DualTouch` | Two head touch pads on `D2`/`D3`. |
| `numpy` | Matrix maths for the body-pose kinematics. |

The `warnings.filterwarnings("ignore")` call is an attempt to silence pygame's
import chatter; the author's own comment `# not work` records that it doesn't.

### 2.2 Servo map (lines 17–39)

The ASCII diagram documents the physical wiring:

```
                 4,
               5, '6'
                 |
          3,2 --[ ]-- 7,8
                [ ]
          1,0 --[ ]-- 10,11
                 |
                '9'
```

* **Legs** — `[2, 3, 7, 8, 0, 1, 10, 11]`, i.e. pairs of *(hip, knee)* for
  left-front, right-front, left-hind, right-hind. Every 8-element leg angle
  list in `actions_dictionary.py` follows exactly this order.
* **Head** — `[4, 6, 5]` = *(yaw, roll, pitch)*.
* **Tail** — `[9]`.

(The comment block labels the first four leg entries as "left front leg" twice
and "right front leg" twice; read them as hip/knee pairs.)

### 2.3 User & config-file discovery (lines 41–45)

```python
is_run_with_root = (os.geteuid() == 0)
User = os.popen('echo ${SUDO_USER:-$LOGNAME}').readline().strip()
UserHome = os.popen('getent passwd %s | cut -d: -f 6' % User).readline().strip()
config_file = '%s/.config/pidog/pidog.conf' % UserHome
```

Pidog examples are usually run with `sudo` (needed for I²C/audio on some
setups). Running as root would make `~` resolve to `/root`, so calibration
offsets would be written to the wrong place. The `${SUDO_USER:-$LOGNAME}` trick
recovers the *invoking* user, and `getent passwd | cut -d: -f6` yields that
user's home directory. `config_file` is passed as `db=` to every `Robot`
instance and to `Sh3001`, so **all calibration state lives in one file**:
`~/.config/pidog/pidog.conf`.

Note this is evaluated **at import time**, spawning two subshells, and
`SOUND_DIR` (§3) is derived from it as `f"{UserHome}/pidog/sounds/"` — i.e. the
sounds are expected in a *clone of the repo in the user's home directory*, not
in the installed package.

### 2.4 Coloured logging helpers (lines 47–72)

ANSI colour constants plus `print_color()` and the four wrappers used
throughout the file:

| Helper | Colour | Used for |
| --- | --- | --- |
| `info` | white | user-facing status (`'Quit'`, `'Please wait'`) |
| `debug` | gray | init progress (`"robot_hat init ... "` / `"done"`) |
| `warn` | yellow | recoverable problems (`No sound found for ...`) |
| `error` | red | failures (init failure, thread exceptions) |

There is no `logging` module usage — everything goes to stdout unconditionally.

### 2.5 `compare_version` and the numpy-2 shim (lines 75–85)

```python
def compare_version(original_version, object_version):
    or_v = tuple(int(val) for val in original_version.split('.'))
    ob_v = tuple(int(val) for val in object_version.split('.'))
    return (or_v >= or_v)          # <-- BUG: compares or_v with itself

if compare_version(np.__version__, '2.0.0'):
    def numpy_mat(data):
        return np.asmatrix(data)
else:
    def numpy_mat(data):
        return numpy_mat(data)     # <-- BUG: infinite recursion
```

Intent: NumPy 2 removed `np.mat`, so use `np.asmatrix` on ≥ 2.0.0 and `np.mat`
on older versions.

Two defects, which happen to cancel out:

1. `return (or_v >= or_v)` compares the tuple with **itself** — it is always
   `True`, regardless of the installed NumPy version. (`ob_v` is computed and
   discarded. The intended expression is `or_v >= ob_v`.)
2. Because of (1), the `else` branch is dead. That is fortunate, since it
   defines `numpy_mat` as a function that calls *itself* — invoking it would
   raise `RecursionError`. The intended body was `return np.mat(data)`.

Net effect: `numpy_mat` is always `np.asmatrix`, which works on NumPy ≥ 1.x as
well, so the shim is harmless in practice — but both lines are wrong.

`numpy_mat` is used for `BODY_STRUCT`, `pose`, `leg_point_struc`, and the
rotation matrices, i.e. everywhere the code relies on `*` meaning *matrix
multiply* rather than element-wise multiply. That is the only reason
`np.matrix` (a deprecated type) is used at all.

---

## 3. `Pidog` class constants (lines 89–124)

### Mechanical structure

| Constant | Value | Meaning |
| --- | --- | --- |
| `LEG` | 42 | Upper leg (thigh) length, mm |
| `FOOT` | 76 | Lower leg (shank) length, mm |
| `BODY_LENGTH` | 117 | Front-to-hind hip distance, mm |
| `BODY_WIDTH` | 98 | Left-to-right hip distance, mm |
| `BODY_STRUCT` | 3×4 matrix | Hip coordinates in the body frame, one column per leg, ordered LF, RF, LH, RH: `[±W/2, ±L/2, 0]`. Transposed (`.T`) so each **column** is a point, which is what the rotation matrix multiplication expects. |
| `SOUND_DIR` | `~/pidog/sounds/` | Where `speak()` looks for audio |

`LEG` and `FOOT` are the two link lengths of the 2-link planar arm solved by
`coord2polar` / `fieldcoord2polar` (§12).

### Servo speed limits (degrees per second)

```python
HEAD_DPS = 300
LEGS_DPS = 428
TAIL_DPS = 500
```

Assigned to `Robot.max_dps` after construction, so `robot_hat` rate-limits each
group independently. The commented-out block above them (`LEGS_DPS = 350`)
records earlier, more conservative tuning. Legs are fastest-but-one because gait
frames must be issued quickly; the tail is the lightest load, hence 500.

### PID constants

```python
KP = 0.033
KI = 0.0
KD = 0.0
```

Used only by `set_rpy(..., pid=True)` for IMU-based self-levelling. Only the
proportional term is active — integral and derivative are disabled. `KP` is
small because the loop runs at whatever rate the caller polls, and overshoot on
a 12-servo body is very visible.

### Pin defaults and head limits

```python
DEFAULT_LEGS_PINS = [2, 3, 7, 8, 0, 1, 10, 11]
DEFAULT_HEAD_PINS = [4, 6, 5]   # yaw, roll, pitch
DEFAULT_TAIL_PIN  = [9]

HEAD_PITCH_OFFSET = 45

HEAD_YAW_MIN, HEAD_YAW_MAX     = -90, 90
HEAD_ROLL_MIN, HEAD_ROLL_MAX   = -70, 70
HEAD_PITCH_MIN, HEAD_PITCH_MAX = -45, 30
```

`HEAD_PITCH_OFFSET = 45` is a **mechanical** offset: the pitch servo's zero
position is 45° away from "head level". It is added in two places — at init
(`head_init_angles[2] += HEAD_PITCH_OFFSET`) and inside `_head_action_thread`
just before writing to the servo — so all *public* head angles are expressed in
the natural "0 = level" frame. The asymmetric pitch range (−45…+30) reflects
that the head can droop further than it can lift before hitting the body.

---

## 4. `__init__` (lines 127–264)

Signature:

```python
def __init__(self, leg_pins=DEFAULT_LEGS_PINS, head_pins=DEFAULT_HEAD_PINS,
             tail_pin=DEFAULT_TAIL_PIN,
             leg_init_angles=None, head_init_angles=None, tail_init_angle=None):
```

### 4.1 MCU reset (lines 131–132)

```python
utils.reset_mcu()
sleep(0.2)
```

Hard-resets the robot_hat co-processor that generates the servo PWM, so a
previous crashed run cannot leave stale servo state. The 200 ms sleep is the
MCU boot time; skipping it makes the subsequent I²C writes fail.

### 4.2 Action dictionary (lines 134–135)

```python
from .actions_dictionary import ActionDict
self.actions_dict = ActionDict()
```

The import is **deliberately local** rather than at module top: `actions_dictionary.py`
does `from .pidog import Pidog` (it calls the `Pidog.legs_angle_calculation`
classmethod to precompute gait angles). A top-level import here would be a
circular import; deferring it to call time breaks the cycle.

`ActionDict` subclasses `dict` and overrides `__getitem__` as
`eval("self.%s" % item.replace(" ", "_"))`, so `actions_dict['lie']` evaluates
the `lie` **property**, which returns a tuple `(frames, part)` where `part ∈
{'legs', 'head', 'tail'}`. That is why `do_action` unpacks
`actions, part = self.actions_dict[action_name]`, and why an unknown name raises
`KeyError`… actually an `AttributeError` wrapped by `eval`; see §14.

### 4.3 Pose / kinematics state (lines 137–153)

```python
self.body_height = 80
self.pose = numpy_mat([0.0, 0.0, self.body_height]).T   # target position vector
self.rpy = np.array([0.0, 0.0, 0.0]) * pi / 180         # radians
self.leg_point_struc = numpy_mat([...]).T               # foot targets, body frame
self.pitch = 0    # measured, from IMU
self.roll = 0     # measured, from IMU
self.roll_last_error = 0
self.roll_error_integral = 0
self.pitch_last_error = 0
self.pitch_error_integral = 0
self.target_rpy = [0, 0, 0]
```

Important distinction:

* `self.rpy` — the **commanded** body orientation, in **radians**.
* `self.roll` / `self.pitch` — the **measured** orientation from the IMU, in
  **degrees**, updated by `_imu_thread`.
* `self.target_rpy` — the setpoint the PID branch of `set_rpy` drives towards,
  in degrees.

Note `self.leg_point_struc` is initialised here but `set_legs()` writes
`self.legpoint_struc` (no underscore between "leg" and "point"), and
`pose2coords()` reads `self.legpoint_struc`. They are **two different
attributes**; the initialised one is never read. Consequence: calling
`pose2coords()` / `pose2legs_angle()` before `set_legs()` raises
`AttributeError: 'Pidog' object has no attribute 'legpoint_struc'`. See §14.

### 4.4 Default initial angles (lines 155–163)

```python
if leg_init_angles == None:
    leg_init_angles = self.actions_dict['lie'][0][0]
if head_init_angles == None:
    head_init_angles = [0, 0, self.HEAD_PITCH_OFFSET]
else:
    head_init_angles[2] += self.HEAD_PITCH_OFFSET
if tail_init_angle == None:
    tail_init_angle = [0]
```

* Legs default to the **lie** pose `[45, -45, -45, 45, 45, -45, -45, 45]` — the
  safe, low-torque folded position to power up in.
* Head pitch is pre-offset so the head is level at boot. Note the `else`
  branch **mutates the caller's list in place** — passing the same list to two
  `Pidog` instances would double-apply the offset.
* Comparisons use `== None` rather than `is None` throughout the file.

### 4.5 Servo groups (lines 167–205)

```python
self.legs = Robot(pin_list=leg_pins, name='legs', init_angles=leg_init_angles,
                  init_order=[0, 2, 4, 6, 1, 3, 5, 7], db=config_file)
self.head = Robot(pin_list=head_pins, name='head', init_angles=head_init_angles, db=config_file)
self.tail = Robot(pin_list=tail_pin,  name='tail', init_angles=tail_init_angle,  db=config_file)
```

`init_order=[0, 2, 4, 6, 1, 3, 5, 7]` makes the legs power up **all hips first,
then all knees**. Energising a knee before its hip would make the leg kick out
and possibly tip the robot over.

`name=` selects the section in `pidog.conf` where that group's calibration
offsets live; `db=config_file` points all three at the same file.

Then per-group state is created:

| Attribute | Purpose |
| --- | --- |
| `legs_action_buffer`, `head_action_buffer`, `tail_action_buffer` | FIFO lists of angle frames waiting to be written to servos |
| `legs_thread_lock`, `head_thread_lock`, `tail_thread_lock` | Guard the corresponding buffer |
| `leg_current_angles`, `head_current_angles`, `tail_current_angles` | Last frame handed to the servos; read by `preset_actions` (e.g. `feet_shake` copies `leg_current_angles` to build a relative motion) |
| `legs_speed`, `head_speed`, `tail_speed` | Current speed (0–100) — note this is **per group, not per frame**: the last `*_move()` call's speed applies to whatever is in the buffer when the thread gets to it |
| `legs_actions_coords_buffer` | Created, never used |

Failure of this block raises `OSError("rotbot_hat I2C init failed…")` (sic) — a
`Pidog` without servos is not usable, so this is the one fatal init step.

### 4.6 Optional peripherals (lines 207–254)

Each peripheral is initialised in its own `try/except` that prints `fail` and
**continues**. The pattern is deliberate: a Pidog missing a chest strip or a
sound-direction board should still walk.

| Block | Creates | Registers thread | On failure |
| --- | --- | --- | --- |
| IMU | `self.imu = Sh3001(db=config_file)`, offsets, `accData`, `gyroData`, `imu_fail_count` | `"imu"` | prints `fail`; `self.imu` never assigned |
| RGB strip | `self.rgb_strip = RGBStrip(addr=0x74, nums=11)`, set to `breath`/`black`, `rgb_thread_run = True` | `"rgb"` | prints `fail` |
| Dual touch | `self.dual_touch = DualTouch('D2', 'D3')`, `self.touch = 'N'` | — (polled by the app) | bare `except:` |
| Sound direction | `self.ears = SoundDirection()` | — (polled by the app) | bare `except:` |
| Audio | `self.music = Music()` | — | bare `except:` |

Note the inconsistency: the first two catch only `OSError`, the last three use a
bare `except:` (which also swallows `KeyboardInterrupt`/`SystemExit`).

`self.thread_list` is the registry that later drives `action_threads_start()`
and `close()` — a peripheral that failed to init simply never appears in it, so
no thread is started and no join is attempted for it.

### 4.7 Ultrasonic + startup (lines 256–264)

```python
self.distance = Value('f', -1.0)
self.sensory_process = None
self.sensory_lock = Lock()

self.exit_flag = False
self._sensory_exit_flag = False
self.action_threads_start()
self.sensory_process_start()
```

`-1.0` is the "no reading yet / invalid" sentinel for distance. Then all
background workers are started — **the constructor leaves five to six threads
running**.

---

## 5. Threading model

This is the single most important thing to understand about `Pidog`.

| Thread | Target | Daemon | Loop exit condition | Touches |
| --- | --- | --- | --- | --- |
| `legs_thread` | `_legs_action_thread` | yes | `exit_flag` | `legs_action_buffer`, `legs.servo_move` |
| `head_thread` | `_head_action_thread` | yes | `exit_flag` | `head_action_buffer`, `head.servo_move` |
| `tail_thread` | `_tail_action_thread` | yes | `exit_flag` | `tail_action_buffer`, `tail.servo_move` |
| `rgb_strip_thread` | `_rgb_strip_thread` | yes | `rgb_thread_run` | `rgb_strip.show()` |
| `imu_thread` | `_imu_thread` | yes | `exit_flag` | `accData`, `gyroData`, `pitch`, `roll` |
| `sensory_thread` | `sensory_process_work` | **no** | (spawns the next one and returns) | creates the ultrasonic device |
| `ultrasonic_thread` | `_ultrasonic_thread` | **no** | `_sensory_exit_flag` | `self.distance` |

**Producer/consumer contract:** the caller's thread appends frames
(`legs_move`, `head_move`, `tail_move`, `do_action`); the group thread pops
frames and blocks inside `robot_hat`'s `servo_move`, which interpolates to the
target at `max_dps` limited by `*_speed`. "Action finished" therefore means
"buffer empty", which is exactly what `is_*_done()` reports and
`wait_*_done()` polls.

Consequence worth internalising: **`legs_move()` returns immediately**. Any
sequential-looking code must call `wait_all_done()` (this is what
`preset_actions` and `ActionFlow.run()` do after every step).

---

## 6. Lifecycle methods

### `action_threads_start()` (lines 358–380)

Creates and starts one daemon thread per entry in `thread_list`. It is called
by `__init__` and again by `close()` if the threads had been stopped. Because
the threads are daemons, a Python process that forgets to call `close()` can
still exit.

Calling it twice without setting `exit_flag` first would start **duplicate**
threads competing for the same buffers; nothing guards against that.

### `close_all_thread()` (lines 270–271)

One-liner: `self.exit_flag = True`. Stops legs/head/tail/imu loops (but *not*
the RGB loop, which watches `rgb_thread_run`, nor the ultrasonic loop, which
watches `_sensory_exit_flag`).

### `close()` (lines 273–327)

The full shutdown sequence:

```python
signal.signal(signal.SIGINT, handler)          # Ctrl-C during shutdown -> "Please wait"
signal.signal(signal.SIGALRM, _handle_timeout)
signal.alarm(5)                                 # hard 5 s budget for shutdown
```

1. **SIGINT is swallowed** during shutdown so an impatient second Ctrl-C cannot
   leave the servos energised in a bad pose.
2. **SIGALRM after 5 s** raises `TimeoutError` inside whatever is currently
   executing, so a wedged `join()` cannot hang the process forever. The
   exception is caught by the outer `except Exception` and reported as
   `Close error: function timeout`. Note `signal.alarm()` only works on the main
   thread of the main interpreter.
3. If the threads were already stopped (`exit_flag == True`), they are
   **restarted** — otherwise `stop_and_lie()` would enqueue frames that nobody
   consumes and `wait_all_done()` would block until the alarm fires.
4. `stop_and_lie()` — return to the safe folded pose.
5. `close_all_thread()` — signal legs/head/tail/imu to stop.
6. Close `dual_touch`, `ears`, `ultrasonic` if present (`hasattr` guards,
   because those inits are allowed to fail).
7. `join()` the three servo threads, then RGB (after `rgb_thread_run = False`
   and `rgb_strip.close()`), then IMU, then the sensory thread with
   `_sensory_exit_flag = True` and `join(timeout=1)`.

The trailing commented-out `finally:` block (restoring the default SIGINT
handler, cancelling the alarm, `sys.exit(0)`) means **the alarm is left armed
and SIGINT stays hijacked after `close()` returns**. If the process lives on
for more than the remaining alarm time, a stray `TimeoutError` can surface at an
arbitrary point. Re-enabling `signal.alarm(0)` would be the fix.

---

## 7. The servo worker threads

### `_legs_action_thread` (lines 383–396)

```python
while not self.exit_flag:
    try:
        with self.legs_thread_lock:
            self.leg_current_angles = list.copy(self.legs_action_buffer[0])
        # lock released before the slow part
        self.legs.servo_move(self.leg_current_angles, self.legs_speed)
        with self.legs_thread_lock:
            self.legs_action_buffer.pop(0)
    except IndexError:
        sleep(0.001)
    except Exception as e:
        error(f'\r_legs_action_thread Exception:{e}')
        break
```

Design notes:

* **`IndexError` is the idle signal.** Rather than a condition variable, the
  thread indexes `[0]` on an empty list and treats the exception as "nothing to
  do", sleeping 1 ms. Simple, but it means an empty buffer costs a 1 kHz
  exception-throwing spin.
* **The lock is held only around the list access**, never across
  `servo_move()` (which blocks for the whole interpolated motion). This is what
  lets `legs_stop()` clear the buffer mid-motion.
* **Legs pop *after* the move; head and tail pop *before*.** This asymmetry is
  significant: for legs, `is_legs_done()` (buffer empty) becomes true only once
  the last frame has physically finished, whereas for head/tail the buffer
  empties one frame *before* the motion completes. So `wait_head_done()` can
  return while the head is still moving — several routines in
  `preset_actions.py` compensate with explicit `sleep()`s.
* A clear during a move leaves the just-completed frame in flight and then
  `pop(0)` removes *someone else's* frame if new frames arrived in the interim —
  a small race window inherent to the pop-after-move ordering.
* Any non-`IndexError` exception **kills the thread permanently** (`break`); the
  robot then silently stops responding to leg commands.

### `_head_action_thread` (lines 399–416)

Same shape, plus the head-specific transformation applied *at write time*:

```python
_angles[0] = self.limit(self.HEAD_YAW_MIN,   self.HEAD_YAW_MAX,   _angles[0])
_angles[1] = self.limit(self.HEAD_ROLL_MIN,  self.HEAD_ROLL_MAX,  _angles[1])
_angles[2] = self.limit(self.HEAD_PITCH_MIN, self.HEAD_PITCH_MAX, _angles[2])
_angles[2] += self.HEAD_PITCH_OFFSET
```

Clamping happens **here**, not in `head_move()`, so callers can enqueue
out-of-range values freely and the hardware is still protected. Because the
clamp is applied to the copy `_angles`, `head_current_angles` keeps the
*unclamped* value — so `head_current_angles` is the commanded, not the actual,
orientation.

### `_tail_action_thread` (lines 419–431)

The simplest of the three: pop, then `servo_move`. No clamping.

### `_rgb_strip_thread` (lines 434–444)

```python
while self.rgb_thread_run:
    try:
        self.rgb_strip.show()
        self.rgb_fail_count = 0
    except Exception as e:
        self.rgb_fail_count += 1
        sleep(0.001)
        if self.rgb_fail_count > 10:
            error(...); break
```

`RGBStrip.show()` renders one animation frame over I²C and paces itself
internally. The failure counter tolerates up to 10 *consecutive* I²C glitches
(the counter resets on every success) before giving up — the chest strip shares
the bus with the IMU and the servo MCU, so occasional NACKs are expected.

### `_imu_thread` (lines 448–510)

Two phases.

**Phase 1 — calibration** (runs once, ~1 s):

```python
time = 10                      # shadows the imported time() function!
for _ in range(time):
    data = self.imu._sh3001_getimudata()
    ...accumulate...
    sleep(0.1)

self.imu_acc_offset[0] = round(-16384 - _ax/time, 0)
self.imu_acc_offset[1] = round(0 - _ay/time, 0)
self.imu_acc_offset[2] = round(0 - _az/time, 0)
self.imu_gyro_offset[...] = round(0 - _g?/time, 0)
```

Averages 10 samples and computes the offsets that would make the readings match
the *expected at-rest values*: **−16384 on X** (i.e. 1 g at ±2 g full scale,
where 16384 LSB = 1 g — so the chip is mounted with its X axis pointing down)
and 0 on the other two accelerometer axes and all three gyro axes. This means
**the robot must be stationary and level for the first second after
construction**, or every later attitude reading is biased.

`time = 10` shadows the module-level `from time import time` inside this
function; harmless here only because the function never calls `time()`.

**Phase 2 — the loop** (every 50 ms):

```python
data = self.imu._sh3001_getimudata()
if data == False:
    self.imu_fail_count += 1
    if self.imu_fail_count > 10:
        error(...); break
self.accData, self.gyroData = data      # <-- executed even when data is False
...apply offsets...
ay = -ay; az = -az
self.pitch = atan(ay / sqrt(ax*ax + az*az)) * 57.2957795
self.roll  = atan(az / sqrt(ax*ax + ay*ay)) * 57.2957795
```

* `57.2957795` is `180/π` — radians to degrees.
* The two `atan(component / magnitude_of_the_other_two)` expressions are the
  standard accelerometer tilt estimate. Only the accelerometer is used; the
  gyro is read and offset-corrected but never fused (no complementary/Kalman
  filter), so `pitch`/`roll` are accurate at rest but noisy while moving.
* The sign flips on `ay`/`az` orient the result to the robot's frame.
* **Bug:** when `data == False` the code increments the counter but does not
  `continue`, so it immediately tries `self.accData, self.gyroData = data` and
  raises `TypeError: cannot unpack non-sequence bool`. That is caught by the
  outer handler, which increments the counter again and sleeps 1 ms — so a
  persistent IMU failure becomes a hot loop that reaches the threshold in ~5
  iterations rather than 10, and sets `self.exit_flag = True`, which
  **shuts down the leg/head/tail threads too**. An IMU cable fault therefore
  bricks all motion.

---

## 8. Buffer control and motion primitives

### Stopping

```python
def legs_stop(self):
    with self.legs_thread_lock:
        self.legs_action_buffer.clear()
    self.wait_legs_done()
```

Clear the queue, then wait until the worker reports done. `head_stop`,
`tail_stop` are identical; `body_stop()` does all three. Note this does **not**
abort the frame currently being interpolated by `servo_move` — it only discards
what has not started yet.

### `legs_move(target_angles, immediately=True, speed=50)`

```python
if immediately: self.legs_stop()      # pre-empt whatever is queued
self.legs_speed = speed
with self.legs_thread_lock:
    self.legs_action_buffer += target_angles
```

`target_angles` is a **list of frames**, each frame an 8-element list in leg-pin
order. `immediately=True` = "interrupt current motion"; `immediately=False` =
"append, play after what's already queued". `ActionFlow`/`do_action` use
`False` for chained animations and `True` for snap-to-pose.

The speed is stored on the instance, not per frame — so appending frames with a
different speed retroactively changes the speed of frames still in the buffer.

### `head_rpy_to_angle(target_yrp, roll_comp=0, pitch_comp=0)` (lines 541–548)

```python
yaw, roll, pitch = target_yrp
signed = -1 if yaw < 0 else 1
ratio  = abs(yaw) / 90
pitch_servo = roll * ratio + pitch * (1 - ratio) + pitch_comp
roll_servo  = -(signed * (roll * (1 - ratio) + pitch * ratio) + roll_comp)
yaw_servo   = yaw
```

This is the head gimbal's cross-coupling correction. The roll and pitch servos
are mounted **before** the yaw joint in the kinematic chain, so as the head
yaws, the world-frame roll and pitch axes rotate into each other:

* At `yaw = 0` (`ratio = 0`): `pitch_servo = pitch`, `roll_servo = -(roll)` —
  the axes line up directly.
* At `yaw = ±90` (`ratio = 1`): `pitch_servo = roll`, `roll_servo = -(±pitch)` —
  the axes have fully swapped.
* In between, the two are linearly blended by `ratio`.

`signed` handles the sign inversion of the roll servo when the head is turned to
the other side. `roll_comp` / `pitch_comp` are static trims added *after* the
blend — `pitch_comp` is exactly what `ActionFlow` uses to compensate for the
sit/stand body tilt (see `action_flow.md` §8).

Note `ratio` is not clamped: a yaw beyond ±90 gives `ratio > 1` and starts
extrapolating. The yaw itself is clamped later, in the worker thread, but the
blend uses the unclamped value.

### `head_move(target_yrps, roll_comp=0, pitch_comp=0, immediately=True, speed=50)`

Maps `head_rpy_to_angle` over a list of yaw/roll/pitch frames and appends the
resulting servo-angle frames. This is the *normal* head API.

### `head_move_raw(target_angles, immediately=True, speed=50)`

Same, bypassing the gimbal maths — the values go straight to the servos (still
clamped and pitch-offset in the worker). Used by `stop_and_lie()` and by
calibration.

### `tail_move(target_angles, immediately=True, speed=50)`

Straightforward append. Frames are 1-element lists.

### `do_action(action_name, step_count=1, speed=50, pitch_comp=0)` (lines 923–938)

```python
actions, part = self.actions_dict[action_name]
if part == 'legs':
    for _ in range(step_count): self.legs_move(actions, immediately=False, speed=speed)
elif part == 'head':
    for _ in range(step_count): self.head_move(actions, pitch_comp=pitch_comp, immediately=False, speed=speed)
elif part == 'tail':
    for _ in range(step_count): self.tail_move(actions, immediately=False, speed=speed)
```

The high-level entry point used everywhere: `do_action('forward', speed=98)`,
`do_action('wag_tail', speed=100)`. Key points:

* Always `immediately=False` — actions **queue**, they never pre-empt. To
  interrupt, callers must call `body_stop()`/`*_stop()` first.
* `step_count` repeats the whole frame set — that is how a multi-step walk is
  requested (`do_action('forward', step_count=5)`).
* Names with spaces work because `ActionDict.__getitem__` replaces `' '` with
  `'_'`.
* Errors are printed, never raised: `KeyError` → `"do_action: No such action"`,
  anything else → `"do_action:<e>"`. Note the lookup actually raises
  `AttributeError` (from `eval("self.<name>")`) for an unknown action, so it
  lands in the *generic* branch, not the tailored `KeyError` message.

### Synchronisation helpers (lines 940–967)

```python
def is_legs_done(self):  return not bool(len(self.legs_action_buffer) > 0)
def wait_legs_done(self):
    while not self.is_legs_done(): sleep(0.001)
def wait_all_done(self):
    self.wait_legs_done(); self.wait_head_done(); self.wait_tail_done()
```

1 kHz busy-polling of the buffer lengths. `is_all_done()` is the non-blocking
variant. Reading `len()` without the lock is safe enough in CPython, but these
are the functions that turn the asynchronous buffers into the sequential API
that `preset_actions` and `ActionFlow` rely on.

Reminder from §7: because head/tail pop *before* moving, `wait_head_done()`
returns slightly early.

---

## 9. Ultrasonic subsystem (lines 576–618)

```python
def sensory_process_work(self, distance_addr, lock):
    echo = Pin('D0'); trig = Pin('D1')
    self.ultrasonic = Ultrasonic(trig, echo, timeout=0.017)
    self.thread_list.append("ultrasonic")
    ...
    ultrasonic_thread = threading.Thread(target=self._ultrasonic_thread,
                                         args=(distance_addr, lock,))
    ultrasonic_thread.start()
```

* `timeout=0.017` s ≈ 17 ms ≈ **2.9 m** maximum range (sound travels ~343 m/s,
  round trip). Beyond that the read times out rather than blocking.
* The device is created **inside the worker**, not in `__init__` — a leftover
  from when this was a separate `multiprocessing.Process` and the `Pin` objects
  could not be inherited across the fork.
* `sensory_process_work` is itself run in a thread (`sensory_process_start`),
  and it spawns *another* thread. Two layers for what is now a single worker.
* Both threads are **non-daemon** (`# ultrasonic_thread.daemon = True` is
  commented out), so a process that never calls `close()` will not exit — the
  most likely cause of a hung example script.
* `_ultrasonic_thread` writes `distance_addr.value` under `lock` every 10 ms; on
  any exception it sleeps 100 ms, prints and **breaks** (distance freezes at its
  last value forever).
* The naming (`sensory_process`, `sensory_process_start`) is historical: they
  are threads now. `sensory_process_start()` still guards against a previous
  instance by setting `_sensory_exit_flag` and `join(timeout=1)` — but it does
  not stop the inner `ultrasonic_thread` it spawned, which the flag does cover.

### `read_distance()`

```python
return round(self.distance.value, 2)
```

Centimetres (as returned by `robot_hat.Ultrasonic.read()`), `-1.0` before the
first successful reading. Negative values are also what the sensor returns on
timeout, so applications treat `distance < 0` as "no echo" — see
`examples/voice_active_dog.py`'s `TOO_CLOSE_DISTANCE` check.

---

## 10. Reset and audio

### `stop_and_lie(speed=85)` (lines 621–630)

```python
self.body_stop()
self.legs_move(self.actions_dict['lie'][0], speed)
self.head_move_raw([[0, 0, 0]], speed)
self.tail_move([[0, 0, 0]], speed)
self.wait_all_done()
sleep(0.1)
```

Cancels everything queued, then commands the folded lie pose, a centred head and
a centred tail, and blocks until done. Note `tail_move([[0, 0, 0]], ...)` passes
a **3-element** frame to a **1-servo** group; `robot_hat` writes the first value
and ignores the rest, so it works by accident.

### `speak(name, volume=100)` / `speak_block(name, volume=100)` (lines 632–678)

Identical except `speak` uses `Music.sound_play_threading` (returns
immediately) and `speak_block` uses `Music.sound_play` (blocks until the clip
ends). Resolution order for `name`:

1. `name` as a literal path, if `os.path.isfile(name)`
2. `SOUND_DIR + name + '.mp3'`
3. `SOUND_DIR + name + '.wav'`
4. otherwise `warn('No sound found for …')` and return `False`

Both call `utils.run_command('sudo killall pulseaudio')` on **every invocation**
— a workaround for silent audio under VNC, where a stale PulseAudio daemon owns
the sink. It costs a subprocess per bark and will prompt for a password if the
user has no passwordless sudo. The `is_run_with_root` / `speak_first` dance is
vestigial: it sets a flag and the warning it guarded is commented out.

Return value is `False` on failure and `None` on success — an inconsistency
callers must not rely on.

---

## 11. Calibration (lines 681–700)

```python
def set_leg_offsets(self, cali_list, reset_list=None):
    self.legs.set_offset(cali_list)
    if reset_list is None:
        self.legs.reset()
        self.leg_current_angles = [0]*8
    else:
        self.legs.servo_positions   = list.copy(reset_list)
        self.legs.leg_current_angles = list.copy(reset_list)
        self.legs.servo_write_all(reset_list)

def set_head_offsets(self, cali_list):
    self.head.set_offset(cali_list)
    self.head_move([[0]*3], immediately=True, speed=80)
    self.head_current_angles = [0]*3

def set_tail_offset(self, cali_list):
    self.tail.set_offset(cali_list)
    self.tail.reset()
    self.tail_current_angles = [0]
```

`Robot.set_offset()` persists the per-servo trim into `pidog.conf`, so
calibration survives restarts. These are what `bin/`/`pidog-control` calibration
tools drive.

Two oddities in `set_leg_offsets`: it writes `self.legs.leg_current_angles`
(a new attribute on the `Robot` object) instead of `self.leg_current_angles`,
and it bypasses the buffer/thread by calling `servo_write_all` directly — fine
during calibration, where no animation is running, but it would fight the leg
thread otherwise. `set_head_offsets` correctly goes through `head_move`.

---

## 12. Kinematics

### 12.1 Frames and conventions

* **Body frame** — origin at the geometric centre of the four hips, `x` to the
  right (`BODY_WIDTH`), `y` forward (`BODY_LENGTH`), `z` up.
* **Leg plane** — each leg is a 2-link planar arm (`LEG = 42`, `FOOT = 76`)
  operating in the `(y, z)` plane; there is no abduction joint, which is why the
  IK reduces to 2-D.
* Angles are degrees at the public boundary, radians internally
  (`self.rpy`).

### 12.2 `set_pose(x, y, z)` / `set_rpy(roll, pitch, yaw, pid=False)` / `set_legs(legs_list)`

* `set_pose` — writes the body translation target into `self.pose` (a 3×1
  matrix). Only the components you pass are changed.
* `set_legs(legs_list)` — takes four `[y_offset, z_offset]` pairs and builds
  `self.legpoint_struc`, the 3×4 matrix of desired **foot positions**:
  `[±W/2, ±L/2 + dy, body_height − dz]`.
* `set_rpy` — two modes:
  * **direct** (`pid=False`): `self.rpy = [roll, pitch, yaw] * π/180`.
  * **PID** (`pid=True`): a self-levelling step. Error is
    `target_rpy − measured` (the measured values come from the IMU thread), the
    offset is `KP*e + KI*∫e + KD*Δe`, converted to radians and **added** to the
    current `rpy`. So `pid=True` is an *incremental* correction meant to be
    called repeatedly in a control loop, whereas `pid=False` is an absolute set.
    With `KI = KD = 0` only the proportional term contributes; the integral and
    last-error state is still accumulated, ready for tuning.

### 12.3 `pose2coords()` (lines 757–790)

Builds the three rotation matrices and composes them:

```python
rot_mat = rotx * roty * rotz          # matrix product (np.matrix semantics)
AB[:, i] = -self.pose - rot_mat * self.BODY_STRUCT[:, i] + self.legpoint_struc[:, i]
```

For each leg *i*: take the hip position in the body frame, rotate it by the
commanded body orientation, offset it by the body translation, and subtract it
from the desired foot position. `AB[:, i]` is the hip→foot vector expressed in
the field frame. It returns both lists:

```python
{"leg":  [foot positions  (legpoint_struc columns)],
 "body": [(legpoint_struc − AB) columns  = rotated hip positions]}
```

Two things to note about the maths: the matrix named `rotx` is actually a
rotation about **y** (it has the `[cos, 0, -sin; 0, 1, 0; sin, 0, cos]` pattern)
and `roty` is a rotation about **x** — the names are swapped relative to their
content, but since the code consistently feeds `roll` into `rotx` and `pitch`
into `roty`, the resulting behaviour is the intended one for this chassis. Also
`np.matrix` `*` is matrix multiplication, which is exactly why `numpy_mat` is
used instead of plain arrays.

### 12.4 `pose2legs_angle()` (lines 792–817)

Reduces each leg's 3-D hip→foot vector to the 2-D `(y, z)` pair the planar IK
needs, solves it, and applies the mirroring convention:

```python
coords.append([leg_coor[1] - body_coor[1],      # Δy
               body_coor[2] - leg_coor[2]])     # Δz (sign flipped: down positive)

leg_angle, foot_angle = self.fieldcoord2polar(coord)
foot_angle = foot_angle - 90
if i % 2 != 0:                 # odd index = right side
    leg_angle  = -leg_angle
    foot_angle = -foot_angle
angles += [leg_angle, foot_angle]
```

* The `−90` on `foot_angle` re-zeros the knee: the IK returns the interior
  angle of the triangle, the servo's zero is the straight-leg position.
* Right-side servos are mirrored (`i % 2 != 0`), because the two sides are
  physically mirrored — the same convention `legs_angle_calculation` uses.
* Result is the 8-element list in leg-pin order, ready for `legs_move`.

### 12.5 `fieldcoord2polar(coord)` / `coord2polar(coord)` (lines 820–856)

Classic 2-link inverse kinematics via the law of cosines:

```
u    = √(y² + z²)                                  # hip → foot distance
β    = acos((FOOT² + LEG² − u²) / (2·FOOT·LEG))    # knee interior angle
α    = atan2(y, z) + acos((LEG² + u² − FOOT²)/(2·LEG·u))   # hip angle
```

Both `cos_angle` values are clamped to `[-1, 1]` before `acos`, which is
essential: floating-point error (or a commanded foot position outside the
`|LEG − FOOT| … LEG + FOOT` reachable annulus) would otherwise raise
`ValueError: math domain error`. Clamping silently saturates at the workspace
boundary instead.

The **only** difference between the two functions:

```python
# fieldcoord2polar
alpha = angle2 + angle1 + self.rpy[1]     # + commanded body pitch
# coord2polar
alpha = angle2 + angle1
```

`fieldcoord2polar` works in the *field* frame — the coordinates came out of
`pose2coords`, which already applied the body rotation, so the hip angle must be
corrected back by the body pitch. `coord2polar` works in the *robot* frame and
needs no such term. The duplication (rather than one function with a flag) is
the main refactoring opportunity in this section.

### 12.6 `polar2coord(angles)` (lines 858–870)

The nominal forward-kinematics inverse of the above, taking `[alpha, beta,
gamma]`. **It is broken**: it references `self.A`, `self.B`, `self.C`, none of
which exist on `Pidog`. Calling it raises `AttributeError`. Its only call site
is the error branch of `set_angle()`, which is itself unreachable (§12.8).

### 12.7 `legs_angle_calculation(coords)` (lines 872–886)

```python
@classmethod
def legs_angle_calculation(cls, coords):
    for i, coord in enumerate(coords):
        leg_angle, foot_angle = Pidog.coord2polar(cls, coord)
        foot_angle = foot_angle - 90
        if i % 2 != 0:
            leg_angle, foot_angle = -leg_angle, -foot_angle
        translate_list += [leg_angle, foot_angle]
```

The **class-level** IK entry point: four `[y, z]` foot coordinates in →
eight joint angles out. This is what `actions_dictionary.py`, `walk.py` and
`trot.py` call to precompute gait frames **without instantiating a `Pidog`** —
which matters because `ActionDict` is built during `Pidog.__init__` itself.

The trick `Pidog.coord2polar(cls, coord)` calls the *unbound* instance method
with the **class object** standing in for `self`. That works only because
`coord2polar` touches nothing but class constants (`self.FOOT`, `self.LEG`) —
attribute lookup on the class finds them. It would break the moment
`coord2polar` referenced instance state, which is precisely why
`fieldcoord2polar` (which reads `self.rpy`) cannot be used this way.

### 12.8 `limit()` and `set_angle()` (lines 889–920)

`limit(min, max, x)` is a plain clamp (shadowing the builtins `min`/`max` as
parameter names). Used by `_head_action_thread`.

`set_angle(angles_list, speed=50, israise=False)` is **dead code**: it calls
`self.limit_angle()`, `self.polar2coord()`, `self.coord_temp` and
`self.servo_move()` — of those, only `polar2coord` exists (and is itself
broken). Nothing in the repository calls `set_angle`. It is a remnant of an
older API and should be deleted.

---

## 13. Miscellaneous

* **`legs_simple_move(angles_list, speed=90)`** (lines 329–353) — bypasses the
  buffer/thread entirely and writes raw servo values with
  `self.legs.servo_write_raw(angles + offset)`, then sleeps a speed-derived
  delay (0.005 s at speed 100 → 0.05 s at speed 0), reduced by the time the
  write itself took. Used for tight custom loops (e.g. the calibration and
  balance demos) where the interpolation in `servo_move` gets in the way.
  Because it applies `self.legs.offset[i]` manually and writes raw, it does
  **not** respect `max_dps`.
* **`legs_switch(flag)`** (lines 355–356) — sets `self.legs_sw_flag`, which
  nothing reads. Dead.
* **`get_battery_voltage()`** — `round(utils.get_battery_voltage(), 2)`, volts.
  A 2S 18650 pack: ~8.4 V full, ~6.6 V empty.
* **`self.touch`** is initialised to `'N'` but never updated by `Pidog`;
  applications poll `self.dual_touch.read()` themselves (returning
  `TouchStyle` values `'N' | 'L' | 'R' | 'LS' | 'RS'`).
* Likewise `self.ears` (sound direction) is created but never polled here —
  `examples/voice_active_dog.py` calls `ears.isdetected()` / `ears.read()`.

---

## 14. Known issues / improvement candidates

Ordered roughly by impact.

1. **`_imu_thread` does not `continue` after `data == False`** — it unpacks a
   bool, raises `TypeError`, and on repeated failure sets `self.exit_flag = True`,
   which stops the leg, head and tail threads. An IMU fault therefore disables
   all motion.
2. **`compare_version` returns `or_v >= or_v`** — always `True`; the version
   check never actually runs. The dead `else` branch defines `numpy_mat` as
   infinitely recursive (`return numpy_mat(data)` instead of `np.mat(data)`).
3. **`leg_point_struc` vs `legpoint_struc`** — `__init__` sets the former,
   `set_legs()`/`pose2coords()` use the latter. `pose2coords()` before
   `set_legs()` raises `AttributeError`.
4. **`polar2coord` references non-existent `self.A/B/C`** — always raises.
5. **`set_angle` is dead code** referencing three more non-existent members
   (`limit_angle`, `coord_temp`, `servo_move`).
6. **`close()` never cancels the 5 s `SIGALRM` nor restores the SIGINT
   handler** (the `finally:` block is commented out), so a `TimeoutError` can
   fire later at an arbitrary point.
7. **Ultrasonic threads are non-daemon**, so forgetting `close()` hangs process
   exit.
8. **Head/tail pop before moving, legs pop after** — `wait_head_done()` /
   `wait_tail_done()` return before the motion physically completes.
9. **Speed is per-group state, not per-frame** — a later `*_move()` with a
   different speed retroactively changes frames already queued.
10. **`speak()` shells out to `sudo killall pulseaudio` on every call** — a
    subprocess per sound effect, and it fails noisily without passwordless sudo.
11. **Worker threads `break` on any unexpected exception**, permanently and
    silently disabling that body part; there is no restart or health check.
12. **Idle worker threads spin at 1 kHz raising `IndexError`**; a
    `threading.Condition` or `queue.Queue` would be both cheaper and race-free.
13. **`do_action`'s `except KeyError` branch is unreachable** — `ActionDict.__getitem__`
    uses `eval("self.<name>")`, so an unknown action raises `AttributeError`
    and gets the generic message.
14. `head_init_angles` is **mutated in place** when supplied by the caller.
15. Unused imports/attributes: `Process`, `I2C`, `sin`, `legs_actions_coords_buffer`,
    `legs_switch`/`legs_sw_flag`, `self.touch`.
16. Inconsistent error handling: `except OSError` for some peripherals, bare
    `except:` for others (which also swallows `KeyboardInterrupt`).
17. `stop_and_lie()` passes a 3-element frame to the 1-servo tail group.
18. `== None` comparisons instead of `is None` throughout.
