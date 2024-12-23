.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

12. Juega con PiDog usando la APP
======================================

En este ejemplo, usaremos la aplicación **SunFounder Controller** para controlar a PiDog.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/app_control.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

Primero necesitas descargar la APP en tu teléfono/tableta, luego conectarte a la red WLAN como PiDog y, finalmente, crear tu propio control remoto en el SunFounder Controller para controlar PiDog.

.. _app_control:

Controla a PiDog con la aplicación
----------------------------------------

#. Instala `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ desde la **App Store (iOS)** o **Google Play (Android)**.

#. Instala el módulo ``sunfounder-controller``.

    Los módulos ``robot-hat``, ``vilib`` y ``picar-x`` deben estar instalados previamente. Para más detalles, consulta: :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Ejecuta el código.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 12_app_control.py

    Después de ejecutar el código, verás el siguiente mensaje, lo que indica que tu PiDog ha iniciado la comunicación en red con éxito.

    .. code-block:: 

        Running on: http://192.168.18.138:9000/mjpg

        * Serving Flask app "vilib.vilib" (lazy loading)
        * Environment: development
        * Debug mode: off
        * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

#. Conecta ``PiDog`` y ``SunFounder Controller``.

    * Conecta tu tablet o teléfono a la red WLAN en la que se encuentra PiDog.

    * Abre la aplicación ``SunFounder Controller``. Haz clic en el icono + para añadir un controlador.

        .. image:: img/app1.png

    * Hay controles predefinidos para algunos productos, aquí selecciona **PiDog**. Asigna un nombre o simplemente toca **Confirmar**.

        .. image:: img/app_preset.jpg

    * Una vez dentro, la aplicación buscará automáticamente a **Mydog**. Al cabo de unos segundos, verás un mensaje indicando “Conectado con éxito.”

        .. image:: img/app_auto_connect.jpg

    .. note::

        * También puedes hacer clic manualmente en el botón |app_connect|. Espera unos segundos, aparecerá MyDog (IP), haz clic en él para conectarte.

            .. image:: img/sc_mydog.jpg

#. Ejecuta el controlador.

    * Cuando aparezca el mensaje “Conectado con éxito”, toca el botón ▶ en la esquina superior derecha.

    * Verás la imagen capturada por la cámara en la aplicación y ahora podrás controlar a PiDog usando estos widgets.

        .. image:: img/sc_run.jpg

Aquí tienes las funciones de los diferentes widgets:

* A: Detectar la distancia de los obstáculos, es decir, la lectura del módulo ultrasónico.
* C: Activar/desactivar la detección de rostros.
* D: Controlar el ángulo de inclinación de la cabeza de PiDog.
* E: Sentarse.
* F: Ponerse de pie.
* G: Acostarse.
* I: Rascar la cabeza de PiDog.
* N: Ladrar.
* O: Mover la cola.
* P: Jadear.
* K: Controlar el movimiento de PiDog (avanzar, retroceder, girar a la izquierda y a la derecha).
* Q: Controlar la orientación de la cabeza de PiDog.
* J: Cambiar al modo de control por voz. Soporta los siguientes comandos de voz:

    * ``forward``
    * ``backward``
    * ``turn left``
    * ``turn right``
    * ``trot``
    * ``stop``
    * ``lie down`` 
    * ``stand up``
    * ``sit``
    * ``bark``
    * ``bark harder``
    * ``pant``
    * ``wag tail``
    * ``shake head``
    * ``stretch``
    * ``doze off``
    * ``push-up``
    * ``howling``
    * ``twist body``
    * ``scratch``
    * ``handshake``
    * ``high five``

Inicio automático al encenderse
-----------------------------------

Cuando controles a PiDog a través de la aplicación, no querrás tener que iniciar sesión en la Raspberry Pi y ejecutar manualmente ``12_app_control.py`` cada vez antes de conectarte a la aplicación.

Hay una forma más práctica de hacerlo. Puedes configurar a PiDog para que ejecute automáticamente ``12_app_control.py`` cada vez que se encienda. De este modo, podrás conectarte directamente a PiDog desde la aplicación y controlarlo fácilmente.

¿Cómo configurarlo?

#. Ejecuta los siguientes comandos para instalar y configurar la aplicación ``pidog_app`` y establecer la conexión WiFi para PiDog.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/bin
        sudo bash pidog_app_install.sh

#. Al finalizar, escribe ``y`` para reiniciar PiDog.

    .. image:: img/auto_start.png

#. #. Después de reiniciar, PiDog iniciará automáticamente el script de control. Luego podrás :ref:`app_control`.

.. warning::

    Si deseas ejecutar otros scripts, primero ejecuta ``pidog_app disable`` para desactivar la función de inicio automático.


.. Configuración del Programa de la APP
.. ----------------------------------------

.. Puedes usar los siguientes comandos para modificar la configuración del modo APP.

.. .. code-block::

..     pidog_app <OPCIÓN> [input]

.. **OPCIÓN**
..     * ``-h`` ``help``: ayuda, muestra este mensaje
..     * ``start`` ``restart``: reiniciar el servicio ``pidog_app``
..     * ``stop``: detener el servicio ``pidog_app``
..     * ``disable``: desactivar el inicio automático del programa ``app_controller`` al arrancar
..     * ``enable``: activar el inicio automático del programa ``app_controller`` al arrancar
..     * ``close_ap``: cerrar el punto de acceso, desactivar el inicio automático del hotspot al arrancar y cambiar al modo ``sta``
..     * ``open_ap``: abrir el punto de acceso, activar el inicio automático del hotspot al arrancar
..     * ``ssid``: configurar el ssid (nombre de red) del punto de acceso
..     * ``psk``: configurar la contraseña del punto de acceso
..     * ``country``: configurar el código de país del punto de acceso

