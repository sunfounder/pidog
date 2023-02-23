#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from preset_actions import shake_head

my_dog = Pidog()
sleep(0.1)

def rest():

    my_dog.wait_all_done()
    my_dog.do_action('lie', speed=50)
    my_dog.wait_all_done()

    while True:
        # Sleeping
        my_dog.rgb_strip.set_mode('breath', 'pink', delay=0.14)
        my_dog.head_move([[0,0,-40]], immediately=True, speed=5)
        my_dog.do_action('wag_tail', step_count=20, speed=20)
        my_dog.do_action('doze_off', speed=95)

        sleep(1)

if __name__ == "__main__":
    try:
        rest()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        my_dog.close()
