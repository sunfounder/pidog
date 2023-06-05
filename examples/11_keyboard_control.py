#!/usr/bin/env python3
import curses
import time
import sys
from pidog import Pidog
from preset_actions import *

# init pidog
# ======================================
my_dog = Pidog()
time.sleep(0.5)

# global variables
# ======================================
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

last_key = None

# KEYS and OPERATIONS:dict
# ======================================
KEYS = {
    "1": {  # keyname
        "pos": [0, 0], # ypos, xpos
        "tip": ["Doze", "Off"],
        "operation": "doze off",
    },
    "2": {
        "pos": [0, 10],
        "tip": ["Push", "Up"],
        "operation": "push up",
    },
    "3": {
        "pos": [0, 20],
        "tip": ["Howling", ""],
        "operation": "howling",
    },
    "4": {
        "pos": [0, 30],
        "tip": ["Body", "Twist"],
        "operation": "twist body",
    },
    "5": {
        "pos": [0, 40],
        "tip": ["Scratch", ""],
        "operation": "scratch",
    },
    "6": {
        "pos": [0, 50],
        "tip": ["", ""],
        "operation": None,
    },
    "7": {
        "pos": [0, 60],
        "tip": ["", ""],
        "operation": None,
    },
    "8": {
        "pos": [0, 70],
        "tip": ["", ""],
        "operation": None,
    },
    "9": {
        "pos": [0, 80],
        "tip": ["", ""],
        "operation": None,
    },
    "0": {
        "pos": [0, 90],
        "tip": ["", ""],
        "operation": None,
    },
    # #################################
    "q": {
        "pos": [5, 5],
        "tip": ["Bark", ""],
        "operation": "bark",
    },
    "w": {
        "pos": [5, 15],
        "tip": ["Forward", ""],
        "operation": "forward",
    },
    "W": {
        "pos": [5, 15],
        "tip_upper": "Trot",
        "operation": "trot",
    },
    "e": {
        "pos": [5, 25],
        "tip": ["Pant", ""],
        "operation": "pant",
    },
    "r": {
        "pos": [5, 35],
        "tip": ["Wag", "Tail"],
        "operation": "wag tail",
    },
    "t": {
        "pos": [5, 45],
        "tip": ["Hand", "Shake"],
        "operation": "handshake",
    },
    "y": {
        "pos": [5, 55],
        "tip": ["", ""],
        "operation": None,
    },
    "u": {
        "pos": [5, 65],
        "tip": ["Head", "Roll"],
        "operation": None,
    },
    "U": {
        "pos": [5, 65],
        "tip_upper": "x2",
        "operation": None,
    },
    "i": {
        "pos": [5, 75],
        "tip": ["Head", "Pitch"],
        "operation": None,
    },
    "I": {
        "pos": [5, 75],
        "tip_upper": "x2",
        "operation": None,
    },
    "o": {
        "pos": [5, 85],
        "tip": ["Head", "Roll"],
        "operation": None,
    },
    "O": {
        "pos": [5, 85],
        "tip_upper": "x2",
        "operation": None,
    },
    "p": {
        "pos": [5, 95],
        "tip": ["Head", "Roll"],
        "operation": None,
    },
    "P": {
        "pos": [5, 95],
        "tip_upper": "x2",
        "operation": None,
    },
    ####################
    "a": {
        "pos": [10, 9],
        "tip": ["Turn", "Left"],
        "operation": "turn left",
    },
    "s": {
        "pos": [10, 19],
        "tip": ["Backward", ""],
        "operation": "backward",
    },
    "d": {
        "pos": [10, 29],
        "tip": ["Turn", "Right"],
        "operation": "turn right",
    },
    "f": {
        "pos": [10, 39],
        "tip": ["Shake", "Head"],
        "operation": "shake head",
    },
    "g": {
        "pos": [10, 49],
        "tip": ["High", "Five"],
        "operation": "high five",
    },
    "h": {
        "pos": [10, 59],
        "tip": ["", ""],
        "operation": None,
    },
    "j": {
        "pos": [10, 69],
        "tip": ["Head", "Yaw"],
        "operation": None,
    },
    "k": {
        "pos": [10, 79],
        "tip": ["Head", "Pitch"],
        "operation": None,
    },
    "l": {
        "pos": [10, 89],
        "tip": ["Head", "Yaw"],
        "operation": None,
    },
    #############
    "z": {
        "pos": [15, 12],
        "tip": ["Lie", ""],
        "operation": "lie",
    },
    "x": {
        "pos": [15, 22],
        "tip": ["Stand", ""],
        "operation": "stand",
    },
    "c": {
        "pos": [15, 32],
        "tip": ["Sit", ""],
        "operation": "sit",
    },
    "v": {
        "pos": [15, 42],
        "tip": ["Stretch", ""],
        "operation": "stretch",
    },
    "b": {
        "pos": [15, 52],
        "tip": ["", ""],
        "operation": None,
    },
    "n": {
        "pos": [15, 62],
        "tip": ["", ""],
        "operation": None,
    },
    "m": {
        "pos": [15, 72],
        "tip": ["Head", "Reset"],
        "operation": None,
    },
}

OPERATIONS = {
    "forward": {
        "function": lambda: my_dog.do_action('forward', speed=98),
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "backward": {
        "function": lambda: my_dog.do_action('backward', speed=98),
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "turn left": {
        "function": lambda: my_dog.do_action('turn_left', speed=98),
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "turn right": {
        "function": lambda: my_dog.do_action('turn_right', speed=98),
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "trot": {
        "function": lambda: my_dog.do_action('trot', speed=98),
        "status": STATUS_STAND,
        "head_pitch": STAND_HEAD_PITCH,
    },
    "stop": {
    },
    "lie": {
        "function": lambda: my_dog.do_action('lie', speed=70),
        "head_pitch": STAND_HEAD_PITCH,
        "status": STATUS_LIE,
    },
    "stand": {
        "function": lambda: my_dog.do_action('stand', speed=70),
        "head_pitch": STAND_HEAD_PITCH,
        "status": STATUS_STAND,
    },
    "sit": {
        "function": lambda: my_dog.do_action('sit', speed=70),
        "head_pitch": SIT_HEAD_PITCH,
        "status": STATUS_SIT,
    },
    "bark": {
        "function": lambda: bark(my_dog, head_yrp, pitch_comp=head_pitch_init),
    },
    "bark harder": {
        "function": lambda: bark_action(my_dog, head_yrp, 'single_bark_1'),
    },
    "pant": {
        "function": lambda: pant(my_dog, head_yrp, pitch_comp=head_pitch_init),
    },
    "wag tail": {
        "function": lambda: my_dog.do_action('wag_tail', speed=100),
        "after": "wag tail",
    },
    "shake head": {
        "function": lambda: shake_head(my_dog, head_yrp),
    },
    "stretch": {
        "function": lambda: my_dog.do_action('stretch', speed=80),
        "after": "stand",
        "status": STATUS_STAND,
    },
    "doze off": {
        "function": lambda: my_dog.do_action('doze_off', speed=95),
        "after": "doze off",
        "status": STATUS_LIE,
    },
    "push up": {
        "function": lambda: pushup(my_dog),
        "after": "push up",
        "status": STATUS_STAND,
    },
    "howling": {
        "function": lambda: howling(my_dog),
        "after": "sit",
        "status": STATUS_SIT,
    },
    "twist body": {
        "function": lambda: body_twisting(my_dog),
        "before": "stretch",
        "after": "sit",
        "status": STATUS_STAND,
    },
    "scratch": {
        "function": lambda: scratch(my_dog),
        "after": "sit",
        "head_pitch": SIT_HEAD_PITCH,
        "status": STATUS_SIT,
    },
    "handshake": {
        "function": lambda: hand_shake(my_dog),
        "after": "sit",
        "head_pitch": SIT_HEAD_PITCH,
        "status": STATUS_SIT,
    },
    "high five": {
        "function": lambda: high_five(my_dog),
        "after": "sit",
        "head_pitch": SIT_HEAD_PITCH,
        "status": STATUS_SIT,
    },
}

#
# ======================================
def run_operation(key):
    global command, head_pitch_init
    if not my_dog.is_legs_done() or not my_dog.is_head_done():
        return
    
    key_data = None
    operation = None
    # before = None
    # after = None

    if key not in KEYS.keys():
        return
    else:
        key_data = KEYS[key]

    if "operation" in key_data and key_data["operation"] != None:
        if key_data["operation"] in OPERATIONS:
            operation = OPERATIONS[key_data["operation"]]
        else:
            return
        # before
        if "before" in operation and operation["before"] != None:
            before = operation["before"]
            if before in OPERATIONS and OPERATIONS[before]["function"] != None:
                OPERATIONS[before]["function"]() # run before function
        # function
        if "function" in operation and operation["function"] != None:
            operation["function"]() # run function function
        # after
        if "after" in operation and operation["after"] != None:
            after = operation["after"]
            if after in OPERATIONS and OPERATIONS[after]["function"] != None:
                OPERATIONS[after]["function"]() # run after function

# define window size
# ======================================
PAD_Y = 22
PAD_X = 110

# define title
# ======================================
TITLE = "Pidog Keyboard Control"

# display fuctions
# ======================================
def pad_refresh(pad):
    # Displays a section of the pad in the middle of the screen.
    # (0,0) : coordinate of upper-left corner of pad area to display.
    # (5,5) : coordinate of upper-left corner of window area to be filled
    #         with pad content.
    # (20, 75) : coordinate of lower-right corner of window area to be
    #          : filled with pad content.
    y, x = pad.getbegyx()
    h, w = pad.getmaxyx()
    if h > curses.LINES:
        h = curses.LINES
    if w > curses.COLS:
        w = curses.COLS
    pad.refresh(0, 0, y, x, h-1, w-1)

def clear_line(pad, line, xlen=PAD_X, color=None):
    if color is None:
        pad.addstr(line, 0, " "*(xlen-2))
    else:
        pad.addstr(line, 0, " "*(xlen-1), color)

def display_title(subpad, color=1):
    clear_line(subpad, 0, color=curses.color_pair(3) | curses.A_REVERSE)
    subpad.addstr(0, int((PAD_X-len(TITLE))/2), TITLE, curses.color_pair(3) | curses.A_REVERSE)
    # subpad.noutrefresh()
    # curses.doupdate()

def set_simulated_key(stdscr, key, color=1):
    if key in KEYS.keys():
        ypos = KEYS[key]["pos"][0]
        xpos = KEYS[key]["pos"][1]
    else:
        raise ValueError("No this key")

    # key_bottom_layer
    key_bottom_layer = [
        "┌────────┐",
        "│        │",
        "│        │",
        "│        │",
        "└────────┘",     
    ]
    for i in range(len(key_bottom_layer)):
        stdscr.addstr(ypos+i, xpos, key_bottom_layer[i], curses.color_pair(color)| curses.A_BOLD)

    # key name
    key_ypos = ypos + 1
    key_xpos = xpos + 1
    stdscr.addstr(key_ypos, key_xpos, key.upper(), curses.color_pair(color))

    # check reuse
    key_upper = key.upper()
    key_lower = key.lower()
    upper_color = 4
    lower_color = 1
    if key.isupper():
        if color != 1:
            upper_color = color
            lower_color = 1
    else:
        upper_color = 4
        lower_color = color

    # tip_upper
    if key_upper in KEYS and "tip_upper" in KEYS[key_upper].keys():
        tip_upper = KEYS[key_upper]["tip_upper"]
        if tip_upper is not None:
            tip_shift_ypos = ypos + 1
            tip_shift_xpos = xpos + 9 - int(len(tip_upper))
            stdscr.addstr(tip_shift_ypos, tip_shift_xpos, tip_upper, curses.color_pair(upper_color))
        
    # tip1 and tip2
    if key_lower in KEYS:
        tip1 = KEYS[key_lower]["tip"][0]
        tip2 = KEYS[key_lower]["tip"][1]

        if tip1 != None and tip1 != "":
            if tip2 == None or tip2 == "":
                tip1_ypos = ypos + 3
                tip1_xpos = xpos + 5 - int(len(tip1)/2)
                stdscr.addstr(tip1_ypos, tip1_xpos, tip1, curses.color_pair(lower_color))
            else:
                tip1_ypos = ypos + 2
                tip1_xpos = xpos + 5 - int(len(tip1)/2)
                tip2_ypos = ypos + 3
                tip2_xpos = xpos + 6 - int(len(tip2)/2)
                stdscr.addstr(tip1_ypos, tip1_xpos, tip1, curses.color_pair(lower_color))
                stdscr.addstr(tip2_ypos, tip2_xpos, tip2, curses.color_pair(lower_color))

def display_tip(subpad, color=1):
    tip_upper = "Some keys are uppercase and lowercase for different functions."
    tip_quit = "Press Ctrl^C to quit"
    clear_line(subpad, 0, color=curses.color_pair(4) | curses.A_REVERSE)
    subpad.addstr(0, 0, tip_upper, curses.color_pair(4)| curses.A_BOLD | curses.A_REVERSE)
    subpad.addstr(0, PAD_X-25, tip_quit, curses.color_pair(4)| curses.A_BOLD | curses.A_REVERSE)

def main(stdscr):
    global last_key

    # reset screen
    stdscr.clear()
    stdscr.move(0, 0)
    stdscr.refresh()

    # disable cursor 
    curses.curs_set(0)
    
    # set colors
    curses.start_color()
    curses.use_default_colors()
    curses.init_color(8, 192, 192, 192)
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(3, curses.COLOR_CYAN, -1)
    curses.init_pair(4, 8, -1)

    # init pad    
    pad = curses.newpad(PAD_Y, PAD_X)

    # init subpad
    title_pad = pad.subpad(1, PAD_X, 0, 0)
    keys_pad = pad.subpad(20, PAD_X, 1, 0)
    tip_pad = pad.subpad(1, PAD_X, 21, 0)

    # display TITLE
    display_title(title_pad)
    # display simulated keys
    for key in KEYS.keys():
        set_simulated_key(keys_pad, key=key)
    # display tip
    display_tip(tip_pad)

    # refresh
    pad_refresh(pad)
    stdscr.move(PAD_Y+1, 0)
    stdscr.refresh()

    stdscr.nodelay(True) # set non-blocking mode for getch()
    stdscr.timeout(100)
    # TODO:
        # what is the detection interval of getch() in non-blocking mode 

    while True:
        curses.flushinp()
        key = stdscr.getch()
        if key == curses.ERR: # if no key
            if last_key == None:
                continue
        # ---- resize window ----
        if key == curses.KEY_RESIZE:
            curses.update_lines_cols()
            stdscr.move(PAD_Y+1, 0)
            stdscr.refresh()
            sleep(0.5)
        if key > 32 and key < 127:
            key = chr(key)
            if key in KEYS:
                if last_key != key:
                    if last_key != None:
                        set_simulated_key(keys_pad, key=last_key, color=1)
                    set_simulated_key(keys_pad, key=key, color=3)
                    my_dog.body_stop()
                    my_dog.rgb_strip.close()
                pad_refresh(keys_pad)
                stdscr.move(PAD_Y+1, 0)
                stdscr.refresh()
                time.sleep(0.1)
                run_operation(key)
                last_key = key
        else:
            if last_key != None and my_dog.is_all_done():
                set_simulated_key(keys_pad,key=last_key, color=1)
                pad_refresh(keys_pad)
                stdscr.move(PAD_Y+1, 0)
                stdscr.refresh()
                last_key = None
        time.sleep(0.1)


if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        my_dog.close()

