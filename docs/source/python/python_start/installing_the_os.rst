.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _install_os_sd:

2. Instalación del Sistema Operativo
============================================================

**Componentes Requeridos**

* Un ordenador personal
* Una tarjeta Micro SD y un lector de tarjetas

1. Instalar Raspberry Pi Imager
----------------------------------

#. Visita la página de descarga del software de Raspberry Pi en `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Elige la versión de Imager compatible con tu sistema operativo. Descarga y abre el archivo para iniciar la instalación.

    .. image:: img/os_install_imager.png
        :align: center

#. Durante la instalación, podría aparecer un mensaje de seguridad, dependiendo de tu sistema operativo. Por ejemplo, Windows podría mostrar un mensaje de advertencia. En tal caso, selecciona **Más información** y luego **Ejecutar de todas formas**. Sigue las instrucciones en pantalla para completar la instalación de Raspberry Pi Imager.

    .. image:: img/os_info.png
        :align: center

#. Abre la aplicación Raspberry Pi Imager haciendo clic en su ícono o escribiendo ``rpi-imager`` en tu terminal.

    .. image:: img/os_open_imager.png
        :align: center

2. Instalar el Sistema Operativo en la Tarjeta Micro SD
------------------------------------------------------------

#. Inserta tu tarjeta SD en tu computadora o portátil usando un lector de tarjetas.

#. Dentro del Imager, haz clic en **Raspberry Pi Device** y selecciona el modelo de Raspberry Pi de la lista desplegable.

    .. image:: img/os_choose_device.png
        :align: center

#. Selecciona **Operating System** y elige la versión recomendada del sistema operativo.

    .. image:: img/os_choose_os.png
        :align: center

#. Haz clic en **Choose Storage** y selecciona el dispositivo de almacenamiento adecuado para la instalación.

    .. note::

        Asegúrate de seleccionar el dispositivo de almacenamiento correcto. Para evitar confusión, desconecta cualquier otro dispositivo de almacenamiento adicional si hay varios conectados.

    .. image:: img/os_choose_sd.png
        :align: center

#. Haz clic en **NEXT** y luego en **EDIT SETTINGS** para personalizar los ajustes de tu sistema operativo.

    .. note::

        Si cuentas con un monitor para tu Raspberry Pi, puedes omitir los siguientes pasos y hacer clic en "Yes" para comenzar la instalación. Podrás ajustar otros parámetros más adelante en el monitor.

    .. image:: img/os_enter_setting.png
        :align: center

#. Define un **hostname** para tu Raspberry Pi.

    .. note::

        El hostname es el identificador de red de tu Raspberry Pi. Podrás acceder a tu Pi usando ``<hostname>.local`` o ``<hostname>.lan``.

    .. image:: img/os_set_hostname.png
        :align: center

#. Crea un **nombre de usuario** y **contraseña** para la cuenta de administrador del Raspberry Pi.

    .. note::

        Establecer un nombre de usuario y una contraseña únicos es fundamental para asegurar tu Raspberry Pi, ya que no tiene una contraseña predeterminada.

    .. image:: img/os_set_username.png
        :align: center

#. Configura la red LAN inalámbrica proporcionando el **SSID** y la **contraseña** de tu red.

    .. note::

        Ajusta el ``país de la red inalámbrica`` usando el código alfabético de dos letras según la `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondiente a tu ubicación.

    .. image:: img/os_set_wifi.png
        :align: center


#. Para conectarte remotamente a tu Raspberry Pi, habilita SSH en la pestaña de Servicios.

    * Para **autenticación por contraseña**, utiliza el nombre de usuario y la contraseña de la pestaña General.
    * Para la autenticación con clave pública, selecciona "Permitir solo autenticación con clave pública". Si ya tienes una clave RSA, se utilizará automáticamente. Si no, haz clic en "Ejecutar SSH-keygen" para generar un nuevo par de claves.

    .. image:: img/os_enable_ssh.png
        :align: center

#. El menú **Options** te permite configurar el comportamiento de Imager durante el proceso de escritura, como reproducir un sonido al finalizar, expulsar el medio una vez terminado y habilitar la telemetría.

    .. image:: img/os_options.png
        :align: center

#. Al terminar de introducir los ajustes de personalización del sistema operativo, haz clic en **Save** para guardarlos. Luego, haz clic en **Yes** para aplicarlos al escribir la imagen.

    .. image:: img/os_click_yes.png
        :align: center

#. Si la tarjeta SD contiene datos existentes, asegúrate de hacer una copia de seguridad para evitar pérdidas de información. Continúa haciendo clic en **Yes** si no es necesario hacer un respaldo.

    .. image:: img/os_continue.png
        :align: center

#. Cuando veas la ventana emergente "Write Successful", significa que la imagen ha sido completamente escrita y verificada. ¡Ahora estás listo para arrancar tu Raspberry Pi desde la tarjeta Micro SD!

    .. image:: img/os_finish.png
        :align: center

#. Ahora puedes insertar la tarjeta SD configurada con Raspberry Pi OS en la ranura para tarjetas microSD ubicada en la parte inferior de la Raspberry Pi.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center