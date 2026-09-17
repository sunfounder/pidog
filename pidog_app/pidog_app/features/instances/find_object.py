"""Find an object in the dog's field of view.

Uses the camera + Vilib color or object detector. The dog scans left/right
with its head, reports whether the object was found and roughly where.
"""
from __future__ import annotations

import logging

from ..base import Feature, FeatureResult

log = logging.getLogger(__name__)

COLORS = {"red", "green", "blue", "yellow"}


class FindObject(Feature):
    name = "find_object"
    description = (
        "Look for a specific object in front of the dog using the camera. "
        "The dog scans left and right with its head and reports whether the "
        "object was found. Currently supports color detection (red, green, "
        "blue, yellow) and QR codes."
    )
    parameters = {
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
    }

    def run(self, target: str = "red", **kwargs) -> FeatureResult:
        log.info("find_object: target=%s", target)
        target = target.lower().strip()
        with self.body.thinking():
            self.camera.start()
            detail = self._detect(target)

        if detail is None:
            return FeatureResult(
                text=f"I can't detect '{target}' yet. Try a color or 'qrcode'.",
                success=False,
            )
        if detail:
            return FeatureResult(text=f"I found the {target}. {detail}", success=True)
        return FeatureResult(
            text=f"I scanned left and right but couldn't find {target}.",
            success=False,
        )

    def _detect(self, target: str) -> str | None:
        """Run the matching detector and scan; return a detail string.

        Returns ``None`` for an unsupported target, ``""`` when the scan
        found nothing, or a non-empty detail string on a hit.
        """
        if target == "qrcode":
            self.camera.qrcode_detect(on=True)
            try:
                if self.sweep_scan(lambda: self.camera.qrcode() is not None):
                    return f"QR code: {self.camera.qrcode()}"
            finally:
                self.camera.qrcode_detect(on=False)
        elif target in COLORS:
            with self.camera.color_detection(target):
                if self.sweep_scan(lambda: self.camera.detected_color() is not None):
                    return f"found {target}"
        else:
            return None
        return ""
