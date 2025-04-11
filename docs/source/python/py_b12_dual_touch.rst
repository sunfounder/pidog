12. 抚摸 PiDog 的头部  
===========================

PiDog 头部的触摸开关能够感应你的触摸方式。你可以调用以下函数来使用它。

.. code-block:: python

   Pidog.dual_touch.read()

* 从左向右触摸模块（以 PiDog 的朝向来看是从前到后），返回 ``"LS"``。
* 从右向左触摸模块，返回 ``"RS"``。
* 如果触摸模块的左侧，返回 ``"L"``。
* 如果触摸模块的右侧，返回 ``"R"``。
* 如果没有触摸模块，返回 ``"N"``。

**Here is an example of its use:**

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()
    while True:
        touch_status = my_dog.dual_touch.read()
        print(f"touch_status: {touch_status}")
        time.sleep(0.5)
    
