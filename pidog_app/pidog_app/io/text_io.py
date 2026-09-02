"""Text-mode IO: a simple REPL."""
from __future__ import annotations

import logging
import sys
import time

from .base import IO

log = logging.getLogger(__name__)


class TextIO(IO):
    """Reads from stdin, writes to stdout. Useful for development."""

    def __init__(self, welcome: str = ""):
        self.welcome = welcome

    def start(self) -> None:
        if self.welcome:
            print(self.welcome)
        log.info("text io started")

    def listen(self) -> str:
        try:
            return input(self.prompt_label())
        except KeyboardInterrupt:
            return "quit"
        except EOFError:
            # stdin is closed (e.g. running as a systemd service). Don't
            # exit — sleep and return empty so the main loop keeps running
            # until an explicit "quit"/"exit" command arrives.
            time.sleep(1)
            return ""

    def speak(self, text: str) -> None:
        print(text)
        log.info("reply: %s", text)

    def play_sound(self, filename:str, volume: int = 50) -> None:
        pass

    def stop(self) -> None:
        log.info("text io stopped")
