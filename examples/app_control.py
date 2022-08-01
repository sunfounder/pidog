from sunfounder_controller import SunFounderController
from pidog import Pidog
from time import sleep
from vilib import Vilib
from preset_actions import *
import os
from time import sleep
from math import pi, atan2, sqrt

my_dog = Pidog(feet_pins=[1, 2, 9, 10, 3, 4, 11, 12],
    head_pins=[7, 5, 6],
    tail_pin=[8]
)

sleep(0.1)
head_yrp = [0, 0, 0]
command = None

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def set_head(roll=None, pitch=None, yaw=None):
    global head_yrp
    if roll is not None:
        head_yrp[1] = roll
    if pitch is not None:
        head_yrp[2] = pitch
    if yaw is not None:
        head_yrp[0] = yaw
    my_dog.head_move([head_yrp], immediately=True, speed=100)

# IP address
def getIP():
    wlan0 = os.popen("ifconfig wlan0 |awk '/inet/'|awk 'NR==1 {print $2}'").readline().strip('\n')
    eth0 = os.popen("ifconfig eth0 |awk '/inet/'|awk 'NR==1 {print $2}'").readline().strip('\n')

    if wlan0 == '':
        wlan0 = None
    if eth0 == '':
        eth0 = None

    return wlan0,eth0


def run_command():
    global command
    if not my_dog.is_feet_done() or not my_dog.is_head_done():
        return
    print("Run command: ", command)
    if command == "forward":
        my_dog.do_action('forward', wait=False, speed=98)
    elif command == "backward":
        my_dog.do_action('backward', wait=False, speed=98)
    elif command == "turn left":
        my_dog.do_action('turn_left', wait=False, speed=98)
    elif command == "turn right":
        my_dog.do_action('turn_right', wait=False, speed=98)
    elif command == "trot":
        my_dog.do_action('trot', wait=False, speed=98)
    elif command == "stop":
        command = None
    elif command == "lie down":
        set_head(pitch=0)
        my_dog.do_action('lie', wait=False, speed=70)
        command = None
    elif command == "stand up":
        set_head(pitch=0)
        my_dog.do_action('stand', wait=False, speed=70)
        command = None
    elif command == "sit":
        set_head(pitch=-40)
        my_dog.do_action('sit', wait=False, speed=70)
        command = None
    elif command in ["bark", "park", "fuck"]:
        my_dog.speak('single_bark_001')
        bark(my_dog, head_yrp)
        command = None
    elif command in ["bark harder", "park harder", "fuck harder", "bark harbor", "park harbor", "fuck harbor"]:
        bark_action(my_dog, head_yrp)
        command = None
    elif command in ["pant", "paint"]:
        pant(my_dog, head_yrp)
        command = None
    elif command in ["wag tail", "wake tail", "wake town", "wait town", "wait tail", "wake time", "wait time", "wait tail"]:
        my_dog.do_action('wag_tail', wait=True, speed=100)
    elif command == "shake head":
        shake_head(my_dog)
        command = None
    elif command == "stretch":
        my_dog.do_action('stretch', wait=True, speed=80)
        command = None
    elif command in ["doze off", "does off"]:
        set_head(pitch=-30)
        my_dog.do_action('doze_off', wait=True, speed=95)
    elif command == "push-up":
        pushup(my_dog)
    elif command == "howling":
        howling(my_dog)
        command = None
    elif command == "twist body":
        body_twisting(my_dog)
        command = "lie down"

def main():
    global command
    sc = SunFounderController()
    sc.set_name('Mydog')
    sc.set_type('Pidog')
    sc.start()

    wlan0,eth0 = getIP()
    if wlan0 != None:
        ip = wlan0
    else:
        ip = eth0
    print('ip : %s'%ip)
    sc.set('video','http://'+ip+':9000/mjpg')

    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=False, web=True)
    
    print("Voice Command: ")
    print("  forward")
    print("  backward")
    print("  turn left")
    print("  turn right")
    print("  trot")
    print("  lie down")
    print("  stand up")
    print("  sit")
    print("  bark")
    print("  bark harder")
    print("  pant")
    print("  wag tail")
    print("  shake head")
    print("  stretch")
    print("  doze off")
    print("  push-up")
    print("  howling")
    print("  twist body")

    while True:
        sc.set("B", my_dog.distance.value)
        # print("Receive: ", sc.getall())

        # Left Joystick move
        k_value = sc.get('K')
        if k_value != None:
            kx, ky = k_value
            # calculate angle and radius
            if kx != 0 or ky != 0:
                ka = atan2(ky, kx) * 180 / pi
                kr = sqrt(kx**2 + ky**2)
                if kr > 100:
                    print('kx,ky,ka,kr: ', kx, ky, ka, kr)
                    if (ka > 45 and ka < 135):
                        command = "forward"
                    elif (ka > 135 or ka < -135):
                        command = "turn left"
                    elif (ka > -45 and ka < 45):
                        command = "turn right"
                    elif (ka > -135 and ka < -45):
                        command = "backward"

        # Right Joystick move head
        q_value = sc.get('Q')
        if q_value != None:
            qx, qy = q_value
            if qx != 0 or qy != 0:
                yaw = map(qx, -100, 100, -90, 90)
                pitch = map(qy, -100, 100, -30, 30)
                set_head(yaw=yaw, pitch=pitch)

        d_value = sc.get('D')
        if d_value != None:
            set_head(roll=d_value)

        # Voice Control
        voice_command = sc.get('J')
        if voice_command != None:
            command = voice_command

        A_val = sc.get('A')
        if A_val != None:
            print("A_val:",A_val)

        run_command()
        sleep(0.008)

 
if __name__ == "__main__":
    main()