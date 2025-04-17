#!/usr/bin/env python3
from pidog import Pidog
import curses
import curses_utils
from time import sleep

# init pidog
# ======================================
my_dog = Pidog()
sleep(.1)

# global variables
# ======================================
leg_offset = list.copy(my_dog.legs.offset)
head_offset = list.copy(my_dog.head.offset)
tail_offset = list.copy(my_dog.tail.offset)

current_servo = "1"

OFFSET_STEP = (180 / 2000) * (20000 / 4095)  # actual precision of steering gear

is_save = False

LEGS_ORIGNAL_ANGLES_60 = [30, -30, -30, 30, 30, -30, -30, 30]
LEGS_ORIGNAL_ANGLES_90 = [0 for _ in range(8)]

legs_orignal_angles = [0 for _ in range(8)]
head_orignal_angles = [0, 0, my_dog.HEAD_PITCH_OFFSET]
tail_orignal_angles = [0]

leg_angles = list.copy(legs_orignal_angles)
head_angles = list.copy(head_orignal_angles)
tail_angle = list.copy(tail_orignal_angles)

# constrain(), constrain value range
# ======================================
def constrain(val, min_val, max_val):

    if val < min_val: return min_val
    if val > max_val: return max_val
    return val

def display_title(subpad, color_pair):
    title = "PiDog  Calibration"
    # tip1
    curses_utils.clear_line(subpad, 0, color_pair=color_pair)
    subpad.addstr(0, int((curses_utils.PAD_X-len(title))/2), title, color_pair)

tip1 = [
    "Press key to select servo:  ",
    "1 ~ 8 : Leg servos",
    "9 : Head yaw    ",
    "0 : Head roll   ",
    "- : Head pitch  ",
    "= : Tail         ",
]
def display_tip1(subpad, color_pair):
    subpad.addstr(0, 0, tip1[0], color_pair | curses.A_BOLD | curses.A_REVERSE)
    for i in range(1, len(tip1)):
        subpad.addstr(i, 0, tip1[i], color_pair | curses.A_BOLD)

tip2 = [
    "Press key to adjust servo:  ",
    "W or A: increase angle ",
    "S or D: decreases angle",
]
def display_tip2(subpad, color_pair):
    subpad.addstr(0, 0, tip2[0], color_pair | curses.A_BOLD | curses.A_REVERSE)
    for i in range(1, len(tip2)):
        subpad.addstr(i, 0, tip2[i], color_pair | curses.A_BOLD)

body = [
    "        [9]        ",
    "   [-] ┌─┐  [0]  ",
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
    "9": [0, 8],
    "0": [1, 12],
    "-": [1, 3],
    "=": [7, 7],
}
def display_dog_body(subpad, color_pair, color_pair_select):
    for i in range(len(body)):
        subpad.addstr(i, 0, body[i], color_pair | curses.A_BOLD)
    servo = current_servo
    if servo in servo_pos.keys():
        subpad.addstr(servo_pos[servo][0], servo_pos[servo][1], f"[{servo}]", color_pair_select | curses.A_BOLD)

tip3 = [
    "Ctrl+C: Quit    Space: Save  ",
]
def display_tip3(subpad, color_pair):
    curses_utils.clear_line(subpad, 0)
    subpad.addstr(0, 0, tip3[0], color_pair | curses.A_BOLD | curses.A_REVERSE)

def display_servo_num(subpad, color_pair, color_pair_select):
    subpad.addstr(0, 0, "Current Servo:", color_pair | curses.A_BOLD)
    subpad.addstr(0, 15, f"{current_servo}", color_pair_select | curses.A_BOLD)

def display_offsets(subpad, color_pair, color_pair_select):
    servo_num = "1234567890-="
    comma = ""
    curses_utils.clear_line(subpad, 0)
    subpad.addstr(0, 0, f"leg_offset:", color_pair | curses.A_BOLD)
    for i, x in enumerate(leg_offset):
        comma = "," if i < len(leg_offset)-1 else ""
        if servo_num[i] == current_servo:
            subpad.addstr(f' {x:.2f}{comma}', color_pair_select | curses.A_BOLD)
        else:
            subpad.addstr(f' {x:.2f}{comma}', color_pair | curses.A_BOLD)
    # 
    curses_utils.clear_line(subpad, 1)
    subpad.addstr(1, 0, f"head_offset:", color_pair | curses.A_BOLD)
    for i, x in enumerate(head_offset):
        comma = "," if i < len(head_offset)-1 else ""
        if servo_num[i+8] == current_servo:
            subpad.addstr(f' {x:.2f}{comma}', color_pair_select | curses.A_BOLD)
        else:
            subpad.addstr(f' {x:.2f}{comma}', color_pair | curses.A_BOLD)
    #
    curses_utils.clear_line(subpad, 2)
    subpad.addstr(2, 0, f"tail_offset:", color_pair | curses.A_BOLD)
    for i, x in enumerate(tail_offset):
        if servo_num[i+11] == current_servo:
            subpad.addstr(f' {x:.2f}', color_pair_select | curses.A_BOLD)
        else:
            subpad.addstr(f' {x:.2f}', color_pair | curses.A_BOLD)

MAX_CALI_TYPE = 2
cali_type = 0
selecet_cali_ruler = [
    "Selecet your calibration ruler type:  ",
    " ",
    "   90 degree calibration ruler   ",
    "   60 degree calibration ruler   ",
]

cali_ruler_tip = [
    "[↑]      Select Up  ",
    "[↓]      Select Down",
    "[Enter]  OK",
]


def display_selecet_cali_ruler(subpad, color_pair, color_pair_select):
    # subpad.box()
    subpad.addstr(0, 0, selecet_cali_ruler[0], color_pair | curses.A_BOLD)
    subpad.addstr(1, 0, selecet_cali_ruler[1], color_pair | curses.A_BOLD )
    for i in range(len(selecet_cali_ruler)-2):
        if i == cali_type:
            subpad.addstr(i+2, 2, selecet_cali_ruler[i+2], color_pair_select | curses.A_BOLD)
        else:
            subpad.addstr(i+2, 2, selecet_cali_ruler[i+2], color_pair | curses.A_BOLD)

def display_selecet_cali_tip(subpad, color_pair):
    for i in range(len(cali_ruler_tip)):
        subpad.addstr(i, 2, cali_ruler_tip[i], color_pair)


def resize_window(pad):
    curses_utils.pad_ypos = 0
    curses_utils.pad_xpos = 0
    curses.update_lines_cols()
    # if curses.COLS < PAD_X - 20:
        # body_pad.refresh(2, curses.COLS-1-len(body[0]))
    # body_pad.erase() # ok
    curses_utils.pad_refresh(pad)
    sleep(0.5)

def main(stdscr):
    global current_servo, cali_type, is_save, legs_orignal_angles
    global leg_offset, head_offset, tail_offset
    global leg_angles, head_angles, tail_angles
    
    inc = 1  # 1 or -1, angle increase direction

    # ---------------- init stdscr ----------------
    # reset screen
    stdscr.clear()
    stdscr.move(0, 0)
    stdscr.refresh()

    # disable cursor 
    curses.curs_set(0)

    # set keyboard mode
    stdscr.nodelay(True) # set non-blocking mode for getch()
    stdscr.keypad(True)
    stdscr.timeout(50) # set timeout when no key is pressed

    # set colors
    curses.start_color()
    curses.use_default_colors()
    curses_utils.init_preset_color_pairs()

    # -------------------- init pad --------------------
    pad = curses.newpad(curses_utils.PAD_Y, curses_utils.PAD_X)
    # pad.box()

    # init subpad
    title_pad = pad.subpad(1, curses_utils.PAD_X, 0, 0)
    cali_ruler_pad = pad.subpad(len(selecet_cali_ruler), len(selecet_cali_ruler[0])+2+10, 2, 0)
    cali_ruler_tip_pad = pad.subpad(len(cali_ruler_tip), len(cali_ruler_tip[0])+2, 2, len(selecet_cali_ruler[0])+2+10+2)
    tip1_pad = pad.subpad(len(tip1), len(tip1[0]), 1, 0)
    tip2_pad = pad.subpad(len(tip2), len(tip2[0]), len(tip1)+2, 0)
    body_pad = pad.subpad(len(body), len(body[0]), 2, curses_utils.PAD_X-len(body[0])-20)
    if curses.COLS < curses_utils.PAD_X - 20:
        body_pad.move(2, 1)
    tip3_pad = pad.subpad(len(tip3), curses_utils.PAD_X, len(body)+3, 0)
    servo_num_pad = pad.subpad(1, curses_utils.PAD_X, len(body)+5, 0)
    offsets_pad = pad.subpad(3, curses_utils.PAD_X, len(body)+6, 0)

    # ------- select calibration ruler interface -------
    display_title(title_pad, curses_utils.CYAN | curses.A_REVERSE)
    display_selecet_cali_ruler(cali_ruler_pad, curses_utils.WHITE, curses_utils.CYAN | curses.A_REVERSE)
    display_selecet_cali_tip(cali_ruler_tip_pad, curses_utils.WHITE)
    curses_utils.pad_refresh(pad)

    # select the calibration ruler type
    while True:
        try:
            key = stdscr.getch()
            if key == curses.ERR: # if no key
                continue
            # ---- resize window ----
            if key == curses.KEY_RESIZE:
                resize_window(pad)
            # ---- select calibration type ----
            elif key == curses.KEY_UP:
                cali_type += 1
                if cali_type > MAX_CALI_TYPE - 1:
                    cali_type = 0
                display_selecet_cali_ruler(cali_ruler_pad, curses_utils.WHITE, curses_utils.CYAN | curses.A_REVERSE)
                curses_utils.pad_refresh(pad)
            elif key == curses.KEY_DOWN:
                cali_type -= 1
                if cali_type < 0:
                    cali_type = MAX_CALI_TYPE - 1
                display_selecet_cali_ruler(cali_ruler_pad, curses_utils.WHITE, curses_utils.CYAN | curses.A_REVERSE)
                curses_utils.pad_refresh(pad)
            elif key in (curses.KEY_ENTER, 10, 13):
                # 90 degree calibration ruler
                if cali_type == 0: 
                    legs_orignal_angles = list.copy(LEGS_ORIGNAL_ANGLES_90)
                    leg_angles = list.copy(LEGS_ORIGNAL_ANGLES_90)
                # 60 degree calibration ruler
                elif cali_type == 1:
                    #
                    legs_orignal_angles = list.copy(LEGS_ORIGNAL_ANGLES_60)
                    leg_angles = list.copy(LEGS_ORIGNAL_ANGLES_60)

                # ----------------
                for i in range(len(leg_angles)):
                    leg_angles[i] += leg_offset[i]
                #
                for i in range(len(head_angles)):
                    head_angles[i] += head_offset[i]
                #
                for i in range(len(tail_angle)):
                    tail_angle[i] += tail_offset[i]
                #
                my_dog.legs_move([legs_orignal_angles], immediately=True, speed=60)
                my_dog.head_move([[0]*3], immediately=True, speed=60)
                my_dog.tail_move([[0]], immediately=True, speed=60)
                my_dog.wait_all_done()
                break
        except KeyboardInterrupt:
            quit()

    # ---------------- calibration interface ----------------
    pad.clear()

    # get the offset

    display_title(title_pad, curses_utils.CYAN | curses.A_REVERSE)
    display_tip1(tip1_pad, curses_utils.WHITE)
    display_tip2(tip2_pad, curses_utils.WHITE)
    display_dog_body(body_pad, curses_utils.WHITE, curses_utils.CYAN)
    display_tip3(tip3_pad, curses_utils.WHITE)
    display_servo_num(servo_num_pad, curses_utils.WHITE, curses_utils.CYAN)
    display_offsets(offsets_pad, curses_utils.WHITE, curses_utils.CYAN)
    curses_utils.pad_refresh(pad)

    while True:
        try:
            key = stdscr.getch()
            if key == curses.ERR: # if no key
                continue
            # ---- resize window ----
            if key == curses.KEY_RESIZE:
                curses_utils.pad_ypos = 0
                curses_utils.pad_xpos = 0
                curses.update_lines_cols()
                # if curses.COLS < PAD_X - 20:
                    # body_pad.refresh(2, curses.COLS-1-len(body[0]))
                # body_pad.erase() # ok
                curses_utils.pad_refresh(pad)
                sleep(0.5)
            # ---- select the servo ----
            elif chr(key) in ('1234567890-='):
                current_servo = chr(key)
                display_dog_body(body_pad, curses_utils.WHITE, curses_utils.CYAN)
                display_servo_num(servo_num_pad, curses_utils.WHITE, curses_utils.CYAN)
                display_offsets(offsets_pad, curses_utils.WHITE, curses_utils.CYAN)
                curses_utils.clear_line(pad, 17)
                curses_utils.pad_refresh(pad)
            # ---- move ----
            elif chr(key) in ('wsadWSAD'):
                if chr(key) in ('wWdD'):
                    inc = 1
                else:
                    inc = -1
                # control legs
                if current_servo in ('12345678'):
                    # get index
                    index = ('12345678').index(current_servo)
                    # 
                    leg_offset[index] += inc*OFFSET_STEP
                    leg_offset[index] = constrain(leg_offset[index], -20, 20)
                    #
                    leg_angles[index] = legs_orignal_angles[index] + leg_offset[index]
                    # move servos
                    my_dog.legs.servo_write_raw(leg_angles)
                # control head
                elif current_servo in ('90-'):
                    index = ('90-').index(current_servo)
                    #
                    head_offset[index] += inc*OFFSET_STEP
                    head_offset[index] = constrain(head_offset[index], -20, 20)
                    #
                    head_angles[index] = head_orignal_angles[index] + head_offset[index]
                    #
                    my_dog.head.servo_write_raw(head_angles)
                # control tail
                elif current_servo == '=':
                    tail_offset[0] += inc*OFFSET_STEP
                    tail_offset[0] = constrain(tail_offset[0], -20, 20)
                    #
                    tail_angle[0] = tail_orignal_angles[0] + tail_offset[0]
                    #
                    my_dog.tail.servo_write_raw(tail_angle)
                # display offsets 
                display_offsets(offsets_pad, curses_utils.WHITE, curses_utils.CYAN)
                curses_utils.clear_line(pad, 17)
                curses_utils.pad_refresh(pad)
            # ---- save calibration ----
            elif key == 32: # space key
                curses_utils.clear_line(pad, 17)
                pad.addstr(17, 0, ' Confirm save ? (y/n)  ', curses_utils.CYAN | curses.A_REVERSE)
                curses_utils.pad_refresh(pad)
                while True:
                    key = stdscr.getch()
                    if key == curses.ERR:
                        continue
                    if chr(key) in ('yY'):
                        my_dog.set_leg_offsets(leg_offset, reset_list=legs_orignal_angles)
                        my_dog.set_head_offsets(head_offset)
                        my_dog.set_tail_offset(tail_offset)
                        sleep(0.5)
                        display_offsets(offsets_pad, curses_utils.WHITE, curses_utils.CYAN)
                        curses_utils.clear_line(pad, 17)
                        pad.addstr(17, 0, ' Offsets saved.  ', curses_utils.CYAN | curses.A_REVERSE)
                        curses_utils.pad_refresh(pad)
                        is_save = True
                        break
                    elif chr(key) in ('nN'):
                        display_offsets(offsets_pad, curses_utils.WHITE, curses_utils.CYAN)
                        curses_utils.clear_line(pad, 17)
                        curses_utils.pad_refresh(pad)
                        break
            else:
                pad.addstr(17, 0, ' Invalid Key  ', curses_utils.YELLOW | curses.A_REVERSE)
                curses_utils.pad_refresh(pad)

        except KeyboardInterrupt:
            # ---- exit and remind to save calibration ----
            if is_save:
                break
            else:
                pad.addstr(17, 0, ' Change not saved, whether to exit? (y/n)  ', curses_utils.WHITE | curses.A_BOLD |curses.A_REVERSE)
                curses_utils.pad_refresh(pad)
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
                    curses_utils.clear_line(pad, 17)
                    curses_utils.pad_refresh(pad)
                    continue

if __name__ == '__main__':
    curses.wrapper(main)

    # try:
    #     curses.wrapper(main)
    # # except Exception as e:
    #     # print(f"\033[31mERROR: {e}\033[m")
    # finally:
    #     my_dog.close()
