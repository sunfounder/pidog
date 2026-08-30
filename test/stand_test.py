from pidog import Pidog
from time import sleep

my_dog = Pidog()

SPEED = 95

my_dog.do_action("stand", speed=SPEED)

sleep(3)
my_dog.close()
