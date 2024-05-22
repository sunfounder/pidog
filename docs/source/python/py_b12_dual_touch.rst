.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

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

