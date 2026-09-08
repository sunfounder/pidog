"""Feature base class and result type."""
from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

log = logging.getLogger(__name__)


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

    Subclasses set ``name`` and ``description`` and implement :meth:`run`
    and :meth:`build_schema`. They receive the shared :class:`Body`,
    :class:`Senses`, and :class:`Camera` facades via the constructor so
    they never touch the raw SunFounder libraries.
    """

    name: str = ""
    description: str = ""

    def __init__(self, body=None, senses=None, camera=None):
        # ``body``/``senses``/``camera`` are normally injected by the app.
        # They default to None so features can be instantiated in tests
        # without hardware, and so simple features that don't need them
        # can omit the arguments.
        self.body = body
        self.senses = senses
        self.camera = camera

    @abstractmethod
    def run(self, **kwargs: Any) -> FeatureResult:
        """Execute the feature. Arguments come from the LLM tool call."""

    def build_schema(self) -> dict:
        """Return the OpenAI-style function/tool spec for this feature.

        Default implementation builds a parameterless tool from
        ``name``/``description``. Override to add parameters.
        """
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }

    def __repr__(self) -> str:
        return f"<Feature {self.name}>"
