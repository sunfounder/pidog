#!/usr/bin/env python3
from time import sleep
from pidog import Pidog
import threading

my_dog = Pidog(feet_pins=[1, 2, 3, 4, 5, 6, 7, 8], 
                head_pins=[9, 10, 11], 
                tail_pin=[12], 
                )
sleep(0.5) 

actions = [
    # name, head_pitch_adjust, speed
    ['stand', 0, 20],
    ['sit', -30, 20],
    ['lie', 0, 20],
    ['lie_with_hands_out', 0,  20],
    ['trot', 0, 98],
    ['forward', 0, 98],
    ['backward', 0, 98],
    ['turn_left', 0, 98],
    ['turn_right', 0, 98],
    ['doze_off', -30, 40],
    ['stretch', 30, 20],
    ['pushup', -30, 50],
    ['shake_head', 0, 60],
    ['tilting_head', 0, 40],
    ['tail_wagging', 0, 100],
]

index = None
exit_flag = False

def show_info():
    print("\033[H\033[J",end='')  # clear terminal windows
    for i, action in enumerate(actions):
        print('   %s. %s'%(i+1, action[0]))
    print('   ESC: Quit \n')
    if index != None:
        print('%s : %s'%(index+1, actions[index]))

def work():
    global index
    global exit_flag
    temp = None

    while True:
        if not isinstance(index, int):
            sleep(0.2)
            continue        
        if index != temp:
            name, head_pitch_adjust, speed = actions[index]
            my_dog.body_stop()  
            if temp != None and actions[temp][0] in ('pushup'):
                my_dog.do_action('lie', wait=False, speed=90)          
            my_dog.head_move([[0, 0, head_pitch_adjust]], immediately=True ,speed=60)
            temp = index 
        my_dog.do_action(name, wait=False, speed=speed)

        if exit_flag == True:
            break
        sleep(0.1)


def action_demonstration():
    global index
    global exit_flag
    
    show_info()

    work_t = threading.Thread(target=work)
    work_t.setDaemon(True)
    work_t.start()

    while True:
        try:
            x = input()
            if int(x) > len(actions):
                print('out of range')
                continue
            index = int(x) - 1
            show_info()
        except ValueError:
            print('ValueError')
        except KeyboardInterrupt:
            exit_flag = True
            while work_t.is_alive():
                sleep(0.1)

            my_dog.close()
        
        sleep(0.05)

if __name__ == "__main__":
    action_demonstration()



