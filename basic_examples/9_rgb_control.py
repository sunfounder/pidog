# !/usr/bin/env python3
''' rgb strip style control

API:
    Pidog.rgb_strip.set_mode(style='breath', color='white', brightness=1, delay=0.01):
        
        Set the display mode of the rgb light strip
        
        - style    str, display style, could be: breath, boom, bark
        - color    str, display color, could be: 16-bit rgb value, eg: #a10a0a; or predefined colors:
                   "white", "black", "red", "yellow", "green", "blue", "cyan", "magenta", "pink"
        - brightness float, display brightness, could be: 0 ~ 1, eg: 0.5
        - delay    float, display animation speed, the smaller the value, the faster the change

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

    # style:"boom", color="#a10a0a"
    my_dog.rgb_strip.set_mode(style="boom", color="#a10a0a")
    time.sleep(3)

    # style:"boom", color="#a10a0a", brightness=0.1, delay=0.1
    my_dog.rgb_strip.set_mode(style="boom", color="#a10a0a", brightness=0.5, delay=0.05)
    time.sleep(3)

    # close
    my_dog.rgb_strip.close()
    time.sleep(2)

