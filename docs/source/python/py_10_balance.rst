.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

10. Balance
=============


Because PiDog is equipped with a 6-DOF IMU module, it has a great sense of balance.

In this example, you can make PiDog walk smoothly on the table, even if you lift one side of the table, PiDog will walk smoothly on the gentle slope.


.. image:: img/py_10.gif

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 10_balance.py

After the program is running, you will see a printed keyboard on the terminal.
You can control PiDog to walk smoothly on the ramp by typing the below keys.


.. list-table:: 
    :widths: 25 25
    :header-rows: 1

    * - Keys
      - Function
    * -  W
      -  Forward 
    * -  E
      -  Stand 
    * -  A
      -  Turn Left 
    * -  S
      -  Backward 
    * -  D
      -  Turn Right 
    * -  R
      -  Each press slightly lifts the body; multiple presses are needed for a noticeable rise.     
    * -  F
      -  Each press lowers the body a bit; it takes multiple presses for a noticeable descent.
    

**Code**


Please find the code in |link_code_10_balance|.
