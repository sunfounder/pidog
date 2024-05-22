.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

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
