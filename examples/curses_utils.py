import curses
import time

# define pad size
# ======================================
PAD_Y = 40
PAD_X = 80

pad_ypos = 0
pad_xpos = 0

# define preset colors and color_pairs
# ======================================
# colors
white = [255, 255, 255]
blue = [59, 142, 234]
royal_blue = [65, 105, 225]
gray = [85, 85, 85]
light_gray = [200, 200, 200]
yellow = [255, 255, 0]

# color pairs
WHITE = None # curses.color_pair(11)
GRAY = None
LIGHT_GRAY = None
BLACK_BLUE = None
WHITE_BLUE = None
WHITE_GRAY = None
BLUE_GRAY = None
YELLOW_GRAY = None

def init_color(color_num, color):
    # The color value of curses is 0 to 1000
    r = int(color[0]/255*1000)
    g = int(color[1]/255*1000)
    b = int(color[2]/255*1000)
    curses.init_color(color_num, r, g, b)

def init_preset_colors():
    init_color(20, white)
    init_color(21, blue)
    init_color(22, royal_blue)
    init_color(23, gray)
    init_color(24, light_gray)
    init_color(25, yellow)

def init_preset__color_pairs():
    global WHITE, BLUE, GRAY, LIGHT_GRAY, BLACK_BLUE, WHITE_BLUE, WHITE_GRAY, BLUE_GRAY, YELLOW_GRAY
    # color_pairs
    curses.init_pair(11, 20, -1) # num, front color, background color (-1 means black)
    WHITE = curses.color_pair(11)

    curses.init_pair(12, 21, -1)
    BLUE = curses.color_pair(12)

    curses.init_pair(13, 23, -1)
    GRAY = curses.color_pair(13)

    curses.init_pair(14, 24, -1)
    LIGHT_GRAY = curses.color_pair(14)

    curses.init_pair(15, -1, 21)
    BLACK_BLUE = curses.color_pair(15)

    curses.init_pair(16, 20, 22)
    WHITE_BLUE = curses.color_pair(16)

    curses.init_pair(17, 20, 23)
    WHITE_GRAY = curses.color_pair(17)

    curses.init_pair(18, 21, 23)
    BLUE_GRAY = curses.color_pair(18)

    curses.init_pair(19, 25, 23)
    YELLOW_GRAY = curses.color_pair(19)

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
    y_2 = y+h
    x_2 = x+w
    if y_2 > curses.LINES-1:
        y_2 = curses.LINES-1
    if x_2 > curses.COLS-1:
        x_2 = curses.COLS-1
    pad.refresh(0, 0, y, x, y_2, x_2)

def clear_line(pad, line, xlen=None, color=None):
    if xlen is None:
        xlen = PAD_X
    if color is None:
        pad.addstr(line, 0, " "*(xlen-2))
    else:
        pad.addstr(line, 0, " "*(xlen-1), color)


def main(stdscr):
    global PAD_X, PAD_Y
    PAD_X = 80
    PAD_Y = 20

    # reset screen
    stdscr.clear()
    stdscr.move(0, 0)
    stdscr.refresh()   
    
    # disable cursor 
    curses.curs_set(0)

    # init colors
    curses.start_color()
    curses.use_default_colors()
    init_preset_colors()
    init_preset__color_pairs()
    # white = [255, 255, 25]
    # r = int(white[0]/255*1000)
    # g = int(white[1]/255*1000)
    # b = int(white[2]/255*1000)
    # curses.init_color(20, r, g, b)
    # curses.init_pair(11, 20, -1)
    # WHITE = curses.color_pair(11)

    # init pad    
    pad = curses.newpad(PAD_Y, PAD_X)

    # init subpad
    subpad_1 = pad.subpad(3, PAD_X, 0, 0)  # height, width, y, x
    subpad_2 = pad.subpad(3, PAD_X, 3, 0)
    subpad_3 = pad.subpad(3, PAD_X, 6, 0)

    # add content tp subpad_1
    subpad_1.addstr(0, 0, "WHITE", WHITE)
    subpad_1.addstr(1, 0, "BLUE", BLUE)
    subpad_1.addstr(2, 0, "GRAY", GRAY)
    pad_refresh(subpad_1)

    # add content tp subpad_2
    subpad_2.addstr(0, 0, "BLACK_BLUE", BLACK_BLUE)
    subpad_2.addstr(0, 20, "BLACK_BLUE_REVERSE", BLACK_BLUE | curses.A_REVERSE)
    subpad_2.addstr(1, 0, "WHITE_BLUE", WHITE_BLUE)
    subpad_2.addstr(1, 20, "WHITE_BLUE_REVERSE", WHITE_BLUE | curses.A_REVERSE)
    subpad_2.addstr(2, 0, "WHITE_GRAY", WHITE_GRAY)
    subpad_2.addstr(2, 20, "WHITE_GARY_REVERSE", WHITE_GRAY | curses.A_REVERSE)
    pad_refresh(subpad_2)

    # add content tp subpad_2
    clear_line(subpad_3, 0, color=BLACK_BLUE)
    clear_line(subpad_3, 1, color=WHITE_BLUE)
    clear_line(subpad_3, 2, color=WHITE_GRAY)
    subpad_3.addstr(0, 0, "BLACK_BLUE", BLACK_BLUE)
    subpad_3.addstr(1, 0, "WHITE_BLUE", WHITE_BLUE)
    subpad_3.addstr(2, 0, "WHITE_GRAY", WHITE_GRAY)
    pad_refresh(subpad_3)

    # pad_refresh(pad)

    while True:
        time.sleep(10)

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
