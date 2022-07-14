#!/usr/bin/env python3
from pidog import Pidog
from time import sleep

my_dog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
            head_pins=[9,10,11],tail_pin=[12],
            # feet_init_angles=[45,0,-45,0,45,0,-45,0]
            )
sleep(0.1)


def delay(time):
    while len(my_dog.feet_actions_buffer) > 0 :
        sleep(0.1)
    sleep(time)


def fly():  
    my_dog.rgb_strip.set_mode('boom',font_color='red',delay=0.01) 
    # my_dog.feet_move([[45,-45,90,-80,90,90,-90,-90]],immediately=True,speed=100)
    my_dog.feet.servo_move([45,-45,90,-80,90,90,-90,-90],speed=100)
    my_dog.speak('wuhu') 
    delay(0.1)

def stand():
    my_dog.rgb_strip.set_mode('breath',font_color='green',delay=0.02)
    # my_dog.feet_move([[20,40,-20,-40,20,40,-20,-40]],immediately=True,speed=100)
    my_dog.feet.servo_move([20,40,-20,-40,20,40,-20,-40],speed=100)
    delay(0.1)

def be_picked_up():
    isUp = False
    upflag = False
    downflag = False

    my_dog.rgb_strip.set_mode('breath',font_color='green',delay=0.02)
    stand()
    # mpu_calibrate()

    while True:
        ax = my_dog.accData[0]
        print('ax: %s,isUp: %s'%(ax,isUp))
        
        # gravity : 1G = 16384 
        if ax < -17000:
            if upflag == False:
                upflag =True
            if downflag == True:
                isUp = False            
                downflag = False
                stand()
                                          
        if ax > -15000:
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
