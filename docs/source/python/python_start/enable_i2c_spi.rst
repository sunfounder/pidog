.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _i2c_spi_config:

6. Verificar la Interfaz I2C y SPI
========================================

Usaremos las interfaces I2C y SPI de la Raspberry Pi. Estas interfaces deberían haberse habilitado al instalar el módulo ``robot-hat`` anteriormente. Para asegurarnos de que todo está en orden, vamos a comprobar si realmente están activadas.

#. Introduce el siguiente comando:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Elige **Interfacing Options** presionando la tecla de flecha hacia abajo en tu teclado y luego presiona la tecla **Enter**.

    .. image:: img/image282.png
        :align: center

#. Luego selecciona **I2C**.

    .. image:: img/image283.png
        :align: center

#. Utiliza las teclas de flecha para seleccionar **<Sí>** -> **<OK>** y así completar la configuración del I2C.

    .. image:: img/image284.png
        :align: center

#. Ve nuevamente a **Interfacing Options** y selecciona **SPI**.

    .. image:: img/image-spi1.png
        :align: center

#. Utiliza las teclas de flecha para seleccionar **<Sí>** -> **<OK>** y así completar la configuración del SPI.

    .. image:: img/image-spi2.png
        :align: center
