#!/usr/bin/env python3
from time import sleep
from pidog import Pidog
from pidog.walk import Walk
import readchar
import threading
import os

my_dog = Pidog()

sleep(0.5)

usage = '''
\033[104m\033[1m  Pidog          Balance         Ctrl + C to Exit  \033[0m
    ┌────────┐┌────────┐┌────────┐┌────────┐
    │Q       ││W       ││E       ││R       │
    │        ││        ││        ││        │
    │        ││ Forward││  Stand ││   UP   │
    └────────┘└────────┘└────────┘└────────┘
       ┌────────┐┌────────┐┌────────┐┌────────┐
       │A       ││S       ││D       ││F       │
       │  Turn  ││        ││  Turn  ││        │
       │  Left  ││Backward││  Right ││  DOWN  │
       └────────┘└────────┘└────────┘└────────┘
'''

stand_coords = [[[-15, 95], [-15, 95], [5, 90], [5, 90]]]
forward_coords = Walk(fb=Walk.FORWARD, lr=Walk.STRAIGHT).get_coords()
backward_coords = Walk(fb=Walk.BACKWARD, lr=Walk.STRAIGHT).get_coords()
turn_left_coords = Walk(fb=Walk.FORWARD, lr=Walk.LEFT).get_coords()
turn_right_coords = Walk(fb=Walk.FORWARD, lr=Walk.RIGHT).get_coords()

current_coords = stand_coords
current_pose = {'x': 0, 'y': 0, 'z': 80}
current_rpy = {'roll': 0, 'pitch': 0, 'yaw': 0}
thread_start = True


def move_thread():
    while thread_start:
        for coord in current_coords:
            # print(coord)
            my_dog.set_rpy(**current_rpy, pid=True)
            my_dog.set_pose(**current_pose)
            my_dog.set_legs(coord)
            angles = my_dog.pose2legs_angle()
            my_dog.legs.servo_move(angles, speed=98)


t = threading.Thread(target=move_thread)


def main():
    global current_coords, current_pose, current_rpy, thread_start
    my_dog.do_action('stand', speed=80)
    my_dog.wait_legs_done()
    # sleep(1)
    t.start()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(usage)
        key = readchar.readkey()
        if key == readchar.key.CTRL_C:
            thread_start = False
            break
        elif key == 'w':
            current_coords = forward_coords
        elif key == 's':
            current_coords = backward_coords
        elif key == 'a':
            current_coords = turn_left_coords
        elif key == 'd':
            current_coords = turn_right_coords
        elif key == 'e':
            current_coords = stand_coords
        elif key == 'r':
            current_pose['z'] += 1
            if current_pose['z'] > 90:
                current_pose['z'] = 90
        elif key == 'f':
            current_pose['z'] -= 1
            if current_pose['z'] < 30:
                current_pose['z'] = 30


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        thread_start = False
        t.join()
        my_dog.close()
