#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from math import sin


my_dog = Pidog(feet_pins=[1, 2, 3, 4, 5, 6, 7, 8], 
                head_pins=[9, 10, 11], 
                tail_pin=[12], 
                # feet_init_angles=[45, 0, -45, 0, 45, 0, -45, 0]
                )
sleep(0.1)

def bark_action():
    h1 = [0, 0, 20]
    h2 = [0, 0, 0]

    f1 = my_dog.feet_angle_calculation([[0, 100], [0, 100], [30, 90], [30, 90]])
    f2 = my_dog.feet_angle_calculation([[-20, 90], [-20, 90], [0, 90], [0, 90]])

    my_dog.feet_move([f1], immediately=True, speed=95)
    my_dog.head_move([h1], immediately=True, speed=95)
    my_dog.wait_all_done()
    sleep(0.01)
    my_dog.feet_move([f2], immediately=True, speed=95)
    my_dog.head_move([h2], immediately=True, speed=95)
    my_dog.wait_all_done()
    sleep(0.01)

def lean_forward():
    my_dog.speak('angry')
    bark_action()
    bark_action()
    sleep(0.2)
    bark_action()


def head_nod(step):
    y=0;r=0;p=30
    angs = []
    for i in range(20):
        r = round(10*sin(i*0.314), 2)
        p = round(20*sin(i*0.314) +10, 2)
        angs.append([y, r, p]) 

    my_dog.head_move(angs*step, immediately=False, speed=80)


def alert():
    my_dog.do_action('stand', step_count=1, speed=90)
    my_dog.rgb_strip.set_mode('breath', front_color='pink', brightness=0.8, delay=0.08)
    while True:
        print(f'distance.value: {round(my_dog.distance.value, 2)} cm, touch {my_dog.touch_sw.is_slide()}') 
        # alert
        if my_dog.distance.value < 15 and my_dog.distance.value > 1:
            my_dog.head_move([[0, 0, 0]], immediately=True, speed=90)
            my_dog.tail_move([[0]], immediately=True, speed=90)
            my_dog.rgb_strip.set_mode('boom', front_color='red', brightness=0.8, delay=0.001)       
            my_dog.do_action('backward', step_count=1, speed=99)
            my_dog.wait_all_done()
            lean_forward()
            while len(my_dog.feet_actions_buffer) > 0:
                sleep(0.1)
            my_dog.do_action('stand', step_count=1, speed=90)
            sleep(0.5)
        else:
            my_dog.rgb_strip.set_mode('breath', front_color='pink', brightness=0.8, delay=0.08)
        # relax
        if my_dog.touch_sw.is_slide() != 'N':
            if len(my_dog.head_actions_buffer) < 2:
                head_nod(1)
                my_dog.do_action('tail_wagging', step_count=20, speed=100)
                my_dog.rgb_strip.set_mode('breath', front_color='pink', brightness=0.8, delay=0.08)
        sleep(0.2)


if __name__ == "__main__":
    try:
        alert()
    except KeyboardInterrupt: 
        my_dog.close()
