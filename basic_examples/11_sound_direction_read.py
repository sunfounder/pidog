# !/usr/bin/env python3
''' read azimuth of sound direction

API:
    Pidog.ears.isdetected():
        return    bool, whether the sound direction recognition module has detected the sound 
        
    Pidog.ears.read()
        return    int, the azimuth of the identified sound, 0 ~ 359

more to see: ../pidog/sound_direction.py

'''

from pidog import Pidog

my_dog = Pidog()

while True:
    if my_dog.ears.isdetected():
        direction = my_dog.ears.read()
        print(f"sound direction: {direction}")
