.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

FAQ
===========================

Q1: Regarding the "pinctrl: not found" error.
-------------------------------------------------------------------

If you encounter the error:

.. code-block::

    pinctrl: not found

It indicates that you have installed the Bullseye system. It is recommended to install the **Bookworm system** instead.

Q2: About the Battery Charger?
-------------------------------------------------------------------

To charge the battery, simply connect a 5V/2A Type-C power supply to the Robot Hat's power port. There's no need to turn on the Robot Hat's power switch during charging.
You can also use the device while charging the battery. 

.. image:: img/robot_hat_pic.png
    :align: center
    :width: 500

During charging, the input power is boosted by the charging chip to charge the battery and simultaneously supply the DC-DC converter for external use, with a charging power of approximately 10W. 
If external power consumption remains high for an extended period, the battery may supplement the power supply, similar to using a phone while charging. However, be mindful of the battery's capacity to avoid completely depleting it during simultaneous charging and usage.
