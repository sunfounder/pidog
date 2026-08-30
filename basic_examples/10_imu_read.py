# !/usr/bin/env python3
''' read imu sh3001 data
    SH3001, an imu with integrated 3-axis accelerometer and 3-axis gyroscope
    Pay attention to the installation direction of the module when using.

    The data "accData" and "gyroData" of the imu will be continuously refreshed
    in the built-in thread of the Pidog class.

API:
    Pidog.accData = [ax, ay, az]
        the acceleration value, default gravity 1G = -16384
        note that the accelerometer direction is opposite to the actual acceleration direction

    Pidog.gyroData = [gx, gy, gz]
        the gyro value

more to see: ../pidog/sh3001.py

'''

from pidog import Pidog
import time

my_dog = Pidog()

while True:
    ax, ay, az = my_dog.accData
    gx, gy, gz = my_dog.gyroData
    print(f"accData: {ax}, {ay}, {az}       gyroData: {gx}, {gy}, {gz}")
    time.sleep(0.2)