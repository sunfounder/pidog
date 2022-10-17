#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from preset_actions import shake_head

my_dog = Pidog()
sleep(0.1)

def loop_arround(amplitude=60, interval=0.5, speed=100):
    my_dog.head_move([[amplitude,0,0]], immediately=True, speed=speed)
    my_dog.wait_all_done()
    sleep(interval)
    my_dog.head_move([[-amplitude,0,0]], immediately=True, speed=speed)
    my_dog.wait_all_done()
    sleep(interval)
    my_dog.head_move([[0,0,0]], immediately=True, speed=speed)
    my_dog.wait_all_done()

def is_sound():
    if my_dog.ears.isdetected():
        direction = my_dog.ears.read()
        if direction != 0:
            return True
        else:
            return False

def rest():
 
    my_dog.do_action('lie', wait=True, speed=50)
    my_dog.wait_all_done()
    # Cleanup sound detection
    is_sound()

    while True: 
        # Sleeping
        my_dog.rgb_strip.set_mode('breath', 'pink', delay=0.14)
        my_dog.head_move([[0,0,-40]], immediately=True, speed=5)
        my_dog.do_action('wag_tail', step_count=20, speed=20)
        my_dog.do_action('doze_off', wait=False, speed=95)
        
        # If heard anything, wake up
        if is_sound():
            # Set light to yellow and stand up
            my_dog.rgb_strip.set_mode('boom', 'yellow', delay=0.01)
            my_dog.body_stop()
            my_dog.do_action('stand', wait=False, speed=90)
            my_dog.head_move([[0, 0, 0]], immediately=True, speed=80)
            my_dog.wait_all_done()
            # Look arround
            loop_arround(60, 0.5, 100)
            sleep(0.5)
            # tilt head and being confused
            my_dog.speak('confused_3')
            my_dog.do_action('tilting_head_left', wait=True, speed=80)
            my_dog.wait_all_done()
            sleep(0.8)
            my_dog.head_move([[0, 0, -10]], immediately=True, speed=80)
            my_dog.wait_all_done()
            sleep(0.8)
            # Shake head to ignore it
            shake_head(my_dog)
            sleep(0.2)
            # Lay down again
            my_dog.rgb_strip.set_mode('breath', 'pink')
            my_dog.do_action('lie', wait=True, speed=50)
            my_dog.wait_all_done()
            sleep(0.2)
            # Cleanup sound detection
            is_sound()

        sleep(1)


if __name__ == "__main__":
    try:
        rest()
    except KeyboardInterrupt:
        my_dog.close()
