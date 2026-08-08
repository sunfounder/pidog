"""IO layer: text and voice interaction modes behind a common interface.

The brain is IO-agnostic. The :class:`IO` interface lets the dog listen
for user input and speak replies. :class:`TextIO` is a simple REPL;
:class:`VoiceIO` wraps the SunFounder STT/TTS (Vosk + Piper) and the
wake-word loop. Switch via ``io.mode`` in ``config.yaml``.
"""
from .base import IO
from .text_io import TextIO
from .voice_io import VoiceIO

__all__ = ["IO", "TextIO", "VoiceIO"]
