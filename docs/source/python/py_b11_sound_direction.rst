
11. 声源方向检测
============================

PiDog 配备了声源方向传感器模块，用于检测声音的来源方向。你可以通过在它附近拍手等方式来触发该功能。

**使用这个模块非常简单，只需调用以下函数：**

.. code-block:: python

    Pidog.ears.isdetected()

当检测到声音时，返回 ``True``；否则返回 ``False``。

.. code-block:: python

    Pidog.ears.read()

该函数返回声音来源的方向，范围为 0 到 359 度；声音来自正前方时返回 0，来自右侧时返回 90。

**以下是一个典型的使用示例：**

.. code-block:: python

    from pidog import Pidog

    my_dog = Pidog()

    while True:
        if my_dog.ears.isdetected():
            direction = my_dog.ears.read()
            print(f"sound direction: {direction}")





