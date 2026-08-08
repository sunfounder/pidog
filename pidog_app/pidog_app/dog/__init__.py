"""Dog facade layer.

Thin wrappers around the SunFounder ``Pidog`` / ``ActionFlow`` classes and
the onboard sensors. Features depend on these facades, never on the raw
library classes, so the underlying libraries can be swapped or mocked.
"""
from .body import Body
from .senses import Senses

__all__ = ["Body", "Senses"]
