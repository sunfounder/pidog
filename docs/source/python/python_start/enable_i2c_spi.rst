.. _i2c_spi_config:

6. Überprüfung der I2C- und SPI-Schnittstelle
=====================================================

Wir werden die I2C- und SPI-Schnittstellen des Raspberry Pi verwenden. Diese Schnittstellen sollten bereits aktiviert worden sein, als Sie das Modul ``robot-hat`` installiert haben. Um sicherzustellen, dass alles in Ordnung ist, überprüfen wir, ob sie tatsächlich aktiviert sind.

#. Geben Sie den folgenden Befehl ein:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Wählen Sie **Interfacing Options** aus, indem Sie die Abwärtspfeiltaste auf Ihrer Tastatur drücken und dann die **Enter**-Taste drücken.

    .. image:: img/image282.png
        :align: center

#. Wählen Sie dann **I2C** aus.

    .. image:: img/image283.png
        :align: center

#. Verwenden Sie die Pfeiltasten auf der Tastatur, um **<Ja>** -> **<OK>** auszuwählen, um die Einrichtung des I2C abzuschließen.

    .. image:: img/image284.png
        :align: center

#. Gehen Sie erneut zu **Interfacing Options** und wählen Sie **SPI** aus.

    .. image:: img/image-spi1.png
        :align: center

#. Verwenden Sie die Pfeiltasten auf der Tastatur, um **<Ja>** -> **<OK>** auszuwählen, um die Einrichtung des SPI abzuschließen.

    .. image:: img/image-spi2.png
        :align: center
