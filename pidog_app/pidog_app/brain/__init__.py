"""Brain layer.

The brain is the LLM-driven reasoning loop. It:

1. Builds a system prompt describing the dog and its available features.
2. Sends the user's message + feature schemas (as ``tools``) to Ollama.
3. If the model emits a tool call, dispatches it to the matching feature
   and feeds the result back to the model.
4. Returns the model's final text reply (or speaks it via the IO layer).

The brain never touches hardware directly — it goes through the
:class:`FeatureRegistry`.
"""
from .brain import Brain
from .prompt import build_system_prompt

__all__ = ["Brain", "build_system_prompt"]
