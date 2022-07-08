#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
import readchar
import numpy as np
from math import pi

dog = Pidog(feet_pins=[1, 2, 3, 4, 5, 6, 7, 8],
    head_pins=[9, 10, 11], tail_pin=[12],
    )

feet_coords = [[0, 80], [0, 80], [0, 80], [0, 80]]

pose = {
    "x": 0,
    "y": 0,
    "z": 80,
}
rpy = {
    "roll": 0,
    "pitch": 0,
    "yaw": 0,
}

while True:

    print("""
    Pose Test:
        === Foot 1 ===  === Foot 2 ===
        [1] < y > [2]    [3] < y > [4]  ==== Pose ====  ====== RPY ======
        [Q] < z > [W]    [E] < z > [R]  [T] < x > [Y]   [U] <  roll > [I]
        === Foot 3 ===  === Foot 4 ===  [G] < y > [H]   [J] < pitch > [K]
        [A] < y > [S]    [D] < y > [F]  [B] < z > [N]   [M] <  yaw  > [,]
        [Z] < z > [X]    [C] < z > [V]
    """
    )
    print(f"feet_coords: {feet_coords}")
    print(f"pose: {list(dog.pose.flatten())}")
    print(f"rpy: {list(dog.rpy / pi * 180)}")
    dog.set_feet(feet_coords)
    dog.set_pose(**pose)
    dog.set_rpy(**rpy)
    angle_list = dog.pose2feet_angle()
    print(f"angle_list: {angle_list}")
    dog.feet.angle_list(angle_list)
    print(f"Roll: {dog.roll}")
    print(f"Pitch: {dog.pitch}")

    key = readchar.readkey().upper()
    if key == '1':
        feet_coords[0][0] -= 1
    elif key == '2':
        feet_coords[0][0] += 1
    elif key == 'Q':
        feet_coords[0][1] -= 1
    elif key == 'W':
        feet_coords[0][1] += 1
    elif key == '3':
        feet_coords[1][0] -= 1
    elif key == '4':
        feet_coords[1][0] += 1
    elif key == 'E':
        feet_coords[1][1] -= 1
    elif key == 'R':
        feet_coords[1][1] += 1
    elif key == 'A':
        feet_coords[2][0] -= 1
    elif key == 'S':
        feet_coords[2][0] += 1
    elif key == 'Z':
        feet_coords[2][1] -= 1
    elif key == 'X':
        feet_coords[2][1] += 1
    elif key == 'D':
        feet_coords[3][0] -= 1
    elif key == 'F':
        feet_coords[3][0] += 1
    elif key == 'C':
        feet_coords[3][1] -= 1
    elif key == 'V':
        feet_coords[3][1] += 1
    elif key == 'T':
        pose["x"] -= 1
    elif key == 'Y':
        pose["x"] += 1
    elif key == 'G':
        pose["y"] -= 1
    elif key == 'H':
        pose["y"] += 1
    elif key == 'B':
        pose["z"] -= 1
        feet_coords[0][1] -= 1
        feet_coords[1][1] -= 1
        feet_coords[2][1] -= 1
        feet_coords[3][1] -= 1
    elif key == 'N':
        pose["z"] += 1
        feet_coords[0][1] += 1
        feet_coords[1][1] += 1
        feet_coords[2][1] += 1
        feet_coords[3][1] += 1
    elif key == 'U':
        rpy["roll"] -= 1
    elif key == 'I':
        rpy["roll"] += 1
    elif key == 'J':
        rpy["pitch"] -= 1
    elif key == 'K':
        rpy["pitch"] += 1
    elif key == 'M':
        rpy["yaw"] -= 1
    elif key == ',':
        rpy["yaw"] += 1

    if key == 'P':
        dog.close_all_thread()
        quit()
    sleep(0.1)
