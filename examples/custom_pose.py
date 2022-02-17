#!/usr/bin/env python3
from pidog import Pidog
from time import sleep


# def main():
#     my_pidog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
#             head_pins=[9,10,11],tail_pin=[12],
#             feet_init_angles=[45,0,-45,0,45,0,-45,0],
#             head_init_angles=[0,0,0],
#             tail_init_angle=[0])
#     sleep(0.1)

#     new_feet_action = [
#         [-90,90,90,-90,90,90,-90,-90]
#     ]
#     new_head_action = [
#          [0,0,20]
#     ]

#     my_pidog.feet_move(new_feet_action,True)
#     my_pidog.head_move(new_head_action,True)

def main():
    my_pidog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
            head_pins=[9,10,11],tail_pin=[12],
            feet_init_angles=[45,0,-45,0,45,0,-45,0],
            head_init_angles=[0,0,0],
            tail_init_angle=[0])
    sleep(0.1)

    new_feet_action = [
        [45,0,-45,0,45,0,-45,0],
        [0,0,0,0,45,0,-45,0],
        [-20,0,-45,0,45,0,-45,0],
        [45,0,-45,0,45,0,-45,0]
    ]
    new_head_action = [
         [0,0,20]
    ]

    my_pidog.feet_move(new_feet_action,True)
    my_pidog.head_move(new_head_action,True)


if __name__ == "__main__":
    main()