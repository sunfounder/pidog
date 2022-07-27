#!/usr/bin/env python3
from pidog import Pidog
from time import sleep

my_dog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
            head_pins=[9,10,11],tail_pin=[12],
            )
sleep(0.1)

def delay(time):
    my_dog.wait_feet_done()
    sleep(time)

def fly():  
    my_dog.rgb_strip.set_mode('boom', front_color='red', delay=0.01) 
    my_dog.feet.servo_move([45,-45,90,-80,90,90,-90,-90], speed=100)
    my_dog.do_action('tail_wagging', step_count=20, speed=100)
    my_dog.speak('woohoo') 
    delay(1)

def stand():
    my_dog.rgb_strip.set_mode('breath', front_color='green', delay=0.02)
    my_dog.do_action('stand', wait=True, speed=60)

def be_picked_up():
    isUp = False
    upflag = False
    downflag = False

    my_dog.rgb_strip.set_mode('breath', front_color='green', delay=0.02)
    stand()

    while True:
        ax = my_dog.accData[0]
        print('ax: %s, is up: %s'%(ax, isUp))
        
        # gravity : 1G = 16384 
        if ax < -16000:
            my_dog.body_stop()
            if upflag == False:
                upflag =True
            if downflag == True:
                isUp = False            
                downflag = False
                stand()
                                          
        if ax > -13000:
            my_dog.body_stop()
            if upflag == True:
                isUp = True
                upflag = False
                fly()
                           
            if downflag == False:
                downflag = True

        sleep(0.2)


if __name__ == "__main__":
    try:
        be_picked_up()
    except KeyboardInterrupt: 
        my_dog.close()
