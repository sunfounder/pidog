.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

1. PiDog Initialization
============================

The functions of PiDog are written in the ``Pidog`` class, and the prototype of this class is shown below.

.. code-block:: python

    Class: Pidog()

    __init__(leg_pins=DEFAULT_LEGS_PINS, 
            head_pins=DEFAULT_HEAD_PINS,
            tail_pin=DEFAULT_TAIL_PIN,
            leg_init_angles=None,
            head_init_angles=None,
            tail_init_angle=None)


PiDog must be instantiated in one of several ways, as shown below.

1. Following are the simplest steps of initialization.

.. code-block:: python

    # Import Pidog class
    from pidog import Pidog

    # instantiate a Pidog
    my_dog = Pidog()

2. PiDog has 12 servos, which can be initialized when we instantiate it.

.. code-block:: python

    # Import Pidog class
    from pidog import Pidog

    # instantiate a Pidog with custom initialized servo angles
    my_dog = Pidog(leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )

In the ``Pidog`` class, the servos are divided into three groups.

* ``leg_init_angles`` : In this array, 8 values determine the angles of eight servos, with the servos (pin numbers) they control being ``2, 3, 7, 8, 0, 1, 10, 11``. From the foldout, you can see where these servos are located.

* ``head_init_angles`` : There is an array with 3 values, controllers for PiDog-head yaw, roll, pitch servos (``no. 4, 6, 5``) which react to yaw, roll, pitch, or Deflection of the body.

* ``tail_init_angle`` : In this array, there is only one value, which is dedicated to controlling the tail servo, which is ``9``.


3. ``Pidog`` allows you to redefine the serial number of the servos when instantiating the robot if your servo order is different.

.. code-block:: python

    # Import Pidog class
    from pidog import Pidog

    # instantiate a Pidog with custom initialized pins & servo angles
    my_dog = Pidog(leg_pins=[2, 3, 7, 8, 0, 1, 10, 11], 
                    head_pins=[4, 6, 5],
                    tail_pin=[9],
                    leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )