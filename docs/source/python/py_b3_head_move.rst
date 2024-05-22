.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

3. Head Move
================

The control of PiDog's head servo is implemented by the following functions.

.. code-block:: python

    Pidog.head_move(target_yrps, roll_comp=0, pitch_comp=0, immediately=True, speed=50)

* ``target_angles`` : It is a two-dimensional array composed of an array of 3 servo angles (referred to as angle group) as elements. These angle groups will be used to control the angles of the 8 foot servos. If multiple angle groups are written, the unexecuted angle groups will be stored in the cache.
* ``roll_comp`` : Provides angular compensation on the roll axis.
* ``pitch_comp`` : Provides angle compensation on the pitch axis.
* ``immediately`` : When calling the function, set this parameter to ``True``, the cache will be cleared immediately to execute the newly written angle group; if the parameter is set to ``False``, the newly written The incoming angular group is added to the execution queue.
* ``speed`` : The speed at which the angular group is executed.


**PiDog's head servo control also has some supporting functions:**


.. code-block:: python

    Pidog.is_head_done()

Whether all the head actions in the buffer to be executed

.. code-block:: python

    Pidog.wait_head_done()

Wait for all the head actions in the buffer to be executed

.. code-block:: python

    Pidog.head_stop()

Clear all the head actions of leg in the buffer, to make head servos stop


**Here are some common use cases:**

1. Nod five times.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(5):
        my_dog.head_move([[0, 0, 30],[0, 0, -30]], speed=80)
        my_dog.wait_head_done()
        time.sleep(0.5)

2. Shake your head for 10 seconds.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.head_move([[30, 0, 0],[-30, 0, 0]], immediately=False, speed=30)

    # keep 10s
    time.sleep(10)

    my_dog.head_move([[0, 0, 0]], immediately=True, speed=80)

3. Whether sitting or half standing, PiDog keeps its head level when shaking its head.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # action list
    shake_head = [[30, 0, 0],[-30, 0, 0]]
    half_stand_leg = [[45, 10, -45, -10, 45, 10, -45, -10]]
    sit_leg = [[30, 60, -30, -60, 80, -45, -80, 45]]

    while True:
        # shake head in half stand
        my_dog.legs_move(half_stand_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=0, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)

        # shake head in sit
        my_dog.legs_move(sit_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=-30, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)

