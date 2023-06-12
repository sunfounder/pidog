#!/usr/bin/env python3
from .pidog import Pidog
from robot_hat import utils
from time import sleep

__version__ = "1.1.0"

utils.reset_mcu()
sleep(0.2)


def __main__():
    print(f"Thanks for using Pidog {__version__} ! woof, woof, woof !")
    utils.reset_mcu()
    sleep(0.2)
