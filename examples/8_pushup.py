#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from preset_actions import pushup, bark

my_dog = Pidog()

sleep(0.5)


def main():
    my_dog.legs_move([[45, -25, -45, 25, 80, 70, -80, -70]], speed=50)
    my_dog.head_move([[0, 0, -20]], speed=90)
    my_dog.wait_all_done()
    sleep(0.2)
    bark(my_dog, [0, 0, -20])
    sleep(0.1)
    bark(my_dog, [0, 0, -20])

    sleep(1)

    while True:
        pushup(my_dog)
        bark(my_dog, [0, 0, -40])
        sleep(0.4)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        my_dog.close()
