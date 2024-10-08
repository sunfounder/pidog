.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_wake_up:

2. Démonstration des fonctionnalités
==========================================

Ce projet présente toutes les actions habituelles et les sons de PiDog.

Vous pouvez faire en sorte que PiDog exécute des mouvements ou émette des sons en entrant le numéro correspondant.

Les mouvements et effets sonores actuellement inclus dans cet exemple sont listés ci-dessous.

.. image:: img/py_2.gif

.. list-table:: 
    :widths: 25 25
    :header-rows: 1

    * - Mouvements : 
      - Effets sonores : 
    * - 1.debout
      - 16.colère
    * - 2.assis
      - 17.confus_1  
    * - 3.couché
      - 18.confus_2
    * - 4.couché avec pattes étendues 
      - 19.confus_3 
    * - 5.trotter
      - 20.grogner_1 
    * - 6.avancer
      - 21.grogner_2 
    * - 7.reculer
      - 22.hurler 
    * - 8.tourner à gauche
      - 23.haletement 
    * - 9.tourner à droite
      - 24.aboiement_simple_1 
    * - 10.somnoler
      - 25.aboiement_simple_2 
    * - 11.s'étirer
      - 26.ronflement 
    * - 12.pompes
      - 27.woohoo 
    * - 13.secouer la tête
      -
    * - 14.incliner la tête
      -
    * - 15.remuer la queue    
      -



**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 2_function_demonstration.py

Après avoir exécuté cet exemple, si vous entrez ``1`` et appuyez sur ``ENTER``, PiDog se mettra debout ; entrez ``2``, PiDog s'assiéra ; entrez ``27``, PiDog émettra un "woohoo~ ".

Appuyez sur ``Ctrl+C`` pour quitter le programme.



**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Avant cela, vous devez vous rendre dans le répertoire source comme ``pidog\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir le résultat.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from time import sleep
    from pidog import Pidog
    import os
    import curses
    import curses_utils

    # Initialisation de PiDog
    # ======================================
    my_dog = Pidog()
    sleep(0.5)

    # Variables globales
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
    # Changer de répertoire de travail
    abspath = os.path.abspath(os.path.dirname(__file__))
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

    # Définir la taille du pad
    # ======================================
    curses_utils.PAD_Y = 22
    curses_utils.PAD_X = 70

    # Fonctions d'affichage
    # ======================================
    def display_head(subpad):
        title = "Function Demonstration"
        tip1 = "Input Function number to see how it goes."
        tip2 = "Actions will repeat 10 times."
        type_name_1 = "Actions:"
        type_name_2 = "Sound Effect:"
        tip3 = "(need to run with sudo)"

        curses_utils.clear_line(subpad, 0, color=curses_utils.BLACK_BLUE)
        subpad.addstr(0, 2, title, curses_utils.BLACK_BLUE | curses.A_BOLD)
        subpad.addstr(1, 2, tip1, curses_utils.GRAY)
        subpad.addstr(2, 2, tip2, curses_utils.GRAY)
        curses_utils.clear_line(subpad, 3, color=curses_utils.WHITE_GRAY)
        subpad.addstr(3, 2, type_name_1, curses_utils.WHITE_GRAY)
        subpad.addstr(3, 30, type_name_2, curses_utils.WHITE_GRAY)
        subpad.addstr(3, 31+len(type_name_2), tip3, curses_utils.YELLOW_GRAY)

    def display_selection(subpad, index):
        global last_display_index
        # reset last selection
        if last_display_index > actions_len + sound_len-1 or last_display_index < 0:
            last_display_index = 0
        if last_display_index != index:
            if last_display_index < actions_len:
                subpad.addstr(last_display_index, 2, f"{last_display_index+1}. {actions[last_display_index][0]}", curses_utils.LIGHT_GRAY)
            else:
                sound_index = last_display_index-actions_len
                subpad.addstr(sound_index, 30, f"{last_display_index+1}. {sound_effects[sound_index]}", curses_utils.LIGHT_GRAY)
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
            subpad.addstr(i, 2, f"{i+1}. {actions[i][0]}", curses_utils.LIGHT_GRAY)
        for i in range(sound_len):
            subpad.addstr(i, 30, f"{i+actions_len+1}. {sound_effects[i]}", curses_utils.LIGHT_GRAY)

    def display_bottom(subpad):
        curses_utils.clear_line(subpad, 0, color=curses_utils.WHITE_GRAY)
        subpad.addstr(0, 0, "Enter function number: ", curses_utils.WHITE_GRAY)
        subpad.addstr(0, curses_utils.PAD_X-16, "Ctrl^C to quit", curses_utils.WHITE_GRAY)


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
        curses_utils.init_preset_colors()
        curses_utils.init_preset__color_pairs()

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

        while True:
            # draw bottom bar
            display_bottom(bottom_pad)
            curses_utils.pad_refresh(bottom_pad)
            # reset cursor
            stdscr.move(actions_len+4, 23)
            stdscr.refresh()
            # red key
            key = stdscr.getstr()
            try:
                index = int(key) - 1
            except ValueError:
                index = -1
            # display selection
            display_selection(selection_pad, index)
            curses_utils.pad_refresh(selection_pad)
            # do fuction
            do_function(index)

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

