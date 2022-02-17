#!/usr/bin/env python3
from pidog import Pidog
from time import sleep

my_dog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
            head_pins=[9,10,11],tail_pin=[12],
            feet_init_angles=[45,0,-45,0,45,0,-45,0],
            )
sleep(0.1)


def is_sound():
    if my_dog.ears.isdetected():
        direction = my_dog.ears.read()
        if direction != 0:
            return True
        else:
            return False

def delay(time):
    while len(my_dog.feet_actions_buffer) > 0 or len(my_dog.head_actions_buffer) > 0:
        sleep(0.1)
    sleep(time)
    

def shake_head(amplitude,interval,speed):
    my_dog.head_move([[amplitude,0,0]],immediately=True,speed=speed)
    delay(interval)
    my_dog.head_move([[-amplitude,0,0]],immediately=True,speed=speed)
    delay(interval)
    my_dog.head_move([[0,0,0]],immediately=True,speed=speed)
    

def rest():
 
    my_dog.do_action('lie',wait=True,speed=50)
    delay(0.2)
    is_sound()

    while True: 
        my_dog.rgb_strip.set_mode('breath','pink')
        my_dog.head_move([[0,0,-30]],immediately=True,speed=5)
        my_dog.do_action('doze_off',wait=False,speed=80)     
        
        if is_sound():       
            my_dog.rgb_strip.set_mode('boom','yellow',delay=0.01)
            my_dog.body_stop()
            sleep(0.5)
            my_dog.do_action('stand',wait=False,speed=95)
            my_dog.head_move([[0,0,0]],immediately=True,speed=80)
            delay(0.2)
            shake_head(60,0.5, 100)
            delay(0.8)
            my_dog.speak('confused_003')
            my_dog.do_action('tilting_head_left',wait=True,speed=80)
            delay(0.8)
            my_dog.do_action('tilting_head_right',wait=True,speed=80)
            delay(0.8)
            my_dog.head_move([[0,0,-10]],immediately=True,speed=80)
            delay(0.8)
            my_dog.head_move([[20,0,-20]],immediately=False,speed=90)
            my_dog.head_move([[-20,0,-20]],immediately=False,speed=90)
            my_dog.head_move([[0,0,-20]],immediately=False,speed=90)
            delay(0.2)
            my_dog.rgb_strip.set_mode('breath','pink')
            my_dog.do_action('lie',wait=True,speed=50)       
            delay(0.2) 
            is_sound()

        sleep(1)


if __name__ == "__main__":
    try:
        rest()
    except KeyboardInterrupt: 
        my_dog.close()
