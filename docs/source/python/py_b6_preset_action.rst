6. 执行预设动作  
=======================

PiDog 的库中预先定义了一些常用的动作。  
你可以通过调用以下函数，让 PiDog 直接执行这些预设动作。

.. code-block:: python

    Pidog.do_action(action_name, step_count=1, speed=50)

* ``action_name``：动作名称，可以使用以下字符串之一：

    * ``"sit"``            —— 坐下  
    * ``"half_sit"``       —— 半坐  
    * ``"stand"``          —— 站立  
    * ``"lie"``            —— 趴下  
    * ``"lie_with_hands_out"`` —— 四肢前伸地趴下  
    * ``"forward"``        —— 向前走  
    * ``"backward"``       —— 倒退  
    * ``"turn_left"``      —— 向左转  
    * ``"turn_right"``     —— 向右转  
    * ``"trot"``           —— 小跑  
    * ``"stretch"``        —— 伸展  
    * ``"push_up"``        —— 俯卧撑  
    * ``"doze_off"``       —— 打瞌睡  
    * ``"nod_lethargy"``   —— 昏昏欲睡地点头  
    * ``"shake_head"``     —— 摇头  
    * ``"tilting_head_left"``  —— 头向左歪  
    * ``"tilting_head_right"`` —— 头向右歪  
    * ``"tilting_head"``        —— 歪头（左右交替）  
    * ``"head_bark"``       —— 头部配合吠叫动作  
    * ``"head_up_down"``    —— 头上下点动  
    * ``"wag_tail"``        —— 摇尾巴

* ``step_count``：执行该动作的次数。
* ``speed``：执行动作的速度。

**以下是一个使用示例：**

1. 做十次俯卧撑，然后坐下来卖萌。

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # 做俯卧撑
        my_dog.do_action("half_sit", speed=60)
        my_dog.do_action("push_up", step_count=10, speed=60)
        my_dog.wait_all_done()
        
        # 卖萌
        my_dog.do_action("sit", speed=60)
        my_dog.do_action("wag_tail", step_count=100,speed=90)
        my_dog.do_action("tilting_head", step_count=5, speed=20)
        my_dog.wait_head_done()
        
        my_dog.stop_and_lie()

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        print("closing ...")
        my_dog.close()
