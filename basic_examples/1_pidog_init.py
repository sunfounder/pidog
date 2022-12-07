# !/usr/bin/env python3
''' pidog initialization

API:
    Class: Pidog()

    __init__(leg_pins=DEFAULT_LEGS_PINS, 
            head_pins=DEFAULT_HEAD_PINS,
            tail_pin=DEFAULT_TAIL_PIN,
            leg_init_angles=None,
            head_init_angles=None,
            tail_init_angle=None)
    
    - leg_pins    list, 8*1 list, the pins of the 8 servos on the legs,
                DEFAULT_LEGS_PINS = [2, 3, 7, 8, 0, 1, 10, 11]
                order: Left Front Leg, Left Front Leg, Right Front Leg, Right Front Leg, Left Hind Leg, Left Hind Leg, Right Hind Leg, Right Hind Leg
    
    - head_pins   list, 3*1 list, the pins of the 3 servos on the head
                DEFAULT_HEAD_PINS = [4, 6, 5]
                order: Yaw, Roll, Pitch
    
    - tail_pin    list, 1*1 list, the pin of the tail servos
                DEFAULT_TAIL_PIN = [9]

    - leg_init_angles    list, 8*1 list, the initial angles of the legs servos
    - head_init_angles   list, 3*1 list, the initial angles of the head servos
    - tail_init_angle    list, 1*1 list, the initial angles of the tail servo

'''

# Import Pidog class
from pidog import Pidog

# instantiate a Pidog with default parameters
# my_dog = Pidog()

# instantiate a Pidog with custom initialized servo angles
my_dog = Pidog(leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                head_init_angles = [0, 0, -25],
                tail_init_angle= [0]
            )
