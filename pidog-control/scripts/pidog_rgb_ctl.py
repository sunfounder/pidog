#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

from pidog.rgb_strip import RGBStrip

COLOR_MAP = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 255),
    "pink": (255, 0, 128),
    "cyan": (0, 255, 255),
    "white": (255, 255, 255),
    "orange": (255, 128, 0),
    "black": (0, 0, 0),
    "off": (0, 0, 0),
}

LIGHT_MODE_MAP = {
    "off": ("monochromatic", (0, 0, 0), 1.0, 0.0),
    "breath": ("breath", None, 1.0, 0.8),
    "listen": ("listen", None, 0.6, 0.8),
    "boom": ("boom", None, 1.0, 0.8),
    "solid": ("monochromatic", None, 1.0, 0.8),
}


def parse_color(value):
    value = value.strip().lower()
    if value in COLOR_MAP:
        return COLOR_MAP[value]
    if value.startswith("#"):
        value = value[1:]
    if len(value) == 6:
        return tuple(int(value[i:i+2], 16) for i in (0, 2, 4))
    raise argparse.ArgumentTypeError("Color must be a known name or hex like #00aaff")


def cmd_status(args):
    data = {
        "python_module": "pidog.rgb_strip.RGBStrip",
        "state": "ready",
    }
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_light(args):
    strip = RGBStrip(0x74, 11)
    try:
        mode_name, default_color, default_bps, default_brightness = LIGHT_MODE_MAP[args.mode]
        color = default_color if default_color is not None else args.color
        bps = args.bps if args.bps is not None else default_bps
        brightness = args.brightness if args.brightness is not None else default_brightness

        if mode_name == "monochromatic":
            rgb = [max(0, min(255, int(c * brightness))) for c in color]
            frame = [rgb[:] for _ in range(strip.light_num)]
            for _ in range(max(args.frames, 1)):
                strip.display(frame)
            result = {
                "ok": True,
                "mode": args.mode,
                "mapped": mode_name,
                "color": list(color),
                "applied_rgb": rgb,
                "bps": bps,
                "brightness": brightness,
                "frames": args.frames,
                "note": "monochromatic rendered via direct display(frame) workaround",
            }
        else:
            strip.set_mode(mode_name, color=color, bps=bps, brightness=brightness)
            for _ in range(max(args.frames, 1)):
                strip.show()
            result = {
                "ok": True,
                "mode": args.mode,
                "mapped": mode_name,
                "color": list(color),
                "bps": bps,
                "brightness": brightness,
                "frames": args.frames,
            }

        if args.mode == "solid":
            result["note"] = "solid is rendered as a direct monochromatic frame in this minimal RGB controller"
        print(json.dumps(result, ensure_ascii=False, indent=2))
    finally:
        try:
            off = [[0, 0, 0] for _ in range(strip.light_num)]
            strip.display(off)
            strip.close()
        except Exception:
            pass


def main():
    parser = argparse.ArgumentParser(description="Minimal direct PiDog RGB controller")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("status")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("light")
    p.add_argument("mode", choices=["off", "breath", "listen", "boom", "solid"])
    p.add_argument("--color", type=parse_color, default=COLOR_MAP["white"])
    p.add_argument("--bps", type=float)
    p.add_argument("--brightness", type=float)
    p.add_argument("--frames", type=int, default=30, help="How many show() frames to render before exit")
    p.set_defaults(func=cmd_light)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
