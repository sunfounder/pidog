#!/usr/bin/env python3
from time import sleep
from pidog import Pidog
import readchar 
from pidog.walk import Walk
from pidog.trot_cal import cal_trot

my_dog = Pidog(feet_pins=[1, 2, 3, 4, 5, 6, 7, 8], 
                head_pins=[9, 10, 11], 
                tail_pin=[12], 
                )
sleep(0.5) 


_forward = Walk(fb=Walk.FORWARD, lr=Walk.STRAIGHT)
_backward = Walk(fb=Walk.BACKWARD, lr=Walk.STRAIGHT)
_forward_left = Walk(fb=Walk.FORWARD, lr=Walk.LEFT)
_forward_right = Walk(fb=Walk.FORWARD, lr=Walk.RIGHT)
_backward_left = Walk(fb=Walk.BACKWARD, lr=Walk.LEFT)
_backward_right = Walk(fb=Walk.BACKWARD, lr=Walk.RIGHT)

forward_data = _forward.get_coords()
backward_data = _backward.get_coords()
forward_left_data = _forward_left.get_coords()
forward_right_data = _forward_right.get_coords()
backward_left_data = _backward_left.get_coords()
backward_right_data = _backward_right.get_coords()


def forward():
    for foot_coord in forward_data:
        # print(foot_coord)
        my_dog.set_feet(foot_coord)
        angles = my_dog.pose2feet_angle()
        my_dog.feet_simple_move(angles, speed=100)

def backward():
    for foot_coord in backward_data:
        # print(foot_coord)
        my_dog.set_feet(foot_coord)
        angles = my_dog.pose2feet_angle()
        my_dog.feet_simple_move(angles, speed=100)

def forward_left():
    for foot_coord in forward_left_data:
        # print(foot_coord)
        my_dog.set_feet(foot_coord)
        angles = my_dog.pose2feet_angle()
        my_dog.feet_simple_move(angles, speed=100)

def forward_right():
    for foot_coord in forward_right_data:
        # print(foot_coord)
        my_dog.set_feet(foot_coord)
        angles = my_dog.pose2feet_angle()
        my_dog.feet_simple_move(angles, speed=100)

def backward_left():
    for foot_coord in backward_left_data:
        # print(foot_coord)
        my_dog.set_feet(foot_coord)
        angles = my_dog.pose2feet_angle()
        my_dog.feet_simple_move(angles, speed=100)

def backward_right():
    for foot_coord in backward_right_data:
        # print(foot_coord)
        my_dog.set_feet(foot_coord)
        angles = my_dog.pose2feet_angle()
        my_dog.feet_simple_move(angles, speed=100)

    
def main():
    while True:
        key = readchar.readchar().lower()
        if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            import sys
            print('')
            sys.exit(0)
        elif key == 'w':
            forward()
        elif key == 's':
            backward()
        elif key == 'q':
            forward_left()
        elif key == 'e':
            forward_right() 
        elif key == 'a':
            backward_left()
        elif key == 'd':
            backward_right()
        else:
            print('key:',key)
            continue
        sleep(0.001)  
    



if __name__ == "__main__":
    main()