#!/usr/bin/env python3
from robot_hat import Pin
from time import sleep


class DualTouch():
    def __init__(self, sw1='D2', sw2='D3'):

        self.touch_1 = Pin(sw1)
        self.touch_2 = Pin(sw2)

    def is_slide(self):
        if self.touch_1.value() == 0:
            sleep(0.1)
            if self.touch_2.value() == 0:
                return 'LS'
            else:
                return 'L'
        elif self.touch_2.value() == 0:
            sleep(0.1)
            if self.touch_1.value() == 0:
                return 'RS'
            else:
                return 'R'
        return 'N'
