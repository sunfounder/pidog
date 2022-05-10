#!/usr/bin/env python3
from robot_hat import PWM, Servo
from robot_hat.utils import reset_mcu
from time import sleep

reset_mcu()
sleep(0.2)

if __name__ == '__main__':
    for i in range(12):
        servo = Servo(PWM(i))         
        servo.angle(0)     
