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
        self.body.stand()
        self.body.set_status(ActionStatus.THINK)
        self.camera.start()
        self.camera.display(local=False, web=True)
        self.camera.face_detect(on=True)
        try:
            #found = self._scan_for_face()
            self._track_face()
            found = True

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

    def _scan_for_face(self, sweeps: int = 3, dwell: float = 1.0, pitch_compensate: int = -40) -> bool:
        positions = [[-50, 0, 0], [0, 0, 0], [50, 0, 0], [0, 0, 0]]
        for _ in range(sweeps):
            for yrp in positions:
                self.body.head_move([yrp], pitch_comp=pitch_compensate, immediately=True, speed=30)
                time.sleep(dwell)
                if self.camera.detected_faces() > 0:
                    return True
        return False

    def _track_face(self) -> bool:
        yaw = 0
        roll = 0
        pitch = 0
        flag = False
        direction = 0

        self.body.sit()
        self.body.head_move([[yaw, 0, pitch]], roll_comp=0, pitch_comp=-40, immediately=True, speed=40)
        self.body.wait_all_done()
        time.sleep(0.5)
        # Cleanup sound detection by servos moving
        if self.senses.is_sound_detected():    
            direction = self.senses.sound_direction()

        while True:
            if flag == False:
                self.body.rgb_strip.set_mode('breath', 'pink', bps=1)
            # If heard somthing, turn to face it
            if self.senses.is_sound_detected():
                flag = False
                direction = self.senses.sound_direction()
                pitch = 0
                if direction > 0 and direction < 160:
                    yaw = -direction
                    if yaw < -80:
                        yaw = -80
                elif direction > 200 and direction < 360:
                    yaw = 360 - direction
                    if yaw > 80:
                        yaw = 80
                self.body.head_move([[yaw, 0, pitch]], roll_comp=0, pitch_comp=-40, immediately=True, speed=40)
                self.body.wait_head_done()
                time.sleep(0.05)

            ex = Vilib.detect_obj_parameter['human_x'] - 320
            ey = Vilib.detect_obj_parameter['human_y'] - 240
            people = Vilib.detect_obj_parameter['human_n']

            # If see someone, bark at him/her
            if people > 0 and flag == False:
                flag = True
                self.body.do_action('wag_tail', step_count=2, speed=100)
                #bark(self.body, [yaw, 0, 0], pitch_comp=-40, volume=80)
                if self.senses.is_sound_detected():
                    direction = self.sensens.sound_direction()

            if ex > 15 and yaw > -80:
                yaw -= 0.5 * int(ex/30.0+0.5)

            elif ex < -15 and yaw < 80:
                yaw += 0.5 * int(-ex/30.0+0.5)

            if ey > 25:
                pitch -= 1*int(ey/50+0.5)
                if pitch < - 30:
                    pitch = -30
            elif ey < -25:
                pitch += 1*int(-ey/50+0.5)
                if pitch > 30:
                    pitch = 30

            print('direction: %s |number: %s | ex, ey: %s, %s | yrp: %s, %s, %s '
                % (direction, people, ex, ey, round(yaw, 2), round(roll, 2), round(pitch, 2)),
                end='\r',
                flush=True,
                )
            self.body.head_move([[yaw, 0, pitch]], pitch_comp=-40, immediately=True, speed=80)
            time.sleep(0.05)

    def stop_tracing():
        self.camera.face_detect(on=False)