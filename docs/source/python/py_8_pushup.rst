
8. 俯卧撑
===============

PiDog 是一只热爱锻炼的机器人，它可以和你一起做俯卧撑！

.. image:: img/py_8.gif

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 8_pushup.py

程序运行后，PiDog 会先进入支撑姿态，然后不断进行俯卧撑并发出叫声。



**代码**

.. note::
    你可以对以下代码进行 **修改/重置/复制/运行/停止**。请确保进入源码路径（如 ``pidog\examples``）后操作。修改后可直接运行查看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import push_up, bark

    my_dog = Pidog()

    sleep(0.5)


    def main():
        my_dog.legs_move([[45, -25, -45, 25, 80, 70, -80, -70]], speed=50)
        my_dog.head_move([[0, 0, -20]], speed=90)
        my_dog.wait_all_done()
        sleep(0.5)
        bark(my_dog, [0, 0, -20])
        sleep(0.1)
        bark(my_dog, [0, 0, -20])

        sleep(1)
        my_dog.rgb_strip.set_mode("speak", color="blue", bps=2)
        while True:
            push_up(my_dog, speed=92)
            bark(my_dog, [0, 0, -40])
            sleep(0.4)


    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()