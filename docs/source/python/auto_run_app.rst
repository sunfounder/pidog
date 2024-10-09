.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

3. Juego Rápido con la Aplicación
=================================================

Ahora que tu PiDog está configurado y listo para funcionar, esta sección es perfecta para quienes desean explorar rápidamente todas sus funciones. Te guiaremos en el proceso de instalación de la aplicación, la conexión de tu PiDog con tu dispositivo móvil y la activación de las múltiples funcionalidades divertidas que ofrece, todo al alcance de tu mano. Al final de este capítulo, podrás controlar y disfrutar de tu PiDog desde tu dispositivo con total confianza. ¡Empecemos a sumergirnos en el mundo de la robótica interactiva!

#. Instala el módulo ``sunfounder-controller``.

    Los módulos robot-hat, vilib y picar-x deben estar instalados previamente; para más detalles, consulta: :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Ejecuta los siguientes comandos:

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/bin
        sudo bash pidog_app_install.sh


#. Reinicia PiDog.

#. Instala `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ desde la **App Store (iOS)** o **Google Play (Android)**.

#. Conéctate a la red WLAN ``pidog``.

    Conecta tu dispositivo móvil a la red de área local (LAN) generada por PiDog. De esta manera, tu dispositivo móvil y PiDog estarán en la misma red, lo que facilitará la comunicación entre las aplicaciones y el PiDog.

    * Encuentra ``pidog`` en las redes WLAN de tu dispositivo móvil (tablet), ingresa la contraseña ``12345678`` y conéctate.

    * El modo de conexión predeterminado es AP. Después de conectarte, aparecerá un mensaje indicando que no hay acceso a Internet en esta red; elige continuar con la conexión.

        .. image:: img/app_no_internet.png

#. Abre la aplicación ``Sunfounder Controller``. Haz clic en el icono + para agregar un control remoto.

    .. image:: img/app1.png

#. Hay controles preconfigurados para algunos productos; selecciona **PiDog**, asígnale un nombre o simplemente toca **Confirmar**.

    .. image:: img/app_preset.jpg

#. Una vez dentro, la aplicación buscará automáticamente el **Mydog**. Después de unos segundos, aparecerá un mensaje indicando “Conectado con éxito”.

    .. image:: img/app_auto_connect.jpg

    .. note::

        * También puedes hacer clic manualmente en el botón |app_connect|. Espera unos segundos y aparecerá MyDog (IP); haz clic para conectarte.

            .. image:: img/sc_mydog.jpg

#. Ejecuta el Controlador.

    * Cuando veas el mensaje "Conectado con éxito", toca el botón ▶ en la esquina superior derecha.

    * La transmisión de la cámara aparecerá en la aplicación, y ahora podrás controlar tu PiDog con los widgets disponibles.

        .. image:: img/sc_run.jpg

Aquí tienes las funciones de los widgets:

* A: Detectar la distancia de obstáculos, es decir, la lectura del módulo ultrasónico.
* C: Activar/desactivar la detección facial.
* D: Controlar el ángulo de inclinación de la cabeza de PiDog.
* E: Sentarse.
* F: Pararse.
* G: Acostarse.
* I: Rascar la cabeza de PiDog.
* N: Ladrar.
* O: Mover la cola.
* P: Jadear.
* K: Controlar el movimiento de PiDog (adelante, atrás, izquierda y derecha).
* Q: Controlar la orientación de la cabeza de PiDog.
* J: Cambiar al modo de control por voz. Se admiten los siguientes comandos de voz:

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

Configuración del Programa de la APP
--------------------------------------------

Puedes introducir los siguientes comandos para modificar la configuración del modo de la APP.

.. code-block::

    pidog_app <OPTION> [input]

**OPCIÓN**
    * ``-h`` ``help`` : ayuda, mostrar este mensaje.
    * ``start`` ``restart`` : reiniciar el servicio pidog_app.
    * ``stop`` : detener el servicio pidog_app.
    * ``disable`` : deshabilitar el programa app_controller en el arranque.
    * ``enable`` : habilitar el programa app_controller en el arranque.
    * ``close_ap`` : cerrar el punto de acceso, deshabilitar el arranque automático del hotspot y cambiar a modo STA.
    * ``open_ap`` : abrir el punto de acceso, habilitar el arranque automático del hotspot.
    * ``ssid`` : establecer el nombre de la red del hotspot.
    * ``psk`` : establecer la contraseña del hotspot.
    * ``country`` : establecer el código de país del hotspot.

