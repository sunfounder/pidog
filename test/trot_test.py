
"""
A full MOVE divided into 8 SECTIONs. like below:
foot| 0 | 1 
====|===|===
 1  |^^^|___
 2  |___|^^^
 3  |___|^^^
 4  |^^^|___

4 feet move in this order: 1, 4, 2, 3
there will be a break after every foot move 

every SECTION devide into 4 STEPs
"""

#!/usr/bin/env python3

import readchar
from time import sleep as delay
from math import cos, pi, sin

class Trot():

    FORWARD = 1
    BACKWARD = -1
    LEFT = -1
    STRAIGHT = 0
    RIGHT = 1

    STEPS = 8
    FOOT_ORDER = [[1, 4], [2, 3]]
    SECTIONS = len(FOOT_ORDER)
    TOTAL_STEPS = SECTIONS * STEPS
    FOOT_STEP_HEIGHT = 20   # the height of the stepping foot
    FOOT_STEP_WIDTH  = 80   # the width of the stepping foot
    Y_OFFSET = -15          # the body y offset
    FOOT_POSITION_OFFSETS = [-10, -10, 20, 20]  # the foot center offset
    Z_ORIGIN = 80

    TURNING_RATE = 0.3
    FOOT_STEP_SCALES_LEFT =   [TURNING_RATE, 1, TURNING_RATE, 1]
    FOOT_STEP_SCALES_MIDDLE = [1, 1, 1, 1]
    FOOT_STEP_SCALES_RIGHT =  [1, TURNING_RATE, 1, TURNING_RATE]
    FOOT_ORIGINAL_Y_TABLE = [0, 1, 1, 0]
    FOOT_STEP_SCALES = [FOOT_STEP_SCALES_LEFT, FOOT_STEP_SCALES_MIDDLE, FOOT_STEP_SCALES_RIGHT]

    def __init__(self, fb, lr):
        """
            Trot init
            fb: FORWARD(1) or BACKWARD(-1)
            lr: LEFT(1), STRAIGHT(0) or RIGHT(-1)
        """
        self.fb = fb
        self.lr = lr

        if self.fb == self.FORWARD:
            if self.lr == self.STRAIGHT:
                self.y_offset = 0 + self.Y_OFFSET
            else:
                self.y_offset = 0 + self.Y_OFFSET
        elif self.fb == self.BACKWARD:
            if self.lr == self.STRAIGHT:
                self.y_offset =  0 + self.Y_OFFSET
            else:
                self.y_offset =  0 + self.Y_OFFSET
        else:
            self.y_offset = self.Y_OFFSET
        self.foot_step_width = [ self.FOOT_STEP_WIDTH * self.FOOT_STEP_SCALES[self.lr+1][i] for i in range(4) ]
        self.section_length = [ self.foot_step_width[i] / (self.SECTIONS-1) for i in range(4) ]
        self.step_down_length = [ self.section_length[i] / self.STEPS for i in range(4) ]
        self.foot_origin = [ self.foot_step_width[i] / 2 + self.y_offset + (self.FOOT_POSITION_OFFSETS[i] * self.FOOT_STEP_SCALES[self.lr+1][i]) for i in range(4) ]

    # Cosine
    def step_y_func(self, foot, step):
        """
        Step function for y axis,
        foot: current foot
        step: current step
        """
        theta = step * pi / (self.STEPS-1)
        temp = (self.foot_step_width[foot] * (cos(theta) - self.fb) / 2 * self.fb)
        y = self.foot_origin[foot] + temp
        return y

    # Linear
    # def step_z_func(self, step):
        # return self.Z_ORIGIN - (self.FOOT_STEP_HEIGHT * step / (self.STEPS-1))
    def step_z_func(self, step):
        return self.Z_ORIGIN - self.FOOT_STEP_HEIGHT

    # Sine
    # def step_z_func(self, step):
    #     theta = step * pi / (self.STEPS-1)
    #     z_temp = self.FOOT_STEP_HEIGHT*sin(theta)
    #     return self.Z_ORIGIN - z_temp

    def get_coords(self):
        """
        get coords action coords calculation,
        fb: forward(1) or backward(-1)
        lr: left(1), middle(0) or right(-1)
        """
        origin_foot_coord = [ [self.foot_origin[i] - self.FOOT_ORIGINAL_Y_TABLE[i] * self.section_length[i], self.Z_ORIGIN] for i in range(4) ]
        foot_coords = []
        for section in range(self.SECTIONS):
            for step in range(self.STEPS):
                if self.fb == 1:
                    raise_feet = self.FOOT_ORDER[section]
                else:
                    raise_feet = self.FOOT_ORDER[self.SECTIONS - section - 1]
                foot_coord = []

                for i in range(4):
                    if i + 1 in raise_feet:
                        y = self.step_y_func(i, step)
                        z = self.step_z_func(step)
                    else:
                        y = origin_foot_coord[i][0] + self.step_down_length[i] * self.fb
                        z = self.Z_ORIGIN
                    foot_coord.append([y, z])
                origin_foot_coord = foot_coord
                foot_coords.append(foot_coord)
        return foot_coords

def test():

    from pidog import Pidog
    dog = Pidog(feet_pins=[1, 2, 3, 4, 5, 6, 7, 8],
        head_pins=[9, 10, 11], tail_pin=[12],
    )

    def pause():
        key = readchar.readkey()
        if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            import sys
            print('')
            sys.exit(0)
    
    forward = Trot(fb=Trot.FORWARD, lr=Trot.STRAIGHT)
    backward = Trot(fb=Trot.BACKWARD, lr=Trot.STRAIGHT)
    forward_left = Trot(fb=Trot.FORWARD, lr=Trot.LEFT)
    forward_right = Trot(fb=Trot.FORWARD, lr=Trot.RIGHT)
    backward_left = Trot(fb=Trot.BACKWARD, lr=Trot.LEFT)
    backward_right = Trot(fb=Trot.BACKWARD, lr=Trot.RIGHT)
    foot_coords = forward.get_coords()

    # try:
    while True:
        for foot_coord in foot_coords:
            print(foot_coord)
            # dog.set_rpy(**rpy)
            # dog.set_pose(**pos)
            # dog.set_rpy(0, 0, 0, True)
            dog.set_feet(foot_coord)
            angles = dog.pose2feet_angle()
            dog.feet.servo_move2(angles, speed=99)
            # dog.feet_simple_move(angles)
            # pause() 
            # delay(0.001)
                
    # finally:
    #     dog.close()

if __name__ == '__main__':
    test()