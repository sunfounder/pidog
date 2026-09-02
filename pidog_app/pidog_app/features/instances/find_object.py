"""Find an object in the dog's field of view.

Uses the camera + Vilib color or object detector. The dog scans left/right
with its head, reports whether the object was found and roughly where.
"""
from __future__ import annotations

import logging
import time

from pidog.action_flow import ActionStatus

from ..base import Feature, FeatureResult

log = logging.getLogger(__name__)


class FindObject(Feature):
    name = "find_object"
    description = (
        "Look for a specific object in front of the dog using the camera. "
        "The dog scans left and right with its head and reports whether the "
        "object was found. Currently supports color detection (red, green, "
        "blue, yellow) and QR codes."
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
                        "target": {
                            "type": "string",
                            "description": (
                                "What to look for. Supported: a color name "
                                "(red, green, blue, yellow) or 'qrcode'."
                            ),
                        },
                    },
                    "required": ["target"],
                },
            },
        }

    def run(self, target: str = "red", **kwargs) -> FeatureResult:
        log.info("find_object: target=%s", target)
        self.body.set_status(ActionStatus.THINK)
        self.camera.start()

        target = target.lower().strip()
        found = False
        detail = ""

        try:
            if target == "qrcode":
                self.camera.qrcode_detect(on=True)
                detail = self._scan_for(lambda: self.camera.qrcode() is not None)
                if detail:
                    found = True
                    detail = f"QR code: {self.camera.qrcode()}"
                self.camera.qrcode_detect(on=False)
            elif target in {"red", "green", "blue", "yellow"}:
                self.camera.color_detect(target)
                detail = self._scan_for(lambda: self.camera.detected_color() is not None)
                found = bool(detail)
                if found:
                    detail = f"found {target}"
                self.camera.color_detect_off()
            else:
                return FeatureResult(
                    text=f"I can't detect '{target}' yet. Try a color or 'qrcode'.",
                    success=False,
                )
        finally:
            self.body.set_status(ActionStatus.STANDBY)

        if found:
            return FeatureResult(text=f"I found the {target}. {detail}", success=True)
        return FeatureResult(
            text=f"I scanned left and right but couldn't find {target}.",
            success=False,
        )

    def _scan_for(self, predicate, sweeps: int = 3, dwell: float = 1.0) -> str:
        """Sweep head left/right; return non-empty string when predicate fires."""
        positions = [[-60, 0, 0], [0, 0, 0], [60, 0, 0], [0, 0, 0]]
        for _ in range(sweeps):
            for yrp in positions:
                self.body.head_move([yrp], immediately=True, speed=70)
                time.sleep(dwell)
                if predicate():
                    return "hit"
        return ""
