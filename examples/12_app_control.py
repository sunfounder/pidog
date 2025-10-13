from zoneinfo import available_timezones
from sunfounder_controller import SunFounderController
from pidog import Pidog
from time import sleep
from vilib import Vilib
from preset_actions import *
import os
from time import sleep
from math import pi, atan2, sqrt

sc = SunFounderController()
my_dog = Pidog()

SIT_HEAD_PITCH = -40
STAND_HEAD_PITCH = 0
STATUS_STAND = 0
STATUS_SIT = 1
STATUS_LIE = 2

sleep(0.1)
head_yrp = [0, 0, 0]
head_origin_yrp = [0, 0, 0]
head_pitch_init = 0
command = None
current_status = STATUS_LIE


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
    my_dog.head_move([head_yrp], pitch_comp=head_pitch_init,
                     immediately=True, speed=100)

# IP address


def getIP():
    wlan0 = os.popen(
        "ifconfig wlan0 |awk '/inet/'|awk 'NR==1 {print $2}'").readline().strip('\n')
    eth0 = os.popen(
        "ifconfig eth0 |awk '/inet/'|awk 'NR==1 {print $2}'").readline().strip('\n')

    if wlan0 == '':
        wlan0 = None
    if eth0 == '':
        eth0 = None

    return wlan0, eth0


def stretch():
    my_dog.do_action('stretch', speed=10)
    my_dog.wait_all_done()
    # sleep(1)


COMMANDS = {
    "forward": {
        "commands": ["forward"],
        "function": lambda: my_dog.do_action('forward', speed=98),
        "after": "forward",
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "backward": {
        "commands": ["backward"],
        "function": lambda: my_dog.do_action('backward', speed=98),
        "after": "backward",
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "turn left": {
        "commands": ["turn left"],
        "function": lambda: my_dog.do_action('turn_left', speed=98),
        "after": "turn left",
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "turn right": {
        "commands": ["turn right"],
        "function": lambda: my_dog.do_action('turn_right', speed=98),
        "after": "turn right",
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "trot": {
        "commands": ["trot", "run"],
        "function": lambda: my_dog.do_action('trot', speed=98),
        "after": "trot",
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "stop": {
        "commands": ["stop"],
    },
    "lie down": {
        "commands": ["lie down"],
        "function": lambda: my_dog.do_action('lie', speed=70),
        "head_pitch": STAND_HEAD_PITCH,
        "status": STATUS_LIE,
    },
    "stand up": {
        "commands": ["stand up"],
        "function": lambda: my_dog.do_action('stand', speed=70),
        "head_pitch": STAND_HEAD_PITCH,
        "status": STATUS_STAND,
    },
    "sit": {
        "commands": ["sit", "sit down", "set", "set down"],
        "function": lambda: my_dog.do_action('sit', speed=70),
        "head_pitch": SIT_HEAD_PITCH,
        "status": STATUS_SIT,
    },
    "bark": {
        "commands": ["bark", "park"],
        "function": lambda: bark(my_dog, head_yrp, pitch_comp=head_pitch_init),
    },
    "bark harder": {
        "commands": ["bark harder", "park harder", "bark harbor", "park harbor"],
        "function": lambda: bark_action(my_dog, head_yrp, 'single_bark_1'),
    },
    "pant": {
        "commands": ["pant", "paint"],
        "function": lambda: pant(my_dog, head_yrp, pitch_comp=head_pitch_init),
    },
    "wag tail": {
        "commands": ["wag tail", "wake tail", "wake town", "wait town", "wait tail", "wake time", "wait time", "wait tail"],
        "function": lambda: my_dog.do_action('wag_tail', speed=100),
        "after": "wag tail",
    },
    "shake head": {
        "commands": ["shake head"],
        "function": lambda: shake_head(my_dog, head_yrp),
    },
    "stretch": {
        "commands": ["stretch"],
        "function": lambda: stretch(),
        "after": "stand up",
        "status": STATUS_STAND,
    },
    "doze off": {
        "commands": ["doze off", "does off"],
        "function": lambda: my_dog.do_action('doze_off', speed=95),
        "after": "doze off",
        "status": STATUS_LIE,
    },
    "push-up": {
        "commands": ["push up", "push-up"],
        "function": lambda: push_up(my_dog),
        "after": "push-up",
        "status": STATUS_STAND,
    },
    "howling": {
        "commands": ["howling"],
        "function": lambda: howling(my_dog),
        "after": "sit",
        "status": STATUS_SIT,
    },
    "twist body": {
        "commands": ["twist body", "taste body", "twist party", "taste party"],
        "function": lambda: body_twisting(my_dog),
        "before": "stretch",
        "after": "sit",
        "status": STATUS_STAND,
    },
    "scratch": {
        "commands": ["scratch"],
        "function": lambda: scratch(my_dog),
        "after": "sit",
        "head_pitch": SIT_HEAD_PITCH,
        "status": STATUS_SIT,
    },
    "handshake": {
        "commands": ["handshake"],
        "function": lambda: hand_shake(my_dog),
        "after": "sit",
        "head_pitch": SIT_HEAD_PITCH,
        "status": STATUS_SIT,
    },
    "high five": {
        "commands": ["high five", "hi five"],
        "function": lambda: high_five(my_dog),
        "after": "sit",
        "head_pitch": SIT_HEAD_PITCH,
        "status": STATUS_SIT,
    },
}

AVAILABLE_COMMANDS = []
for command_name in COMMANDS:
    AVAILABLE_COMMANDS.extend(COMMANDS[command_name]["commands"])

def set_head_pitch_init(pitch):
    global head_pitch_init
    head_pitch_init = pitch
    my_dog.head_move([head_yrp], pitch_comp=pitch, immediately=True, speed=80)


def change_status(status):
    global current_status
    current_status = status
    if status == STATUS_STAND:
        set_head_pitch_init(STAND_HEAD_PITCH)
        my_dog.do_action('stand', speed=70)
    elif status == STATUS_SIT:
        set_head_pitch_init(SIT_HEAD_PITCH)
        my_dog.do_action('sit', speed=70)
    elif status == STATUS_LIE:
        set_head_pitch_init(STAND_HEAD_PITCH)
        my_dog.do_action('lie', speed=70)


def run_command():
    global command, head_pitch_init
    if not my_dog.is_legs_done():
        return
    if command is None:
        return
    print(command)
    for name in COMMANDS:
        if command in COMMANDS[name]["commands"]:
            if "head_pitch" in COMMANDS[name]:
                set_head_pitch_init(COMMANDS[name]["head_pitch"])
            if "status" in COMMANDS[name]:
                if current_status != COMMANDS[name]["status"]:
                    change_status(COMMANDS[name]["status"])
            if "before" in COMMANDS[name]:
                before_command = COMMANDS[name]["before"]
                COMMANDS[before_command]["function"]()
            if "function" in COMMANDS[name]:
                COMMANDS[name]["function"]()
            if "after" in COMMANDS[name]:
                command = COMMANDS[name]["after"]
            else:
                command = None
            break


def main():
    global command
    sc.set_name('Mydog')
    sc.set_type('Pidog')
    sc.start()

    wlan0, eth0 = getIP()
    if wlan0 != None:
        ip = wlan0
    else:
        ip = eth0
    print('ip : %s' % ip)
    sc.set('video', 'http://'+ip+':9000/mjpg')

    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=False, web=True)

    print("Voice Command: ")
    for command_name in AVAILABLE_COMMANDS:
        print(command_name)

    last_kx = 0
    last_ky = 0
    last_qx = 0
    last_qy = 0

    while True:
        # print("Receive: ", sc.getall())

        sc.set("A", round(my_dog.read_distance(),2))

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
            print(f'voice command: {voice_command}')
            if voice_command in AVAILABLE_COMMANDS:
                command = voice_command
            else:
                print("\033[0;31m no this voice command\033[m")

        # Bark
        n_value = sc.get('N')
        if n_value:
            command = 'bark'

        # Wag tail
        O_value = sc.get('O')
        if O_value:
            command = 'wag tail'
        elif command == 'wag tail':
            command = None

        # pant
        P_value = sc.get('P')
        if P_value:
            command = 'pant'

        # Scratch
        I_value = sc.get('I')
        if I_value:
            command = 'scratch'

        # Sit
        E_value = sc.get('E')
        if E_value:
            command = 'sit'

        # Stand
        F_value = sc.get('F')
        if F_value:
            command = 'stand up'

        # Lie
        G_value = sc.get('G')
        if G_value:
            command = 'lie down'

        # Face detection
        C_value = sc.get('C')
        if C_value:
            Vilib.face_detect_switch(True)
        else:
            Vilib.face_detect_switch(False)

        run_command()
        sleep(0.008)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        sc.close()
        Vilib.camera_close()
        my_dog.close()
