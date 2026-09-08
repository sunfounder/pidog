"""Senses facade: read-only access to the dog's sensors.

Exposes ultrasonic distance, head touch, IMU (gyro/accel), and sound
direction as simple methods. Features query senses through this object
rather than poking ``Pidog`` attributes directly.
"""
from __future__ import annotations

import logging
from typing import Tuple

from pidog.pidog import Pidog
from pidog.dual_touch import TouchStyle

log = logging.getLogger(__name__)


class Senses:
    """Read-only sensor access over a :class:`Pidog` instance."""

    def __init__(self, dog: Pidog):
        self.dog = dog

    # ── ultrasonic "eyes" ────────────────────────────────────────────────
    def distance_cm(self) -> float:
        """Distance to the nearest obstacle in centimetres (0 = no echo)."""
        return float(self.dog.read_distance())

    def too_close(self, threshold_cm: float = 10.0) -> bool:
        d = self.distance_cm()
        return 1.0 < d < threshold_cm

    # ── head touch sensors ───────────────────────────────────────────────
    def touch(self) -> str:
        """Current touch gesture code on the head sensors.

        One of: ``'N'`` (none), ``'L'`` (rear), ``'R'`` (front),
        ``'LS'`` (rear->front slide), ``'RS'`` (front->rear slide).
        Compare with :class:`pidog.dual_touch.TouchStyle`.
        """
        return self.dog.dual_touch.read()

    def is_petted(self) -> bool:
        """True when any touch style is currently active (not 'N')."""
        return self.dog.dual_touch.read() != TouchStyle.NONE.value

    # ── 6-axis IMU (SH3001) ──────────────────────────────────────────────
    def imu(self) -> Tuple[list, list]:
        """Return ``(acc, gyro)`` as 3-element lists ``[x, y, z]``.

        Values are populated continuously by the Pidog IMU background thread.
        """
        return list(self.dog.accData), list(self.dog.gyroData)

    def attitude(self) -> Tuple[float, float]:
        """Return ``(pitch, roll)`` in degrees from the IMU.

        Yaw is not provided by the SH3001 integration in pidog.
        """
        return float(self.dog.pitch), float(self.dog.roll)

    # ── sound direction ──────────────────────────────────────────────────
    def is_sound_detected(self) -> bool:
        """True when sound direction is detected (busy line pulled LOW by 064B)."""
        return self.dog.ears.isdetected()
    
    def sound_direction(self) -> int:
        """Direction of the last detected sound (angle index, -1 = none)."""
        return self.dog.ears.read()
