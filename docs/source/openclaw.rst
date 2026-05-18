.. _pidog_skill:

.. start_using_pidog

21. Uso de OpenClaw para controlar PiDog
========================================


**¿Qué es OpenClaw?**

Piénsalo como una versión mejorada de ChatGPT. Mientras que los chatbots tradicionales solo pueden hablar (generar texto), OpenClaw puede actuar. Entiende tus instrucciones en lenguaje natural y puede ejecutar operaciones en tu equipo, como ejecutar comandos, gestionar archivos y llamar a distintas herramientas.

Aquí hay algunos escenarios de aplicación fantásticos:

* **Asistente personal integral:** Permítele ayudarte a gestionar tu agenda, establecer recordatorios y seguir tareas. Solo necesitas decirlo en una aplicación de chat (como Telegram, WhatsApp) y él lo recordará y ejecutará.
* **“Pegamento” de automatización:** Puede actuar como intermediario para tus distintos servicios. Por ejemplo, puede vigilar un sitio web en busca de cambios de precio. Cuando detecte una caída, puede desencadenar automáticamente un flujo de trabajo de automatización n8n para enviarte una notificación por correo.
* **Asistente de desarrollo dedicado:** Te ayuda a gestionar servidores, ejecutar scripts y revisar registros. Puedes decir simplemente “Revisa la carga del sistema” y podrá conectarse por SSH a tu servidor, ejecutar el comando y devolverte los resultados.
* **Compañero de hardware:** Este es un caso de uso muy interesante. Puedes hacer que OpenClaw controle hardware conectado a una Raspberry Pi. Por ejemplo, un desarrollador lo usó para controlar una aspiradora robótica con un brazo mecánico, o incluso para ayudar a analizar datos de un simulador de carreras y mostrarlos en una pantalla LED. ¡El equipo oficial de Raspberry Pi incluso lo utilizó para construir un fotomatón automático para una boda, solo mediante conversación, sin escribir ni una sola línea de código!


.. important::

   El Raspberry Pi Zero 2W tiene solo 512 MB de RAM, mientras que OpenClaw requiere un mínimo de 1 GB. Por lo tanto, no puede funcionar correctamente. Se recomienda una Raspberry Pi 4/5 o superior.

Inicio rápido de OpenClaw
------------------------------

Si quieres experimentar el poder de OpenClaw lo más rápido posible, usa este método. Instalará automáticamente y lanzará un asistente de configuración interactivo.

1.  Abre la terminal en tu Raspberry Pi y ejecuta el siguiente comando directamente. Este comando descarga el script de instalación desde el sitio oficial y lo ejecuta:

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash
   
    .. note:: Debido a que las nuevas versiones se actualizan rápidamente, es normal que los pasos de instalación difieran ligeramente.

2.  El script descargará e instalará OpenClaw automáticamente.

    .. image:: /img/openclaw/install_open_claw.png


3.  Luego verás un aviso de seguridad que te preguntará si confías en OpenClaw. Cuando estés seguro de que es seguro y confiable, usa las teclas de flecha para seleccionar “Yes” y presiona Enter.

    .. image:: /img/openclaw/security_open_claw.png


4.  Selecciona Quick Start y luego presiona Enter.

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  Selecciona tu modelo y luego presiona Enter. Aquí usamos OpenAI como ejemplo.

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  Selecciona OpenAI API Key.

    .. image:: /img/openclaw/api_key_open_claw.png

7.  Pega la clave API ahora.

    .. image:: /img/openclaw/paste_api_key_open_claw.png

.. |link_openai_platform| raw:: html

    <a href="https://platform.openai.com/settings/organization/api-keys" target="_blank">OpenAI Platform</a>

8.  Ve a |link_openai_platform| e inicia sesión. En la página de **API keys**, haz clic en **Create new secret key**.

    .. image:: /img/openclaw/llm_openai_create.png

9.  Completa los datos (Owner, Name, Project y permisos si es necesario), luego haz clic en **Create secret key**.

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. Una vez creada la clave, cópiala de inmediato — no podrás verla de nuevo. Si la pierdes, tendrás que generar una nueva.

    .. image:: /img/openclaw/llm_openai_copy.png

11. Pega la clave en la configuración de OpenClaw.

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. Selecciona el modelo que deseas usar. En este ejemplo usaremos **Keep current**.

    .. image:: /img/openclaw/model_config_open_claw.png

13. A continuación, viene la selección de canal. Los canales se refieren a los servicios de comunicación compatibles con OpenClaw, como Telegram, WhatsApp, Discord y más. Usa la flecha hacia abajo para seleccionar la opción “Skip for now” y luego presiona Enter.

    .. image:: /img/openclaw/channel_open_claw.png

14. Luego se te pedirá configurar habilidades de inmediato. Selecciona “Yes” y presiona Enter.

    .. image:: /img/openclaw/config_skill_open_claw.png

15. Instala las habilidades que necesitas. En el ejemplo siguiente, seleccionamos la opción “Skip for now” (presiona la barra espaciadora para seleccionar) y luego presionamos Enter.

    .. image:: /img/openclaw/install_skill_open_claw.png


16. A continuación están los Hooks; marcaremos “command-logger” y “session-memory”.

    .. image:: /img/openclaw/hooks2_open_claw.png


17. La instalación ya está completa. Puedes iniciar OpenClaw seleccionando “Hatch in TUI” y presionando Enter.

   .. image:: /img/openclaw/hatch_open_claw.png


.. note:: 
   
   Puedes iniciar OpenClaw ingresando el siguiente comando:

    .. code-block:: bash

       openclaw tui

   Y puedes presionar ctrl+c dos veces para salir de la interfaz tui.

------------------------------------------------------------------------

Hacer que OpenClaw opere el PiDog
----------------------------------------------

**¿Qué es PiDog Skill?**

PiDog Skill es una extensión para OpenClaw que te permite controlar tu robot perro SunFounder PiDog V2 mediante lenguaje natural. En lugar de recordar parámetros complejos de línea de comandos, puedes decirle a OpenClaw lo que quieres que haga PiDog — como “haz que el perro se siente” o “pon las luces LED en morado” — y OpenClaw ejecutará automáticamente los comandos adecuados.

Estas son algunas cosas que puedes hacer con PiDog Skill:

* **Acciones básicas:** Haz que PiDog se ponga de pie, se siente, se tumbe, mueva la cola, ladre, camine hacia adelante/atrás o gire a la izquierda/derecha
* **Mantener postura:** Mantén a PiDog en una postura específica (como de pie) durante periodos prolongados
* **Control de luces LED:** Cambia los colores de los ojos con efectos como breath, listen, boom o luz sólida
* **Personalización de color:** Elige entre rojo, verde, azul, amarillo, morado, rosa, cian, blanco, naranja o colores hexadecimales personalizados

----------------------------------------------------------------

Requisitos previos
------------------------------

Antes de poder usar PiDog Skill con OpenClaw, asegúrate de tener:

1.  **PiDog V2** correctamente ensamblado y conectado a tu Raspberry Pi
2.  **OpenClaw** instalado y en funcionamiento
3.  Que los siguientes directorios existan en tu sistema:

   - ``~/pidog``
   - ``~/robot-hat``
   - ``~/vilib``

Puedes verificar la instalación ejecutando:

.. code-block:: bash

   python3 -c "import pidog"

Si este comando se ejecuta sin errores, estás listo para continuar.

----------------------------------------------------------------

Instalación de PiDog Skill
------------------------------

Sigue estos pasos para instalar PiDog Skill en OpenClaw:

1. **Crea el directorio de skills** (si aún no existe):

   .. code-block:: bash

      mkdir -p ~/.openclaw/workspace/skills/

2. **Copia los archivos de PiDog skill** al directorio de skills de OpenClaw:

   .. code-block:: bash

      cp -r ~/pidog/pidog-control ~/.openclaw/workspace/skills/pidog-control/

   .. note:: Reemplaza ``~/pidog-skill`` con la ruta real donde se encuentran tus archivos de PiDog skill.

3. **Verifica la instalación** comprobando los archivos de la skill:

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/pidog-control/scripts/

   Deberías ver ``pidog_ctl.py`` y ``pidog_rgb_ctl.py`` en la salida.

----------------------------------------------------------------

Prueba de PiDog Skill
------------------------------

Antes de usar la skill con OpenClaw, se recomienda probar la funcionalidad básica directamente desde la terminal.

**Paso 1: Comprueba el estado de PiDog**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py status

**Paso 2: Ejecuta una prueba segura**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py safe-test

**Paso 3: Prueba acciones básicas**

Haz que PiDog se siente:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action sit

Haz que PiDog se ponga de pie y mantenga la postura:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action stand --hold

Haz que PiDog ladre:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action bark

**Paso 4: Prueba las luces LED**

Prueba el efecto de luz boom con color morado:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple

Prueba otros efectos de luz:

.. code-block:: bash

   # Efecto breath con color rojo
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light breath --color red

   # Efecto listen con color azul
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light listen --color blue

   # Apagar las luces
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light off

----------------------------------------------------------------

Uso de PiDog Skill en OpenClaw
------------------------------

Una vez que hayas verificado que PiDog Skill funciona desde la línea de comandos, puedes comenzar a usarlo dentro de OpenClaw.

1. **Inicia la TUI de OpenClaw**:

   .. code-block:: bash

      openclaw tui

2. **Envía comandos en lenguaje natural** para controlar PiDog. Aquí tienes algunos ejemplos:

   * "Haz que el perro se siente"
   * "Haz que PiDog se ponga de pie y se mantenga"
   * "Mueve la cola del perro"
   * "Haz que el perro ladre"
   * "Pon las luces LED en morado con efecto boom"
   * "Configura las luces de los ojos con efecto breath en color rojo"
   * "Haz que PiDog camine hacia adelante"

3. **OpenClaw traducirá automáticamente** tu solicitud al comando apropiado y lo ejecutará en PiDog.

----------------------------------------------------------------

Acciones y Comandos Disponibles
----------------------------------

Aquí tienes la lista completa de acciones compatibles con PiDog Skill:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Acción
     - Descripción
   * - stand
     - Hace que PiDog se ponga de pie
   * - sit
     - Hace que PiDog se siente
   * - lie
     - Hace que PiDog se tumbe
   * - wag-tail
     - Mueve la cola de PiDog
   * - bark
     - Emite un ladrido
   * - forward
     - Camina hacia adelante
   * - backward
     - Camina hacia atrás


**Mantener Postura:**

Añade ``--hold`` a cualquier acción para mantener a PiDog en esa postura. Por ejemplo: "stand --hold"

**Efectos de Luz:**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Efecto
     - Descripción
   * - off
     - Apaga todas las luces LED
   * - breath
     - Efecto de respiración/pulsación suave
   * - listen
     - Modo de escucha reactiva
   * - boom
     - Efecto de explosión dinámica (el más llamativo)
   * - solid
     - Luz constante y fija (usa boom para un efecto más notable)

**Colores Compatibles:**

red, green, blue, yellow, purple, pink, cyan, white, orange, o códigos hexadecimales como ``#FF5733``

----------------------------------------------------------------

Resolución de Problemas
------------------------------

Problemas con OpenClaw
^^^^^^^^^^^^^^^^^^^^^^^^

P. Durante la instalación, aparece el error ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. ¿Qué debo hacer?

   Puedes ignorarlo por ahora, pero es posible que encuentres problemas en los siguientes pasos. Consulta cada uno según sea necesario en ese momento.


P. Cuando ejecuto ``openclaw tui``, aparece el error ``-bash: openclaw: command not found``. ¿Qué debo hacer?

   Ejecuta el siguiente comando:

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   Ahora deberías poder iniciar la interfaz tui con ``openclaw tui``.



P. En ``openclaw tui``, aparece ``not connected to gateway — message not sent`` o el mensaje ``gateway disconnected: closed``.

   Esto ocurre porque el servicio OpenClaw Gateway no está iniciado. Abre otra terminal y ejecuta el siguiente comando para iniciar OpenClaw Gateway:

   .. code-block:: bash

      openclaw gateway

   Luego reinicia ``openclaw tui`` y podrás usarlo directamente.


P. Quiero configurar el servicio OpenClaw Gateway para que se ejecute en segundo plano o se inicie automáticamente al arrancar. ¿Cómo lo hago?

   Normalmente, el servicio OpenClaw Gateway debería iniciarse automáticamente al arrancar. Si no lo hace, puedes iniciarlo manualmente con los siguientes comandos.

   1. Crea el directorio ``~/.config/systemd/user``:

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. Crea el archivo ``openclaw-gateway.service``:

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF


   3. Luego recarga la configuración de systemd:

   .. code-block:: bash

      systemctl --user daemon-reload

   4. Inicia el servicio:

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   En este punto, reinicia ``openclaw tui`` y podrás usarlo directamente.

   5. Actívalo para que se inicie al arrancar:

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


P. Mi OpenClaw no puede operar el sistema, ¿qué debo hacer?

   Un OpenClaw recién instalado puede no tener permisos para operar tu sistema Raspberry Pi por defecto; solo puede chatear. Necesitamos configurar los permisos manualmente.

   1.  Abre el archivo de configuración de OpenClaw:

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  Encuentra la opción ``tools`` y cambia ``profile`` y ``exec`` como se muestra.

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3.  Guarda y sal.

   4.  Ingresa el siguiente comando en la terminal para reiniciar OpenClaw Gateway:

      .. code-block:: bash

         openclaw gateway restart

   Ahora, OpenClaw debería tener permisos de lectura y escritura y podrá operar tu sistema Raspberry Pi.

Problemas con PiDog
^^^^^^^^^^^^^^^^^^^^^^^^


P. PiDog no responde a los comandos. ¿Qué debo hacer?

   Primero, verifica que PiDog esté correctamente conectado y encendido. Luego prueba el comando básico:

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py status

   Si esto falla, verifica que existan los directorios necesarios:

      - ``~/pidog``
      - ``~/robot-hat``
      - ``~/vilib``

P. La prueba ``import pidog`` falla.

   Esto significa que la biblioteca Python de PiDog no está correctamente instalada. Consulta la guía oficial de instalación de PiDog V2 para instalar las bibliotecas necesarias.

P. Las luces LED no funcionan como se espera.

   Si la luz sólida no se muestra claramente, usa el efecto ``boom`` en su lugar — produce los resultados más visibles:

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple

P. OpenClaw no reconoce la skill de PiDog.

   Recuérdale a OpenClaw que sincronice las skills diciendo en la TUI: *"Please rsync my skills"* o reinicia OpenClaw Gateway:

   .. code-block:: bash

      openclaw gateway restart

P. La acción de ladrido no suena bien.

   La acción de ladrido usa el sonido ``single_bark_1`` por defecto. Este es el comportamiento normal de PiDog V2.

----------------------------------------------------------------

.. end_using_pidog



