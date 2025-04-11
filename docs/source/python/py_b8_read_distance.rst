8. 读取距离  
==================

PiDog 通过其头部的超声波模块可以探测前方的障碍物。

该超声波模块的测量范围为 2 至 400 厘米。

你可以使用以下函数读取距离值，返回的是浮点型数字：

.. code-block:: python

    Pidog.ultrasonic.read_distance()

**以下是一个使用示例：**

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()
    while True:
        distance = my_dog.ultrasonic.read_distance()
        distance = round(distance,2)
        print(f"Distance: {distance} cm")
        time.sleep(0.5)
