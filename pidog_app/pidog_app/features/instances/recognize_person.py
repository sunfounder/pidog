"""Recognize a person in front of the dog.

Uses the camera face detector. The dog looks for a face, wags its tail
and barks a greeting when someone is recognized. (Face *identification* —
telling specific people apart — can be layered on later by adding a
face-classification model in :mod:`pidog_app.vision`.)
"""
from __future__ import annotations

import logging
import time

from pidog.action_flow import ActionStatus

from ..base import Feature, FeatureResult

log = logging.getLogger(__name__)


class RecognizePerson(Feature):
    name = "recognize_person"
    description = (
        "Look for a person in front of the dog using the camera's face "
        "detector. If a face is found the dog wags its tail and greets "
        "them. Use this when the user says 'who is there', 'do you see "
        "someone', or 'greet me'."
    )

    def run(self, **kwargs) -> FeatureResult:
        log.info("recognize_person")
        self.body.set_status(ActionStatus.ACTIONS)
        self.camera.start()
        self.camera.face_detect(on=True)
        try:
            found = self._scan_for_face()
        finally:
            self.camera.face_detect(on=False)
            self.body.set_status(ActionStatus.STANDBY)

        if found:
            self.body.do("wag tail", "bark")
            self.body.wait_done()
            return FeatureResult(
                text="I see someone in front of me — wagging my tail and saying hi!",
                success=True,
            )
        return FeatureResult(
            text="I looked around but I don't see anyone right now.",
            success=False,
        )

    def _scan_for_face(self, sweeps: int = 3, dwell: float = 1.0) -> bool:
        positions = [[-50, 0, 0], [0, 0, 0], [50, 0, 0], [0, 0, 0]]
        for _ in range(sweeps):
            for yrp in positions:
                self.body.head_move([yrp], immediately=True, speed=70)
                time.sleep(dwell)
                if self.camera.detected_faces() > 0:
                    return True
        return False
