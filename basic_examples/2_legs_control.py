# !/usr/bin/env python3
''' legs control
    Basic use of leg servos control

API:
    Pidog.legs_move(target_angles, immediately=True, speed=50)

        legs servo angles control, it will store the target_angles in a buffer, and the built-in leg servo control thread will control the angle of the servos

        - target_angles   n*8 2D list, angle arrangements of leg servos, could be one group of angles,
                          or multiple groups of angles, the order of the servos is:
                          [[ left front leg, left front leg, right front leg, right front leg,
                              left hind leg, left hind leg,right hind leg, right hind leg],
                          [...], ...]

        - immediately    bool, whether to execute the specified action immediately, if true: it will clear the buffer first, and store the target_angles,
                         the set actions will be executed immediately; if false, the will add target_angles at the end of the buffer, the actions will be
                         executed after previous actions have been executed

        - speed    int, speed of action, 0 ~ 100

    Pidog.is_legs_done()
        whether all the actions of leg in the buffer to be executed

    Pidog.wait_legs_done()
        wait for all the actions of leg in the buffer to be executed

    Pidog.legs_stop()
        clear all the actions of leg in the buffer, to make legs stop

'''

from pidog import Pidog
import time

my_dog = Pidog()

# single action
single_action = [ # half stand
    [45, 10, -45, -10, 45, 10, -45, -10],
]
my_dog.legs_move(single_action, speed=30)

single_action_2 = [ # push_up preparation
    [45, 35, -45, -35, 80, 70, -80, -70]
]
my_dog.legs_move(single_action_2, immediately=False, speed=20)

# wait all actions done
my_dog.wait_legs_done()
time.sleep(0.5)

# multiple actions
multiple_actions  = [ # push_up
    [90, -30, -90, 30, 80, 70, -80, -70],
    [45, 35, -45, -35, 80, 70, -80, -70]
]

while True:
    my_dog.legs_move(multiple_actions, immediately=False, speed=75)
    time.sleep(0.1)
