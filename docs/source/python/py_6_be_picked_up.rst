6. 被举起来啦！
===================

尝试将 PiDog 从地面抱起，PiDog 会仿佛感觉自己飞起来了一样，摆出“超人”姿势，并兴奋地欢呼！

.. image:: img/py_6.gif

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 6_be_picked_up.py

程序运行后，6-DOF IMU 模块会持续检测竖直方向的加速度。
当判断 PiDog 处于失重状态时，它会摆出超人姿势并发出欢呼声；
否则，则认为它处于地面上，并做出站立动作。



**代码**

.. note::
    您可以对以下代码进行 **修改/重置/复制/运行/停止**。请确保已进入源码路径（如 ``pidog\examples``）进行操作。修改后可直接运行查看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep

    my_dog = Pidog()
    sleep(0.1)


    def fly():
        my_dog.rgb_strip.set_mode('boom', color='red', bps=3)
        my_dog.legs.servo_move([45, -45, 90, -80, 90, 90, -90, -90], speed=60)
        my_dog.do_action('wag_tail', step_count=10, speed=100)
        my_dog.speak('woohoo', volume=80)
        my_dog.wait_legs_done()
        sleep(1)

    def stand():
        my_dog.rgb_strip.set_mode('breath', color='green', bps=1)
        my_dog.do_action('stand', speed=60)
        my_dog.wait_legs_done()
        sleep(1)

    def be_picked_up():
        isUp = False
        upflag = False
        downflag = False

        stand()

        while True:
            ax = my_dog.accData[0]
            print('ax: %s, is up: %s' % (ax, isUp))

            # 重力加速度参考值：1G = -16384
            if ax < -18000: # 向下加速，与重力方向一致，加速度 < -1G
                my_dog.body_stop()
                if upflag == False:
                    upflag = True
                if downflag == True:
                    isUp = False
                    downflag = False
                    stand()

            if ax > -13000: # 向上加速，与重力方向相反，加速度 > -1G
                my_dog.body_stop()
                if upflag == True:
                    isUp = True
                    upflag = False
                    fly()
                if downflag == False:
                    downflag = True

            sleep(0.02)


    if __name__ == "__main__":
        try:
            be_picked_up()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()