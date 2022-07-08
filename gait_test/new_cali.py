from awesome_print import AwesomePrint
import readchar
from pidog import Pidog

dog = Pidog(feet_pins=[1, 2, 3, 4, 5, 6, 7, 8],
    head_pins=[9, 10, 11], tail_pin=[12],
    )
# dog.feet.set_offset([0,0,0,0,0,0,0,0])

ap = AwesomePrint()
# ┌─┐│┼│└─┘
DOG_POSITION_X = 10
DOG_POSITION_Y = 4
CALIBRATE_STEP = 0.1
original_coords = [[0, 87], [0, 87], [0, 87], [0, 87]]
def main():
    selected_foot = 0
    foot_coords = [[0, 87], [0, 87], [0, 87], [0, 87]]
    leg_options = [[], [], [], []]
    while True:
        ap.clear()
        ap.hide_cursor()
        ap.print("                           PiDog Calibration                           ", options=["bg_grey"])
        ap.print(" ┌─┐",  [DOG_POSITION_Y, DOG_POSITION_X])
        ap.print(" │ │",  [DOG_POSITION_Y+1, DOG_POSITION_X])
        ap.print("┌└─┘┐", [DOG_POSITION_Y+2, DOG_POSITION_X])
        ap.print("|   |", [DOG_POSITION_Y+3, DOG_POSITION_X])
        ap.print("|   |", [DOG_POSITION_Y+4, DOG_POSITION_X])
        ap.print("|   |", [DOG_POSITION_Y+5, DOG_POSITION_X])
        ap.print("└───┘", [DOG_POSITION_Y+6, DOG_POSITION_X])
        ap.print("  /",   [DOG_POSITION_Y+7, DOG_POSITION_X])
        ap.print(" /",    [DOG_POSITION_Y+8, DOG_POSITION_X])
        ap.print("[1]===", [DOG_POSITION_Y+3, DOG_POSITION_X-6], options=leg_options[0])
        ap.print("===[2]", [DOG_POSITION_Y+3, DOG_POSITION_X+5], options=leg_options[1])
        ap.print("[3]===", [DOG_POSITION_Y+6, DOG_POSITION_X-6], options=leg_options[2])
        ap.print("===[4]", [DOG_POSITION_Y+6, DOG_POSITION_X+5], options=leg_options[3])

        ap.print("[1],[2],[3],[4] selecte the foot to calibrate", [5, 25])
        ap.print("[Q] Quit the program", [6, 25])
        ap.print("  [W]", [7, 25])
        ap.print("[A][S][D]    Move the current foot.", [8, 25])
        ap.print(f"Offset: {dog.feet.offset}", [9, 25])

        dog.set_feet(foot_coords)
        angles = dog.pose2feet_angle()
        dog.feet_simple_move(angles)

        key = readchar.readkey()
        if key == "q":
            break
        elif key == "1":
            selected_foot = 0
        elif key == "2":
            selected_foot = 1
        elif key == "3":
            selected_foot = 2
        elif key == "4":
            selected_foot = 3
        elif key == "w":
            foot_coords[selected_foot][1] -= CALIBRATE_STEP
        elif key == "s":
            foot_coords[selected_foot][1] += CALIBRATE_STEP
        elif key == "a":
            foot_coords[selected_foot][0] -= CALIBRATE_STEP
        elif key == "d":
            foot_coords[selected_foot][0] += CALIBRATE_STEP

        leg_options = [[],[],[],[]]
        leg_options[selected_foot] = ["bg_light_blue"]

    ap.print(f"Original coords: {original_coords}", [15, 1])
    ap.print(f"Current coords: {foot_coords}")
    offsets = []
    original_angles = []
    current_angles = []
    positive_list = [-1, 1, -1, 1]
    for i in range(4):
        original_angle = dog.coord2polar(original_coords[i])
        current_angle = dog.coord2polar(foot_coords[i])
        original_angles.append(original_angle)
        current_angles.append(current_angle)
        leg_angle  = (original_angle[0] - current_angle[0]) * positive_list[i] + dog.feet.offset[i*2]
        foot_angle = (original_angle[1] - current_angle[1]) * positive_list[i] + dog.feet.offset[i*2+1]
        offsets += [leg_angle, foot_angle]
    ap.print(f"Original angles: {original_angles}")
    ap.print(f"Current angles: {current_angles}")
    ap.print(f"Angle offset: {offsets}")
    yn = input(f"Do you want to save the offset values? (y/N) ")
    if yn == "y":
        dog.feet.set_offset(offsets)
        ap.print(f"Saved!")
    else:
        ap.print(f"Canceled!")
    dog.close_all_thread()
    quit()

if __name__ == "__main__":
    try:
        main()
    finally:
        ap.show_cursor()
