"""Application wiring: dependency injection + main loop.

This module builds the object graph (config -> dog -> senses -> camera ->
features -> registry -> brain -> io) and runs the conversation loop.

Run as a module (preferred):

    python -m pidog_app

It also works when launched directly by file path (e.g. from an IDE
debugger) thanks to the bootstrap below.
"""
from __future__ import annotations

import logging
import sys

# ── bootstrap: allow running this file directly (e.g. from a debugger) ──
# Relative imports (`from .config import ...`) only work when Python knows
# this file belongs to the `pidog_app` package. That's true for
# `python -m pidog_app` but NOT when an IDE runs the file by path. In that
# case `__package__` is empty, so we re-launch via runpy as a module.
if __package__ in (None, ""):
    import os
    import runpy

    # Add the parent of the `pidog_app/` package dir to sys.path so the
    # package is importable, then re-run as a module.
    _pkg_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _pkg_parent not in sys.path:
        sys.path.insert(0, _pkg_parent)
    runpy.run_module("pidog_app", run_name="__main__")
    raise SystemExit(0)

from .config import Config, load_config
from .dog import Body, Senses
from .vision import Camera
from .features import FeatureRegistry
from .features.instances import (
    WakeFromStasis,
    FindObject,
    RecognizePerson,
    CheckWaterBowl,
)
from .brain import Brain
from .io import TextIO, VoiceIO

log = logging.getLogger(__name__)

# Name of the parent logger that all ``pidog_app.*`` child loggers propagate
# to. ``main()`` attaches a single ``FileHandler`` here so every subsystem's
# records land in the same log file, while each module keeps its own child
# logger name (e.g. ``pidog_app.brain.brain``) for fine-grained filtering.
ROOT_LOGGER_NAME = "pidog_app"


# ── dependency injection ──────────────────────────────────────────────────
def build_features(body: Body, senses: Senses, camera: Camera) -> list:
    """Instantiate every feature with the shared facades.

    Add new features here — that's the only place to register them.
    """
    return [
        WakeFromStasis(body, senses, camera),
        FindObject(body, senses, camera),
        RecognizePerson(body, senses, camera),
        CheckWaterBowl(body, senses, camera),
    ]


def build_io(cfg: Config) -> TextIO | VoiceIO:
    mode = cfg.get("io.mode", "text")
    name = cfg.get("dog.name", "Scooby Doo")
    welcome = f"Hi, I'm {name}. Type 'quit' to exit."

    if mode == "voice":
        v = cfg.get("io.voice", {})
        return VoiceIO(
            welcome=welcome,
            wake_word=v.get("wake_word") or [f"hey {name.lower()}"],
            answer_on_wake=v.get("answer_on_wake", ""),
            stt_language=v.get("stt_language", "en-us"),
            tts_model=v.get("tts_model", "en_US-ryan-low"),
            keyboard_enable=True,
        )
    return TextIO(welcome=welcome)


def build_app(config_path: str | None = None) -> "App":
    cfg = load_config(config_path)
    return App(cfg)


# ── app object ────────────────────────────────────────────────────────────
class App:
    """Owns all subsystems and runs the conversation loop."""

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.body = Body()
        self.senses = Senses(self.body.dog)
        self.camera = Camera(
            vflip=cfg.get("vision.camera_vflip", False),
            hflip=cfg.get("vision.camera_hflip", False),
        )
        self.registry = FeatureRegistry(
            build_features(self.body, self.senses, self.camera)
        )

        # LLM: use the OpenAI-compatible /v1/chat/completions endpoint so we
        # get the standard `choices[0].message` shape (with `tool_calls`) that
        # the brain's non-stream parser expects. The `pidog.llm.Ollama` preset
        # targets the native /api/chat endpoint instead, which returns a
        # different shape and would break tool-call parsing.
        from pidog.llm import LLM
        ip = cfg.get("llm.ip", "localhost")
        port = cfg.get("llm.port", 11434)
        llm = LLM(
            base_url=f"http://{ip}:{port}/v1",
            api_key="ollama",  # any non-empty string works for Ollama
            model=cfg.get("llm.model", "qwen2.5:7b"),
        )
        llm.set_max_messages(cfg.get("llm.max_messages", 20))
        self.llm = llm

        self.brain = Brain(
            llm=self.llm,
            registry=self.registry,
            name=cfg.get("dog.name", "Scooby Doo"),
        )
        self.io = build_io(cfg)

    # ── lifecycle ────────────────────────────────────────────────────────
    def start(self) -> None:
        log.info("starting pidog app")
        self.body.start()
        self.io.start()
        self.brain.setup()

    def stop(self) -> None:
        log.info("stopping pidog app")
        try:
            self.io.stop()
        finally:
            try:
                self.camera.close()
            finally:
                self.body.stop()

    # ── main loop ────────────────────────────────────────────────────────
    def run(self) -> None:
        self.start()
        voice = VoiceIO(            
            stt_language="en-us",
            tts_model="en_US-ryan-low",
            keyboard_enable=True)
        voice.speak("Hi there, I'm Scooby Doo. Ask me and I will do whatever you want. Type quit to stop playing.")
        try:
            while True:
                user_text = self.io.listen()
                if not user_text:
                    continue
                if user_text.strip().lower() in {"quit", "exit"}:
                    break
                reply = self.brain.handle(user_text)
                self.io.speak(reply)
        except KeyboardInterrupt:
            pass
        finally:
            self.stop()


def _level_to_int(value) -> int:
    """Accept either a numeric level (e.g. ``20``) or a name (e.g. ``"INFO"``)."""
    if isinstance(value, int):
        return value
    # ``getLevelName`` maps "INFO" -> 20 (and "WARN" -> 30, etc.).
    level = logging.getLevelName(str(value).upper())
    if isinstance(level, int):
        return level
    # Unknown level name -> fall back to INFO.
    return logging.INFO


def _configure_logging(cfg: Config) -> None:
    """Attach a single ``FileHandler`` to the parent ``pidog_app`` logger.

    Every subsystem uses a child logger (``pidog_app.brain.brain``,
    ``pidog_app.dog.body``, ...) created via ``logging.getLogger(__name__)``.
    Child loggers propagate their records up to this parent, so all output
    lands in the configured log file while preserving the per-module name in
    each record.

    Reads ``logging.filename`` and ``logging.level`` from ``cfg`` (with
    sensible defaults) so logging can be tuned from ``config.yaml``.
    """
    filename = cfg.get("logging.filename", "app.log")
    level = _level_to_int(cfg.get("logging.level", logging.INFO))

    root = logging.getLogger(ROOT_LOGGER_NAME)
    root.setLevel(level)
    # Avoid stacking duplicate handlers if main() is re-entered (e.g. tests).
    if not any(isinstance(h, logging.FileHandler) and
               getattr(h, "_pidog_app", False) for h in root.handlers):
        handler = logging.FileHandler(filename)
        handler.setLevel(level)
        handler.setFormatter(logging.Formatter(
            "%(asctime)s %(levelname)s %(name)s: %(message)s"
        ))
        handler._pidog_app = True  # marker so we don't add it twice
        root.addHandler(handler)


def main() -> int:
    config_path = sys.argv[1] if len(sys.argv) > 1 else None
    cfg = load_config(config_path)
    _configure_logging(cfg)
    app = App(cfg)
    app.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
