from sunfounder_controller import SunFounderController
from pidog import Pidog
from time import sleep
# from vilib import Vilib
from preset_actions import *
import os
from time import sleep
from math import pi, atan2, sqrt

sc = SunFounderController()
my_dog = Pidog(feet_pins=[1, 2, 9, 10, 3, 4, 11, 12],
    head_pins=[7, 5, 6],
    tail_pin=[8]
)

SIT_HEAD_PITCH = -40
STAND_HEAD_PITCH = 0

sleep(0.1)
head_yrp = [0, 0, 0]
head_origin_yrp = [0, 0, 0]
command = None

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def set_head(roll=None, pitch=None, yaw=None):
    global head_yrp
    if roll is not None:
        head_yrp[1] = roll + head_origin_yrp[1]
    if pitch is not None:
        head_yrp[2] = pitch + head_origin_yrp[2]
    if yaw is not None:
        head_yrp[0] = yaw + head_origin_yrp[0]
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

COMMANDS = {
    "forward": {
        "commands": ["forward"],
        "function": lambda: my_dog.do_action('forward', wait=False, speed=98),
        "after": "forward",
        "head_pitch": STAND_HEAD_PITCH,
    },
    "backward": {
        "commands": ["backward"],
        "function": lambda: my_dog.do_action('backward', wait=False, speed=98),
        "after": "backward",
        "head_pitch": STAND_HEAD_PITCH,
    },
    "turn left": {
        "commands": ["turn left"],
        "function": lambda: my_dog.do_action('turn_left', wait=False, speed=98),
        "after": "turn left",
        "head_pitch": STAND_HEAD_PITCH,
    },
    "turn right": {
        "commands": ["turn right"],
        "function": lambda: my_dog.do_action('turn_right', wait=False, speed=98),
        "after": "turn right",
        "head_pitch": STAND_HEAD_PITCH,
    },
    "trot": {
        "commands": ["trot"],
        "function": lambda: my_dog.do_action('trot', wait=False, speed=98),
        "after": "trot",
        "head_pitch": STAND_HEAD_PITCH,
    },
    "stop": {
        "commands": ["stop"],
        "after": None,
    },
    "lie down": {
        "commands": ["lie down"],
        "function": lambda: my_dog.do_action('lie', wait=False, speed=70),
        "after": None,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "stand up": {
        "commands": ["stand up"],
        "function": lambda: my_dog.do_action('stand', wait=False, speed=70),
        "after": None,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "sit": {
        "commands": ["sit", "sit down", "set", "set down"],
        "function": lambda: my_dog.do_action('sit', wait=False, speed=70),
        "after": None,
        "head_pitch": SIT_HEAD_PITCH,
    },
    "bark": {
        "commands": ["bark", "park", "fuck"],
        "function": lambda: bark(my_dog, head_yrp),
        "after": None,
    },
    "bark harder": {
        "commands": ["bark harder", "park harder", "fuck harder", "bark harbor", "park harbor", "fuck harbor"],
        "function": lambda: bark_action(my_dog, head_yrp, 'single_bark_1'),
        "after": None,
    },
    "pant": {
        "commands": ["pant", "paint"],
        "function": lambda: pant(my_dog, head_yrp),
        "after": None,
    },
    "wag tail": {
        "commands": ["wag tail", "wake tail", "wake town", "wait town", "wait tail", "wake time", "wait time", "wait tail"],
        "function": lambda: my_dog.do_action('wag_tail', wait=True, speed=100),
        "after": "wag tail",
    },
    "shake head": {
        "commands": ["shake head"],
        "function": lambda: shake_head(my_dog, head_yrp),
        "after": None,
    },
    "stretch": {
        "commands": ["stretch"],
        "function": lambda: my_dog.do_action('stretch', wait=True, speed=80),
        "after": "sit",
    },
    "doze off": {
        "commands": ["doze off", "does off"],
        "function": lambda: my_dog.do_action('doze_off', wait=True, speed=95),
        "after": "doze off",
    },
    "push-up": {
        "commands": ["push-up"],
        "function": lambda: pushup(my_dog),
        "after": "push-up",
    },
    "howling": {
        "commands": ["howling"],
        "function": lambda: howling(my_dog),
        "after": "sit",
    },
    "twist body": {
        "commands": ["twist body"],
        "function": lambda: body_twisting(my_dog),
        "before": "stretch",
        "after": "sit",
    },
    "scratch": {
        "commands": ["scratch"],
        "function": lambda: scratch(my_dog),
        "before": "sit",
        "after": "sit",
        "head_pitch": SIT_HEAD_PITCH,
    },
    "handshake": {
        "commands": ["handshake"],
        "function": lambda: hand_shake(my_dog),
        "before": "sit",
        "after": "sit",
        "head_pitch": SIT_HEAD_PITCH,
    },
    "high five": {
        "commands": ["high five", "hi five"],
        "function": lambda: high_five(my_dog),
        "before": "sit",
        "after": "sit",
        "head_pitch": SIT_HEAD_PITCH,
    },
}


def run_command():
    global command
    if not my_dog.is_feet_done() or not my_dog.is_head_done():
        return
    if command is None:
        return
    print(command)
    for name in COMMANDS:
        if command in COMMANDS[name]["commands"]:
            if "head_pitch" in COMMANDS[name]:
                print("head_pitch:", COMMANDS[name]["head_pitch"])
                head_origin_yrp[2] = COMMANDS[name]["head_pitch"]
            if "before" in COMMANDS[name]:
                print("Run before command:", COMMANDS[name]["before"])
                before_command = COMMANDS[name]["before"]
                COMMANDS[before_command]["function"]()
            if "function" in COMMANDS[name]:
                print("Run command:", name)
                COMMANDS[name]["function"]()
            if "after" in COMMANDS[name]:
                print("Set after command:", COMMANDS[name]["after"])
                command = COMMANDS[name]["after"]
            break

def main():
    global command
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

    # Vilib.camera_start(vflip=False,hflip=False)
    # Vilib.display(local=False, web=True)
    
    print("Voice Command: ")
    for command_name in COMMANDS:
        print(command_name)

    last_kx = 0
    last_ky = 0
    last_qx = 0
    last_qy = 0

    while True:
        sc.set("B", my_dog.distance.value)
        # print("Receive: ", sc.getall())

        # Left Joystick move
        k_value = sc.get('K')
        if k_value != None:
            kx, ky = k_value
            # calculate angle and radius
            if last_ky != ky or last_kx != kx:
                last_ky = ky
                last_kx = kx
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
                else:
                    command = None

        # Right Joystick move head
        q_value = sc.get('Q')
        if q_value != None:
            qx, qy = q_value
            if last_qx != qx or last_qy != qy:
                last_qx = qx
                last_qy = qy
                if qx != 0 or qy != 0:
                    yaw = map(qx, 100, -100, -90, 90)
                    pitch = map(qy, -100, 100, -30, 30)
                else:
                    yaw = 0
                    pitch = 0
                set_head(yaw=yaw, pitch=pitch)

        d_value = sc.get('D')
        if d_value != None:
            set_head(roll=d_value)

        # Voice Control
        voice_command = sc.get('J')
        if voice_command != None:
            command = voice_command
            print("Voice Command: ", command)

        run_command()
        sleep(0.008)

 
if __name__ == "__main__":
    # try:
        main()
    # except KeyboardInterrupt:
    #     pass
    # finally:
        sc.close()
        # Vilib.camera_close()
        my_dog.close()