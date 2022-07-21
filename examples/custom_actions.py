#!/usr/bin/env python3
from pidog import Pidog
from time import sleep

my_pidog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
        head_pins=[9,10,11],tail_pin=[12],
        feet_init_angles=[45,0,-45,0,45,0,-45,0],
        head_init_angles=[0,0,0],
        tail_init_angle=[0])

def main():
    sleep(0.1)

    def delay(time):
        while len(my_pidog.head_actions_buffer) > 0 :
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

    my_pidog.feet_speed = 90
    my_pidog.feet_move(feet_action_1,True)
    my_pidog.head_move(head_action_1,True)
    delay(0.5)
    while True:
        my_pidog.feet_move(feet_action_2,False,speed=50)
        delay(0.5)

if __name__ == "__main__":
    try:
        main()
    finally:
        my_pidog.close()