# !/usr/bin/env python3
''' rgb strip style control

API:
    Pidog.rgb_strip.set_mode(style='breath', color='white', bps=1, brightness=1):

        Set the display mode of the rgb light strip

        - style  str, display style, could be: "breath", "boom", "bark", "speak", "listen"
        - color  str, list or hex, display color,
                  could be: 16-bit rgb value, eg: #a10a0a;
                  or 1*3 list of rgb, eg: [255, 100, 80];
                  or predefined colors:"white", "black", "red", "yellow", "green", "blue", "cyan", "magenta", "pink"
        - bps    float or int, beats per second, this number of style actions executed per second

    Pidog.rgb_strip.close():
        - turn off rgb display


more to see: ../pidog/rgb_strip.py

'''

from pidog import Pidog
import time

my_dog = Pidog()

while True:
    # style="breath", color="pink"
    my_dog.rgb_strip.set_mode(style="breath", color='pink')
    time.sleep(3)

    # style:"listen", color=[0, 255, 255]
    my_dog.rgb_strip.set_mode(style="listen", color=[0, 255, 255])
    time.sleep(3)

    # style:"boom", color="#a10a0a"
    my_dog.rgb_strip.set_mode(style="boom", color="#a10a0a")
    time.sleep(3)

    # style:"boom", color="#a10a0a", brightness=0.5, bps=2.5
    my_dog.rgb_strip.set_mode(style="boom", color="#a10a0a", bps=2.5, brightness=0.5)
    time.sleep(3)

    # close
    my_dog.rgb_strip.close()
    time.sleep(2)

