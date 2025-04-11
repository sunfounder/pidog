
4. 互动反馈
================

在本项目中，PiDog 将以有趣的方式与你进行互动。

当你从正前方伸手摸它的头时，它会警觉地吠叫。


.. image:: img/py_4-2.gif
    :width: 430


但如果你从后方轻抚它的头顶，它则会露出享受的神情。

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/touch_head.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 4_response.py

运行此示例后，PiDog 的超声波模块会检测前方是否有障碍物，
当检测到你的手靠近时，它会点亮红色呼吸灯，后退一步并发出吠叫声。

同时，触摸传感器也会开始工作。如果你轻抚（而非轻触）其头部，
PiDog 会摇头、摇尾巴，展现出一副非常享受的样子。




**代码**

.. note::
    您可以对以下代码进行 **修改/重置/复制/运行/停止**。但请确保已进入代码路径（如 ``pidog\examples``）后再进行操作。修改后可直接运行查看效果。

.. raw:: html

    <run></run>

.. code-block:: python


    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from math import sin
    from preset_actions import bark_action

    my_dog = Pidog()
    sleep(0.1)

    def lean_forward():
        my_dog.speak('angry', volume=80)
        bark_action(my_dog)
        sleep(0.2)
        bark_action(my_dog)
        sleep(0.8)
        bark_action(my_dog)

    def head_nod(step):
        y = 0
        r = 0
        p = 30
        angs = []
        for i in range(20):
            r = round(10*sin(i*0.314), 2)
            p = round(20*sin(i*0.314) + 10, 2)
            angs.append([y, r, p])

        my_dog.head_move(angs*step, immediately=False, speed=80)

    def alert():
        my_dog.do_action('stand', step_count=1, speed=90)
        my_dog.rgb_strip.set_mode('breath', color='pink', bps=1, brightness=0.8)
        while True:
            print(
                f'distance.value: {round(my_dog.ultrasonic.read_distance(), 2)} cm, touch {my_dog.dual_touch.read()}')
            # 警觉状态
            if my_dog.ultrasonic.read_distance() < 15 and my_dog.ultrasonic.read_distance() > 1:
                my_dog.head_move([[0, 0, 0]], immediately=True, speed=90)
                my_dog.tail_move([[0]], immediately=True, speed=90)
                my_dog.rgb_strip.set_mode('bark', color='red', bps=2, brightness=0.8)
                my_dog.do_action('backward', step_count=1, speed=98)
                my_dog.wait_all_done()
                lean_forward()
                while len(my_dog.legs_action_buffer) > 0:
                    sleep(0.1)
                my_dog.do_action('stand', step_count=1, speed=90)
                sleep(0.5)
            # 放松状态
            if my_dog.dual_touch.read() != 'N':
                if len(my_dog.head_action_buffer) < 2:
                    head_nod(1)
                    my_dog.do_action('wag_tail', step_count=10, speed=80)
                    my_dog.rgb_strip.set_mode('listen', color="#8A2BE2", bps=0.35, brightness=0.8)
            # 平静状态
            else:
                my_dog.rgb_strip.set_mode('breath', color='pink', bps=1, brightness=0.8)
                my_dog.tail_stop()
            sleep(0.2)

    if __name__ == "__main__":
        try:
            alert()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()
