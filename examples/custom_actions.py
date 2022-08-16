#!/usr/bin/env python3
from pidog import Pidog
from time import sleep

my_dog = Pidog(feet_pins=[3, 4, 8, 9, 1, 2, 11, 12],
    head_pins=[5, 7, 6],
    tail_pin=[10],
    feet_init_angles=[45,0,-45,0,45,0,-45,0],
    head_init_angles=[0,0,0],
    tail_init_angle=[0]
)

def main():
    sleep(0.1)

    def delay(time):
        while len(my_dog.head_actions_buffer) > 0 :
            sleep(0.1)
        sleep(time)

    feet_action_1 = [
        [30, 60, -30, -60, 80, -45, -80, 45],
    ]
    feet_action_2 = [ 
        [30, 60, 45, 30, 80, -45, -80, 35],
        [30, 60, 90, -60, 80, -45, -80, 35],
    ]
    head_action_1 = [
         [0,10,-30]
    ]

    my_dog.feet_speed = 90
    my_dog.feet_move(feet_action_1,True)
    my_dog.head_move(head_action_1,True)
    delay(0.5)
    while True:
        my_dog.feet_move(feet_action_2,False,speed=50)
        delay(0.5)

if __name__ == "__main__":
    try:
        main()
    finally:
        my_dog.close()