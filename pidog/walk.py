
"""
A full MOVE divided into 8 SECTIONs. like below:
leg| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7
====|===|===|===|===|===|===|===|===
 1  |^^^|___|___|___|___|___|___|___
 2  |___|___|___|___|^^^|___|___|___
 3  |___|___|___|___|___|___|^^^|___
 4  |___|___|^^^|___|___|___|___|___

4 legs move in this order: 1, 4, 2, 3
there will be a break after every leg move

every SECTION devide into 4 STEPs
"""

#!/usr/bin/env python3

from math import cos, pi


class Walk():

    FORWARD = 1
    BACKWARD = -1
    LEFT = -1
    STRAIGHT = 0
    RIGHT = 1

    SECTION_COUNT = 8
    STEP_COUNT = 6
    LEG_ORDER = [1, 0, 4, 0, 2, 0, 3, 0]
    LEG_STEP_HEIGHT = 20    # the height of the stepping leg
    LEG_STEP_WIDTH = 80    # the width of the stepping leg
    CENTER_OF_GRAVIRTY = -15  # the center of gravity of the robot
    LEG_POSITION_OFFSETS = [-10, -10, 20, 20]  # the leg center offset
    Z_ORIGIN = 80

    TURNING_RATE = 0.3
    LEG_STEP_SCALES_LEFT = [TURNING_RATE, 1, TURNING_RATE, 1]
    LEG_STEP_SCALES_MIDDLE = [1, 1, 1, 1]
    LEG_STEP_SCALES_RIGHT = [1, TURNING_RATE, 1, TURNING_RATE]
    LEG_ORIGINAL_Y_TABLE = [0, 2, 3, 1]
    LEG_STEP_SCALES = [LEG_STEP_SCALES_LEFT,
                       LEG_STEP_SCALES_MIDDLE, LEG_STEP_SCALES_RIGHT]

    def __init__(self, fb, lr):
        """
            Walk init
            fb: FORWARD(1) or BACKWARD(-1)
            lr: LEFT(1), STRAIGHT(0) or RIGHT(-1)
        """
        self.fb = fb
        self.lr = lr

        if self.fb == self.FORWARD:
            if self.lr == self.STRAIGHT:
                self.y_offset = 0 + self.CENTER_OF_GRAVIRTY
            else:
                self.y_offset = 0 + self.CENTER_OF_GRAVIRTY
        elif self.fb == self.BACKWARD:
            if self.lr == self.STRAIGHT:
                self.y_offset = 0 + self.CENTER_OF_GRAVIRTY
            else:
                self.y_offset = 0 + self.CENTER_OF_GRAVIRTY
        else:
            self.y_offset = self.CENTER_OF_GRAVIRTY
        self.leg_step_width = [
            self.LEG_STEP_WIDTH * self.LEG_STEP_SCALES[self.lr+1][i] for i in range(4)]
        self.section_length = [self.leg_step_width[i] /
                               (self.SECTION_COUNT-1) for i in range(4)]
        self.step_down_length = [
            self.section_length[i] / self.STEP_COUNT for i in range(4)]
        self.leg_origin = [self.leg_step_width[i] / 2 + self.y_offset + (
            self.LEG_POSITION_OFFSETS[i] * self.LEG_STEP_SCALES[self.lr+1][i]) for i in range(4)]

    # Cosine
    def step_y_func(self, leg, step):
        """
        Step function for y axis,
        leg: current leg
        step: current step
        """
        theta = step * pi / (self.STEP_COUNT-1)
        temp = (self.leg_step_width[leg] *
                (cos(theta) - self.fb) / 2 * self.fb)
        y = self.leg_origin[leg] + temp
        return y

    # Linear
    def step_z_func(self, step):
        return self.Z_ORIGIN - (self.LEG_STEP_HEIGHT * step / (self.STEP_COUNT-1))

    def get_coords(self):
        """
        get coords action coords calculation,
        fb: forward(1) or backward(-1)
        lr: left(1), middle(0) or right(-1)
        """
        origin_leg_coord = [[self.leg_origin[i] - self.LEG_ORIGINAL_Y_TABLE[i]
                             * 2 * self.section_length[i], self.Z_ORIGIN] for i in range(4)]
        leg_coord = list.copy(origin_leg_coord)
        leg_coords = []
        for section in range(self.SECTION_COUNT):
            for step in range(self.STEP_COUNT):
                if self.fb == 1:
                    raise_leg = self.LEG_ORDER[section]
                else:
                    raise_leg = self.LEG_ORDER[self.SECTION_COUNT - section - 1]

                for i in range(4):
                    if raise_leg != 0 and i == raise_leg-1:
                        y = self.step_y_func(i, step)
                        z = self.step_z_func(step)
                    else:
                        y = leg_coord[i][0] + \
                            self.step_down_length[i] * self.fb
                        z = self.Z_ORIGIN
                    leg_coord[i] = [y, z]
                leg_coords.append(list.copy(leg_coord))
        leg_coords.append(origin_leg_coord)
        return leg_coords
