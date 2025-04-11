.. _py_b2_leg_move: 

2. 腿部动作
=================

PiDog 的腿部动作是通过以下函数实现的：

.. code-block:: python

    Pidog.legs_move(target_angles, immediately=True, speed=50)

* ``target_angles``：这是一个二维数组，其中的每个元素是包含 8 个舵机角度的数组（称为角度组）。这些角度组用于控制 PiDog 的 8 个腿部舵机。如果写入多个角度组，未立即执行的部分将存入缓存中。
* ``immediately`` ：当调用该函数时，若该参数为 ``True``，则会立即清除缓存并执行新写入的角度组；若设置为 ``False``，新写入的角度组将被加入到执行队列中。
* ``speed`` ：设定角度组动作的执行速度。

**以下列出了一些常见的用法：**

1.  立即执行动作

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # 半站立姿态
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)   


2. 向执行队列中添加多个角度组

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # 半站立
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # 连续动作
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70],
                      [90, -30, -90, 30, 80, 70, -80, -70],
                      [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   


3. 在 10 秒内循环动作

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # 半站立
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # 俯卧撑准备姿势
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], immediately=False, speed=20)

    # 俯卧撑循环
    for _ in range(99):
        my_dog.legs_move([[90, -30, -90, 30, 80, 70, -80, -70],
                          [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   

    # 保持姿势 10 秒
    time.sleep(10)

    # 停止并恢复半站立
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], immediately=True, speed=50)  


**PiDog 的腿部控制还支持以下配套函数：**

.. code-block:: python

    Pidog.is_legs_done()

用于判断缓存中的角度组是否已全部执行完毕。若执行完毕，返回 ``True``；否则返回 ``False``。

.. code-block:: python

    Pidog.wait_legs_done()

挂起程序，直到缓存中的所有角度组执行完毕后才继续。

.. code-block:: python

    Pidog.legs_stop() 

清空缓存中的角度组。