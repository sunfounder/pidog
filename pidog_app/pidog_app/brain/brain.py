"""Brain: the LLM tool-calling loop.

The brain talks to Ollama (via the existing :class:`sunfounder_voice_assistant.llm.LLM`
wrapper, which speaks the OpenAI-compatible API), sends the feature
schemas as ``tools``, dispatches any tool call to the
:class:`FeatureRegistry`, and returns the model's final text reply.

The existing wrapper's ``prompt()`` strips ``tool_calls`` from the
response, so the brain calls ``chat()`` directly and manages the message
list itself to support the OpenAI tool-calling protocol.
"""
from __future__ import annotations

import json
import logging
from typing import Any, Optional

from ..features import FeatureRegistry
from .prompt import build_system_prompt

log = logging.getLogger(__name__)

# Safety cap on tool-call round-trips per user turn.
MAX_TOOL_ROUNDS = 3


class Brain:
    """LLM-driven reasoning loop that decides chat-vs-feature."""

    def __init__(self, llm, registry: FeatureRegistry, name: str = "Scooby Doo"):
        self.llm = llm
        self.registry = registry
        self.name = name
        self._setup_done = False

    # ── setup ────────────────────────────────────────────────────────────
    def setup(self) -> None:
        """Configure the LLM with the system prompt and message limit."""
        system_prompt = build_system_prompt(self.name, self.registry)
        self.llm.set_instructions(system_prompt)
        self._setup_done = True
        log.info("brain ready; features: %s", self.registry.names())

    # ── main entry ───────────────────────────────────────────────────────
    def handle(self, user_text: str) -> str:
        """Process one user turn and return the dog's reply text.

        May invoke zero or one feature (tool) along the way.
        """
        if not self._setup_done:
            self.setup()

        self.llm.add_message("user", user_text)
        tools = self.registry.tools()

        for round_idx in range(MAX_TOOL_ROUNDS):
            message = self._chat_raw(tools=tools if tools else None)
            tool_calls = message.get("tool_calls")
            content = message.get("content") or ""

            if not tool_calls:
                # Plain reply — record and return.
                self.llm.add_message("assistant", content)
                return content

            # Record the assistant message *with* its tool_calls so the
            # model sees the call history on the next round.
            self.llm.messages.append({
                "role": "assistant",
                "content": content,
                "tool_calls": tool_calls,
            })

            # Dispatch every tool call (usually just one) and feed results back.
            for call in tool_calls:
                result_text = self._dispatch(call)
                self.llm.messages.append({
                    "role": "tool",
                    "tool_call_id": call.get("id", ""),
                    "content": result_text,
                })
            # Loop again so the model can compose a reply from the tool results.

        # Exhausted rounds: return whatever we have.
        return "I tried but couldn't finish that in time."

    # ── internals ────────────────────────────────────────────────────────
    def _chat_raw(self, tools: Optional[list] = None) -> dict:
        """Call llm.chat() and return the raw assistant ``message`` dict."""
        kwargs: dict[str, Any] = {"stream": False}
        if tools:
            kwargs["tools"] = tools
        response = self.llm.chat(**kwargs)
        data = response.json()
        if "error" in data:
            raise RuntimeError(f"LLM error: {data['error'].get('message', data['error'])}")
        return data["choices"][0]["message"]

    def _dispatch(self, call: dict) -> str:
        """Run one tool call and return a string result for the model."""
        fn = call.get("function", {}) or {}
        name = fn.get("name", "")
        raw_args = fn.get("arguments", "{}")
        try:
            args = json.loads(raw_args) if isinstance(raw_args, str) else (raw_args or {})
        except json.JSONDecodeError:
            args = {}

        feature = self.registry.get(name)
        if feature is None:
            log.warning("model called unknown tool: %s", name)
            return f"Error: unknown tool '{name}'."

        log.info("dispatching tool: %s args=%s", name, args)
        try:
            result = feature.run(**args)
            text = result.text
            if result.extra:
                text += f"\n(extra: {json.dumps(result.extra)})"
            return text
        except Exception as e:
            log.exception("feature %s failed", name)
            return f"Error running {name}: {e}"
