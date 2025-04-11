5. 休息状态
================

在本项目中，PiDog 会趴在地上打盹，当它听到周围的声音时，会迷迷糊糊地站起来，看看是谁打扰了它的美梦。

.. image:: img/py_5.gif

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 5_rest.py

程序运行后，PiDog 会趴在地上，摇头摆尾，仿佛在打瞌睡。
此时，声音方向传感器模块开始工作。
如果 PiDog 听到响动，它会立刻站起来，环顾四周，露出一副迷惑的表情，
然后再次进入打盹状态。


**代码**

.. note::
    您可以对以下代码进行 **修改/重置/复制/运行/停止**。但请确保已进入源码路径（如 ``pidog\examples``）后操作。修改后可直接运行查看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import shake_head

    my_dog = Pidog()
    sleep(0.1)

    def loop_around(amplitude=60, interval=0.5, speed=100):
        my_dog.head_move([[amplitude,0,0]], immediately=True, speed=speed)
        my_dog.wait_all_done()
        sleep(interval)
        my_dog.head_move([[-amplitude,0,0]], immediately=True, speed=speed)
        my_dog.wait_all_done()
        sleep(interval)
        my_dog.head_move([[0,0,0]], immediately=True, speed=speed)
        my_dog.wait_all_done()

    def is_sound():
        if my_dog.ears.isdetected():
            direction = my_dog.ears.read()
            if direction != 0:
                return True
            else:
                return False
        else:
            return False

    def rest():
        my_dog.wait_all_done()
        my_dog.do_action('lie', speed=50)
        my_dog.wait_all_done()

        while True:
            # 进入睡眠状态
            my_dog.rgb_strip.set_mode('breath', 'pink', bps=0.3)
            my_dog.head_move([[0,0,-40]], immediately=True, speed=5)
            my_dog.do_action('doze_off', speed=92)
            # 清除之前的声音检测
            sleep(1)
            is_sound()

            # 持续休息，直到检测到声音
            while is_sound() is False:
                my_dog.do_action('doze_off', speed=92)
                sleep(0.2)

            # 听到声音后唤醒
            # Set light to yellow and stand up
            my_dog.rgb_strip.set_mode('boom', 'yellow', bps=1)
            my_dog.body_stop()
            my_dog.do_action('stand', speed=90)
            my_dog.head_move([[0, 0, 0]], immediately=True, speed=80)
            my_dog.wait_all_done()
            # 环顾四周
            loop_around(60, 1, 60)
            sleep(0.5)
            # 歪头迷惑
            my_dog.speak('confused_3', volume=80)
            my_dog.do_action('tilting_head_left', speed=80)
            my_dog.wait_all_done()
            sleep(1.2)
            my_dog.head_move([[0, 0, -10]], immediately=True, speed=80)
            my_dog.wait_all_done()
            sleep(0.4)
            # 摇头，表示不在意
            shake_head(my_dog)
            sleep(0.2)

            # 再次趴下休息
            my_dog.rgb_strip.set_mode('breath', 'pink', bps=1)
            my_dog.do_action('lie', speed=50)
            my_dog.wait_all_done()
            sleep(1)


    if __name__ == "__main__":
        try:
            rest()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()