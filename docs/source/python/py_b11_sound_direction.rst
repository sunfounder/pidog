.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

11. Sound Direction Detect
================================

The PiDog has a Sound Direction Sensor Module that detects where sound is coming from, and we can trigger it by clapping near it.

**Using this module is as simple as calling these functions.**

.. code-block:: python

    Pidog.ears.isdetected()

Returns ``True`` if sound is detected, ``False`` otherwise.

.. code-block:: python

    Pidog.ears.read()

This function returns the direction of the sound source, with a range of 0 to 359; if the sound comes from the front, it returns 0; if it comes from the right, it returns 90.

**An example of how to use this module is as follows:**

.. code-block:: python

    from pidog import Pidog

    my_dog = Pidog()

    while True:
        if my_dog.ears.isdetected():
            direction = my_dog.ears.read()
            print(f"sound direction: {direction}")





