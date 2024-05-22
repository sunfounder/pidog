.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _i2c_spi_config:

6. Check I2C and SPI Interface
========================================

We will be using Raspberry Pi's I2C and SPI interfaces. These interfaces should have been enabled when installing the ``robot-hat`` module earlier. To ensure everything is in order, let's check if they are indeed enabled.

#. Input the following command:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Choose **Interfacing Options** by press the down arrow key on your keyboard, then press the **Enter** key.

    .. image:: img/image282.png
        :align: center

#. Then **I2C**.

    .. image:: img/image283.png
        :align: center

#. Use the arrow keys on the keyboard to select **<Yes>** -> **<OK>** to complete the setup of the I2C.

    .. image:: img/image284.png
        :align: center

#. Go to **Interfacing Options** again and select **SPI**.

    .. image:: img/image-spi1.png
        :align: center

#. Use the arrow keys on the keyboard to select **<Yes>** -> **<OK>** to complete the setup of the SPI.

    .. image:: img/image-spi2.png
        :align: center
