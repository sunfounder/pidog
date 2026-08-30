#!/usr/bin/env python3
from robot_hat import Servo
from robot_hat.utils import reset_mcu
from time import sleep

reset_mcu()
sleep(1)

if __name__ == '__main__':
    for i in range(12):
        print(f"Servo {i} testing")
        for y  in range(-30, 31, 5):
            Servo(i).angle(y)
            sleep(0.2)
        Servo(i).angle(0)
        sleep(1)
