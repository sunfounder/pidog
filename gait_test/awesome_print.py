import os

class AwesomePrint:
    OPTIONS = {
        "black"     : '\033[30m',
        "red"       : '\033[31m',
        "green"     : '\033[32m',
        "yellow"    : '\033[33m',
        "blue"      : '\033[34m',
        "megenta"   : '\033[35m',
        "cyan"      : '\033[36m',
        "white"     : '\033[37m',
        "bg_black"  : '\033[40m',
        "bg_red"    : '\033[41m',
        "bg_green"  : '\033[42m',
        "bg_yellow" : '\033[43m',
        "bg_blue"   : '\033[44m',
        "bg_purple" : '\033[45m',
        "bg_cyan"   : '\033[46m',
        "bg_white"  : '\033[47m',
        "grey"            : '\033[90m',
        "light_red"       : '\033[91m',
        "light_green"     : '\033[92m',
        "light_yellow"    : '\033[93m',
        "light_blue"      : '\033[94m',
        "light_megenta"   : '\033[95m',
        "light_cyan"      : '\033[96m',
        "white"           : '\033[97m',
        "bg_grey"         : '\033[100m',
        "bg_light_red"    : '\033[101m',
        "bg_light_green"  : '\033[102m',
        "bg_light_yellow" : '\033[103m',
        "bg_light_blue"   : '\033[104m',
        "bg_light_purple" : '\033[105m',
        "bg_light_cyan"   : '\033[106m',
        "bg_light_white"  : '\033[107m',
        "bold"      : '\033[1m',
        "italic"    : '\033[3m',
        "underline" : '\033[4m',
    }
    END = '\033[0m'

    def __init__(self):
        pass

    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def fill(self, color):
        """
        Fill the whole screen with a color.
        color: the color to fill
        """
        if not color.startswith("bg_"):
            color = f"bg_{color}"
        size = os.get_terminal_size()
        for _ in range(size.lines):
            print(f"{self.OPTIONS[color]}{' '*size.columns}{self.END}")

    def print(self, msg, coord=None, options=None):
        """
        Print a message with coord and options.
        msg: the message to print
        coord: the coord of the message, starts from 1, negative means from the end
        options: the options of the message, a list of strings
        """
        if options == None:
            options = []
        coord_str = ""
        if coord != None:
            coord_str = f"\033[{coord[0]};{coord[1]}H"
        options_str = "".join([self.OPTIONS[option] for option in options])
        # size = os.get_terminal_size()
        print(f"{coord_str}{options_str}{msg}{self.END}")

    def hide_cursor(self):
        print("\033[?25l")
    def show_cursor(self):
        print("\033[?25h")

    def progress(self, now, total, coord=None,length=80, bg_color="black", fg_color="green", mode="percent"):
        """
        Print a progress bar.
        total: the total number of the progress
        now: the current number of the progress
        length: the length of the progress bar
        """
        if not bg_color.startswith("bg_"):
            bg_color = f"bg_{bg_color}"
        if not fg_color.startswith("bg_"):
            fg_color = f"bg_{fg_color}"
        value = int(now/total * length)
        left = length - value
        progress_fg_str = " " * value
        progress_bg_str = " " * left
        coord_str = ""
        if coord != None:
            coord_str = f"\033[{coord[0]};{coord[1]}H"
        progress_str = f"{self.OPTIONS[fg_color]}{progress_fg_str}{self.OPTIONS[bg_color]}{progress_bg_str}{self.END}"
        if mode == "percent":
            progress_value_str = f"{int(now/total*100)}%"
        elif mode == "number":
            progress_value_str = f"{now}/{total}"
        print(f"{coord_str}|{progress_str}| {progress_value_str}{self.END}")


def test():
    import time

    ap = AwesomePrint()
    ap.clear()
    ap.fill("black")
    ap.hide_cursor()
    ap.print("This is a black text.", [1, 1], ["black"])
    ap.print("This is a red text.", [2, 1], ["red"])
    ap.print("This is a green text.", [3, 1], ["green"])
    ap.print("This is a yellow text.", [4, 1], ["yellow"])
    ap.print("This is a blue text.", [5, 1], ["blue"])
    ap.print("This is a megenta text.", [6, 1], ["megenta"])
    ap.print("This is a cyan text.", [7, 1], ["cyan"])
    ap.print("This is a white text.", [8, 1], ["white"])
    ap.print("This is a bg_black text.", [1, 40], ["bg_black"])
    ap.print("This is a bg_red text.", [2, 40], ["bg_red"])
    ap.print("This is a bg_green text.", [3, 40], ["bg_green"])
    ap.print("This is a bg_yellow text.", [4, 40], ["bg_yellow"])
    ap.print("This is a bg_blue text.", [5, 40], ["bg_blue"])
    ap.print("This is a bg_purple text.", [6, 40], ["bg_purple"])
    ap.print("This is a bg_cyan text.", [7, 40], ["bg_cyan"])
    ap.print("This is a bg_white text.", [8, 40], ["bg_white"])

    ap.print("This is a bold and cyan text.", [9, 1], ["bold", "cyan"])
    ap.print("This is a italic and bg_yellow text.", [10, 1], ["italic", "bg_yellow"])
    ap.print("This is a underline and green text.", [11, 1], ["underline", "green"])
    ap.print("Background color and front color cannot mix", [12, 1], ["bg_red", "green"])

    total = 1052

    for i in range(1, total + 1):
        ap.progress(i, total, [13, 4])
        ap.progress(i, total, [14, 4], fg_color="red", bg_color="blue", mode="number")
        time.sleep(0.01)

if __name__ == "__main__":
    test()
