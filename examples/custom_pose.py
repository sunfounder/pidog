#!/usr/bin/env python3
from pidog import Pidog
from time import sleep


def main():
    my_dog = Pidog()
    sleep(0.1)

    new_legs_action = [
        [45, 0, -45, 0, 45, 0, -45, 0],
        [0, 0, 0, 0, 45, 0, -45, 0],
        [-20, 0, -45, 0, 45, 0, -45, 0],
        [45, 0, -45, 0, 45, 0, -45, 0]
    ]
    new_head_action = [
        [0, 0, 20]
    ]

    my_dog.legs_move(new_legs_action, True)
    my_dog.head_move(new_head_action, True)


if __name__ == "__main__":
    main()
