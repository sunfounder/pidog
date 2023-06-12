from pidog import Pidog
from time import sleep

my_dog = Pidog()

SPEED = 100

try:
    while True:
        my_dog.do_action("stand", speed=SPEED)
        sleep(2)
        my_dog.do_action("lie", speed=SPEED)
        sleep(2)
        my_dog.do_action("pushup", speed=SPEED)
        sleep(2)
        my_dog.do_action("lie", speed=SPEED)
        sleep(2)
except KeyboardInterrupt:
    my_dog.close()
