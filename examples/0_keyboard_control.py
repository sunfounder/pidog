#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
import readchar 
''' https://github.com/magmax/python-readchar '''

manual = '''
Use the following keys to select the servo to be controlled, 
servo corresponding keys refer to the following chart:
                     9,
                   0, '-'
                     |
              2,1 --[ ]-- 3,4
                    [ ]
              6,5 --[ ]-- 7,8
                     |
                    '='
                    / 
    1 ~ 8 : Leg servos      W: increase angle
    9 : Head yaw            S: decreases angle 
    0 : Head roll            
    - : Head pitch          R: enter/quit calibrate mode
    = : Tail                SPACE: confirm calibration
                                            Ctrl+C: Quit

'''

my_dog = Pidog(feet_pins=[1, 2, 3, 4, 5, 6, 7, 8],
        head_pins=[9, 10, 11], tail_pin=[12],
        )

my_dog.do_action('lie')
while len(my_dog.feet_actions_buffer) > 0:
    sleep(0.01)

feet_angles = 0.0
head_angles = 0.0
tail_angle = 0.0
feet_offset = 0.0
head_offset = 0.0
tail_offset = 0.0
mode = 'move'  # move/calibrate 
servo_num = '1' 

OFFSET_STEP = (180 / 2000) * (20000 / 4095) # 舵机实际精度
MOVE_STEP = 1

def get_real_values():
    global feet_angles, head_angles, tail_angle
    global feet_offset, head_offset, tail_offset
    feet_angles = list.copy(my_dog.feet_current_angle)
    head_angles = list.copy(my_dog.head_current_angle)
    tail_angle = list.copy(my_dog.tail_current_angle)
    feet_offset = list.copy(my_dog.feet.offset)
    head_offset = list.copy(my_dog.head.offset)
    tail_offset = list.copy(my_dog.tail.offset) 

def show_info():
    print("\033[H\033[J", end='')  # clear terminal windows
    print(manual)
    if mode == 'calibrate':
        print('[ Calibrate Mode ] servo_num: %s'%servo_num)   
        print('feet_offset: %s'%feet_offset)
        print('head_offset: %s'%head_offset)
        print('tail_offset: %s'%tail_offset)    
    else:
        print('[  Control Mode  ] servo_num: %s'%servo_num)  
        print('feet_angles: %s'%feet_angles)
        print('head_angles: %s'%head_angles)
        print('tail_angle: %s'%tail_angle)

def reset():
    my_dog.feet_move([[0]*8], immediately=True, speed=80)
    my_dog.head_move([[0*3]], immediately=True, speed=80)
    my_dog.tail_move([[0]], immediately=True, speed=80)
    while len(my_dog.feet_actions_buffer) > 0:
        sleep(0.01)

def keyboard_control():
    global feet_angles, head_angles, tail_angle
    global feet_offset, head_offset, tail_offset
    global mode, servo_num
    inc = 1  # 1 or -1
    get_real_values()
    show_info()
    my_dog.feet_move([feet_angles], True, 80)
    my_dog.head_move([head_angles], True, 80)
    my_dog.tail_move([tail_angle], True, 80)
    
    while True:
        # readkey
        key = readchar.readkey()
        key = key.lower()
        # enter/quit calibrate mode
        if key == 'r':
            if mode == 'move':
                mode = 'calibrate'
                reset()
            else:
                mode = 'move'
                reset()
            get_real_values()
            show_info() 
            sleep(0.05)
        # select the servo
        elif key in ('1234567890-='):     
            servo_num = key
            show_info()
        # move
        elif key in 'ws':
            # set increment
            if key == 'w':
                inc = 1
            elif key == 's':
                inc = -1
            # control feet 
            if servo_num in ('12345678'):
                index = int(servo_num)-1
                
                # move
                if mode == 'move':    
                    feet_angles[index] += inc*MOVE_STEP
                    if feet_angles[index] > 90:
                        feet_angles[index] = 90
                    elif feet_angles[index] < -90:
                        feet_angles[index] = -90
                # offset
                elif mode == 'calibrate':
                    feet_angles[index] += inc*OFFSET_STEP
                    feet_offset[index] = feet_angles[index] + my_dog.feet.offset[index]
                    if feet_offset[index] > 20:
                        feet_offset[index] = 20
                        feet_angles[index] = 20 - my_dog.feet.offset[index]
                    elif feet_offset[index] < -20:
                        feet_offset[index] = -20
                        feet_angles[index] = -20 - my_dog.feet.offset[index]
                my_dog.feet_simple_move(feet_angles)  
            # control head 
            elif servo_num in ('90-'):
                if servo_num == '9':
                    index = 0
                elif servo_num == '0':
                    index = 1
                elif servo_num == '-':
                    index = 2  
                # move             
                if mode == 'move':
                    head_angles[index] += inc*MOVE_STEP
                    if head_angles[index] > 35:
                        head_angles[index] = 35
                    elif head_angles[index] < -60:
                        head_angles[index] = -60         
                # offset
                elif mode == 'calibrate': 
                    head_angles[index] += inc*OFFSET_STEP
                    head_offset[index] = my_dog.head.offset[index] + head_angles[index]
                    if head_offset[index] > 20:
                        head_offset[index] = 20
                        head_angles[index] = 20 - my_dog.head.offset[index]
                    elif head_offset[index] < -20:
                        head_offset[index] = -20  
                        head_angles[index] = -20 - my_dog.head.offset[index]
                my_dog.head_move_raw([head_angles], True, 80)  
            # control tail
            elif servo_num == '=':
                # move
                if mode == 'move':
                    tail_angle[0] += inc*MOVE_STEP
                    if tail_angle[0] > 90:
                        tail_angle[0] = 90
                    elif tail_angle[0] < -90:
                        tail_angle[0] = -90       
                # offset 
                elif mode == 'calibrate': 
                    tail_angle[0] += inc*OFFSET_STEP
                    tail_offset[0] = my_dog.tail.offset[0] + tail_angle[0]
                    if tail_offset[0] > 20:
                        tail_offset[0] = 20
                        tail_angle[0] = 20 - my_dog.tail.offset[0]
                    elif tail_offset[0] < -20:
                        tail_offset[0] = -20  
                        tail_angle[0] = - 20 - my_dog.tail.offset[0]
                my_dog.tail_move([tail_angle], True, 80)  
            # show_info
            show_info()    
        # calibrate
        elif key == readchar.key.SPACE:
            if mode == 'calibrate':
                print('Confirm save ?(y/n)')
                while True:
                    key = readchar.readkey()
                    key = key.lower()
                    if key == 'y':
                        my_dog.feet_offset(feet_offset)
                        my_dog.head_offset(head_offset)
                        my_dog.tail_offset(tail_offset)
                        sleep(0.5)
                        get_real_values()
                        show_info()  
                        print('offset saved') 
                        break
                    elif key == 'n':
                        show_info()
                        break   
                    sleep(0.01)
        # qiut
        elif key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            my_dog.close()

        sleep(0.01)


if __name__ == "__main__":

    keyboard_control()



