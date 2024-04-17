#!/usr/bin/env python3
from pidog import Pidog
import os
import curses
import curses_utils
from time import sleep

# init pidog
# ======================================
my_dog = Pidog()
sleep(0.5)

# global variables
# ======================================
actions = [
    # name, head_pitch_adjust(-1, use last_pitch), speed
    ['stand', 0, 50],
    ['sit', -30, 50],
    ['lie', 0, 20],
    ['lie_with_hands_out', 0,  20],
    ['trot', 0, 95],
    ['forward', 0, 98],
    ['backward', 0, 98],
    ['turn_left', 0, 98],
    ['turn_right', 0, 98],
    ['doze_off', -30, 90],
    ['stretch', 20, 20],
    ['push_up', -30, 50],
    ['shake_head', -1, 90],
    ['tilting_head', -1, 60],
    ['wag_tail', -1, 100],
]
actions_len = len(actions)

sound_effects = []
# change working directory
abspath = os.path.abspath(os.path.dirname(__file__))
# print(abspath)
os.chdir(abspath)
for name in os.listdir('../sounds'):
    sound_effects.append(name.split('.')[0])
sound_effects.sort()
sound_len = len(sound_effects)
# limit sound quantity
if sound_len > actions_len:
    sound_len = actions_len
    sound_effects = sound_effects[:actions_len]

last_index = 0
last_display_index = 0
exit_flag = False
last_head_pitch = 0

STANDUP_ACTIONS = ['trot', 'forward', 'backward', 'turn_left', 'turn_right']

# define pad size
# ======================================
curses_utils.PAD_Y = 22
curses_utils.PAD_X = 70

# display fuctions
# ======================================
def display_head(subpad):
    title = "Function Demonstration"
    tip1 = "Input Function number to see how it goes."
    tip2 = "Actions will repeat 10 times."
    type_name_1 = "Actions:"
    type_name_2 = "Sound Effect:"
    tip3 = "(need to run with sudo)"

    curses_utils.clear_line(subpad, 0, color_pair=curses_utils.WHITE_BLUE | curses.A_REVERSE)
    subpad.addstr(0, 2, title, curses_utils.WHITE_BLUE | curses.A_BOLD | curses.A_REVERSE)
    subpad.addstr(1, 2, tip1, curses_utils.WHITE)
    subpad.addstr(2, 2, tip2, curses_utils.WHITE)
    curses_utils.clear_line(subpad, 3, color_pair=curses_utils.WHITE | curses.A_REVERSE)
    subpad.addstr(3, 2, type_name_1, curses_utils.WHITE | curses.A_REVERSE)
    subpad.addstr(3, 30, type_name_2, curses_utils.WHITE | curses.A_REVERSE)
    subpad.addstr(3, 31+len(type_name_2), tip3, curses_utils.YELLOW | curses.A_REVERSE)

def display_selection(subpad, index):
    global last_display_index
    # reset last selection
    if last_display_index > actions_len + sound_len-1 or last_display_index < 0:
        last_display_index = 0
    if last_display_index != index:
        if last_display_index < actions_len:
            subpad.addstr(last_display_index, 2, f"{last_display_index+1}. {actions[last_display_index][0]}", curses_utils.WHITE | curses.A_DIM)
        else:
            sound_index = last_display_index-actions_len
            subpad.addstr(sound_index, 30, f"{last_display_index+1}. {sound_effects[sound_index]}", curses_utils.WHITE | curses.A_DIM)
        last_display_index = index
    # highlight currernt selection
    if index > actions_len + sound_len-1 or index < 0:
        pass
    elif index < actions_len:
        subpad.addstr(index, 2, f"{index+1}. {actions[index][0]}", curses_utils.WHITE_BLUE)
    else:    
        sound_index = index-actions_len
        subpad.addstr(sound_index, 30, f"{index+1}. {sound_effects[sound_index]}", curses_utils.WHITE_BLUE)

def display_actions(subpad):
    for i in range(actions_len):
        subpad.addstr(i, 2, f"{i+1}. {actions[i][0]}", curses_utils.WHITE | curses.A_DIM)
    for i in range(sound_len):
        subpad.addstr(i, 30, f"{i+actions_len+1}. {sound_effects[i]}", curses_utils.WHITE | curses.A_DIM)

def display_bottom(subpad, num=''):
    curses_utils.clear_line(subpad, 0, color_pair=curses_utils.WHITE | curses.A_DIM)
    subpad.addstr(0, 0, f"Enter function number: {num}", curses_utils.WHITE | curses.A_DIM)
    subpad.addstr(0, curses_utils.PAD_X-16, "Ctrl^C to quit", curses_utils.WHITE | curses.A_DIM)


def do_function(index):
    global last_index, last_head_pitch
    my_dog.body_stop()
    if index < 0:
        return
    if index < actions_len:
        name, head_pitch_adjust, speed = actions[index]
        # If last action is push_up, then lie down first
        if last_index < len(actions) and actions[last_index][0] in ('push_up'):
            last_head_pitch = 0
            my_dog.do_action('lie', speed=60)
        # If this action is trot, forward, turn left, turn right and backward, and, last action is not, then stand up
        if name in STANDUP_ACTIONS and last_index < len(actions) and actions[last_index][0] not in STANDUP_ACTIONS:
            last_head_pitch = 0
            my_dog.do_action('stand', speed=60)
        if head_pitch_adjust != -1:
            last_head_pitch = head_pitch_adjust
        my_dog.head_move_raw([[0, 0, last_head_pitch]], immediately=False, speed=60)
        my_dog.do_action(name, step_count=10, speed=speed, pitch_comp=last_head_pitch)
        last_index = index
    elif index < actions_len + sound_len:
        my_dog.speak(sound_effects[index - len(actions)], volume=80)
        last_index = index

def main(stdscr):
    # reset screen
    stdscr.clear()
    stdscr.move(4, 0)
    stdscr.refresh()

    # disable cursor 
    curses.curs_set(0)

    # init color 
    curses.start_color()
    curses.use_default_colors()
    curses_utils.init_preset_color_pairs()

    # init pad    
    pad = curses.newpad(curses_utils.PAD_Y, curses_utils.PAD_X)   

    # init subpad
    head_pad = pad.subpad(4, curses_utils.PAD_X, 0, 0)
    selection_pad = pad.subpad(actions_len, curses_utils.PAD_X, 4, 0)
    bottom_pad = pad.subpad(1, curses_utils.PAD_X, actions_len+4, 0)
    # add content to a
    display_head(head_pad)
    display_actions(selection_pad)
    display_head(head_pad)
    curses_utils.pad_refresh(pad)
    curses_utils.pad_refresh(selection_pad)

    # for i in range(2):
    #     for i in range(30):
    #         display_selection(selection_pad, i)
    #         curses_utils.pad_refresh(selection_pad)
    #         sleep(0.1)

    # enable cursor and echo
    curses.curs_set(0)
    curses.echo()

    # stdscr.nodelay(True) # set non-blocking mode for getch()
    # stdscr.timeout(10)
    # curses.cbreak()

    index_str = ''
    index = -1

    display_bottom(bottom_pad)
    curses_utils.pad_refresh(bottom_pad)

    while True:
        # draw bottom bar
        # display_bottom(bottom_pad)
        # display_bottom(bottom_pad, f'{index+1}')
        # curses_utils.pad_refresh(bottom_pad)
        # reset cursor
        stdscr.move(actions_len+4, 23)
        stdscr.refresh()
        # red key
        key = stdscr.getch()
        key = curses.unctrl(key)

        if key in b'0123456789':
            index_str += str(int(key))
            display_bottom(bottom_pad, index_str)
            curses_utils.pad_refresh(bottom_pad)
        elif key == b'^J': # enter
            index = int(index_str)-1
            # display selection
            display_selection(selection_pad, index)
            curses_utils.pad_refresh(selection_pad)
            # do fuction
            do_function(index)
            # reset display
            index_str = ''
            display_bottom(bottom_pad, index_str)
            curses_utils.pad_refresh(bottom_pad)

        sleep(0.2)

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        my_dog.close()