#!/usr/bin/env python3
from pidog import Pidog
import curses
from time import sleep

# init pidog
# ======================================
my_dog = Pidog()

my_dog.legs_move([[0]*8], immediately=True, speed=60)
my_dog.head_move([[0]*3], immediately=True, speed=60)
my_dog.tail_move([[0]], immediately=True, speed=60)
my_dog.wait_all_done()

# global variables
# ======================================
leg_angles = [0.0]*8
head_angles = [0.0]*3
tail_angle = [0.0]*1
leg_offsets = [0.0]*8
head_offsets = [0.0]*3
tail_offset = [0.0]*1
current_servo = "1"

OFFSET_STEP = (180 / 2000) * (20000 / 4095)  # actual precision of steering gear

is_save = False

# get_real_values()
# ======================================
def get_real_values():
    global leg_angles, head_angles, tail_angle
    global leg_offsets, head_offsets, tail_offset
    leg_angles = list.copy(my_dog.leg_current_angles)
    head_angles = list.copy(my_dog.head_current_angles)
    tail_angle = list.copy(my_dog.tail_current_angles)
    leg_offsets = list.copy(my_dog.legs.offset)
    head_offsets = list.copy(my_dog.head.offset)
    tail_offset = list.copy(my_dog.tail.offset)
    for i, x in enumerate(leg_angles):
        leg_angles[i] = round(x, 2)
    for i, x in enumerate(head_angles):
        head_angles[i] = round(x, 2)
    tail_angle[0] = round(tail_angle[0], 2)
    for i, x in enumerate(leg_offsets):
        leg_offsets[i] = round(x, 2)
    for i, x in enumerate(head_offsets):
        head_offsets[i] = round(x, 2)
    tail_offset[0] = round(tail_offset[0], 2)

# constrain(), constrain value range
# ======================================
def constrain(val, min_val, max_val):

    if val < min_val: return min_val
    if val > max_val: return max_val
    return val

# define pad size
# ======================================
PAD_Y = 40
PAD_X = 80

pad_ypos = 0
pad_xpos = 0

# define color
# ======================================


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
    if h > curses.LINES-1:
        h = curses.LINES-1
    if w > curses.COLS-1:
        w = curses.COLS-1
    pad.refresh(0, 0, y, x, h, w)

def clear_line(pad, line, xlen=PAD_X, color=None):
    if color is None:
        pad.addstr(line, 0, " "*(xlen-2))
    else:
        pad.addstr(line, 0, " "*(xlen-1), color)

def display_title(subpad, color=1):
    title = "PiDog  Calibration"
    # tip1
    clear_line(subpad, 0, color=curses.color_pair(3) | curses.A_REVERSE)
    subpad.addstr(0, int((PAD_X-len(title))/2), title, curses.color_pair(3) | curses.A_REVERSE)
    # subpad.noutrefresh()
    # curses.doupdate()

tip1 = [
    "Press key to select servo:",
    "1 ~ 8 : Leg servos",
    "9 : Head yaw ↺   ",
    "0 : Head roll ↔  ",
    "- : Head pitch ↕ ",
    "= : Tail         ",
]
def display_tip1(subpad, color=1):
    subpad.addstr(0, 0, tip1[0], curses.color_pair(4)| curses.A_BOLD | curses.A_REVERSE)
    for i in range(1, len(tip1)):
        subpad.addstr(i, 0, tip1[i], curses.color_pair(4)| curses.A_BOLD)

tip2 = [
    "Press key to adjust servo:",
    "W: increase angle ",
    "S: decreases angle",
]
def display_tip2(subpad, color=1):
    subpad.addstr(0, 0, tip2[0], curses.color_pair(4)| curses.A_BOLD | curses.A_REVERSE)
    for i in range(1, len(tip2)):
        subpad.addstr(i, 0, tip2[i], curses.color_pair(4)| curses.A_BOLD)

body = [
    "        ↺ [9]     ",
    "  ↕[-] ┌─┐ ↔[0]  ",
    "       │ │       ",
    "[2][1]┌└─┘┐[3][4]",
    "      │   │      ",
    "      │   │      ",
    "[6][5]└─┬─┘[7][8]",
    "       [=]       ",
    "        /        ",
]
servo_pos = { # servo_pos in body
    "1": [3, 3], # ypos, xpos
    "2": [3, 0],
    "3": [3, 11],
    "4": [3, 14],
    "5": [6, 3],
    "6": [6, 0],
    "7": [6, 11],
    "8": [6, 14],
    "9": [0, 10],
    "0": [1, 12],
    "-": [1, 3],
    "=": [7, 7],
}
def display_dog_body(subpad, servo="1", color=1):
    for i in range(len(body)):
        subpad.addstr(i, 0, body[i], curses.color_pair(color)| curses.A_BOLD)
    if servo in servo_pos.keys():
        subpad.addstr(servo_pos[servo][0], servo_pos[servo][1], f"[{servo}]", curses.color_pair(3)| curses.A_BOLD)

tip3 = [
    "Ctrl+C: Quit    Space: Save",
]
def display_tip3(subpad, color=1):
    max_y, max_x = subpad.getmaxyx()
    clear_line(subpad, 0)
    subpad.addstr(0, 0, tip3[0], curses.color_pair(4)| curses.A_BOLD | curses.A_REVERSE)


def display_servo_num(subpad, color=1):
    subpad.addstr(0, 0, "Current Servo:", curses.color_pair(4)| curses.A_BOLD)
    subpad.addstr(0, 15, f"{current_servo}", curses.color_pair(3)| curses.A_BOLD)

def display_offsets(subpad, servo="1", color=1):
    servo_num = "1234567890-="
    comma = ""
    clear_line(subpad, 0)
    subpad.addstr(0, 0, f"leg_offsets:", curses.color_pair(4)| curses.A_BOLD)
    for i, x in enumerate(leg_offsets):
        comma = "," if i < len(leg_offsets)-1 else ""
        if servo_num[i] == current_servo:
            subpad.addstr(f' {x:.2f}{comma}', curses.color_pair(3)| curses.A_BOLD)
        else:
            subpad.addstr(f' {x:.2f}{comma}', curses.color_pair(color)| curses.A_BOLD)
    # 
    clear_line(subpad, 1)
    subpad.addstr(1, 0, f"head_offsets:", curses.color_pair(4)| curses.A_BOLD)
    for i, x in enumerate(head_offsets):
        comma = "," if i < len(head_offsets)-1 else ""
        if servo_num[i+8] == current_servo:
            subpad.addstr(f' {x:.2f}{comma}', curses.color_pair(3)| curses.A_BOLD)
        else:
            subpad.addstr(f' {x:.2f}{comma}', curses.color_pair(color)| curses.A_BOLD)
    #
    clear_line(subpad, 2)
    subpad.addstr(2, 0, f"tail_offset:", curses.color_pair(4)| curses.A_BOLD)
    for i, x in enumerate(tail_offset):
        if servo_num[i+11] == current_servo:
            subpad.addstr(f' {x:.2f}', curses.color_pair(3)| curses.A_BOLD)
        else:
            subpad.addstr(f' {x:.2f}', curses.color_pair(color)| curses.A_BOLD)


def main(stdscr):
    # global winlines, wincols
    global pad_ypos, pad_xpos, current_servo
    global is_save
    
    inc = 1  # 1 or -1, angle increase direction

    # winlines = curses.LINES
    # wincols = curses.LINES

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
    # curses.init_pair(3, curses.COLOR_BLUE, -1)
    curses.init_pair(4, 8, -1)

    # init pad    
    pad = curses.newpad(PAD_Y, PAD_X)
    # pad.box()

    # get the offset
    get_real_values()

    # init subpad
    title_pad = pad.subpad(1, PAD_X, 0, 0)
    tip1_pad = pad.subpad(len(tip1), len(tip1[0]), 1, 0)
    # tip2_pad = pad.subpad(len(tip2), len(tip2[0]), 1, PAD_X-len(tip2[0])-1)
    tip2_pad = pad.subpad(len(tip2), len(tip2[0]), len(tip1)+2, 0)
    # body_pad = pad.subpad(len(body), len(body[0]), 2, int((PAD_X-len(body[0]))/2)-2)
    body_pad = pad.subpad(len(body), len(body[0]), 2, PAD_X-len(body[0])-20)
    if curses.COLS < PAD_X - 20:
        body_pad.move(2, 1)
    tip3_pad = pad.subpad(len(tip3), PAD_X, len(body)+3, 0)
    servo_num_pad = pad.subpad(1, PAD_X, len(body)+4, 0)
    offsets_pad = pad.subpad(3, PAD_X, len(body)+5, 0)

    display_title(title_pad)
    display_tip1(tip1_pad)
    display_tip2(tip2_pad)
    display_dog_body(body_pad, current_servo)
    display_tip3(tip3_pad)
    display_servo_num(servo_num_pad)
    display_offsets(offsets_pad)

    pad_refresh(pad)

    stdscr.nodelay(True) # set non-blocking mode for getch()
    stdscr.timeout(50) # set timeout when no key is pressed

    while True:
        try:
            key = stdscr.getch()
            if key == curses.ERR: # if no key
                continue
            # ---- resize window ----
            if key == curses.KEY_RESIZE:
                pad_ypos = 0
                pad_xpos = 0
                curses.update_lines_cols()
                # if curses.COLS < PAD_X - 20:
                    # body_pad.refresh(2, curses.COLS-1-len(body[0]))
                # body_pad.erase() # ok
                pad_refresh(pad)
                sleep(0.5)
            # ---- select the servo ----
            elif chr(key) in ('1234567890-='):
                current_servo = chr(key)
                display_dog_body(body_pad, current_servo)
                display_servo_num(servo_num_pad)
                display_offsets(offsets_pad)
                clear_line(pad, 17)
                pad_refresh(pad)
            # ---- move ----
            elif chr(key) in ('wsWS'):
                if chr(key) in ('wW'):
                    inc = 1
                else:
                    inc = -1
                # control legs
                if current_servo in ('12345678'):
                    # get index
                    index = ('12345678').index(current_servo)
                    # 
                    leg_angles[index] += inc*OFFSET_STEP
                    offset_temp = leg_angles[index] + my_dog.legs.offset[index]
                    offset_temp = constrain(offset_temp, -20, 20)
                    #
                    leg_angles[index] = offset_temp - my_dog.legs.offset[index]
                    leg_offsets[index] = offset_temp
                    # move servos
                    my_dog.legs_simple_move(leg_angles)
                # control head
                elif current_servo in ('90-'):
                    index = ('90-').index(current_servo)
                    # 
                    head_angles[index] += inc*OFFSET_STEP
                    offset_temp = my_dog.head.offset[index] + head_angles[index]
                    offset_temp = constrain(offset_temp, -20, 20)
                    #
                    head_offsets[index] = offset_temp
                    head_angles[index] = offset_temp - my_dog.head.offset[index]
                    #
                    my_dog.head_move_raw([head_angles], True, 80)
                # control tail
                elif current_servo == '=':
                    tail_angle[0] += inc*OFFSET_STEP
                    offset_temp = my_dog.tail.offset[0] + tail_angle[0]
                    offset_temp = constrain(offset_temp, -20, 20)
                    #
                    tail_offset[0] = offset_temp
                    tail_angle[0] = offset_temp - my_dog.tail.offset[0]
                    #
                    my_dog.tail_move([tail_angle], True, 80) 
                # display offsets 
                display_offsets(offsets_pad)
                clear_line(pad, 17)
                pad_refresh(pad)
            # ---- save calibration ----
            elif key == 32: # space key
                clear_line(pad, 17)
                pad.addstr(17, 0, 'Confirm save ? (y/n)  ', curses.color_pair(3) | curses.A_REVERSE)
                pad_refresh(pad)
                while True:
                    key = stdscr.getch()
                    if key == curses.ERR:
                        continue
                    if chr(key) in ('yY'):
                        my_dog.set_leg_offsets(leg_offsets)
                        my_dog.set_head_offsets(head_offsets)
                        my_dog.set_tail_offset(tail_offset)
                        sleep(0.5)
                        get_real_values()
                        display_offsets(offsets_pad)
                        clear_line(pad, 17)
                        pad.addstr(17, 0, 'Offsets saved.  ', curses.color_pair(3) | curses.A_REVERSE)
                        pad_refresh(pad)
                        is_save = True
                        break
                    elif chr(key) in ('nN'):
                        display_offsets(offsets_pad)
                        clear_line(pad, 17)
                        pad_refresh(pad)
                        break
        except KeyboardInterrupt:
            # ---- exit and remind to save calibration ----
            if is_save:
                break
            else:
                pad.addstr(17, 0, 'Change not saved, whether to exit? (y/n)  ', curses.color_pair(3) | curses.A_REVERSE)
                pad_refresh(pad)
                key = None
                while True:
                    key = stdscr.getch()
                    if key == curses.ERR:
                        continue
                    if chr(key) in ('ynYN'):
                        break
                if chr(key) in 'yY':
                    break
                else:
                    clear_line(pad, 17)
                    pad_refresh(pad)
                    continue

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        my_dog.close()
