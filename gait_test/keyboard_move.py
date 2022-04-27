#!/usr/bin/env python3
from public_functions import *

from walk_final import cal_walk
from turn_left_final import cal_turn_left
from turn_right_final import cal_turn_right
from backward_final import cal_backward

# load datas
print('\n forward_data:')
forward_datas = cal_walk()
print('\n turn_left_data:')
turn_left_datas = cal_turn_left()
print('\n turn_right_data:')
turn_right_datas = cal_turn_right()
print('\n backward_data:')
backward_datas = cal_backward()

delay_s = 0.012

def forward():
    for angles in forward_datas:
        feet_simple_move(angles,delay_s)

def turn_left():
    for angles in turn_left_datas:
        feet_simple_move(angles,delay_s)

def turn_right():
    for angles in turn_right_datas:
        feet_simple_move(angles,delay_s)

def backward():
    for angles in backward_datas:
        feet_simple_move(angles,delay_s)




def main():

    while True:
        key = readchar.readkey()
        if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            import sys
            print('')
            sys.exit(0)
        elif key == 'w':
            forward()
        elif key == 'a':
            turn_left()
        elif key == 'd':
            turn_right()
        elif key == 's':
            backward()            
        else:
            print('key:',key)
            continue
        sleep(0.001)


if __name__ == '__main__':
    main()