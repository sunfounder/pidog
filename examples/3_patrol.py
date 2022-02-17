#!/usr/bin/env python3
import time
from pidog import Pidog
from time import sleep


t = time.time()
my_dog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
                head_pins=[9,10,11],
                tail_pin=[12],
                feet_init_angles=[45,0,-45,0,45,0,-45,0]
                )
sleep(0.1) 
print(1, time.time() -t)
t = time.time()
def delay_s(time):
    while (len(my_dog.feet_actions_buffer) > 0 or len(my_dog.head_actions_buffer) > 0) :
        sleep(0.01)
    sleep(time)

# t = time.time()
stand = my_dog.feet_angle_calculation([[0,110],[0,110],[30,95],[30,95]])


def look_far():
    my_dog.head_move([[0,0,-15]], speed=80)
    my_dog.tail_move([[0]], speed=80)
    my_dog.feet_move([stand], speed=80)

def bark():
    h1 = [0,0,15]
    h2 = [0,0,-15]
    h3 = [h2]*1 + [h1] + [h2]
    h = h3*3 

    my_dog.speak('angry', 'wav')
    for _ in range(3):
        # delay_s(0.1)
        my_dog.head_move([h1], immediately=True, speed=90) 
        delay_s(0.05)
        my_dog.head_move([h2], immediately=True, speed=90) 
        delay_s(0.01)


def patrol():
    my_dog.rgb_strip.set_mode('breath', 'pink', delay=0.1)
    my_dog.do_action('trot', step_count=4, wait=False, speed=90)
    print(time.time() -t)
    my_dog.do_action('shake_head', step_count=2, wait=False, speed=50)
    my_dog.do_action('tail_wagging', step_count=10, wait=False, speed=99)
    while len(my_dog.feet_actions_buffer) > 0:
        sleep(0.05)
    my_dog.body_stop()
    my_dog.rgb_strip.set_mode('boom', 'red', delay=0.01)
    sleep(0.25)
    look_far()
    delay_s(0.8)
    bark()
    delay_s(0.8)
    my_dog.rgb_strip.set_mode('breath', 'red', delay=0.1)

if __name__ == "__main__":
    try:  
        patrol()
        # Keep the main thread active for process termination processing
        while True:       
            sleep(1)
    except KeyboardInterrupt:
        my_dog.close()



