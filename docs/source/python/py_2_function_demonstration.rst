2. 功能演示
===============================

本项目将展示 PiDog 所有常用的动作和声音效果。

您可以通过输入对应的编号，让 PiDog 执行动作或播放声音。

以下是本示例当前支持的动作与声音效果列表：

.. image:: img/py_2.gif

.. list-table:: 
    :widths: 25 25
    :header-rows: 1

    * - 动作（Actions）: 
      - 音效（Sound Effect）: 
    * - 1. stand（站立）
      - 16. angry（生气）
    * - 2. sit（坐下）
      - 17. confused_1（困惑1）  
    * - 3. lie（趴下）
      - 18. confused_2（困惑2）
    * - 4. lie_with_hands_out（四脚趴）
      - 19. confused_3（困惑3） 
    * - 5. trot（小跑）
      - 20. growl_1（低吼1） 
    * - 6. forward（前进）
      - 21. growl_2（低吼2） 
    * - 7. backward（后退）
      - 22. howling（嚎叫） 
    * - 8. turn_left（左转）
      - 23. pant（喘气） 
    * - 9. turn_right（右转）
      - 24. single_bark_1（叫声1） 
    * - 10. doze_off（打瞌睡）
      - 25. single_bark_2（叫声2） 
    * - 11. stretch（伸展）
      - 26. snoring（打鼾） 
    * - 12. pushup（俯卧撑）
      - 27. woohoo（欢呼） 
    * - 13. shake_head（摇头）
      - 
    * - 14. tilting_head（歪头）
      - 
    * - 15. wag_tail（摇尾巴）    
      - 



**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 2_function_demonstration.py

运行此示例后，输入 ``1`` 并按 ``ENTER``，PiDog 将站立；输入 ``2``，PiDog 将坐下；输入 ``27``，PiDog 会发出 “woohoo~” 的欢呼声。

按下 ``Ctrl+C`` 可退出程序。



**代码**

.. note::
    您可以对以下代码进行 **修改 / 重置 / 复制 / 运行 / 停止**。但在此之前，请先切换到源码路径，例如 ``pidog\examples``。修改后可直接运行查看效果。

.. raw:: html

    <run></run>

.. code-block:: python 

    #!/usr/bin/env python3
    from time import sleep
    from pidog import Pidog
    import os
    import curses
    import curses_utils

    # 初始化 PiDog
    # ======================================
    my_dog = Pidog()
    sleep(0.5)

    # 全局变量
    # ======================================
    actions = [
        # 名称, 头部俯仰调整（-1 表示使用上一次值）, 动作速度
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
    # 更改当前工作目录
    abspath = os.path.abspath(os.path.dirname(__file__))
    # print(abspath)
    os.chdir(abspath)
    for name in os.listdir('../sounds'):
        sound_effects.append(name.split('.')[0])
    sound_effects.sort()
    sound_len = len(sound_effects)
    # 限制声音数量
    if sound_len > actions_len:
        sound_len = actions_len
        sound_effects = sound_effects[:actions_len]

    last_index = 0
    last_display_index = 0
    exit_flag = False
    last_head_pitch = 0

    STANDUP_ACTIONS = ['trot', 'forward', 'backward', 'turn_left', 'turn_right']

    # 设置界面尺寸
    # ======================================
    curses_utils.PAD_Y = 22
    curses_utils.PAD_X = 70

    # 显示相关函数
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
        # 清除上一次高亮
        if last_display_index > actions_len + sound_len-1 or last_display_index < 0:
            last_display_index = 0
        if last_display_index != index:
            if last_display_index < actions_len:
                subpad.addstr(last_display_index, 2, f"{last_display_index+1}. {actions[last_display_index][0]}", curses_utils.LIGHT_GRAY)
            else:
                sound_index = last_display_index-actions_len
                subpad.addstr(sound_index, 30, f"{last_display_index+1}. {sound_effects[sound_index]}", curses_utils.LIGHT_GRAY)
            last_display_index = index
        # 高亮当前选择
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
            # 若上一个动作是 push_up，先执行 lie
            if last_index < len(actions) and actions[last_index][0] in ('push_up'):
                last_head_pitch = 0
                my_dog.do_action('lie', speed=60)
            # 若当前为站立类动作且上一个不是，则先站立
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
        # 初始化界面
        stdscr.clear()
        stdscr.move(4, 0)
        stdscr.refresh()

        # 禁用光标
        curses.curs_set(0)

        # 初始化颜色
        curses.start_color()
        curses.use_default_colors()
        curses_utils.init_preset_colors()
        curses_utils.init_preset__color_pairs()

        # 初始化 pad    
        pad = curses.newpad(curses_utils.PAD_Y, curses_utils.PAD_X)   

        # 初始化子区域
        head_pad = pad.subpad(4, curses_utils.PAD_X, 0, 0)
        selection_pad = pad.subpad(actions_len, curses_utils.PAD_X, 4, 0)
        bottom_pad = pad.subpad(1, curses_utils.PAD_X, actions_len+4, 0)
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

