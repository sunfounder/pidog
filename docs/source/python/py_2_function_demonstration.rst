2. Function Demonstration
===============================

This project shows you all of PiDog's usual actions and sounds.

You can make PiDog make actions or make sounds by entering the serial number.

The motion/sound effects currently included in this example are listed below.

.. image:: img/py_2.gif

.. list-table:: 
    :widths: 25 25
    :header-rows: 1

    * - Actions: 
      - Sound Effect: 
    * - 1.stand
      - 16.angry
    * - 2.sit
      - 17.confused_1  
    * - 3.lie
      - 18.confused_2
    * - 4.lie_with_hands_out 
      - 19.confused_3 
    * - 5.trot
      - 20.growl_1 
    * - 6.forward
      - 21.growl_2 
    * - 7.backward
      - 22.howling 
    * - 8.turn_left
      - 23.pant 
    * - 9.turn_right
      - 24.single_bark_1 
    * - 10.doze_off
      - 25.single_bark_2 
    * - 11.stretch
      - 26.snoring 
    * - 12.pushup
      - 27.woohoo 
    * - 13.shake_head
      -
    * - 14.tilting_head
      -
    * - 15.wag_tail    
      -



**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 2_function_demonstration.py

After running this example, you input ``1`` and press ``ENTER``, PiDog will stand; input ``2``, PiDog will sit down; input ``27``, PiDog will issue "woohoo~ ".

Press ``Ctrl+C`` to exit the program.



**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``pidog\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python


    #!/usr/bin/env python3
    from time import sleep
    from pidog import Pidog
    import os

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
        ['pushup', -30, 50],
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
            else:
                print(f"{index+1}. {sound_effects[index-len(actions)]}")


    def do_function(index):
        global last_index
        my_dog.body_stop()
        if index < len(actions):
            name, head_pitch_adjust, speed = actions[index]
            # If last action is pushup, then lie down first
            if last_index < len(actions) and actions[last_index][0] in ('pushup'):
                my_dog.do_action('lie', wait=False, speed=60)
            # If this action is trot, forward, turn left, turn right and backward, and, last action is not, then stand up
            if name in STANDUP_ACTIONS and last_index < len(actions) and actions[last_index][0] not in STANDUP_ACTIONS:
                my_dog.do_action('stand', wait=False, speed=60)
            my_dog.head_move_raw([[0, 0, head_pitch_adjust]],
                                immediately=True, speed=60)
            my_dog.do_action(name, step_count=10, wait=False, speed=speed)
        elif index < len(actions) + len(sound_effects):
            my_dog.speak(sound_effects[index - len(actions)])
        last_index = index


    def function_demonstration():
        global index
        global exit_flag

        show_info()

        while True:
            try:
                num = input("Enter function number: ")
                if int(num) > len(actions) + len(sound_effects):
                    print('Out of range')
                    continue
                index = int(num) - 1
                do_function(index)
                show_info()
            except ValueError:
                print('ValueError')
            except KeyboardInterrupt:
                my_dog.close()
            sleep(0.05)


    if __name__ == "__main__":
        function_demonstration()
