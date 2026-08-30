from pidog.rgb_strip import RGBStrip
import time

strip = RGBStrip(0X74, 11)

mode_list = [
    {
        "color": "red",
        "brightness": 0.8,
        "bps": 1,
    },
    {
        "color": "green",
        "brightness": 0.2,
        "bps": 2,
    },
    {
        "color": "blue",
        "brightness": 0.5,
        "bps": 3,
    },
    {
        "color": "white",
        "brightness": 0.5,
        "bps": 4,
    },
]

for mode in mode_list:
    print(
        f'Color: {mode["color"]}, brightness: {mode["brightness"]}, bps: {mode["bps"]}'
    )
    strip.set_mode('breath',
                   color=mode["color"],
                   brightness=mode["brightness"],
                   bps=mode["bps"])

    start_time = time.time()
    while ((time.time() - start_time) <= 3):
        strip.show()
