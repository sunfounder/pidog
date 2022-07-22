#!/usr/bin/env python3
import time
from pidog import Pidog
from time import sleep


t = time.time()
my_dog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
                head_pins=[9,10,11],
                tail_pin=[12],
                feet_init_angles=[45,0,-45,0,45,0,-45,0]
                )
sleep(0.1) 
# print(1, time.time() -t)
# t = time.time()
# def delay_s(time):
#     while (len(my_dog.feet_actions_buffer) > 0 or len(my_dog.head_actions_buffer) > 0) :
#         sleep(0.01)
#     sleep(time)

stand = my_dog.feet_angle_calculation([[0,110],[0,110],[30,95],[30,95]])

# def look_far():
    # my_dog.head_move([[0,0,-15]], speed=80)

def bark(yaw):
    h1 = [yaw, 0,  15]
    h2 = [yaw, 0, -15]

    my_dog.speak('angry')
    for _ in range(3):
        # delay_s(0.1)
        my_dog.head_move([h1], immediately=True, speed=90)
        my_dog.wait_head_done()
        sleep(0.05)
        my_dog.head_move([h2], immediately=True, speed=90)
        my_dog.wait_head_done()
        sleep(0.01)

def patrol():
    my_dog.rgb_strip.set_mode('breath', 'white', delay=0.1)
    my_dog.do_action('forward', step_count=2, wait=False, speed=98)
    my_dog.do_action('shake_head', step_count=1, wait=False, speed=80)
    my_dog.do_action('tail_wagging', step_count=5, wait=False, speed=99)
    print(f"distance: {my_dog.distance.value} cm")
    if my_dog.distance.value < 15:
        my_dog.body_stop()
        head_yaw = my_dog.head_current_angle[0]
        my_dog.rgb_strip.set_mode('boom', 'red', delay=0.01)
        my_dog.tail_move([[0]], speed=80)
        my_dog.feet_move([stand], speed=70)
        my_dog.wait_all_done()
        bark(head_yaw)
    my_dog.rgb_strip.set_mode('breath', 'white', delay=0.1)

if __name__ == "__main__":
    try:
        while True:  
            patrol()
    finally:
        my_dog.close()



