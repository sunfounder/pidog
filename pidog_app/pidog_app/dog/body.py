"""Body facade: movement, posture, head, tail, and the chest light strip.

Wraps :class:`pidog.Pidog` and :class:`pidog.ActionFlow` so feature code
stays decoupled from the SunFounder API.
"""
from __future__ import annotations

import logging
from typing import Iterable

from pidog.pidog import Pidog
from pidog.action_flow import ActionFlow, ActionStatus, Operations, Posetures

log = logging.getLogger(__name__)


class Body:
    """High-level control of the dog's actuators and chest RGB strip."""

    def __init__(self, dog: Pidog | None = None):
        # ``Pidog()`` talks to I2C hardware; allow injection for tests.
        self.dog = dog if dog is not None else Pidog()
        self.action_flow = ActionFlow(self.dog)

    # ── lifecycle ────────────────────────────────────────────────────────
    def start(self) -> None:
        """Start the action-flow thread and sit up."""
        self.action_flow.start()
        self.dog.rgb_strip.close()
        self.change_posture(Posetures.SIT)

    def stop(self) -> None:
        """Stop actuators and release hardware cleanly."""
        try:
            self.action_flow.stop()
        finally:
            self.dog.close()

    # ── posture ──────────────────────────────────────────────────────────
    def change_posture(self, posture: Posetures) -> None:
        self.action_flow.change_poseture(posture)

    def sit(self) -> None:
        self.change_posture(Posetures.SIT)

    def stand(self) -> None:
        self.change_posture(Posetures.STAND)

    def lie(self) -> None:
        self.change_posture(Posetures.LIE)

    # ── actions ──────────────────────────────────────────────────────────
    def do(self, *actions: str | Operations) -> None:
        """Queue one or more named actions (e.g. ``body.do("bark", "nod")``)."""
        self.action_flow.add_action(*actions)

    def wait_done(self) -> None:
        """Block until all queued actions finish."""
        self.action_flow.wait_actions_done()

    def set_status(self, status: ActionStatus) -> None:
        self.action_flow.set_status(status)

    # ── chest light strip ────────────────────────────────────────────────
    def light(self, mode: str, color: str, speed: int = 1) -> None:
        """Set the chest RGB strip mode (e.g. 'breath', 'listen', 'close')."""
        self.dog.rgb_strip.set_mode(mode, color, speed)

    def light_off(self) -> None:
        self.dog.rgb_strip.close()

    # ── head ─────────────────────────────────────────────────────────────
    def head_move(self, yrp_list: Iterable[list], immediately: bool = False,
                  speed: int = 80) -> None:
        """Move head to [yaw, roll, pitch] points."""
        self.dog.head_move(list(yrp_list), immediately=immediately, speed=speed)

    # ── convenience ──────────────────────────────────────────────────────
    @property
    def available_actions(self) -> list[str]:
        """Names of all actions the ActionFlow knows how to run."""
        return [op.value for op in Operations]
