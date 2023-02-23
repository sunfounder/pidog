from pidog.rgb_strip import RGBStrip
from time import sleep

strip = RGBStrip()

mode_list = [
    {
        "color": "red",
        "brightness": 0.8,
        "delay": 0.01,
    },
    {
        "color": "green",
        "brightness": 0.2,
        "delay": 0.05,
    },
    {
        "color": "yellow",
        "brightness": 0.5,
        "delay": 0.1,
    },
]

for mode in mode_list:
    print(
        f'Color: {mode["color"]}, brightness: {mode["brightness"]}, delay: {mode["delay"]}')
    sleep(1)
    for _ in range(5):
        strip.set_mode('breath', color=mode["color"],
                       brightness=mode["brightness"], delay=mode["delay"])
        strip.show()
