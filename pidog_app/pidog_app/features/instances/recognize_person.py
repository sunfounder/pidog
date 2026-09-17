"""Recognize a person in front of the dog.

Uses the camera face detector. The dog looks for a face, wags its tail
and barks a greeting when someone is recognized. (Face *identification* —
telling specific people apart — can be layered on later by adding a
face-classification model in :mod:`pidog_app.vision`.)
"""
from __future__ import annotations

import logging
import select
import sys
import time

from pidog.action_flow import Operations

from ..base import Feature, FeatureResult

log = logging.getLogger(__name__)


def _stdin_pollable() -> bool:
    """True when sys.stdin can be polled by select()."""
    try:
        sys.stdin.fileno()
        return True
    except Exception:
        return False


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
        with self.body.thinking():
            self.camera.start()
            self.camera.display(local=False, web=True)
            self.camera.face_detect(on=True)
            try:
                face_track_time = self.cfg.get("vision.face_track_timeout", 30.0)
                face_track_seen_hold = self.cfg.get("vision.face_track_seen_hold", 10.0)
                found = self._track_face(timeout = face_track_time, seen_hold = face_track_seen_hold)
            finally:
                self.camera.face_detect(on=False)

        if found:
            self.body.do_and_wait(Operations.WAG_TAIL, Operations.BARK)
            return FeatureResult(
                text="I see someone in front of me — wagging my tail and saying hi!",
                success=True,
            )
        return FeatureResult(
            text="I looked around but I don't see anyone right now.",
            success=False,
        )

    def _look(self, yaw: float, pitch: float, speed: int = 40) -> None:
        """Point the head at [yaw, 0, pitch] with -40 pitch compensation."""
        self.body.head_move([[yaw, 0, pitch]], pitch_comp=-40, immediately=True, speed=speed)

    def _track_face(self, timeout: float = 20.0, seen_hold: float = 3.0) -> bool:
        """Look for a face and follow it with the head.

        Returns True if a face was seen. The loop ends when:
          * ``seen_hold`` seconds pass after the first detection (the
            greeting has been given, so the feature can return);
          * ``timeout`` seconds elapse with no face found; or
          * the user types 'stop tracking' / 'enough' into stdin
            (best-effort — skipped when stdin is unusable or already at
            EOF, e.g. when running as a service).

        ``timeout`` is a hard bound so :meth:`run` always returns a
        FeatureResult — previously this loop ran forever and hung the
        LLM tool call.
        """

        log.info(f"track face started with timeout={timeout}s, seen_hold={seen_hold}s")

        yaw = 0
        pitch = 0
        seen = False          # a face was detected at least once -> return value
        seen_at = None        # timestamp of the latest greeting -> seen_hold exit
        greeted = False       # greeting already issued for the current face
        direction = 0
        scan_yaw = 0
        scan_yaw_dir = 1
        scan_pitch = 0
        scan_pitch_dir = 1
        prev_yaw = None
        prev_pitch = None
        light_set = False
        warned: set[str] = set()   # each sensor failure is logged once

        def heard() -> bool:
            try:
                return bool(self.senses.is_sound_detected())
            except Exception as e:
                if "detect" not in warned:
                    log.warning("is_sound_detected failed: %s", e)
                    warned.add("detect")
                return False

        def sound_dir() -> int:
            try:
                return self.senses.sound_direction()
            except Exception as e:
                if "dir" not in warned:
                    log.warning("sound_direction failed: %s", e)
                    warned.add("dir")
                return -1

        start = time.time()
        stdin_ok = _stdin_pollable()

        self._look(yaw, pitch)
        self.body.wait_all_done()
        time.sleep(0.5)
        # Cleanup sound detection by servos moving
        if heard():
            direction = sound_dir()

        while True:
            # Check for keyboard input to stop tracking (best-effort;
            # skipped entirely when stdin isn't a pollable fd).
            if stdin_ok:
                try:
                    ready = select.select([sys.stdin], [], [], 0)[0]
                except (OSError, ValueError):
                    stdin_ok = False
                else:
                    if ready:
                        cmd = sys.stdin.readline().strip().lower()
                        if cmd == "":
                            stdin_ok = False   # EOF — stop polling
                        elif cmd in ("stop tracking", "enough", "enough tracking"):
                            log.info("face tracking stopped by user: %s", cmd)
                            break
            # Hard bound: always return so run() produces a FeatureResult.
            if time.time() - start >= timeout:
                log.info("face tracking timed out after %.0fs", timeout)
                break
            # Face already greeted — hold briefly then finish.
            if seen_at is not None and time.time() - seen_at >= seen_hold:
                break
            if not light_set:
                self.body.light(mode='breath', color='pink', speed=1)
                light_set = True
            # If heard something, turn to face
            if heard():
                greeted = False   # a new sound may reveal a face — greet again
                direction = sound_dir()
                pitch = 0
                if direction > 0 and direction < 160:
                    yaw = -direction
                    if yaw < -80:
                        yaw = -80
                elif direction > 200 and direction < 360:
                    yaw = 360 - direction
                    if yaw > 80:
                        yaw = 80
                self._look(yaw, pitch)
                self.body.wait_head_done()
                time.sleep(0.05)

            ex, ey, people = self.camera.detect_face()

            # If see someone, bark at him/her
            if people > 0 and not greeted:
                greeted = True
                seen = True
                seen_at = time.time()
                self.body.do_action('wag_tail', step_count=2, speed=100)
                try:
                    self.body.dog.speak('single_bark_1', 80)
                except Exception as e:
                    log.warning("bark sound failed: %s", e)

                if heard():
                    direction = sound_dir()

            if people > 0:
                # Track face: adjust yaw and pitch toward detected face
                # Use a generous deadzone so the head stays still once the
                # face is roughly centered, instead of constant micro-adjustments.
                if ex > 40 and yaw > -80:
                    yaw -= 0.5 * int(ex/30.0+0.5)

                elif ex < -40 and yaw < 80:
                    yaw += 0.5 * int(-ex/30.0+0.5)

                if ey > 40:
                    pitch -= 1*int(ey/50+0.5)
                    if pitch < - 30:
                        pitch = -30
                elif ey < -40:
                    pitch += 1*int(-ey/50+0.5)
                    if pitch > 30:
                        pitch = 30
            else:
                # No face found: scan left-right with a small up-down oscillation
                scan_yaw += scan_yaw_dir * 2
                if scan_yaw > 60:
                    scan_yaw = 60
                    scan_yaw_dir = -1
                elif scan_yaw < -60:
                    scan_yaw = -60
                    scan_yaw_dir = 1

                scan_pitch += scan_pitch_dir * 1.5
                if scan_pitch > 20:
                    scan_pitch = 20
                    scan_pitch_dir = -1
                elif scan_pitch < -20:
                    scan_pitch = -20
                    scan_pitch_dir = 1

                yaw = scan_yaw
                pitch = scan_pitch

            if yaw != prev_yaw or pitch != prev_pitch:
                self._look(yaw, pitch, speed=80)
                prev_yaw = yaw
                prev_pitch = pitch
            time.sleep(0.05)
        return seen
