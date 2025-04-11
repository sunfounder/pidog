
1. PiDog 初始化
============================

PiDog 的各项功能都封装在 ``Pidog`` 类中，以下是该类的构造函数原型：

.. code-block:: python

    Class: Pidog()

    __init__(leg_pins=DEFAULT_LEGS_PINS, 
            head_pins=DEFAULT_HEAD_PINS,
            tail_pin=DEFAULT_TAIL_PIN,
            leg_init_angles=None,
            head_init_angles=None,
            tail_init_angle=None)


您可以通过以下几种方式对 PiDog 进行实例化：

1. 最基础的初始化方式如下所示：

.. code-block:: python

    # 导入 Pidog 类
    from pidog import Pidog

    # 实例化一个 Pidog 对象
    my_dog = Pidog()

2. PiDog 配备了 12 个舵机，可以在实例化时指定其初始角度：

.. code-block:: python

    # 导入 Pidog 类
    from pidog import Pidog

    # 带自定义初始角度的实例化方式
    my_dog = Pidog(leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )

在 ``Pidog`` 类中，舵机被划分为三个控制组：

* ``leg_init_angles``：该数组包含 8 个值，对应 8 个舵机的角度，控制的舵机（引脚编号）为 ``2, 3, 7, 8, 0, 1, 10, 11``。具体位置可参考结构展开图。

* ``head_init_angles``：包含 3 个值，控制 PiDog 的头部转向，包括偏航、横滚和俯仰，对应舵机编号为 ``4, 6, 5``。

* ``tail_init_angle``：仅包含一个值，控制尾部舵机，对应舵机编号为 ``9``。


3. 如果您的舵机接线顺序与默认不同， ``Pidog`` 类支持在实例化时自定义舵机引脚编号：

.. code-block:: python

    # 导入 Pidog 类
    from pidog import Pidog

    # 自定义舵机引脚与初始角度进行实例化
    my_dog = Pidog(leg_pins=[2, 3, 7, 8, 0, 1, 10, 11], 
                    head_pins=[4, 6, 5],
                    tail_pin=[9],
                    leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )