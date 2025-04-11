4. 尾巴控制  
===================

以下是控制 PiDog 尾巴的相关函数，使用方法与 :ref:`py_b2_leg_move` 类似。


.. code-block:: python

    Pidog.tail_move(target_angles, immediately=True, speed=50)

* ``target_angles``：这是一个二维数组，每个元素包含一个舵机角度值（即角度组），用于控制尾巴的舵机角度。如果传入多个角度组，未执行的部分将会被存入缓存队列。
* ``immediately``：调用函数时设为 ``True``，表示立即清空缓存并执行当前角度组；设为 ``False`` 时，当前角度组会加入执行队列。
* ``speed``：执行该角度组时的速度。

**PiDog 的尾舵控制还提供以下辅助函数：**

.. code-block:: python

    Pidog.is_tail_done()

判断尾巴动作缓存是否已执行完毕。

.. code-block:: python

    Pidog.wait_tail_done()

等待尾巴动作缓存执行完成。

.. code-block:: python

    Pidog.tail_stop()

清空缓存中的所有尾部动作，使尾舵停止运动。


**以下是一些常见用法：**


1. 摇尾巴持续 10 秒

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.tail_move([[30],[-30]], immediately=False, speed=30)

    # 保持摇尾动作 10 秒
    time.sleep(10)

    my_dog.tail_stop()