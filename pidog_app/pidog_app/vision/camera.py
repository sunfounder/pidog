"""Camera facade over :class:`vilib.Vilib`.

Wraps the SunFounder vision library so feature code stays decoupled.
Provides camera lifecycle, photo capture, and on/off switches for the
built-in detectors (face, color, QR, traffic sign, object, hand, pose,
image classification).
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

log = logging.getLogger(__name__)

# ``Vilib`` is imported lazily because its module-level init pulls in
# picamera2 / camera hardware, which isn't available on dev machines.
_Vilib = None


def _get_vilib():
    global _Vilib
    if _Vilib is None:
        from vilib import Vilib as _V
        _Vilib = _V
    return _Vilib


class Camera:
    """Thin wrapper around the Vilib camera + detection helpers."""

    def __init__(self, vflip: bool = False, hflip: bool = False):
        self._started = False
        self._vflip = vflip
        self._hflip = hflip

    # ── lifecycle ────────────────────────────────────────────────────────
    def start(self) -> None:
        if self._started:
            return
        _get_vilib().camera_start(vflip=self._vflip, hflip=self._hflip)
        self._started = True
        log.info("camera started")

    def close(self) -> None:
        if not self._started:
            return
        _get_vilib().camera_close()
        self._started = False

    # ── capture ──────────────────────────────────────────────────────────
    def capture(self, name: str, path: str | Path = "photos") -> Path:
        """Take a still photo and return its path."""
        p = Path(path)
        p.mkdir(parents=True, exist_ok=True)
        _get_vilib().take_photo(name, path=str(p))
        return p / f"{name}.jpg"

    # ── detectors (toggle on/off; read results from Vilib state) ─────────
    def face_detect(self, on: bool = True) -> None:
        _get_vilib().face_detect_switch(on)

    def color_detect(self, color: str = "red") -> None:
        _get_vilib().color_detect(color)

    def color_detect_off(self) -> None:
        _get_vilib().close_color_detection()

    def qrcode_detect(self, on: bool = True) -> None:
        _get_vilib().qrcode_detect_switch(on)

    def traffic_detect(self, on: bool = True) -> None:
        _get_vilib().traffic_detect_switch(on)

    def object_detect(self, on: bool = True,
                      model_path: Optional[str] = None,
                      labels_path: Optional[str] = None) -> None:
        _get_vilib().object_detect_switch(on)
        if model_path:
            _get_vilib().object_detect_set_model(model_path)
        if labels_path:
            _get_vilib().object_detect_set_labels(labels_path)

    def hands_detect(self, on: bool = True) -> None:
        _get_vilib().hands_detect_switch(on)

    def pose_detect(self, on: bool = True) -> None:
        _get_vilib().pose_detect_switch(on)

    def image_classify(self, on: bool = True,
                       model_path: Optional[str] = None,
                       labels_path: Optional[str] = None) -> None:
        _get_vilib().image_classify_switch(on)
        if model_path:
            _get_vilib().image_classify_set_model(model_path)
        if labels_path:
            _get_vilib().image_classify_set_labels(labels_path)

    # ── result accessors ─────────────────────────────────────────────────
    def qrcode(self) -> Optional[str]:
        """Last decoded QR code string, or None."""
        return _get_vilib().get_qrcode() or None

    def detected_faces(self) -> int:
        """Number of faces currently detected in the frame."""
        # Vilib exposes detector state via its `face_detect_*` attributes.
        return getattr(Vilib, "face_detect_count", 0)

    def detected_color(self) -> Optional[dict]:
        """Color detector result if any: ``{'color':..., 'x':..., 'y':...}``."""
        info = getattr(Vilib, "color_detect_info", None)
        return dict(info) if info else None
