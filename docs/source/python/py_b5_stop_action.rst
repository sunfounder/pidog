5. 停止所有动作  
======================

通过前几章的学习，你应该已经注意到，PiDog 的舵机控制被划分为三个独立的线程。  
这意味着即使只有两行代码，也能实现 PiDog 的头部和身体同时运动。

**以下是一些与三组舵机控制线程配合使用的重要函数：**

.. code-block:: python

    Pidog.wait_all_done()
    
等待腿部、头部和尾部的所有动作缓冲执行完毕。

.. code-block:: python

    Pidog.body_stop()
    
停止腿部、头部和尾部的所有动作。

.. code-block:: python

    Pidog.stop_and_lie()
    
停止腿部、头部和尾部的所有动作，并将 PiDog 重置为“趴下”姿态。

.. code-block:: python

    Pidog.close()
    
停止所有动作，重置为“趴下”姿态，并关闭所有舵机控制线程，通常用于程序退出时调用。


**以下是一些常见用法示例：**



.. code-block:: python
    :emphasize-lines: 10,36,45

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # 俯卧撑准备动作
        my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], speed=30)
        my_dog.head_move([[0, 0, 0]], pitch_comp=-10, speed=80) 
        my_dog.wait_all_done()  # 等待所有动作完成
        time.sleep(0.5)

        # 俯卧撑动作
        leg_pushup_action = [
            [90, -30, -90, 30, 80, 70, -80, -70],
            [45, 35, -45, -35, 80, 70, -80, -70],       
        ]
        head_pushup_action = [
            [0, 0, -30],
            [0, 0, 20],
        ]
        
        # 填充动作缓冲区
        for _ in range(50):
            my_dog.legs_move(leg_pushup_action, immediately=False, speed=50)
            my_dog.head_move(head_pushup_action, pitch_comp=-10, immediately=False, speed=50)
        
        # 显示缓冲区长度
        print(f"legs buffer length (start): {len(my_dog.legs_action_buffer)}")
        
        # 保持 5 秒后显示缓冲区长度
        time.sleep(5)
        print(f"legs buffer length (5s): {len(my_dog.legs_action_buffer)}")
        
        # 停止动作并显示缓冲区长度
        my_dog.stop_and_lie()
        print(f"legs buffer length (stop): {len(my_dog.legs_action_buffer)}")

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        print("closing ...")
        my_dog.close()  # 关闭所有舵机线程