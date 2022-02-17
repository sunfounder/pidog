#!/usr/bin/env python3
from pidog import Pidog
from time import sleep


my_dog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
                head_pins=[9,10,11],
                tail_pin=[12],
                feet_init_angles=[45,0,-45,0,45,0,-45,0]
                )
sleep(0.5) 
 
 
def delay(time):
    while len(my_dog.feet_actions_buffer) > 0 or len(my_dog.head_actions_buffer) > 0:
        sleep(0.1)
    sleep(time)


def body_twisting(times=3):
    f1 = [-80, 70, 80, -70, -20, 64, 20, -64]
    f2 = [-70, 50, 80, -90, 10, 20, 20, -64]
    f3 = [-80, 90, 70, -50, -20, 64, -10, -20]
    f = [f2] + [f1] + [f3] + [f1]

    h1 = [0,0,20]
    h2 = [0,30,20]
    h3 = [0,-30,20]
    h = [h2] + [h1] + [h3] + [h1]

    for _ in range(times):
        my_dog.feet_move(f,immediately=False,speed=90)
        # my_dog.head_move(h,immediately=False,speed=75)


def leg_press(times=2):
    f1 = [-45, 20, 45, -20, -20, 64, 20, -64]
    f2 = [-90, 90, 90, -90, -20, 64, 20, -64]
    f = [f1] + [f2]*3 
    for _ in range(times):
        my_dog.feet_move(f,immediately=False,speed=90)

def pant(times=6):
    h1 = [0,0,-30]
    h2 = [0,0,-40]
    h = [h1] + [h2] + [h1]
    my_dog.speak('pant')
    for _ in range(times):
        my_dog.head_move(h,immediately=False,speed=70)  


def wake_up():

    my_dog.rgb_strip.set_mode('breath',font_color='pink',brightness=0.8,delay=0.08)
    my_dog.do_action('doze_off',step_count=3,wait=False,speed=80)
    my_dog.head_move([[0,0,-30]],immediately=True,speed=5)
    delay(0.2)
    my_dog.head_move([[0,0,30]]*2,immediately=True)
    my_dog.do_action('stretch',wait=True,speed=90)
    delay(0.2)
    # leg_press()
    # delay(0.2)
    body_twisting()
    delay(0.2)
    my_dog.head_move([[0,0,-30]],immediately=True,speed=90)
    my_dog.do_action('sit',wait=True,speed=90)  
    my_dog.do_action('tail_wagging',step_count=50, wait=False, speed=99)
    my_dog.do_action('tail_wagging',step_count=5, wait=False, speed=99)

    delay(0.5)
    pant(8)


if __name__ == "__main__":
    try:
        wake_up()
        print('done')
        # Keep the main thread active for process termination processing
        while True:       
            sleep(1)
    except KeyboardInterrupt: 
        my_dog.close()

