"""IO interface definition."""
from __future__ import annotations

from abc import ABC, abstractmethod


class IO(ABC):
    """Abstract interaction interface: listen for input, speak output."""

    @abstractmethod
    def listen(self) -> str:
        """Block until the user provides input; return it as text."""

    @abstractmethod
    def speak(self, text: str) -> None:
        """Output the dog's reply (print, TTS, ...)."""

    @abstractmethod
    def start(self) -> None:
        """Perform any startup (welcome message, mic warm-up, ...)."""

    @abstractmethod
    def stop(self) -> None:
        """Release resources."""

    def prompt_label(self) -> str:
        """Label shown before the input prompt in text mode (optional)."""
        return ">>> "
