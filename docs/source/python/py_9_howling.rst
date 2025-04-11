
9. 嚎叫
===============


PiDog 不只是只可爱的狗狗，它也能像狼一样威风地嚎叫！快来听听它的声音吧！


.. image:: img/py_9.gif

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 9_howling.py

程序运行后，PiDog 会坐在地上发出嚎叫声。



**代码**

.. note::
    你可以对下方代码进行 **修改 / 重置 / 复制 / 运行 / 停止** 操作。在此之前，请先进入源码路径（例如 ``pidog\examples``）。修改后可直接运行查看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import howling

    my_dog = Pidog()

    sleep(0.5)


    def main():
        my_dog.do_action('sit', speed=50)
        my_dog.head_move([[0, 0, 0]], pitch_comp=-40, immediately=True, speed=80)
        sleep(0.5)
        while True:
            howling(my_dog)


    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()

