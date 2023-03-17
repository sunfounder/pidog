12. Pat the PiDog's Head
=========================

The Touch Swich on the head of PiDog can detect how you touch it. You can call the following functions to use it.

.. code-block:: python

   Pidog.dual_touch.read()

* Touch the module from left to right (front to back for PiDog's orientation), it will return ``"LS"``.
* Touch the module from right to left, it will return ``"RS"``.
* Touch the module If the left side of the module is touched, it will return ``"L"``.
* If the right side of the module is touched, it will return ``"R"``.
* If the module is not touched, it will return ``"N"``.

**Here is an example of its use:**

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()
    while True:
        touch_status = my_dog.dual_touch.read()
        print(f"touch_status: {touch_status}")
        time.sleep(0.5)

