# !/usr/bin/env python3
''' read ultrasonic distance data

API:
    Pidog.ultrasonic.read_distance()
        return the distance read by ultrasound
        - return float

'''

from pidog import Pidog
import time

my_dog = Pidog()
while True:
    distance = my_dog.ultrasonic.read_distance()
    distance = round(distance,2)
    print(f"Distance: {distance} cm")
    time.sleep(0.5)
