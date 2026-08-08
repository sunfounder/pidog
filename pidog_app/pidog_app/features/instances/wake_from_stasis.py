"""Wake the dog from dormant stasis.

The dog performs a stretch + stand sequence and announces it is awake.
This is the entry feature when the dog has been sitting idle / powered
into a low-power posture.
"""
from __future__ import annotations

import logging

from pidog.action_flow import ActionStatus, Posetures

from ..base import Feature, FeatureResult

log = logging.getLogger(__name__)


class WakeFromStasis(Feature):
    name = "wake_from_stasis"
    description = (
        "Wake the dog up from dormant stasis. The dog stretches, stands up, "
        "lights its chest, and signals it is ready to interact. Use this "
        "when the dog has been idle or when the user says 'wake up'."
    )

    def run(self, **kwargs) -> FeatureResult:
        log.info("waking from stasis")
        self.body.light("breath", "cyan", 1)
        self.body.set_status(ActionStatus.ACTIONS)
        # Stretch first (loosens servos), then stand.
        self.body.do("stretch")
        self.body.wait_done()
        self.body.stand()
        self.body.wait_done()
        self.body.do("nod")
        self.body.wait_done()
        self.body.set_status(ActionStatus.STANDBY)
        return FeatureResult(
            text="I've woken up, stretched, and I'm standing ready.",
            success=True,
        )
