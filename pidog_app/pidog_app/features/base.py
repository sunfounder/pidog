"""Feature base class and result type."""
from __future__ import annotations

import logging
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable

log = logging.getLogger(__name__)

# Default head positions ([yaw, roll, pitch]) swept while scanning.
SCAN_POSITIONS = ((-60, 0, 0), (0, 0, 0), (60, 0, 0), (0, 0, 0))

_NO_PARAMETERS = {
    "type": "object",
    "properties": {},
    "required": [],
}


@dataclass
class FeatureResult:
    """Outcome of running a feature.

    Attributes:
        text:    Human-readable summary the LLM should use to compose its
                 spoken/written reply.
        success: Whether the feature achieved its goal.
        extra:   Optional structured payload (e.g. detected labels) the
                 brain may pass back to the LLM as tool result metadata.
    """
    text: str
    success: bool = True
    extra: dict = field(default_factory=dict)


class Feature(ABC):
    """Base class for all dog features.

    Subclasses set ``name`` and ``description`` and implement :meth:`run`.
    They receive the shared :class:`Body`, :class:`Senses`, and
    :class:`Camera` facades via the constructor so they never touch the
    raw SunFounder libraries.

    Attributes:
        parameters: OpenAI-style ``parameters`` object for the tool
                    schema. Leave as ``None`` for a parameterless tool.
    """

    name: str = ""
    description: str = ""
    parameters: dict | None = None

    def __init__(self, body=None, senses=None, camera=None, cfg=None):
        # ``body``/``senses``/``camera``/``cfg`` are normally injected by
        # the app. They default to None so features can be instantiated in
        # tests without hardware, and so simple features that don't need
        # them can omit the arguments.
        self.body = body
        self.senses = senses
        self.camera = camera
        self.cfg = cfg

    @abstractmethod
    def run(self, **kwargs: Any) -> FeatureResult:
        """Execute the feature. Arguments come from the LLM tool call."""

    def build_schema(self) -> dict:
        """Return the OpenAI-style function/tool spec for this feature."""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters or dict(_NO_PARAMETERS),
            },
        }

    # ── shared helpers ───────────────────────────────────────────────────
    def sweep_scan(
        self,
        predicate: Callable[[], bool],
        positions: Iterable = SCAN_POSITIONS,
        sweeps: int = 3,
        dwell: float = 1.0,
        speed: int = 70,
        pitch_comp: int = 0,
    ) -> bool:
        """Sweep the head through ``positions`` until ``predicate`` fires.

        Moves through each [yaw, roll, pitch] position, dwells, then checks
        ``predicate``. Returns True as soon as it reports True; False after
        ``sweeps`` full passes with no hit.
        """
        for _ in range(sweeps):
            for yrp in positions:
                self.body.head_move(
                    [list(yrp)], pitch_comp=pitch_comp,
                    immediately=True, speed=speed,
                )
                time.sleep(dwell)
                if predicate():
                    return True
        return False

    def __repr__(self) -> str:
        return f"<Feature {self.name}>"
