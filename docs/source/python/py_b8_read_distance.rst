.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

8. Read Distance
==================

Through the Ultrasonic Module in its head, PiDog can detect obstacles ahead.

An ultrasonic module can detect objects between 2 and 400 cm away.

With the following function, you can read the distance as a floating point number.

.. code-block:: python

    Pidog.ultrasonic.read_distance()

**Here is an example of usage:**

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()
    while True:
        distance = my_dog.ultrasonic.read_distance()
        distance = round(distance,2)
        print(f"Distance: {distance} cm")
        time.sleep(0.5)    
