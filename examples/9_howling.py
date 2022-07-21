#!/usr/bin/env python3
from pidog import Pidog
from time import sleep


my_dog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
                head_pins=[9,10,11],
                tail_pin=[12],
                )
sleep(0.5) 

    
def howling():
    my_dog.do_action('sit', speed=95)
    my_dog.head_move([[0,0,-30]], speed=95)
    my_dog.wait_all_done()

    for _ in range(100):
        my_dog.do_action('half_sit', wait=True, speed=80)
        my_dog.head_move([[0,0,-60]], speed=80)
        my_dog.wait_all_done()
        my_dog.speak('howling')
        my_dog.do_action('sit', speed=60)
        my_dog.head_move([[0,0,10]], speed=70)
        my_dog.wait_all_done()

        my_dog.do_action('sit', speed=60)
        my_dog.head_move([[0,0,10]], speed=80)
        my_dog.wait_all_done()

        sleep(2.34)


if __name__ == "__main__":
    try:
        howling()
        # Keep the main thread active for process termination processing
        while True:       
            sleep(1)
    except KeyboardInterrupt:
        my_dog.close()
    