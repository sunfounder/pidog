#!/usr/bin/env python3
from robot_hat import Servo
from robot_hat.utils import reset_mcu
from time import sleep

reset_mcu()
sleep(1)

if __name__ == '__main__':
    servos = []
    for i in range(12):
        print(f"Servo {i} set to zero")
        Servo(i).angle(10)
        sleep(0.1)
        Servo(i).angle(0)
        sleep(0.1)
    while True:
        sleep(1)
