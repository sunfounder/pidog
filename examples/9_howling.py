#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from preset_actions import howling

my_dog = Pidog(feet_pins=[1, 2, 9, 10, 3, 4, 11, 12],
    head_pins=[7, 5, 6],
    tail_pin=[8],
)

sleep(0.5) 

def main():
    while True:
        howling(my_dog)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        my_dog.close()
    