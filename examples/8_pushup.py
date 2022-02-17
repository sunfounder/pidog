#!/usr/bin/env python3
from re import S
from pidog import Pidog
from time import sleep


my_dog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
                head_pins=[9,10,11],
                tail_pin=[12],
                )
sleep(0.5) 


def pushup():
    my_dog.feet_move([[45, -25, -45, 25, 80, 70, -80, -70]],speed=90)
    my_dog.head_move([[0, 0, -20]],speed=90)
    my_dog.wait_all_done()

    sleep(0.5)

    for _ in range(100):
        my_dog.do_action('head_bark',speed=60)
        my_dog.do_action('pushup',speed=80)
        my_dog.wait_all_done()
        my_dog.do_action('head_bark',speed=90)
        sleep(0.4)
        my_dog.speak('single_bark_001')
        my_dog.wait_all_done()
        sleep(0.8)


if __name__ == "__main__":
    try:
        pushup()
        # Keep the main thread active for process termination processing
        while True:       
            sleep(1)
    except KeyboardInterrupt:
        my_dog.close()
  