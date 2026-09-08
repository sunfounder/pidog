"""Concrete features for the dog.

Each feature is a small, self-contained class. Add new features by
creating a new module here and registering it in
:mod:`pidog_app.app` (``build_features``).
"""
from .wake_from_stasis import WakeFromStasis
from .find_object import FindObject
from .recognize_person import RecognizePerson
from .check_water_bowl import CheckWaterBowl

__all__ = [
    "WakeFromStasis",
    "FindObject",
    "RecognizePerson",
    "CheckWaterBowl",
]
