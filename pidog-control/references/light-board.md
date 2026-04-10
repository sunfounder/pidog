# PiDog Light Board Notes

PiDog uses an `rgb_strip` object on the `Pidog` instance.

From the public repository:
- initialization uses `self.rgb_strip = RGBStrip(addr=0X74, nums=11)`
- examples call `my_dog.rgb_strip.set_mode(...)`

From a local PiDog test example (`~/pidog/test/rgb_strip_test.py`):
- `RGBStrip.set_mode('boom', color=..., brightness=..., bps=...)` is used directly
- the effect is driven by repeated `strip.show()` calls over time

So this skill follows the official API directly instead of guessing attribute names.

## Official control pattern

Use:

```python
my_dog.rgb_strip.set_mode(mode, color=color, bps=bps, brightness=brightness)
```

Observed example modes include:
- `breath`
- `listen`

This skill exposes a practical subset:
- `off`
- `breath`
- `listen`
- `boom`
- `solid` (experimental alias)

`off` is implemented by calling `breath` with black and zero brightness.
`boom` is exposed directly because a local PiDog test script uses it explicitly.
`solid` is not a true steady-on mode; it is an experimental alias mapped to `boom` as the closest tested approximation.

## Color inputs

The script supports:
- named colors: red, green, blue, yellow, purple, pink, cyan, white, orange, black, off
- hex RGB: `#RRGGBB`
- RGB tuples passed internally to `set_mode`

## Compatibility goal

The goal is a broadly usable PiDog V2 interface for users who followed the official installation path.
Current real-device confidence level:
- `breath`: usable
- `listen`: usable
- `off`: usable
- `boom`: validated in real use on this machine
- `solid`: experimental only

When exact mode semantics differ between releases, keep the adjustment localized in `scripts/pidog_ctl.py`.