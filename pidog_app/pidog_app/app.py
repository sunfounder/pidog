"""Application wiring: dependency injection + main loop.

This module builds the object graph (config -> dog -> senses -> camera ->
features -> registry -> brain -> io) and runs the conversation loop.
"""
from __future__ import annotations

import logging
import sys

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


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    config_path = sys.argv[1] if len(sys.argv) > 1 else None
    app = build_app(config_path)
    app.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
