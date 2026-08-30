"""Configuration loader.

Loads ``config.yaml`` from the project root and overlays environment
variables on top. Env vars use the prefix ``PIDOG_`` and map nested keys
with underscores, e.g. ``PIDOG_LLM_IP`` -> ``llm.ip``.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as e:  # pragma: no cover
    raise ImportError("PyYAML is required: pip install pyyaml") from e

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "config.yaml"
ENV_PREFIX = "PIDOG_"


def _deep_get(data: dict, dotted: str, default: Any = None) -> Any:
    cur = data
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return default
        cur = cur[part]
    return cur


def _deep_set(data: dict, dotted: str, value: Any) -> None:
    cur = data
    parts = dotted.split(".")
    for part in parts[:-1]:
        cur = cur.setdefault(part, {})
    cur[parts[-1]] = value


def _apply_env_overrides(data: dict) -> dict:
    for key, value in os.environ.items():
        if not key.startswith(ENV_PREFIX):
            continue
        dotted = key[len(ENV_PREFIX):].lower().replace("_", ".")
        _deep_set(data, dotted, value)
    return data


class Config:
    """Dict-like config with attribute access for top-level sections."""

    def __init__(self, data: dict):
        self._data = data

    def get(self, dotted: str, default: Any = None) -> Any:
        return _deep_get(self._data, dotted, default)

    @property
    def data(self) -> dict:
        return self._data

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            raise AttributeError(name)
        if name in self._data:
            return self._data[name]
        raise AttributeError(name)


def load_config(path: str | os.PathLike | None = None) -> Config:
    cfg_path = Path(path) if path else DEFAULT_CONFIG_PATH
    with open(cfg_path, "r") as f:
        data = yaml.safe_load(f) or {}
    _apply_env_overrides(data)
    return Config(data)
