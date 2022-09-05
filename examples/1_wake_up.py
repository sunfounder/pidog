#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from preset_actions import pant
from preset_actions import body_twisting

my_dog = Pidog()
sleep(0.5)


def wake_up():
    my_dog.rgb_strip.set_mode(
        'breath', front_color='yellow', brightness=0.8, delay=0.095)
    my_dog.head_move([[0, 0, 30]]*2, immediately=True)
    my_dog.do_action('stretch', wait=True, speed=20)
    my_dog.wait_all_done()
    sleep(0.2)
    body_twisting(my_dog)
    my_dog.wait_all_done()
    sleep(0.2)
    my_dog.head_move([[0, 0, -30]], immediately=True, speed=90)
    my_dog.do_action('sit', wait=False, speed=50)
    my_dog.wait_feet_done()
    my_dog.do_action('wag_tail', step_count=10, wait=False, speed=100)
    my_dog.rgb_strip.set_mode('breath', front_color=[
                              245, 10, 10], brightness=0.8, delay=0.002)
    pant(my_dog, pitch_init=-40)
    my_dog.wait_all_done()
    my_dog.rgb_strip.close()


if __name__ == "__main__":
    try:
        wake_up()
    except KeyboardInterrupt:
        pass
    finally:
        my_dog.close()
