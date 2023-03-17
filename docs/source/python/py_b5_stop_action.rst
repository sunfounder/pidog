5. Stop All Actions
======================

After the previous chapters, you can find that the servo control of PiDog is divided into three threads.
This allows PiDog's head and body to move at the same time, even with two lines of code.

**Here are a few functions that work with the three servo threads:**

.. code-block:: python

    Pidog.wait_all_done()
    
Wait for all the actions in the leg actions buffer, head buffer and tail buffer to be executed

.. code-block:: python

    Pidog.body_stop()
    
Stop all the actions of legs, head and tail

.. code-block:: python

    Pidog.stop_and_lie()
    
Stop all the actions of legs, head and tail, then reset to "lie" pose

.. code-block:: python

    Pidog.close()
    
Stop all the actions, reset to "lie" pose, and  close all the threads, usually used when exiting a program


**Here are some common usages:**



.. code-block:: python
    :emphasize-lines: 10,36,45

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # pushup prepare
        my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], speed=30)
        my_dog.head_move([[0, 0, 0]], pitch_comp=-10, speed=80) 
        my_dog.wait_all_done() # wait all the actions to be done
        time.sleep(0.5)

        # pushup 
        leg_pushup_action = [
            [90, -30, -90, 30, 80, 70, -80, -70],
            [45, 35, -45, -35, 80, 70, -80, -70],       
        ]
        head_pushup_action = [
            [0, 0, -30],
            [0, 0, 20],
        ]
        
        # fill action buffers
        for _ in range(50):
            my_dog.legs_move(leg_pushup_action, immediately=False, speed=50)
            my_dog.head_move(head_pushup_action, pitch_comp=-10, immediately=False, speed=50)
        
        # show buffer length
        print(f"legs buffer length (start): {len(my_dog.legs_action_buffer)}")
        
        # keep 5 second & show buffer length
        time.sleep(5)
        print(f"legs buffer length (5s): {len(my_dog.legs_action_buffer)}")
        
        # stop action & show buffer length
        my_dog.stop_and_lie()
        print(f"legs buffer length (stop): {len(my_dog.legs_action_buffer)}")

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        print("closing ...")
        my_dog.close() # close all the servo threads