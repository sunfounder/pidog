.. _py_wake_up: 

1. 唤醒
===============

这是 PiDog 的第一个项目，它将唤醒沉睡中的 PiDog。

.. image:: img/py_wakeup.gif


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

执行代码后，  
PiDog 将依次完成以下动作：

伸展、扭动身体、坐下、摇尾巴、喘气



**代码**

.. note::
    您可以对以下代码进行 **修改 / 重置 / 复制 / 运行 / 停止**。但在此之前，请先切换到源码路径，例如 ``pidog\examples``。修改代码后可直接运行以查看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import pant
    from preset_actions import body_twisting

    my_dog = Pidog(head_init_angles=[0, 0, -30])
    sleep(1)

    def wake_up():
        # stretch
        my_dog.rgb_strip.set_mode('listen', color='yellow', bps=0.6, brightness=0.8)
        my_dog.do_action('stretch', speed=50)
        my_dog.head_move([[0, 0, 30]]*2, immediately=True)
        my_dog.wait_all_done()
        sleep(0.2)
        body_twisting(my_dog)
        my_dog.wait_all_done()
        sleep(0.5)
        my_dog.head_move([[0, 0, -30]], immediately=True, speed=90)
        # sit and wag_tail
        my_dog.do_action('sit', speed=25)
        my_dog.wait_legs_done()
        my_dog.do_action('wag_tail', step_count=10, speed=100)
        my_dog.rgb_strip.set_mode('breath', color=[245, 10, 10], bps=2.5, brightness=0.8)
        pant(my_dog, pitch_comp=-30, volume=80)
        my_dog.wait_all_done()
        # hold
        my_dog.do_action('wag_tail', step_count=10, speed=30)
        my_dog.rgb_strip.set_mode('breath', 'pink', bps=0.5)
        while True:
            sleep(1)

    if __name__ == "__main__":
        try:
            wake_up()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()
