#!/usr/bin/env python3
from .pidog import Pidog
from robot_hat import utils
from time import sleep
from .version import VERSION
utils.reset_mcu()
sleep(0.2)


def __main__():
    print(f"Thanks for using Pidog {VERSION} ! woof, woof, woof !")
    utils.reset_mcu()
    sleep(0.2)
