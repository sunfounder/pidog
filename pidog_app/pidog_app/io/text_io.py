"""Text-mode IO: a simple REPL."""
from __future__ import annotations

import logging
import sys

from .base import IO

log = logging.getLogger(__name__)


class TextIO(IO):
    """Reads from stdin, writes to stdout. Useful for development."""

    def __init__(self, welcome: str = ""):
        self.welcome = welcome

    def start(self) -> None:
        if self.welcome:
            print(self.welcome)

    def listen(self) -> str:
        try:
            return input(self.prompt_label())
        except (EOFError, KeyboardInterrupt):
            return "quit"

    def speak(self, text: str) -> None:
        print(text)

    def stop(self) -> None:
        pass
