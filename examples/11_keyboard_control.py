#!/usr/bin/env python3
from time import sleep
from pidog import Pidog
import readchar
from preset_actions import *
import os

my_dog = Pidog()

sleep(0.5)

usage = '''
\033[104m\033[1m  Pidog                                  Keyboard Control                             Ctrl + C to Exit  \033[0m
┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
│1       ││2       ││3       ││4       ││5       ││6       ││7       ││8       ││9       ││0       │
│  Doze  ││  Push  ││        ││  Body  ││        ││        ││        ││        ││        ││        │
│   Off  ││   Up   ││ Howling││  Twist ││ Scratch││        ││        ││        ││        ││        │
└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
    ┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
    │Q       ││W       ││E       ││R       ││T       ││Y       ││U       ││I       ││O       ││P       │
    │        ││        ││        ││   Wag  ││  Hand  ││        ││  Head  ││  Head  ││  Head  ││        │
    │  Bark  ││ Forward││  Pant  ││  Tail  ││  Shake ││        ││  Roll  ││  Pitch ││  Roll  ││        │
    └────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
       ┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
       │A       ││S       ││D       ││F       ││G       ││H       ││J       ││K       ││L       │
       │  Turn  ││        ││  Turn  ││  Shake ││  High  ││        ││  Head  ││  Head  ││  Head  │
       │  Left  ││Backward││  Right ││  Head  ││  Five  ││        ││   Yaw  ││  Pitch ││   Yaw  │
       └────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
          ┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
          │Z       ││X       ││C       ││V       ││B       ││N       ││M       │
          │        ││        ││        ││        ││        ││        ││  Head  │
          │   Lie  ││  Stand ││   Sit  ││ Stretch││        ││        ││  Reset │
          └────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
'''

SIT_HEAD_PITCH = -40
STAND_HEAD_PITCH = 0
STATUS_STAND = 0
STATUS_SIT = 1
STATUS_LIE = 2
HEAD_SPEED = 80
HEAD_ANGLE = 20

head_yrp = [0, 0, 0]
head_pitch_init = 0
command = None
current_status = STATUS_LIE

def set_head(roll=None, pitch=None, yaw=None):
    global head_yrp
    if roll is not None:
        head_yrp[1] = roll
    if pitch is not None:
        head_yrp[2] = pitch
    if yaw is not None:
        head_yrp[0] = yaw
    my_dog.head_move([head_yrp], immediately=True, speed=HEAD_SPEED)

COMMANDS = {
    "forward": {
        "commands": ["forward"],
        "function": lambda: my_dog.do_action('forward', wait=False, speed=98),
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "backward": {
        "commands": ["backward"],
        "function": lambda: my_dog.do_action('backward', wait=False, speed=98),
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "turn left": {
        "commands": ["turn left"],
        "function": lambda: my_dog.do_action('turn_left', wait=False, speed=98),
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "turn right": {
        "commands": ["turn right"],
        "function": lambda: my_dog.do_action('turn_right', wait=False, speed=98),
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "trot": {
        "commands": ["trot"],
        "function": lambda: my_dog.do_action('trot', wait=False, speed=98),
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "stop": {
        "commands": ["stop"],
    },
    "lie down": {
        "commands": ["lie down"],
        "function": lambda: my_dog.do_action('lie', wait=False, speed=70),
        "head_pitch": STAND_HEAD_PITCH,
        "status": STATUS_LIE,
    },
    "stand up": {
        "commands": ["stand up"],
        "function": lambda: my_dog.do_action('stand', wait=False, speed=70),
        "head_pitch": STAND_HEAD_PITCH,
        "status": STATUS_STAND,
    },
    "sit": {
        "commands": ["sit", "sit down", "set", "set down"],
        "function": lambda: my_dog.do_action('sit', wait=False, speed=70),
        "head_pitch": SIT_HEAD_PITCH,
        "status": STATUS_SIT,
    },
    "bark": {
        "commands": ["bark", "park", "fuck"],
        "function": lambda: bark(my_dog, head_yrp, pitch_init=head_pitch_init),
    },
    "bark harder": {
        "commands": ["bark harder", "park harder", "fuck harder", "bark harbor", "park harbor", "fuck harbor"],
        "function": lambda: bark_action(my_dog, head_yrp, 'single_bark_1'),
    },
    "pant": {
        "commands": ["pant", "paint"],
        "function": lambda: pant(my_dog, head_yrp, pitch_init=head_pitch_init),
    },
    "wag tail": {
        "commands": ["wag tail", "wake tail", "wake town", "wait town", "wait tail", "wake time", "wait time", "wait tail"],
        "function": lambda: my_dog.do_action('wag_tail', wait=True, speed=100),
        "after": "wag tail",
    },
    "shake head": {
        "commands": ["shake head"],
        "function": lambda: shake_head(my_dog, head_yrp),
    },
    "stretch": {
        "commands": ["stretch"],
        "function": lambda: my_dog.do_action('stretch', wait=True, speed=80),
        "after": "stand up",
        "status": STATUS_STAND,
    },
    "doze off": {
        "commands": ["doze off", "does off"],
        "function": lambda: my_dog.do_action('doze_off', wait=True, speed=95),
        "after": "doze off",
        "status": STATUS_LIE,
    },
    "push-up": {
        "commands": ["push-up"],
        "function": lambda: pushup(my_dog),
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
        "commands": ["twist body"],
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

def set_head_pitch_init(pitch):
    global head_pitch_init
    head_pitch_init = pitch
    my_dog.head_move([head_yrp], pitch_init=pitch, immediately=True, speed=HEAD_SPEED)

def change_status(status):
    global current_status
    current_status = status
    if status == STATUS_STAND:
        set_head_pitch_init(STAND_HEAD_PITCH)
        my_dog.do_action('stand', wait=False, speed=70)
    elif status == STATUS_SIT:
        set_head_pitch_init(SIT_HEAD_PITCH)
        my_dog.do_action('sit', wait=False, speed=70)
    elif status == STATUS_LIE:
        set_head_pitch_init(STAND_HEAD_PITCH)
        my_dog.do_action('lie', wait=False, speed=70)
    my_dog.wait_all_done()

def run_command():
    global command, head_pitch_init
    if not my_dog.is_feet_done() or not my_dog.is_head_done():
        return
    if command is None:
        return
    print(command)
    for name in COMMANDS:
        if command in COMMANDS[name]["commands"]:
            if "status" in COMMANDS[name]:
                if current_status != COMMANDS[name]["status"]:
                    change_status(COMMANDS[name]["status"])
            if "head_pitch" in COMMANDS[name]:
                head_pitch_init = COMMANDS[name]["head_pitch"]
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
            else:
                command = None
            break

COMMAND_KEY_MAP = {
    "W": "trot",
    "w": "forward",
    "s": "backward",
    "a": "turn left",
    "d": "turn right",
    "z": "lie down",
    "x": "stand up",
    "c": "sit",
    "q": "bark",
    "Q": "bark harder",
    "e": "pant",
    "r": "wag tail",
    "t": "shake head",
    "v": "stretch",
    "1": "doze off",
    "2": "push-up",
    "3": "howling",
    "4": "twist body",
    "5": "scratch",
    "t": "handshake",
    "g": "high five",
}

def main():
    global head_yrp, command
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        print(usage)
        print("\033[?25l") # Hide terminal cursor
        key = readchar.readchar()
        if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            import sys
            print('')
            # sys.exit(0)
            break
        elif key in COMMAND_KEY_MAP:
            command = COMMAND_KEY_MAP[key]
        # Head Pitch
        elif key in 'uiojklUIOJKLm':
            if key == 'i':
                head_yrp[2] = HEAD_ANGLE
            elif key == 'I':
                head_yrp[2] = HEAD_ANGLE * 2
            elif key == 'k':
                head_yrp[2] = -HEAD_ANGLE
            elif key == 'K':
                head_yrp[2] = -HEAD_ANGLE * 2
            # Head Yaw
            elif key == 'j':
                head_yrp[0] = HEAD_ANGLE
            elif key == 'J':
                head_yrp[0] = HEAD_ANGLE * 2
            elif key == 'l':
                head_yrp[0] = -HEAD_ANGLE
            elif key == 'L':
                head_yrp[0] = -HEAD_ANGLE * 2
            # Head Roll
            elif key == 'u':
                head_yrp[1] = -HEAD_ANGLE
            elif key == 'U':
                head_yrp[1] = -HEAD_ANGLE * 2
            elif key == 'o':
                head_yrp[1] = HEAD_ANGLE
            elif key == 'O':
                head_yrp[1] = HEAD_ANGLE * 2
            # Head Reset
            elif key == 'm':
                head_yrp = [0, 0, 0]
            my_dog.head_move([head_yrp], pitch_init=head_pitch_init, immediately=True, speed=HEAD_SPEED)
        else:
            print('key:',key)
            continue
        run_command()
        # sleep(0.001)

if __name__ == "__main__":
    # try:
    # except Exception as e:
        # raise e
    # finally:
    main()
    print("\033[?25h") # Show terminal cursor
    my_dog.close()