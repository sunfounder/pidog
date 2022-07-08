#!/usr/bin/env python3
from pidog import Pidog
from time import time, sleep
import readchar
import numpy as np
from math import pi, sin, cos

dog = Pidog(feet_pins=[1, 2, 3, 4, 5, 6, 7, 8],
    head_pins=[9, 10, 11], tail_pin=[12],
    )

foot_step_height = 20  # the height of the stepping foot
foot_step_width = 50   # the width of the stepping foot
raise_time_period = 6  # the time period of the stepping foot
move_time_period = 6   # the time period of the robot moving with all foot on floor
y_offset = 0           # the body y offset
foot_stand_offset = 10   # the foot center offset

quarter_period = raise_time_period + move_time_period
total_period = quarter_period * 4
y_step = foot_step_width / total_period
foot_y_origin = [
    -foot_step_width/2 - foot_stand_offset,
     foot_step_width/2 - foot_stand_offset,
     foot_step_width/2 + foot_stand_offset,
    -foot_step_width/2 + foot_stand_offset,
]
def feet_simple_move(angles, delay=0.001):
    tt = time()

    rel_angles = []
    for i in range(len(angles)):
        rel_angles.append(angles[i] + dog.feet.offset[i])
    dog.feet.angle_list(rel_angles) 

    tt2 = time() - tt
    delay2 = 0.001*len(angles) - tt2
    # print('\r time: %s    '%delay2,end='')

    if delay2 < -delay:
        delay2 = -delay
    sleep(delay + delay2)

foot_order = [1, 2, 0, 3]

# def get_y(i):
#     new_i = i % quarter_period
#     y = - foot_step_width * ((cos((new_i+raise_time_period/2) * pi / total_period) - 1) / 2 + int(i / quarter_period)) / 4
#     print(y)
#     return y

def get_y(i):
    return (i * -y_step) + (foot_step_width / 2)

def walk():
    pose = {"y": foot_step_width / 2, "z": 80}
    foot_coords = [ [foot_y_origin[i], pose["z"]] for i in range(4) ]

    for i in range(total_period + 1):
        pose["y"] = get_y(i)
        dog.set_feet(foot_coords)
        dog.set_pose(**pose)
        # dog.set_rpy(**rpy)
        angle_list = dog.pose2feet_angle()
        key = readchar.readkey()
        if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            import sys
            print('')
            sys.exit(0)
        print(i)
        if i % quarter_period >= move_time_period:
            _i = i % quarter_period - move_time_period
            print(f"_i: {_i}")
            y = - foot_step_width * ((cos(_i * pi / (raise_time_period - 1)) - 1) / 2)
            z = foot_step_height * sin(_i * pi / (raise_time_period - 1))
            print(y, z)
            current_foot = int(i / quarter_period)
            current_foot = foot_order[current_foot]
            foot_coords[current_foot][0] = foot_y_origin[current_foot] - y
            foot_coords[current_foot][1] = pose["z"] - z
            if current_foot in [0, 1]:
                foot_coords[current_foot][0] -= foot_stand_offset
            else:
                foot_coords[current_foot][0] += foot_stand_offset
        print(f"foot_coords: {foot_coords}")
        print(pose)
        # pose["y"] -= y_step
        feet_simple_move(angle_list, delay=0.01)  # 0.005 ~ 0.05

if __name__ == '__main__':
    while True:
        walk()