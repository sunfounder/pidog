---
name: pidog-control
description: Control a SunFounder PiDog V2 installed with the official tutorial under the user's home directory (`~/pidog`, with related dependencies such as `~/robot-hat` and `~/vilib`). Use when the user wants PiDog to perform basic motions, posture changes, barking or simple expressive behaviors, or control the onboard RGB light board. Also use when verifying that a standard PiDog V2 Python installation is present and ready.
---

# PiDog Control

Control a SunFounder PiDog V2 using the standard tutorial-style installation layout under `~/`.

## Scope

This skill is designed for the common setup used by PiDog hobbyists who followed the SunFounder installation docs and installed the projects under their home directory:
- `~/pidog`
- `~/robot-hat`
- `~/vilib`

This version of the skill focuses on:
- basic motion / posture control
- simple expressive actions such as bark and tail wag
- RGB light-board control
- basic environment checks

Do not assume custom wiring, custom virtualenvs, or nonstandard install prefixes unless the user says so.

## Safety

Before movement:
- Tell the user to place PiDog on the floor or on a stable open surface.
- Prefer short actions first.
- Avoid repeated or continuous movement loops unless explicitly requested.
- If the setup is unverified, run `status` first and then `safe-test`.

If the user asks for something outside the supported action set, inspect the local examples under `~/pidog/examples/` before inventing APIs.

## Standard workflow

1. If the machine state is unknown, run:
   ```bash
   python3 scripts/pidog_ctl.py status
   ```
2. For the first real movement on a new machine, run:
   ```bash
   python3 scripts/pidog_ctl.py safe-test
   ```
3. Then run the requested action or light command.
4. Report exactly what happened.

## Supported commands

### Inspect environment

```bash
python3 scripts/pidog_ctl.py status
```

Checks:
- expected directories under `~/`
- whether the `pidog` package is importable
- availability of `Pidog`
- available speech utilities

### Safe movement test

```bash
python3 scripts/pidog_ctl.py safe-test
```

Runs a minimal `do_action('stand')` → `do_action('sit')` test.

### Basic actions

```bash
python3 scripts/pidog_ctl.py action stand
python3 scripts/pidog_ctl.py action sit
python3 scripts/pidog_ctl.py action lie
python3 scripts/pidog_ctl.py action bark
python3 scripts/pidog_ctl.py action wag-tail
python3 scripts/pidog_ctl.py action forward
python3 scripts/pidog_ctl.py action backward
python3 scripts/pidog_ctl.py action turn-left
python3 scripts/pidog_ctl.py action turn-right
```

To keep a posture instead of auto-cleaning at the end:

```bash
python3 scripts/pidog_ctl.py action stand --hold
python3 scripts/pidog_ctl.py action sit --hold
python3 scripts/pidog_ctl.py action lie --hold
```

When switching between hold postures, the helper tries to stop the previous hold process automatically so the user usually does not need to manually `pkill` the prior command.

These map to the official high-level API:
- `dog.do_action('stand')`
- `dog.do_action('sit')`
- `dog.do_action('lie')`
- `dog.do_action('wag_tail')`
- `dog.speak('single_bark_1')` for the default bark effect in this skill

### Light-board control

General path through the main helper:

```bash
python3 scripts/pidog_ctl.py light off
python3 scripts/pidog_ctl.py light breath --color purple
python3 scripts/pidog_ctl.py light listen --color yellow
python3 scripts/pidog_ctl.py light boom --color orange
python3 scripts/pidog_ctl.py light solid --color '#00aaff'
```

Minimal direct RGB path that avoids initializing the full `Pidog()` runtime:

```bash
python3 scripts/pidog_rgb_ctl.py light breath --color red
python3 scripts/pidog_rgb_ctl.py light listen --color yellow
python3 scripts/pidog_rgb_ctl.py light off
```

This maps to the official light-board API:
- `dog.rgb_strip.set_mode(mode, color=..., bps=..., brightness=...)`

Recommended modes in this skill:
- `off`
- `breath`
- `listen`
- `boom`

Experimental alias:
- `solid` (mapped to `boom`, not a true steady-on solid mode)

Supported color names are defined in the script and can also be passed as hex RGB values.
Real-device testing showed that `breath` and `listen` are usable but visually brief. A local `rgb_strip_test.py` example confirmed direct use of `RGBStrip.set_mode('boom', ...)`, so this skill now exposes `boom` and maps `solid` to it as the closest tested approximation.

## Design assumptions

This skill assumes the official PiDog V2 install flow was used and that the runtime is on the default system Python path after `pip3 install .` from `~/pidog`.

This skill follows the public repository structure directly:
- package import: `from pidog import Pidog`
- motion interface: `do_action(...)`
- light-board interface: `rgb_strip.set_mode(...)`
- sound effects: `speak(...)`

Prefer these official APIs over heuristic method-name probing.

## If something fails

Check these in order:
1. `~/pidog` exists
2. `python3 -c "import pidog"` works
3. PiDog is powered correctly
4. Servo calibration has been completed
5. The light board hardware is connected and enabled

## References

Read these as needed:
- `references/install-layout.md` for standard home-directory layout assumptions
- `references/api-notes.md` for confirmed upstream interfaces
- `references/actions.md` for the exposed public action set
- `references/light-board.md` for light-board behavior and mode mapping notes
- `references/troubleshooting.md` when runtime checks or hardware behavior fail
- official docs: https://docs.sunfounder.com/projects/pidog/en/latest/

Keep this skill focused on the standard install path and the basic features promised here.