10. 读取 IMU 数据
====================

通过 6 自由度 IMU 模块，PiDog 能够判断自己是否处于倾斜状态，或是否被提起。

该模块集成了三轴加速度计与三轴陀螺仪，可用于测量三个方向的加速度与角速度。

.. note::

    在使用该模块前，请确保模块安装方向正确。模块上的标签可用于判断是否装反。

**使用以下方式读取加速度：**

.. code-block:: python

   ax, ay, az = Pidog.accData

当 PiDog 水平放置时，x 轴方向（即 ax）上的加速度应接近重力加速度（1g），其值大约为 -16384。
而 y 轴与 z 轴方向的加速度应接近 0。

**使用以下方式读取角速度：**

.. code-block:: python

   gx, gy, gz = my_dog.gyroData

当 PiDog 静置在水平面时，三个方向的角速度值应接近 0。


**以下是一些 6 自由度模块的典型用法示例：**

1. 实时读取加速度和角速度

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    my_dog.do_action("pushup", step_count=10, speed=20)

    while True:
        ax, ay, az = my_dog.accData
        gx, gy, gz = my_dog.gyroData
        print(f"accData: {ax/16384:.2f} g ,{ay/16384:.2f} g, {az/16384:.2f} g       gyroData: {gx} °/s, {gy} °/s, {gz} °/s")
        time.sleep(0.2)
        if my_dog.is_legs_done():
            break

    my_dog.stop_and_lie()

    my_dog.close()

2. 计算 PiDog 身体的倾斜角度

.. code-block:: python

    from pidog import Pidog
    import time
    import math

    my_dog = Pidog()

    while True:
        ax, ay, az = my_dog.accData
        body_pitch = math.atan2(ay,ax)/math.pi*180%360-180
        print(f"Body Degree: {body_pitch:.2f} °" )
        time.sleep(0.2)

    my_dog.close()

3. 当身体倾斜时，PiDog 保持头部水平

.. code-block:: python

    from pidog import Pidog
    import time
    import math

    my_dog = Pidog()

    while True:
        ax, ay, az = my_dog.accData
        body_pitch = math.atan2(ay,ax)/math.pi*180%360-180
        my_dog.head_move([[0, 0, 0]], pitch_comp=-body_pitch, speed=80)
        time.sleep(0.2)

    my_dog.close()