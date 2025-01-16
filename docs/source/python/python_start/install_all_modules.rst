.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _install_all_modules:

5. Instalar Todos los Módulos (Importante)
==============================================

#. Actualiza tu sistema.

    Asegúrate de estar conectado a Internet y actualiza tu sistema:

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt update
        sudo apt upgrade

    .. note::

        Los paquetes relacionados con Python3 deben estar instalados si estás utilizando la versión Lite del sistema operativo.

        .. raw:: html

            <run></run>

        .. code-block::
        
            sudo apt install git python3-pip python3-setuptools python3-smbus


#. Instalar el módulo ``robot-hat``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
        cd robot-hat
        sudo python3 setup.py install


#. Instalar el módulo ``vilib``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone -b picamera2 https://github.com/sunfounder/vilib.git
        cd vilib
        sudo python3 install.py


#. Descargar el código.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone https://github.com/sunfounder/pidog.git --depth 1

#. Instalar el módulo ``pidog``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd pidog
        sudo python3 setup.py install

    Este paso tomará un poco de tiempo, así que ten paciencia.

#. Ejecutar el script ``i2samp.sh``.

    Finalmente, debes ejecutar el script ``i2samp.sh`` para instalar los componentes necesarios para el amplificador i2s; de lo contrario, el robot no emitirá sonido.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog
        sudo bash i2samp.sh
        
    .. image:: img/i2s.png

    Escribe ``y`` y presiona ``Enter`` para continuar ejecutando el script.

    .. image:: img/i2s2.png

    Escribe ``y`` y presiona ``Enter`` para ejecutar ``/dev/zero`` en segundo plano.

    .. image:: img/i2s3.png

    Escribe ``y`` y presiona ``Enter`` para reiniciar la máquina.

    .. note::
        Si no hay sonido después de reiniciar, es posible que necesites ejecutar el script ``i2samp.sh`` varias veces.
