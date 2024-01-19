.. _i2c_spi_config:

6. I2CおよびSPIインターフェースの確認
========================================

Raspberry PiのI2CおよびSPIインターフェースを使用します。これらのインターフェースは、以前に ``robot-hat`` モジュールをインストールする際に有効にされているはずです。すべてが順調であることを確認するために、実際に有効になっているかどうかを確認しましょう。

#. 次のコマンドを入力します：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. キーボードの下矢印キーで **Interfacing Options** を選択し、 **Enter** キーを押します。

    .. image:: img/image282.png
        :align: center

#. 次に **I2C** を選択します。

    .. image:: img/image283.png
        :align: center

#. キーボードの矢印キーを使用して、 **<Yes>** -> **<OK>** を選択し、I2Cの設定を完了します。

    .. image:: img/image284.png
        :align: center

#. 再度 **Interfacing Options** に行き、 **SPI** を選択します。

    .. image:: img/image-spi1.png
        :align: center

#. キーボードの矢印キーを使用して、 **<Yes>** -> **<OK>** を選択し、SPIの設定を完了します。

    .. image:: img/image-spi2.png
        :align: center
