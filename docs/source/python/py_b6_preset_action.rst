6. プリセットアクションを実行する
==========================================

PiDogのライブラリには、よく使われるアクションが予め記述されています。
以下の関数を呼び出して、PiDogにこれらのアクションを直接行わせることができます。

.. code-block:: python

    Pidog.do_action(action_name, step_count=1, speed=50)

* ``action_name``: アクション名、以下の文字列が記述できます。

    * ``"sit"``
    * ``"half_sit"``
    * ``"stand"``
    * ``"lie"``
    * ``"lie_with_hands_out"``
    * ``"forward"``
    * ``"backward"``
    * ``"turn_left"``
    * ``"turn_right"``
    * ``"trot"``
    * ``"stretch"``
    * ``"pushup"``
    * ``"doze_off"``
    * ``"nod_lethargy"``
    * ``"shake_head"``
    * ``"tilting_head_left"``
    * ``"tilting_head_right"``
    * ``"tilting_head"``
    * ``"head_bark"``
    * ``"head_up_down"``
    * ``"wag_tail"``

* ``step_count``: このアクションを何回実行するか。
* ``speed``: アクションを実行する速度。

**使用例を以下に示します**：

1. 腕立て伏せを10回実行し、その後床に座ってかわいらしい態度をとる。


.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # pushup
        my_dog.do_action("half_sit", speed=60)
        my_dog.do_action("pushup", step_count=10, speed=60)
        my_dog.wait_all_done()
        
        # act cute
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