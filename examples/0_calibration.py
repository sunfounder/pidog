#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
import readchar
''' https://github.com/magmax/python-readchar '''

manual = '''
                      ↺{c9}[9]\033[0m
                ↕{c11}[-]\033[0m ┌─┐ ↔{c10}[0]\033[0m
                     │ │
              {c2}[2]\033[0m{c1}[1]\033[0m┌└─┘┐{c3}[3]\033[0m{c4}[4]\033[0m
                    │   │
                    │   │
              {c6}[6]\033[0m{c5}[5]\033[0m└─┬─┘{c7}[7]\033[0m{c8}[8]\033[0m
                     {c12}[=]\033[0m
                      / 
    1 ~ 8 : Leg servos      W: increase angle
    9 : Head yaw ↺          S: decreases angle 
    0 : Head roll ↔          
    - : Head pitch ↕       
    = : Tail                
'''

my_dog = Pidog()

my_dog.legs_move([[0]*8], immediately=True, speed=80)
my_dog.head_move([[0]*3], immediately=True, speed=80)
my_dog.tail_move([[0]], immediately=True, speed=80)
my_dog.wait_all_done()

leg_angles = 0.0
head_angles = 0.0
tail_angle = 0.0
leg_offsets = 0.0
head_offset = 0.0
tail_offset = 0.0
servo_num = '1'

OFFSET_STEP = (180 / 2000) * (20000 / 4095)  # 舵机实际精度
MOVE_STEP = 1


def get_real_values():
    global leg_angles, head_angles, tail_angle
    global leg_offsets, head_offset, tail_offset
    leg_angles = list.copy(my_dog.leg_current_angles)
    head_angles = list.copy(my_dog.head_current_angles)
    tail_angle = list.copy(my_dog.tail_current_angles)
    leg_offsets = list.copy(my_dog.legs.offset)
    head_offset = list.copy(my_dog.head.offset)
    tail_offset = list.copy(my_dog.tail.offset)


def show_info():
    selected_servo_colors = {
        "c1": '\033[97m',
        "c2": '\033[97m',
        "c3": '\033[97m',
        "c4": '\033[97m',
        "c5": '\033[97m',
        "c6": '\033[97m',
        "c7": '\033[97m',
        "c8": '\033[97m',
        "c9": '\033[97m',
        "c10": '\033[97m',
        "c11": '\033[97m',
        "c12": '\033[97m',
    }
    if servo_num in "123456789":
        cnum = int(servo_num)
    elif servo_num == "0":
        cnum = 10
    elif servo_num == "-":
        cnum = 11
    elif servo_num == "=":
        cnum = 12
    selected_servo_colors[f"c{cnum}"] = '\033[1m\033[104m'
    print("\033[H\033[J", end='')  # clear terminal windows
    print(
        "\033[104m\033[1m                         Calibration                         \033[0m")
    print("\033[90m  Press coresponding key to select servo,\n  [W] and [S] to adjust the servo\033[0m")
    print(manual.format(**selected_servo_colors))
    print(
        f"\033[100m\033[1m   Ctrl+C: Quit    Space: Save                               \033[0m")
    print('Current Servo: %s' % servo_num)
    print('leg_offsets: [{c1}{0}\033[0m, {c2}{1}\033[0m, {c3}{2}\033[0m, {c4}{3}\033[0m, {c5}{4}\033[0m, {c6}{5}\033[0m, {c7}{6}\033[0m, {c8}{7}\033[0m]'.format(
        *[round(val, 2)for val in leg_offsets], **selected_servo_colors))
    print('head_offset: [{c9}{0}\033[0m, {c10}{1}\033[0m, {c11}{2}\033[0m]'.format(
        *[round(val, 2)for val in head_offset], **selected_servo_colors))
    print('tail_offset: [{c12}{0}\033[0m]'.format(
        round(tail_offset[0], 2), **selected_servo_colors))


def keyboard_control():
    global leg_angles, head_angles, tail_angle
    global leg_offsets, head_offset, tail_offset
    global servo_num
    inc = 1  # 1 or -1
    get_real_values()
    show_info()
    my_dog.legs_move([leg_angles], True, 80)
    my_dog.head_move_raw([head_angles], True, 80)
    my_dog.tail_move([tail_angle], True, 80)

    while True:
        # readkey
        key = readchar.readkey()
        key = key.lower()

        # select the servo
        if key in ('1234567890-='):
            servo_num = key
            show_info()
        # move
        elif key in 'ws':
            # set increment
            if key == 'w':
                inc = 1
            elif key == 's':
                inc = -1
            # control legs
            if servo_num in ('12345678'):
                index = int(servo_num)-1

                leg_angles[index] += inc*OFFSET_STEP
                leg_offsets[index] = leg_angles[index] + \
                    my_dog.legs.offset[index]
                if leg_offsets[index] > 20:
                    leg_offsets[index] = 20
                    leg_angles[index] = 20 - my_dog.legs.offset[index]
                elif leg_offsets[index] < -20:
                    leg_offsets[index] = -20
                    leg_angles[index] = -20 - my_dog.legs.offset[index]
                my_dog.legs_simple_move(leg_angles)
            # control head
            elif servo_num in ('90-'):
                if servo_num == '9':
                    index = 0
                elif servo_num == '0':
                    index = 1
                elif servo_num == '-':
                    index = 2
                head_angles[index] += inc*OFFSET_STEP
                head_offset[index] = my_dog.head.offset[index] + \
                    head_angles[index]
                if head_offset[index] > 20:
                    head_offset[index] = 20
                    head_angles[index] = 20 - my_dog.head.offset[index]
                elif head_offset[index] < -20:
                    head_offset[index] = -20
                    head_angles[index] = -20 - my_dog.head.offset[index]
                my_dog.head_move_raw([head_angles], True, 80)
            # control tail
            elif servo_num == '=':
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
            print('Confirm save ?(y/n)')
            while True:
                key = readchar.readkey()
                key = key.lower()
                if key == 'y':
                    my_dog.leg_offsets(leg_offsets)
                    my_dog.head_offset(head_offset)
                    my_dog.tail_offset(tail_offset)
                    sleep(0.5)
                    get_real_values()
                    show_info()
                    print('Offset saved')
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
