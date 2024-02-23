#!/usr/bin/env python3
from robot_hat import Pin
import time


class DualTouch():

    SLIDE_MAX_INTERVAL = 0.5 # second, Maximum effective interval for sliding detection

    def __init__(self, sw1='D2', sw2='D3'):

        self.touch_L = Pin(sw1)
        self.touch_R = Pin(sw2)
        self.last_touch = 'N'
        self.last_touch_time = 0

    # def read(self):
    #     if self.touch_L.value() == 1:
    #         time.sleep(0.1)
    #         if self.touch_R.value() == 1:
    #             return 'LS'
    #         else:
    #             return 'L'
    #     elif self.touch_R.value() == 1:
    #         time.sleep(0.1)
    #         if self.touch_L.value() == 1:
    #             return 'RS'
    #         else:
    #             return 'R'
    #     return 'N'

    def read(self):
        if self.touch_L.value() == 1:
            if self.last_touch == 'R' and\
                time.time() - self.last_touch_time <= self.SLIDE_MAX_INTERVAL:
                val = 'RS'
            else:
                val = 'L'
            self.last_touch_time = time.time()
            self.last_touch = 'L'
            return val
        elif self.touch_R.value() == 1:
            if self.last_touch == 'L' and\
                time.time() - self.last_touch_time <= self.SLIDE_MAX_INTERVAL:
                val = 'LS'
            else:
                val = 'R'
            self.last_touch_time = time.time()
            self.last_touch = 'R'
            return val
        return 'N'