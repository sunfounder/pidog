#!/usr/bin/env python3
from pidog import Pidog
from time import sleep, time
from math import pi
import numpy as np
from awesome_print import AwesomePrint

ap = AwesomePrint()

dog = Pidog(feet_pins=[1, 2, 3, 4, 5, 6, 7, 8],
    head_pins=[9, 10, 11], tail_pin=[12],
    )

dog.KP = 0.03
dog.KI = 0.0
dog.KD = 0.0

ap.clear()
roll_offset_list = []
pitch_offset_list = []
while True:
    start = time()
    dog.set_rpy(0, 0, pid=True)
    angle_list = dog.pose2feet_angle()
    dog.feet.angle_list(angle_list)
    ap.print(f"Roll: {dog.roll}", [2, 5])
    ap.print(f"Pitch: {dog.pitch}", [3, 5])
    roll_offset_list.append(dog.rpy[0] * 180 / pi)
    pitch_offset_list.append(dog.rpy[1] * 180 / pi)
    roll_offset = np.mean(roll_offset_list)
    pitch_offset = np.mean(pitch_offset_list)
    ap.print(f"Roll Offset: {roll_offset}", [4, 5])
    ap.print(f"Pitch Offset: {pitch_offset}", [5, 5])
    if len(roll_offset_list) > 100:
        roll_offset_list.pop(0)
        pitch_offset_list.pop(0)
    ap.print(time()-start, [7, 5])

