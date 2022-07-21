#!/usr/bin/env python3
from time import sleep
from pidog import Pidog
import readchar 

my_dog = Pidog(feet_pins=[1, 2, 3, 4, 5, 6, 7, 8], 
                head_pins=[9, 10, 11], 
                tail_pin=[12], 
                )
sleep(0.5) 

def main():
    print("[W] Forward")
    print("[S] Backward")
    print("[A] Turn Left")
    print("[D] Turn Right")
    my_dog.do_action('stand', wait=True, speed=60)
    while True:
        key = readchar.readchar().lower()
        if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            import sys
            print('')
            # sys.exit(0)
            break
        elif key == 'w':
            my_dog.do_action('forward', wait=True, speed=98)
        elif key == 's':
            my_dog.do_action('backward', wait=True, speed=98)
        elif key == 'a':
            my_dog.do_action('turn_left', wait=True, speed=98)
        elif key == 'd':
            my_dog.do_action('turn_right', wait=True, speed=98)
        else:
            print('key:',key)
            continue
        sleep(0.001)  
    



if __name__ == "__main__":
    try:
        main()
    finally:
        my_dog.close()