"""Perform one or more named body actions.

The LLM can ask the dog to move or do tricks. Valid action names are the
``@property`` names on :class:`pidog.actions_dictionary.ActionDict`
(e.g. ``wag_tail``, ``shake_head``, ``forward``). Names that also exist
in :class:`pidog.action_flow.Operations` are queued through
``body.do_action_flow`` so they get posture transitions and
before/after hooks; dictionary-only names run directly through
``body.do_action``.
"""
from __future__ import annotations

import logging

from pidog.action_flow import ActionStatus, Operations
from pidog.actions_dictionary import ActionDict

from ..base import Feature, FeatureResult

log = logging.getLogger(__name__)

# Names offered to the LLM = every @property on ActionDict (underscore
# spelling, e.g. "wag_tail"). ActionDict.__getitem__ also accepts the
# space-separated spelling, so names are normalised before lookup.
ACTION_NAMES = sorted(
    name for name, attr in vars(ActionDict).items()
    if isinstance(attr, property)
)

# Operations values ("wag tail", "turn left", ...) that route through
# ActionFlow for proper posture handling.
_OPERATION_VALUES = {op.value for op in Operations}


class PerformActions(Feature):
    name = "perform_actions"
    description = (
        "Perform one or more physical body actions or tricks, e.g. "
        "'wag_tail', 'shake_head', 'forward', 'sit', 'stretch', or "
        "'push_up'. Use this when the user asks the dog to move or do a "
        "trick, or when the conversation calls for a gesture."
    )

    def build_schema(self) -> dict:
        schema = super().build_schema()
        schema["function"]["parameters"] = {
            "type": "object",
            "properties": {
                "actions": {
                    "type": "array",
                    "description": "Action names to perform, in order.",
                    "items": {"type": "string", "enum": ACTION_NAMES},
                    "minItems": 1,
                },
            },
            "required": ["actions"],
        }
        return schema

    def run(self, actions=None, **kwargs) -> FeatureResult:
        log.info("perform_actions: %s", actions)
        if not isinstance(actions, list) or not actions:
            return FeatureResult(
                text="No valid actions were given to perform.",
                success=False,
            )

        done, unknown = [], []
        # THINK suppresses the standby loop's random fidget actions so
        # they can't fight the servos mid-sequence.
        self.body.set_status(ActionStatus.THINK)
        try:
            for raw in actions:
                name = str(raw).strip().lower().replace(" ", "_")
                if name not in ACTION_NAMES:
                    unknown.append(str(raw))
                    continue
                self._perform(name)
                done.append(name)
        finally:
            self.body.set_status(ActionStatus.STANDBY)

        if unknown:
            log.warning("unknown actions requested: %s", unknown)
        text = f"I performed: {', '.join(done)}." if done else "I couldn't perform any of those."
        if unknown:
            text += f" Unknown actions: {', '.join(unknown)}."
        return FeatureResult(text=text, success=bool(done))

    def _perform(self, name: str) -> None:
        op_value = name.replace("_", " ")
        if op_value in _OPERATION_VALUES:
            # e.g. "wag tail", "turn left" — ActionFlow adds posture
            # transitions and before/after hooks.
            self.body.do_action_flow(op_value)
            self.body.wait_done()
            # wait_done() returns once the queue drains back to STANDBY;
            # re-assert THINK so standby fidgets don't slip between
            # actions in a multi-action sequence.
            self.body.set_status(ActionStatus.THINK)
            return
        # Dictionary-only action: run it directly. Legs gaits (e.g.
        # 'trot') need a standing base — the dog idles sitting.
        _, part = self.body.dog.actions_dict[name]
        if part == "legs":
            self.body.stand()
        self.body.do_action(name, step_count=1, speed=80)
        self.body.wait_all_done()
