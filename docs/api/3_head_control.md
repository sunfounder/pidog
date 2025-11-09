# 3_head_control

**File:** `basic_examples/3_head_control.py`

## Module Description

head control
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

    Pidog.head_move(target_yrps, roll_comp=0, pitch_comp=0, immediately=True, speed=50)

        legs servo angles control with "relative ypr angles", You can set "roll_comp" and "pitch_comp" so that the initial position of the head is in a
        horizontal position to offset the influence of body tilt. In this way, the same set of c can be used for different body tilt angles

        - target_yrps    n*3 2D list, relative angle arrangements of head servos

        - roll_comp   angle compensation on roll axis

        - pitch_comp    angle compensation on pitch axis

        - immediately   bool, whether to execute the specified action immediately

        - speed   int, speed of action, 0 ~ 100

    Pidog.is_head_done()
        whether all the head actions in the buffer to be executed

    Pidog.wait_head_done()
        wait for all the head actions in the buffer to be executed

    Pidog.head_stop()
        clear all the head actions of leg in the buffer, to make head servos stop

