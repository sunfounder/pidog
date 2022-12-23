.. _py_b2_leg_move:

Leg Move
========

PiDog's leg movements are implemented by the following functions.

.. code-block:: python

    Pidog.legs_move(target_angles, immediately=True, speed=50)

* ``target_angles``: It is a two-dimensional array composed of an array of 8 servo angles (referred to as angle group) as elements. These angle groups will be used to control the angles of the 8 foot servos. If multiple angle groups are written, the unexecuted angle groups will be stored in the cache.
* ``immediately`` : When calling the function, set this parameter to ``True``, the cache will be cleared immediately to execute the newly written angle group; if the parameter is set to ``False``, the newly written The incoming angular group is added to the execution queue.
* ``speed`` : The speed at which the angular group is executed.

**Some common usages are listed below:**

1.  Take action immediately.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # half stand
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)   


2. Add some angular groups to the execution queue.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # half stand
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # multiple actions
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70],
                        [90, -30, -90, 30, 80, 70, -80, -70],
                        [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   

3. Perform repetitions within 10 seconds.


.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # half stand
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # pushup preparation
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], immediately=False, speed=20)

    # pushup
    for _ in range(99):
        my_dog.legs_move([[90, -30, -90, 30, 80, 70, -80, -70],
                            [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   

    # keep 10s
    time.sleep(10)

    # stop and half stand
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], immediately=True, speed=50)  


**PiDog's leg control also has the following functions that can be used together:**

.. code-block:: python

    Pidog.is_legs_done()

This function is used to determine whether the angle group in the cache has been executed. If yes, return ``True``; otherwise, return ``False``.

.. code-block:: python

    Pidog.wait_legs_done()

Suspends the program until the angle groups in the cache have been executed.

.. code-block:: python

    Pidog.legs_stop() 

Empty the angular group in the cache.