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

Instalar Todos los Módulos (Importante)
==============================================

.. note::

    Si estás utilizando la versión Lite del sistema operativo, debes instalar los paquetes relacionados con Python3.

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt install git python3-pip python3-setuptools python3-smbus

#. Instalar el módulo ``robot-hat``.

   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
       cd robot-hat
       sudo python3 install.py

#. Instalar el módulo ``vilib``.

   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone https://github.com/sunfounder/vilib.git
       cd vilib
       sudo python3 install.py

#. Instalar el módulo ``pidog``.

   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone https://github.com/sunfounder/pidog.git --depth 1
       cd pidog
       sudo pip3 install . --break

   Este paso tomará un poco de tiempo, así que ten paciencia.

#. Ejecutar el script ``i2samp.sh``.

   Finalmente, necesitas ejecutar el script ``i2samp.sh`` para instalar los componentes necesarios para el amplificador i2s; de lo contrario, el robot no tendrá sonido.
   
   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/robot-hat
       sudo bash i2samp.sh
   
   Escriba ``y`` y presione **Enter** tres veces para continuar el script, iniciar ``/dev/zero`` en segundo plano y luego reiniciar el sistema.

   
   .. note::
       Si no hay sonido después de reiniciar, puede que necesites ejecutar el script ``i2samp.sh`` varias veces.

       Además, si intentas reproducir audio directamente (por ejemplo, con ``aplay``) sin ejecutar antes un ejemplo de PiDog, debes activar el altavoz manualmente:

       .. code-block:: bash

          robot_hat enable_speaker

       Esto solo necesita hacerse una vez por arranque. Ejecutar cualquier ejemplo de PiDog (que inicializa ``Pidog()``) lo hace automáticamente.
