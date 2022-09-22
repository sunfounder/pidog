#!/usr/bin/env python3
from pidog import Pidog
from time import sleep

my_dog = Pidog()


def main():
    sleep(0.1)

    def delay(time):
        while len(my_dog.head_action_buffer) > 0:
            sleep(0.1)
        sleep(time)

    legs_action_1 = [
        [30, 60, -30, -60, 80, -45, -80, 45],
    ]
    legs_action_2 = [
        [30, 60, 45, 30, 80, -45, -80, 35],
        [30, 60, 90, -60, 80, -45, -80, 35],
    ]
    head_action_1 = [
        [0, 10, -30]
    ]

    my_dog.legs_speed = 90
    my_dog.legs_move(legs_action_1, True)
    my_dog.head_move(head_action_1, True)
    delay(0.5)
    while True:
        my_dog.legs_move(legs_action_2, False, speed=50)
        delay(0.5)


if __name__ == "__main__":
    try:
        main()
    finally:
        my_dog.close()
