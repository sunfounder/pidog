.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

11. Play PiDog with Keyboard
======================================


In this example, we will use the keyboard to control PiDog. You can press these keys in the terminal to make it act.


.. list-table:: 
    :widths: 25 50 25 50 25 50
    :header-rows: 1

    * - Keys
      - Function
      - Keys
      - Function
      - Keys
      - Function  
    * - 1
      - doze off
      - q
      - bark harder
      - a
      - turn left
    * - 2
      - push-up
      - w
      - forward
      - s
      - backward
    * - 3
      - howling
      - e
      - pant
      - d
      - turn right
    * - 4
      - twist body
      - r
      - wag tail
      - f
      - shake head
    * - 5
      - scratch
      - t
      - hake head
      - g
      - high five
    * - u
      - head roll
      - U
      - head roll+
      - z
      - lie
    * - i
      - head pitch
      - I
      - head pitch+
      - x
      - stand up
    * - o
      - head roll
      - O
      - head roll+
      - c
      - sit
    * - j
      - head yaw
      - J
      - head yaw+
      - v
      - stretch
    * - k
      - head pitch
      - K
      - head pitch+
      - m
      - head reset
    * - l
      - head yaw
      - L
      - head yaw+
      - W
      - trot


**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 11_keyboard_control.py

After the program runs, you will see a printed keyboard on the terminal. Now you can control PiDog with keyboard in terminal.



**Code**

Please find the code in |link_code_11_keyboard_control|.
