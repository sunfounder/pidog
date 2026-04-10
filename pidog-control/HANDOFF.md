# PiDog Skill Handoff

This is a handoff note you can send directly to someone else. It covers:
- what the current setup can do
- what has been verified on this machine
- how to install / place the skill
- how to run it
- known limitations

## Quick summary

This package is a local OpenClaw skill for **SunFounder PiDog V2**.

Expected install layout on the target machine:
- `~/pidog`
- `~/robot-hat`
- `~/vilib`

Supported now:
- actions: `stand`, `sit`, `lie`, `wag-tail`, `bark`, `forward`, `backward`, `turn-left`, `turn-right`
- posture hold: `--hold`
- lights: `off`, `breath`, `listen`, `boom`, `solid`
- colors: named colors or `#RRGGBB`

Verified on this machine:
- actions: `stand`, `sit`, `lie`, `wag-tail`, `bark`
- lights: `boom`, `listen`, `breath`, `off`
- visible in real use: red, yellow, purple

Recommended defaults:
- action demo: `sit`
- light demo: `boom --color purple`
- first light troubleshooting step: `scripts/pidog_rgb_ctl.py`

## How to install

Copy the whole folder to:

```text
~/.openclaw/workspace/skills/pidog-control/
```

## First tests

```bash
python3 scripts/pidog_ctl.py status
python3 scripts/pidog_ctl.py safe-test
python3 scripts/pidog_rgb_ctl.py light boom --color purple
```

## Important notes

- The default bark implementation uses `single_bark_1`, not a generic `bark` sound name.
- `solid` should not be treated as guaranteed true steady-on. For a clearly visible result, prefer `boom`.
- If `import pidog` fails, fix the PiDog Python installation first.