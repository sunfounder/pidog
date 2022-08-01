#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from preset_actions import pushup, bark

my_dog = Pidog(feet_pins=[1, 2, 9, 10, 3, 4, 11, 12],
    head_pins=[7, 5, 6],
    tail_pin=[8],
)

sleep(0.5)

def main():
    my_dog.feet_move([[45, -25, -45, 25, 80, 70, -80, -70]],speed=90)
    my_dog.head_move([[0, 0, -20]],speed=90)
    my_dog.wait_all_done()
    sleep(0.2)
    bark(my_dog)
    sleep(0.1)
    bark(my_dog)

    sleep(1)

    while True:
        pushup(my_dog)
        bark(my_dog)
        sleep(0.4)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        my_dog.close()
  