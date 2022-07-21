#!/usr/bin/env python3
from pidog import Pidog
from time import sleep

my_dog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
                head_pins=[9,10,11],
                tail_pin=[12],
                # feet_init_angles=[45,0,-45,0,45,0,-45,0]
                )
sleep(0.5) 
 
def body_twisting(times=1):
    f1 = [-80, 70, 80, -70, -20, 64, 20, -64]
    f2 = [-70, 50, 80, -90, 10, 20, 20, -64]
    f3 = [-80, 90, 70, -50, -20, 64, -10, -20]
    f = [f2] + [f1] + [f3] + [f1]

    h1 = [0,0,20]
    h2 = [0,30,20]
    h3 = [0,-30,20]
    h = [h2] + [h1] + [h3] + [h1]

    for _ in range(times):
        my_dog.feet_move(f,immediately=False,speed=50)

def pant(times=6):
    h1 = [0,0,-30]
    h2 = [0,0,-40]
    h = [h1] + [h2] + [h1]
    my_dog.speak('pant')
    for _ in range(times):
        my_dog.head_move(h, immediately=False, speed=92)


def wake_up():
    my_dog.rgb_strip.set_mode('breath', front_color='yellow', brightness=0.8, delay=0.095)
    my_dog.head_move([[0, 0, 30]]*2, immediately=True)
    my_dog.do_action('stretch', wait=True, speed=20)
    my_dog.wait_all_done()
    sleep(0.2)
    body_twisting()
    my_dog.wait_all_done()
    sleep(0.2)
    my_dog.head_move([[0, 0, -30]],immediately=True,speed=90)
    my_dog.do_action('sit', wait=False, speed=50)
    my_dog.wait_feet_done()
    my_dog.do_action('tail_wagging', step_count=10, wait=False, speed=100)
    my_dog.rgb_strip.set_mode('breath', front_color=[245, 10, 10], brightness=0.8, delay=0.002)
    pant(10)
    my_dog.wait_all_done()
    my_dog.rgb_strip.close()

if __name__ == "__main__":
    try:
        wake_up()
    finally: 
        my_dog.close()
        quit()

