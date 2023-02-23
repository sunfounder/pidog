#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from vilib import Vilib
from preset_actions import bark

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
    direction = 0

    my_dog.do_action('sit', speed=50)
    my_dog.head_move([[yaw, 0, pitch]], pitch_comp=-40, immediately=True, speed=80)
    delay(0.5)
    if my_dog.ears.isdetected():
        direction = my_dog.ears.read()

    while True:
        # If heard somthing, turn to face it
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
            my_dog.head_move([[yaw, 0, pitch]], pitch_comp=-40, immediately=True, speed=100)
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

