#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from preset_actions import pant
from preset_actions import body_twisting

my_dog = Pidog(head_init_angles=[0, 0, -30])
sleep(1)

def wake_up():
    # stretch
    my_dog.rgb_strip.set_mode(
        'breath', color='yellow', brightness=0.8, delay=0.095)
    my_dog.do_action('stretch', speed=30)
    my_dog.head_move([[0, 0, 30]]*2, immediately=True)
    my_dog.wait_all_done()
    sleep(0.2)
    body_twisting(my_dog)
    my_dog.wait_all_done()
    sleep(0.5)
    my_dog.head_move([[0, 0, -30]], immediately=True, speed=90)
    # sit and wag_tail
    my_dog.do_action('sit', speed=25)
    my_dog.wait_legs_done()
    my_dog.do_action('wag_tail', step_count=10, speed=100)
    my_dog.rgb_strip.set_mode('breath', color=[245, 10, 10], brightness=0.8, delay=0.002)
    pant(my_dog, pitch_comp=-30)
    my_dog.wait_all_done()
    # hold
    my_dog.do_action('wag_tail', step_count=1, speed=30)
    my_dog.rgb_strip.set_mode('breath', 'pink', delay=0.14)
    while True:
        sleep(1)

if __name__ == "__main__":
    try:
        wake_up()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        my_dog.close()
