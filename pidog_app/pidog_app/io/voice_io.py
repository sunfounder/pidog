"""Voice-mode IO: wake-word + STT (Vosk) + TTS (Piper).

Wraps the SunFounder STT/TTS engines. The dog listens for a wake word,
then transcribes one utterance and returns it. Replies are spoken via
TTS. Falls back to keyboard input alongside the microphone so you can
still type during development.
"""
from __future__ import annotations

import logging
import threading

from pidog.stt import STT
from pidog.tts import Piper
from pidog_app.dog import Body

from .base import IO

log = logging.getLogger(__name__)


class VoiceIO(IO):
    """Wake-word-driven voice interaction."""

    def __init__(
        self,
        welcome: str = "",
        wake_word: list[str] | None = None,
        answer_on_wake: str = "",
        stt_language: str = "en-us",
        tts_model: str = "en_US-ryan-low",
        keyboard_enable: bool = True,
        body: Body = None,
    ):
        self.welcome = welcome
        self.wake_word = [w.lower() for w in (wake_word or [])]
        self.answer_on_wake = answer_on_wake
        self.keyboard_enable = keyboard_enable
        self.body = body

        self.stt = STT(language=stt_language)
        self.tts = Piper(model=tts_model)

        self._keyboard_thread = None
        self._keyboard_text: list[str] = []
        self._running = False

    # ── lifecycle ────────────────────────────────────────────────────────
    def start(self) -> None:
        log.info("voice io starting")
        if self.welcome:
            self.tts.say(self.welcome)
        if self.keyboard_enable:
            self._running = True
            self._keyboard_thread = threading.Thread(
                target=self._keyboard_loop, daemon=True
            )
            self._keyboard_thread.start()

    def stop(self) -> None:
        self._running = False
        log.info("voice io stopping")
        try:
            self.stt.close()
        except Exception:
            log.debug("stt close failed", exc_info=True)

    # ── listen / speak ───────────────────────────────────────────────────
    def listen(self) -> str:
        # Drain any keyboard input first.
        if self._keyboard_text:
            text = self._keyboard_text.pop(0)
            log.info("keyboard input: %s", text)
            return text

        while self._running:
            text = self.stt.listen().strip().lower()
            if not text:
                continue
            # Wake-word gate.
            if self.wake_word and not any(w in text for w in self.wake_word):
                continue
            # Strip the wake word from the transcript.
            for w in self.wake_word:
                if text.startswith(w):
                    text = text[len(w):].strip()
            if self.answer_on_wake and not text:
                self.speak(self.answer_on_wake)
                continue
            if text:
                log.info("heard: %s", text)
                return text
        return "quit"

    def speak(self, text: str) -> None:
        if text:
            print(text)
            self.tts.say(text)
            log.info("reply: %s", text)

    def play_sound(self, filename: str, volume: int = 50) -> None:
        if filename:
            self.body.speak(filename, volume)

    # ── keyboard fallback ────────────────────────────────────────────────
    def _keyboard_loop(self) -> None:
        while self._running:
            try:
                line = input()
            except (EOFError, KeyboardInterrupt):
                self._running = False
                return
            if line.strip():
                self._keyboard_text.append(line.strip())
