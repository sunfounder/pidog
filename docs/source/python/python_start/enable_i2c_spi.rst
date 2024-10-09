.. note::

    Ciao, benvenuto nella Community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime speciali.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _i2c_spi_config:

6. Verifica delle interfacce I2C e SPI
========================================

Utilizzeremo le interfacce I2C e SPI del Raspberry Pi. Queste interfacce dovrebbero essere già abilitate durante l'installazione del modulo ``robot-hat``. Per assicurarci che tutto sia configurato correttamente, verifichiamo se sono effettivamente attive.

#. Inserisci il seguente comando:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Seleziona **Interfacing Options** premendo il tasto freccia in basso sulla tastiera, quindi premi il tasto **Enter**.

    .. image:: img/image282.png
        :align: center

#. Seleziona poi **I2C**.

    .. image:: img/image283.png
        :align: center

#. Usa i tasti freccia della tastiera per selezionare **<Yes>** -> **<OK>** per completare la configurazione dell'I2C.

    .. image:: img/image284.png
        :align: center

#. Torna su **Interfacing Options** e seleziona **SPI**.

    .. image:: img/image-spi1.png
        :align: center

#. Usa i tasti freccia della tastiera per selezionare **<Yes>** -> **<OK>** per completare la configurazione dello SPI.

    .. image:: img/image-spi2.png
        :align: center
