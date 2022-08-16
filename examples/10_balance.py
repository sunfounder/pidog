#!/usr/bin/env python3
from time import sleep
from pidog import Pidog
from pidog.walk import Walk
import readchar
import threading

my_dog = Pidog()

sleep(0.5)

stand_coords = [[[0, 80], [0, 80], [0, 80], [0, 80]]]
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
            my_dog.set_feet(coord)
            angles = my_dog.pose2feet_angle()
            my_dog.feet.servo_move2(angles, speed=98)

t = threading.Thread(target=move_thread)
def main():
    global current_coords, current_pose, current_rpy, thread_start
    t.start()

    while True:
        key = readchar.readkey()
        if key == 'w':
            current_coords = forward_coords
        elif key == 's':
            current_coords = backward_coords
        elif key == 'a':
            current_coords = turn_left_coords
        elif key == 'd':
            current_coords = turn_right_coords
        elif key == 'q':
            thread_start = False
            break
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
    finally:
        t.join()
        my_dog.close()