.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

10. IMU Read
==============


Through the 6-DOF IMU Module, PiDog can determine if it's standing on a slope, or if it's being picked up.

The 6-DOF IMU Module is equipped with a 3-axis accelerometer and a 3-axis gyroscope, allowing acceleration and angular velocity to be measured in three directions.

.. note::

    Before using the module, make sure that it is correctly assembled. The label on the module will let you know if it is reversed.

**You can read their acceleration with:**

.. code-block:: python

   ax, ay, az = Pidog.accData

With the PiDog placed horizontally, the acceleration on the x-axis (ie ax) should be close to the acceleration of gravity (1g), with a value of -16384.
The values of the y-axis and x-axis are close to 0.

**Use the following way to read their angular velocity:**

.. code-block:: python

   gx, gy, gz = my_dog.gyroData

In the case where PiDog is placed horizontally, all three values are close to 0.


**Here are some examples of how 6-DOF Module is used:**

1. Read real-time acceleration, angular velocity

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    my_dog.do_action("pushup", step_count=10, speed=20)

    while True:
        ax, ay, az = my_dog.accData
        gx, gy, gz = my_dog.gyroData
        print(f"accData: {ax/16384:.2f} g ,{ay/16384:.2f} g, {az/16384:.2f} g       gyroData: {gx} °/s, {gy} °/s, {gz} °/s")
        time.sleep(0.2)
        if my_dog.is_legs_done():
            break

    my_dog.stop_and_lie()

    my_dog.close()

2. Calculate the lean angle of PiDog's body.

.. code-block:: python

    from pidog import Pidog
    import time
    import math

    my_dog = Pidog()

    while True:
        ax, ay, az = my_dog.accData
        body_pitch = math.atan2(ay,ax)/math.pi*180%360-180
        print(f"Body Degree: {body_pitch:.2f} °" )
        time.sleep(0.2)

    my_dog.close()

3. While leaning, PiDog keeps its eyes level.

.. code-block:: python

    from pidog import Pidog
    import time
    import math

    my_dog = Pidog()

    while True:
        ax, ay, az = my_dog.accData
        body_pitch = math.atan2(ay,ax)/math.pi*180%360-180
        my_dog.head_move([[0, 0, 0]], pitch_comp=-body_pitch, speed=80)
        time.sleep(0.2)

    my_dog.close()