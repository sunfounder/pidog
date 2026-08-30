# PiDog Troubleshooting

Use this checklist when the helper script or skill does not behave as expected.

## Import fails

Symptoms:
- `import pidog` fails
- `python3 scripts/pidog_ctl.py status` reports unavailable runtime

Checks:
1. Confirm `~/pidog` exists
2. Confirm the package was installed with `pip3 install .` from `~/pidog`
3. Confirm dependencies were installed from `~/robot-hat` and `~/vilib`
4. Confirm the command is using the same Python environment where PiDog was installed

## Robot initializes but movement fails

Checks:
1. Confirm power supply is adequate
2. Confirm the robot completed servo calibration
3. Confirm I2C-related hardware is connected correctly
4. Try `lie` or `sit` before more complex actions

## Sound works inconsistently

The upstream PiDog code warns that sound playback may require sudo in some environments.
The `Pidog.speak()` implementation also kills `pulseaudio` in some cases to work around VNC/audio issues.

Real-device validation on this setup showed an additional case:
- `speak('bark')` can fail with `No sound found for bark`

So this skill now treats missing named sounds as a real failure instead of printing a false success message.

## Light board does not behave as expected

Checks:
1. Confirm the `rgb_strip` hardware is present and initialized
2. Try `breath` before other modes
3. If one mode fails but another works, keep the mode mapping change in `scripts/pidog_ctl.py`

Real-device validation on this setup showed:
- `breath` works, but the visible effect may be brief or limited rather than a long obvious animation
- `listen` works, but may present as a very short flowing effect
- `off` works
- `solid` is not reliable as a true solid mode through the current compatibility mapping, and shutdown produced `_rgb_strip_thread Exception:list index out of range`

Treat that shutdown exception as a known cleanup edge case to investigate if it recurs.
Prefer `breath`, `listen`, `boom`, and `off` as the stable public light controls for now.

## Close/cleanup behavior

Use `dog.close()` when finishing. The upstream class performs a full shutdown routine and returns PiDog to a resting position.