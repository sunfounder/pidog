.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _remote_desktop:

Acceso remoto a escritorio para Raspberry Pi
=================================================

Para aquellos que prefieren una interfaz gráfica (GUI) en lugar del acceso mediante línea de comandos, Raspberry Pi admite la funcionalidad de escritorio remoto. Esta guía te guiará a través de la configuración y uso de VNC (Virtual Network Computing) para acceder de forma remota.

Te recomendamos utilizar `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ para este propósito.

**Habilitar el servicio VNC en Raspberry Pi**

El servicio VNC viene preinstalado en Raspberry Pi OS, pero está desactivado por defecto. Sigue estos pasos para activarlo:

#. Ingresa el siguiente comando en el terminal de Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block::

        sudo raspi-config

#. Navega hasta **Opciones de Interfaz** utilizando la tecla de flecha hacia abajo y luego presiona **Enter**.

    .. image:: img/config_interface.png
        :align: center

#. Selecciona **VNC** de las opciones.

    .. image:: img/vnc.png
        :align: center

#. Utiliza las teclas de flecha para elegir **<Sí>** -> **<OK>** -> **<Finalizar** y así completar la activación del servicio VNC.

    .. image:: img/vnc_yes.png
        :align: center

**Iniciar sesión a través de VNC Viewer**

#. Descarga e instala `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ en tu computadora personal.

#. Una vez instalado, abre VNC Viewer. Introduce el nombre del host o la dirección IP de tu Raspberry Pi y presiona Enter.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Cuando se te solicite, ingresa el nombre de usuario y la contraseña de tu Raspberry Pi, luego haz clic en **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Después de unos segundos, se mostrará el escritorio de Raspberry Pi OS. Ahora puedes abrir el terminal para comenzar a ingresar comandos.

    .. image:: img/bookwarm.png
        :align: center
