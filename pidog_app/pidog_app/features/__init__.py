"""Feature layer.

A *feature* is a self-contained capability the dog can perform on demand
(wake from stasis, find an object, recognize a person, check the water
bowl, ...). Each feature exposes:

* ``schema``      — an OpenAI-style tool/function spec the LLM uses to
                    decide when to invoke it and what arguments to pass.
* ``run(**args)`` — executes the feature, returning a human-readable
                    result string that the LLM folds back into the chat.

The :class:`FeatureRegistry` collects all features and produces the
``tools`` array the brain sends to the model.
"""
from .base import Feature, FeatureResult
from .registry import FeatureRegistry

__all__ = ["Feature", "FeatureResult", "FeatureRegistry"]
