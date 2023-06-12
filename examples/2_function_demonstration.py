#!/usr/bin/env python3
from time import sleep
from pidog import Pidog
import os

# change working directory
abspath = os.path.abspath(os.path.dirname(__file__))
# print(abspath)
os.chdir(abspath)

my_dog = Pidog()
sleep(0.5)

actions = [
    # name, head_pitch_adjust, speed
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
    ['stretch', 30, 20],
    ['push_up', -30, 50],
    ['shake_head', 0, 90],
    ['tilting_head', 0, 60],
    ['wag_tail', 0, 100],
]

sound_effects = []
for name in os.listdir('../sounds'):
    sound_effects.append(name.split('.')[0])
sound_effects.sort()


index = None
last_index = 2
exit_flag = False

STANDUP_ACTIONS = ['trot', 'forward', 'backward', 'turn_left', 'turn_right']


def show_info():
    print("\033[H\033[J", end='')  # clear terminal windows
    print(
        "\033[104m\033[1m  Function Demonstration                            \033[0m")
    print("\033[90m  Input Function number to see how it goes.\n  Actions will repeat 10 times.\033[0m")
    print(
        "\033[100m\033[1m   Actions:                    Sound Effect:        \033[0m")
    first_line = 5
    last_line = 0
    for i, action in enumerate(actions):
        print(f'\033[{i+first_line};4H{i+1}. {action[0]}')
    last_line = i+first_line
    for i, sound_effect in enumerate(sound_effects):
        print(f'\033[{i+first_line};32H{i+len(actions)+1}. {sound_effect}')
    last_line = max(i+first_line, last_line) - 1
    print(
        f"\033[100m\033[1m\033[{last_line +2};0H   Ctrl+C: Quit                                     \033[0m")
    if index != None:
        print('Current selection: ', end="")
        if index < len(actions):
            print(f"{index+1}. {actions[index][0]}")
        elif index < len(actions) + len(sound_effects):
            print(f"{index+1}. {sound_effects[index-len(actions)]}")
            print("\033[033mNote that you need to run with \"sudo\", otherwise there may be no sound.\033[m")
        else:
            print('\033[033mOut of range\033[m')

def do_function(index):
    global last_index
    my_dog.body_stop()
    if index < len(actions):
        name, head_pitch_adjust, speed = actions[index]
        # If last action is push_up, then lie down first
        if last_index < len(actions) and actions[last_index][0] in ('push_up'):
            my_dog.do_action('lie', speed=60)
        # If this action is trot, forward, turn left, turn right and backward, and, last action is not, then stand up
        if name in STANDUP_ACTIONS and last_index < len(actions) and actions[last_index][0] not in STANDUP_ACTIONS:
            my_dog.do_action('stand', speed=60)
        my_dog.head_move_raw([[0, 0, head_pitch_adjust]],
                             immediately=True, speed=60)
        my_dog.do_action(name, step_count=10, speed=speed)
    elif index < len(actions) + len(sound_effects):
        my_dog.speak(sound_effects[index - len(actions)])
    last_index = index


def function_demonstration():
    global index
    global exit_flag

    show_info()

    while True:
        try:
            num = input("Enter function number\033[5m:\033[m")
            if int(num) > len(actions) + len(sound_effects):
                index = int(num) - 1
                show_info()
                continue
            index = int(num) - 1
            do_function(index)
            show_info()
        except ValueError:
            print('ValueError')
        sleep(0.05)


if __name__ == "__main__":
    try:
        function_demonstration()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        my_dog.close()