# !/usr/bin/env python3
''' tail control
    Basic use of tail servo control

API:
    Pidog.tail_move(target_angles, immediately=True, speed=50)

        tail servo angles control, it will store the target_angles in a buffer, and the built-in tail servo control thread
        will control the angle of the tail servo

        - target_angles   n*1 2D list, angle arrangements of tail servo, could be one group of angle,
                          or multiple groups of angle, eg:
                          [[30], [-30], [...], ...]

        - immediately    bool, whether to execute the specified action immediately, if true: it will clear the buffer first, and store the target_angles,
                         the set actions will be executed immediately; if false, the will add target_angles at the end of the buffer, the actions will be
                         executed after previous actions have been executed

        - speed    int, speed of action, 0 ~ 100

    Pidog.is_tail_done()
        whether all the tail actions in the buffer to be executed

    Pidog.wait_tail_done()
        wait for all the tail actions in the buffer to be executed

    Pidog.tail_stop()
        clear all the tail actions of leg in the buffer, to make tail servo stop

'''

from pidog import Pidog
import time

my_dog = Pidog()

# stand action
stand_action = [
    [25, 35, -25, -35, 35, 35, -35, -35],
]
my_dog.legs_move(stand_action, speed=30)
# wait all legs actions done
my_dog.wait_legs_done()


wag_tail_actions = [
    [-30], [30],
]

while True:
    my_dog.tail_move(wag_tail_actions, speed=100)
    my_dog.wait_tail_done()

