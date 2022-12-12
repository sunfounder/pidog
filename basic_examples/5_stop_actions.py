# !/usr/bin/env python3
''' stop all actions

    
API:
    Pidog.wait_all_done()
        wait for all the actions in the leg actions buffer, head buffer and tail buffer to be executed

    Pidog.body_stop()
        stop all the actions of legs, head and tail

    Pidog.stop_and_lie()
        stop all the actions of legs, head and tail, then reset to "lie" pose

    Pidog.close()
        stop all the actions, reset to "lie" pose, and  close all the threads,
        usually used when exiting a program

'''

from pidog import Pidog
import time

my_dog = Pidog()

try:
    # pushup prepare
    pushup_prepare_action = [
        [45, 35, -45, -35, 80, 70, -80, -70]
    ]
    my_dog.legs_move(pushup_prepare_action, speed=30)
    my_dog.head_move([[0, 0, 0]], pitch_comp=-10, speed=80) # head level
    my_dog.wait_all_done() # wait all the actions to be done
    time.sleep(0.5)

    # pushup 
    pushup_action = [
        [90, -30, -90, 30, 80, 70, -80, -70],
        [45, 35, -45, -35, 80, 70, -80, -70],       
    ]
    head_up_down_action = [
        [0, 0, -30],
        [0, 0, 20],
    ]
    # fill action buffers
    for _ in range(20):
        my_dog.legs_move(pushup_action, immediately=False, speed=50)
        my_dog.head_move(head_up_down_action, pitch_comp=-10, immediately=False, speed=50)
    print(f"legs buffer length (start): {len(my_dog.legs_action_buffer)}")
    time.sleep(5)
    print(f"legs buffer length (5s): {len(my_dog.legs_action_buffer)}")
    
    my_dog.body_stop()
    print(f"legs buffer length (stop): {len(my_dog.legs_action_buffer)}")
    time.sleep(1)

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"\033[31mERROR: {e}\033[m")
finally:
    print("closing ...")
    my_dog.close()

