"""Feature registry: collects features and exposes them to the brain."""
from __future__ import annotations

import logging
from typing import Iterable

from .base import Feature

log = logging.getLogger(__name__)


class FeatureRegistry:
    """Holds the set of features available to the dog.

    The brain asks the registry for the ``tools`` array (one entry per
    feature) and looks up a feature by name when the LLM emits a tool call.
    """

    def __init__(self, features: Iterable[Feature] | None = None):
        self._features: dict[str, Feature] = {}
        if features:
            for f in features:
                self.register(f)

    def register(self, feature: Feature) -> None:
        if not feature.name:
            raise ValueError(f"Feature {feature} has no name")
        if feature.name in self._features:
            raise ValueError(f"Duplicate feature name: {feature.name}")
        self._features[feature.name] = feature
        log.debug("registered feature: %s", feature.name)

    def get(self, name: str) -> Feature | None:
        return self._features.get(name)

    def names(self) -> list[str]:
        return list(self._features.keys())

    def tools(self) -> list[dict]:
        """OpenAI-style ``tools`` array for the LLM request."""
        return [f.build_schema() for f in self._features.values()]

    def __iter__(self):
        return iter(self._features.values())

    def __len__(self) -> int:
        return len(self._features)
