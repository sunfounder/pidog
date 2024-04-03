import curses
import time
import os

# os.environ['TERM'] = 'xterm-256color'
is_256color = False
if os.environ['TERM'] == 'xterm-256color':
    is_256color = True
else:
    is_256color = False

# define pad size
# ======================================
PAD_Y = 40
PAD_X = 80

pad_ypos = 0
pad_xpos = 0

# define preset colors and color_pairs
# ======================================
# color pairs
BLACK = None
BLUE = None
CYAN = None
GREEN = None
MAGENTA = None
RED = None
WHITE = None
YELLOW = None
WHITE_BLUE = None

def init_preset_color_pairs():
    global BLACK, BLUE, CYAN, GREEN, MAGENTA, RED, WHITE, YELLOW, WHITE_BLUE

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    BLACK = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    BLUE = curses.color_pair(2)

    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    CYAN = curses.color_pair(3)
   
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN = curses.color_pair(4)

    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    MAGENTA = curses.color_pair(5)

    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)
    RED = curses.color_pair(6)

    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
    WHITE = curses.color_pair(7)

    curses.init_pair(8, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    YELLOW = curses.color_pair(8)

    curses.init_pair(9, curses.COLOR_WHITE, curses.COLOR_BLUE)
    WHITE_BLUE = curses.color_pair(9)

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

def clear_line(pad, line, xlen=None, color_pair=None):
    if xlen is None:
        xlen = PAD_X
    if color_pair is None:
        pad.addstr(line, 0, " "*(xlen-2))
    else:
        # pad.addstr(line, 0, " "*(xlen-1), BLUE|curses.A_REVERSE)
        pad.addstr(line, 0, " "*(xlen-1), color_pair)

# test
# ======================================
def test(screen):
    screen.clear()
    screen.refresh()
    save_colors = [curses.color_content(i) for i in range(curses.COLORS)]
    curses.curs_set(0)
    curses.start_color()

    print(BLACK, WHITE, YELLOW)
    init_preset_color_pairs()
    print(BLACK, WHITE, YELLOW)
    
    color_pairs = {
    'BLACK': [1, BLACK],
    'BLUE': [2, BLUE],
    'CYAN': [3, CYAN],
    'GREEN': [4, GREEN],
    'MAGENTA': [5, MAGENTA],
    'RED': [6, RED],
    'WHITE': [7, WHITE],
    'YELLOW': [8, YELLOW],
    'WHITE_BLUE': [9, WHITE_BLUE],
    }

    i = 2
    for color_name, value in color_pairs.items():
        index, color_pair = value
        screen.addstr(i, 0, f'{color_name}', color_pair)
        screen.addstr(i, 20, f'{color_name} A_REVERSE', color_pair | curses.A_REVERSE)
        screen.addstr(i, 40, f'{color_name} A_DIM', color_pair | curses.A_DIM)
        screen.addstr(i, 60, f'{color_name} A_BOLD', color_pair | curses.A_BOLD)
        i += 1

    screen.getch()

if __name__ == "__main__":
    try:
        curses.wrapper(test)
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
