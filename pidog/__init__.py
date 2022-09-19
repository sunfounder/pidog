#!/usr/bin/env python3
from .pidog import Pidog
from robot_hat import utils
from time import sleep

utils.reset_mcu()
sleep(0.2)


def __main__():
    print("Thanks for using Pidog ! woof, woof, woof !")
    utils.reset_mcu()
    sleep(0.2)
