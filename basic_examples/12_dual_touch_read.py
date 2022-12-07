# !/usr/bin/env python3
''' read dual_touch module

API:
    Pidog.dual_touch.read()
        - return str, dual_touch status:
            - 'N'  no touch
            - 'L'  left touched
            - 'LS' left slide
            - 'R'  right touched
            - 'RS' right slide
'''

from pidog import Pidog
import time

my_dog = Pidog()
while True:
    touch_status = my_dog.dual_touch.read()
    print(f"touch_status: {touch_status}")
    time.sleep(0.5)