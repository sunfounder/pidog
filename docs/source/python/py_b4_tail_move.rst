Tail Move
============

Following are the functions that control PiDog's tail. This function is similar to :ref:`py_b2_leg_move`.


.. code-block:: python

    Pidog.tail_move(target_angles, immediately=True, speed=50)

* ``target_angles`` : It is a two-dimensional array composed of an array of 1 servo angles (referred to as angle group) as elements. These angle groups will be used to control the angles of the 8 foot servos. If multiple angle groups are written, the unexecuted angle groups will be stored in the cache.
* ``immediately`` : When calling the function, set this parameter to ``True``, the cache will be cleared immediately to execute the newly written angle group; if the parameter is set to ``False``, the newly written The incoming angular group is added to the execution queue.
* ``speed`` : The speed at which the angular group is executed.


**PiDog's tail servo control also has some supporting functions:**

.. code-block:: python

    Pidog.is_tail_done()

whether all the tail actions in the buffer to be executed

.. code-block:: python

    Pidog.wait_tail_done()

wait for all the tail actions in the buffer to be executed

.. code-block:: python

    Pidog.tail_stop()

clear all the tail actions of leg in the buffer, to make tail servo stop


**Here are some common usages:**


1. Wag tail for 10 seconds.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.tail_move([[30],[-30]], immediately=False, speed=30)

    # keep 10s
    time.sleep(10)

    my_dog.tail_stop()