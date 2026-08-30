#!/usr/bin/env python3
from .pidog import Pidog
from robot_hat import utils
from time import sleep
from .version import __version__

def __main__():
    print(f"Thanks for using Pidog {__version__} ! woof, woof, woof !")
    utils.reset_mcu()
    sleep(0.2)
