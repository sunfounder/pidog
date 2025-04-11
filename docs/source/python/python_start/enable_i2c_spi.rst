
.. _i2c_spi_config:

6. 检查 I2C 和 SPI 接口
========================================

我们将使用 Raspberry Pi 的 I2C 和 SPI 接口。安装 ``robot-hat`` 模块时应已启用这些接口。为确保一切正常，我们来检查它们是否确实已被启用。

#. 输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 通过键盘的下箭头键选择 **Interfacing Options**，然后按 **Enter** 键。

    .. image:: img/image282.png
        :align: center

#. 然后选择 **I2C** 。

    .. image:: img/image283.png
        :align: center

#. 使用键盘上的箭头键选择 **<Yes>** -> **<OK>** 完成 I2C 的设置。

    .. image:: img/image284.png
        :align: center

#. 再次进入 **Interfacing Options** 并选择 **SPI** 。

    .. image:: img/image-spi1.png
        :align: center

#. 使用键盘上的箭头键选择 **<Yes>** -> **<OK>** 完成 SPI 的设置。

    .. image:: img/image-spi2.png
        :align: center
