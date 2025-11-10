#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from vilib import Vilib
from pidog.preset_actions import bark

my_dog = Pidog()

sleep(0.1)

STEP = 0.5

def delay(time):
    my_dog.wait_legs_done()
    my_dog.wait_head_done()
    sleep(time)

def ball_track():
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=False, web=True)
    Vilib.color_detect(color="red")  # close, red, green, blue, yellow , orange, purple
    sleep(0.2)
    print('start')
    yaw = 0
    roll = 0
    pitch = 0
    flag = False
    direction = 0

    my_dog.do_action('stand', speed=50)
    my_dog.head_move([[yaw, 0, pitch]], immediately=True, speed=80)
    delay(0.5)

    while True:

        ball_x = Vilib.detect_obj_parameter['color_x'] - 320
        ball_y = Vilib.detect_obj_parameter['color_y'] - 240
        width = Vilib.detect_obj_parameter['color_w']

        if ball_x > 15 and yaw > -80:
            yaw -= STEP

        elif ball_x < -15 and yaw < 80:
            yaw += STEP

        if ball_y > 25:
            pitch -= STEP
            if pitch < - 40:
                pitch = -40
        elif ball_y < -25:
            pitch += STEP
            if pitch > 20:
                pitch = 20

        print(f"yaw: {yaw}, pitch: {pitch}, width: {width}")

        my_dog.head_move([[yaw, 0, pitch]], immediately=True, speed=100)
        if width == 0:
            pitch = 0
            yaw = 0
        elif width < 300:
            if my_dog.is_legs_done():
                if yaw < -30:
                    print("turn right")
                    my_dog.do_action('turn_right', speed=98)
                elif yaw > 30:
                    print("turn left")
                    my_dog.do_action('turn_left', speed=98)
                else:
                    my_dog.do_action('forward', speed=98)
        sleep(0.02)


if __name__ == "__main__":
    try:
        ball_track()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        Vilib.camera_close()
        my_dog.close()

