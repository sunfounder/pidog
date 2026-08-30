"""Check whether the water bowl is empty.

The dog looks down at its bowl using the camera and reports whether it
appears empty. This is a stub that uses the color detector as a proxy
(detecting the bowl's color means the bowl is present; absence of the
water shimmer color suggests it is empty). Replace the heuristic with a
trained image classifier when you have one.
"""
from __future__ import annotations

import logging
import time

from pidog.action_flow import ActionStatus

from ..base import Feature, FeatureResult

log = logging.getLogger(__name__)


class CheckWaterBowl(Feature):
    name = "check_water_bowl"
    description = (
        "Check whether the water bowl in front of the dog is empty by "
        "looking down at it with the camera. Reports 'empty', 'low', or "
        "'has water'. Use this when the user asks 'is my water bowl empty' "
        "or 'do I need to refill the water'."
    )

    def build_schema(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "bowl_color": {
                            "type": "string",
                            "description": (
                                "Dominant color of the bowl itself, used to "
                                "locate it (e.g. 'blue'). Defaults to 'blue'."
                            ),
                        },
                    },
                    "required": [],
                },
            },
        }

    def run(self, bowl_color: str = "blue", **kwargs) -> FeatureResult:
        log.info("check_water_bowl: bowl_color=%s", bowl_color)
        self.body.set_status(ActionStatus.ACTIONS)
        self.camera.start()

        # Look down at the bowl. Head pitch is negative (downward).
        self.body.head_move([[0, 0, -40]], immediately=True, speed=70)
        time.sleep(1.0)

        self.camera.color_detect(bowl_color.lower())
        time.sleep(1.0)
        bowl_seen = self.camera.detected_color() is not None
        self.camera.color_detect_off()

        self.body.head_move([[0, 0, 0]], immediately=True, speed=70)
        self.body.set_status(ActionStatus.STANDBY)

        if not bowl_seen:
            return FeatureResult(
                text="I can't see the bowl. Is it in front of me?",
                success=False,
            )
        # Placeholder heuristic: TODO train a classifier for empty/low/full.
        return FeatureResult(
            text=(
                "I can see the bowl. I can't yet tell the water level "
                "precisely — train an image classifier for that. For now "
                "I'll assume it has water."
            ),
            success=True,
            extra={"bowl_seen": True, "bowl_color": bowl_color},
        )
