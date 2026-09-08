"""Vision facade: camera + computer-vision helpers over ``vilib.Vilib``.

Features call :class:`Camera` methods instead of touching ``Vilib``
directly, so detection backends can be swapped or mocked.
"""
from .camera import Camera

__all__ = ["Camera"]
