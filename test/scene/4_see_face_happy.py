#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from vilib import Vilib
from preset_actions import bark, pant

my_dog = Pidog()

sleep(0.1)


def delay(time):
    my_dog.wait_legs_done()
    my_dog.wait_head_done()
    sleep(time)


def face_track():
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=True)
    Vilib.human_detect_switch(True)
    sleep(0.2)
    print('start')
    yaw = 0
    roll = 0
    pitch = 0
    flag = False
    pitch_comp = -20

    my_dog.do_action('sit', speed=50)
    my_dog.head_move([[yaw, 0, pitch]], pitch_comp=pitch_comp, immediately=True, speed=80)
    delay(0.5)

    while True:
        if flag == False:
            my_dog.rgb_strip.set_mode('breath', 'pink', delay=0.1)
        # If heard somthing, turn to face it

        ex = Vilib.detect_obj_parameter['human_x'] - 320
        ey = Vilib.detect_obj_parameter['human_y'] - 240
        people = Vilib.detect_obj_parameter['human_n']

        # If see someone, bark at him/her
        if people > 0:
            my_dog.do_action('wag_tail', step_count=5, speed=100)
            bark(my_dog, [yaw, 0, 0], pitch_comp=pitch_comp)
            pant(my_dog, [yaw, 0, 0], pitch_comp=pitch_comp)

        sleep(0.05)


if __name__ == "__main__":
    try:
        face_track()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        Vilib.camera_close()
        my_dog.close()

