#!/usr/bin/env python3
from time import sleep
from pidog import Pidog
import readchar
from preset_actions import *
import os

my_dog = Pidog()

sleep(0.5)

usage = '''
\033[104m\033[1m  Pidog                                  Keyboard Control                             Ctrl + C to Exit  \033[0m
┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
│1       ││2       ││3       ││4       ││5       ││6       ││7       ││8       ││9       ││0       │
│  Doze  ││  Push  ││        ││  Body  ││        ││        ││        ││        ││        ││        │
│   Off  ││   Up   ││ Howling││  Twist ││        ││        ││        ││        ││        ││        │
└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
    ┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
    │Q       ││W       ││E       ││R       ││T       ││Y       ││U       ││I       ││O       ││P       │
    │        ││        ││        ││   Wag  ││        ││        ││  Head  ││  Head  ││  Head  ││        │
    │  Bark  ││ Forward││  Pant  ││  Tail  ││        ││        ││  Roll  ││  Pitch ││  Roll  ││        │
    └────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
       ┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
       │A       ││S       ││D       ││F       ││G       ││H       ││J       ││K       ││L       │
       │  Turn  ││        ││  Turn  ││  Shake ││        ││        ││  Head  ││  Head  ││  Head  │
       │  Left  ││Backward││  Right ││  Head  ││        ││        ││   Yaw  ││  Pitch ││   Yaw  │
       └────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
          ┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
          │Z       ││X       ││C       ││V       ││B       ││N       ││M       │
          │        ││        ││        ││        ││        ││        ││  Head  │
          │   Lie  ││  Stand ││   Sit  ││ Stretch││        ││        ││  Reset │
          └────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
'''

head_yrp = [0, 0, 0]
head_angle = 20
head_speed = 80

def set_head(roll=None, pitch=None, yaw=None):
    global head_yrp
    if roll is not None:
        head_yrp[1] = roll
    if pitch is not None:
        head_yrp[2] = pitch
    if yaw is not None:
        head_yrp[0] = yaw
    my_dog.head_move([head_yrp], immediately=True, speed=head_speed)

def main():
    global head_yrp
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        print(usage)
        print("\033[?25l") # Hide terminal cursor
        key = readchar.readchar()
        if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            import sys
            print('')
            # sys.exit(0)
            break
        elif key == 'W':
            set_head(pitch=0)
            my_dog.do_action('trot', wait=True, speed=98)
        elif key == 'w':
            set_head(pitch=0)
            my_dog.do_action('forward', wait=True, speed=98)
        elif key == 's':
            set_head(pitch=0)
            my_dog.do_action('backward', wait=True, speed=98)
        elif key == 'a':
            set_head(pitch=0)
            my_dog.do_action('turn_left', wait=True, speed=98)
        elif key == 'd':
            set_head(pitch=0)
            my_dog.do_action('turn_right', wait=True, speed=98)
        elif key == 'z':
            set_head(pitch=0)
            my_dog.do_action('lie', wait=True, speed=70)
        elif key == 'x':
            set_head(pitch=0)
            my_dog.do_action('stand', wait=True, speed=70)
        elif key == 'c':
            set_head(pitch=-40)
            my_dog.do_action('sit', wait=True, speed=70)
        elif key == 'q':
            my_dog.speak('single_bark_1')
            bark(my_dog, head_yrp)
        elif key == 'Q':
            bark_action(my_dog, head_yrp)
        elif key == 'e':
            pant(my_dog, head_yrp)
        elif key == 'r':
            my_dog.do_action('wag_tail', wait=True, speed=100)
        elif key == 'f':
            shake_head(my_dog)
        elif key == 'v':
            my_dog.do_action('stretch', wait=True, speed=80)
        elif key == '1':
            set_head(pitch=-30)
            my_dog.do_action('doze_off', wait=True, speed=95)
        elif key == '2':
            pushup(my_dog)
        elif key == '3':
            howling(my_dog)
        elif key == '4':
            body_twisting(my_dog)
        # Head Pitch
        elif key in 'uiojklUIOJKLm':
            if key == 'i':
                head_yrp[2] = head_angle
            elif key == 'I':
                head_yrp[2] = head_angle * 2
            elif key == 'k':
                head_yrp[2] = -head_angle
            elif key == 'K':
                head_yrp[2] = -head_angle * 2
            # Head Yaw
            elif key == 'j':
                head_yrp[0] = head_angle
            elif key == 'J':
                head_yrp[0] = head_angle * 2
            elif key == 'l':
                head_yrp[0] = -head_angle
            elif key == 'L':
                head_yrp[0] = -head_angle * 2
            # Head Roll
            elif key == 'u':
                head_yrp[1] = -head_angle
            elif key == 'U':
                head_yrp[1] = -head_angle * 2
            elif key == 'o':
                head_yrp[1] = head_angle
            elif key == 'O':
                head_yrp[1] = head_angle * 2
            # Head Reset
            elif key == 'm':
                head_yrp = [0, 0, 0]
            my_dog.head_move([head_yrp], immediately=True, speed=head_speed)
        else:
            print('key:',key)
            continue
        # sleep(0.001)

if __name__ == "__main__":
    # try:
    # except Exception as e:
        # raise e
    # finally:
    main()
    print("\033[?25h") # Show terminal cursor
    my_dog.close()