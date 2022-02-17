#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from vilib import Vilib

my_dog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
            head_pins=[9,10,11],tail_pin=[12],
            feet_init_angles = [30, 60, -30, -60, 80, -45, -80, 45],
            head_init_angles = [0, 0, -40]
            )
sleep(0.1)


def delay(time):
    while len(my_dog.feet_actions_buffer) > 0 or len(my_dog.head_actions_buffer) > 0:
        sleep(0.001)
    sleep(time)

def face_track():
    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=True,web=True)
    Vilib.human_detect_switch(True)
    sleep(0.2)
    print('start')
    yaw = 0
    roll = 0
    pitch = 0
    flag = False
    direction = 0
     
    my_dog.head_move_adjust([yaw,0,pitch],pitch_init=-40,immediately=True,speed=80)
    delay(0.5)
    if my_dog.ears.isdetected():
        direction = my_dog.ears.read()
    
    while True:
        if flag == False:
            my_dog.rgb_strip.set_mode('breath', 'pink', delay=0.1)
        if my_dog.ears.isdetected(): 
            flag = False
            direction = my_dog.ears.read()
            pitch = 0
            if direction > 0 and direction < 100:
                yaw = -direction
                if yaw < -80:
                    yaw = -80
            elif direction > 260 and direction < 360:
                yaw = 360 - direction
                if yaw > 80:
                    yaw = 80
            my_dog.head_move_adjust([yaw,0,pitch],pitch_init=-40,immediately=True,speed=80)
            sleep(0.05)

        ex = Vilib.detect_obj_parameter['human_x'] - 320
        ey = Vilib.detect_obj_parameter['human_y'] - 240
        people = Vilib.detect_obj_parameter['human_n']
       
        if people > 0 and flag == False:
            flag = True
            my_dog.head_move_adjust([yaw,0,25], pitch_init=-40, immediately=True,speed=100)
            my_dog.speak('single_bark_001')
            delay(0.08)
            my_dog.head_move_adjust([yaw,0,0],pitch_init=-40, immediately=True,speed=100)
            delay(0.5)
            if my_dog.ears.isdetected(): 
                direction = my_dog.ears.read()

        if ex > 15 and yaw > -80:
            yaw -= 0.5
            
        elif ex < -15 and yaw < 80:
            yaw += 0.5

        if ey > 25:
            pitch -= 0.5
            if pitch < - 30:
                pitch = -30
        elif ey < -25:
            pitch += 0.5
            if pitch > 30:
                pitch = 30
           
        
        print('direction: %s |number: %s | ex,ey: %s, %s | yrp: %s, %s, %s '
            %(direction, people, ex, ey, round(yaw,2), round(roll,2), round(pitch,2))
        )
        my_dog.head_move_adjust([yaw,0,pitch],pitch_init=-40,immediately=True,speed=100)
        sleep(0.05)


if __name__ == "__main__":
    try:
        face_track()
    except KeyboardInterrupt:
        Vilib.camera_close()
        my_dog.close() 

