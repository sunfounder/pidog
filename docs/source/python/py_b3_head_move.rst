
3. 头部控制
================

PiDog 的头部舵机控制是通过以下函数实现的：

.. code-block:: python

    Pidog.head_move(target_yrps, roll_comp=0, pitch_comp=0, immediately=True, speed=50)

* ``target_angles``：这是一个二维数组，每个元素包含三个舵机角度值（即角度组）。这些角度组用于控制 PiDog 的三个头部舵机。如果写入多个角度组，未立即执行的部分将会进入缓存队列。
* ``roll_comp``：对横滚轴进行角度补偿。
* ``pitch_comp``：对俯仰轴进行角度补偿。
* ``immediately``：设为 ``True`` 时立即清除缓存并执行当前角度组；设为 ``False`` 时角度组将加入到待执行队列中。
* ``speed``：角度组动作的执行速度。



**PiDog 的头部控制还提供了以下辅助函数：**

.. code-block:: python

    Pidog.is_head_done()

判断头部动作缓存是否已执行完毕。

.. code-block:: python

    Pidog.wait_head_done()

等待缓存中的头部动作执行完成。

.. code-block:: python

    Pidog.head_stop()

清空缓存中的所有头部动作，使头部舵机停止运动。


**以下是一些常见的使用示例：**

1. 点头五次

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(5):
        my_dog.head_move([[0, 0, 30],[0, 0, -30]], speed=80)
        my_dog.wait_head_done()
        time.sleep(0.5)

2. 摇头十秒

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.head_move([[30, 0, 0],[-30, 0, 0]], immediately=False, speed=30)

    # 持续摇头 10 秒
    time.sleep(10)

    my_dog.head_move([[0, 0, 0]], immediately=True, speed=80)

3. 无论坐着或半蹲，PiDog 都能在摇头时保持头部水平

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # 动作预设
    shake_head = [[30, 0, 0],[-30, 0, 0]]
    half_stand_leg = [[45, 10, -45, -10, 45, 10, -45, -10]]
    sit_leg = [[30, 60, -30, -60, 80, -45, -80, 45]]

    while True:
        # 半蹲状态下摇头
        my_dog.legs_move(half_stand_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=0, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)

        # 坐姿状态下摇头
        my_dog.legs_move(sit_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=-30, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)

