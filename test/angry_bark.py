from pidog import Pidog
from time import sleep

my_dog = Pidog()

SPEED = 90

my_dog.do_action("stand", speed=SPEED)
my_dog.wait_all_done()
sleep(1)

yrp = [0, 0, 0]
h1 = [0 + yrp[0], 0 + yrp[1], 20 + yrp[2]]
h2 = [0 + yrp[0], 0 + yrp[1],  0 + yrp[2]]

f1 = my_dog.legs_angle_calculation(
    [[0, 100], [0, 100], [30, 90], [30, 90]])
f2 = my_dog.legs_angle_calculation(
    [[-20, 90], [-20, 90], [0, 90], [0, 90]])

my_dog.speak("angry")
my_dog.legs_move([f1], immediately=True, speed=95)
my_dog.head_move([h1], immediately=True, speed=95)
my_dog.wait_all_done()
sleep(0.01)
my_dog.legs_move([f2], immediately=True, speed=95)
my_dog.head_move([h2], immediately=True, speed=95)
my_dog.wait_all_done()
sleep(0.01)

my_dog.close()
