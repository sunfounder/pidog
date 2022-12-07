# !/usr/bin/env python3
''' head control
    Basic use of head servos control

API:
    Pidog.head_move_raw(target_angles, immediately=True, speed=50)
        
        head servo angles control with "raw servo angles", it will store the target_angles in a buffer, and the built-in head servo control thread
        will control the angle of the servos

        - target_angles   n*3 2D list, angle arrangements of head servos, could be one group of angles,
                          or multiple groups of angles, the order of the servos is:
                          [[ yaw_servo, roll_servo, pitch_servo], [...], ...]
        
        - immediately    bool, whether to execute the specified action immediately, if true: it will clear the buffer first, and store the target_angles,
                         the set actions will be executed immediately; if false, the will add target_angles at the end of the buffer, the actions will be
                         executed after previous actions have been executed
        
        - speed    int, speed of action, 0 ~ 100

    Pidog.head_move(target_yrps, roll_init=0, pitch_init=0, immediately=True, speed=50)
        
        legs servo angles control with "relative ypr angles", You can set "roll_init" and "pitch_init" so that the initial position of the head is in a 
        horizontal position to offset the influence of body tilt. In this way, the same set of c can be used for different body tilt angles

        - target_yrps    n*3 2D list, relative angle arrangements of head servos

        - roll_init   int, initial angle of roll axis

        - pitch    int, initial angle of pitch axis

        - immediately   bool, whether to execute the specified action immediately

        - speed   int, speed of action, 0 ~ 100

    Pidog.is_head_done()
        whether all the head actions in the buffer to be executed

    Pidog.wait_head_done()
        wait for all the head actions in the buffer to be executed

    Pidog.head_stop()
        clear all the head actions of leg in the buffer, to make head servos stop

'''

from pidog import Pidog
import time

my_dog = Pidog()


# sit
sit_action = [
    [30, 60, -30, -60, 80, -45, -80, 45],
]
my_dog.legs_move(sit_action, speed=30)
# wait all legs actions done
my_dog.wait_legs_done()


# level-view by head_move_raw()
# my_dog.head_move_raw([[0, 0, -30]], speed=80)

# level-view by head_move()
my_dog.head_move([[0, 0, 0]], pitch_init=-30, speed=80)

# actually "head_move_raw([[0, 0, -30]]" is the same as "head_move([[0, 0, 0]], pitch_init=-30)"

my_dog.wait_head_done()

head_test_actions = [ # relative angles
    [0, 0, 0], [90, 0, 0], [0, 0, 0], [-90, 0, 0], [0, 0, 0],
    [0, 0, 0], [0, 60, 0], [0, 0, 0], [0, -60, 0], [0, 0, 0],
    [0, 0, 0], [0, 0, 45], [0, 0, 0], [0, 0, -60], [0, 0, 0],
]

while True:
    my_dog.head_move(head_test_actions, pitch_init=-30, speed=50)
    my_dog.wait_head_done()
    time.sleep(0.2)
