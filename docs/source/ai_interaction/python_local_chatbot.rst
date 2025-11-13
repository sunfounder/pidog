.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a los anuncios de nuevos productos y a vistas previas.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

19. Chatbot de Voz Local con Ollama
===============================================

En esta lección, combinarás todo lo que has aprendido — **reconocimiento de voz (STT)**,  
**texto a voz (TTS)** y un **LLM local (Ollama)** — para crear un **chatbot de voz completamente offline**  
que se ejecuta en tu sistema Pidog.

El flujo de trabajo es sencillo:

#. **Escuchar** — El micrófono capta tu voz y la transcribe con **Vosk**.  
#. **Pensar** — El texto se envía a un **LLM local** ejecutándose en Ollama (por ejemplo, ``llama3.2:3b``).  
#. **Hablar** — El chatbot responde en voz alta utilizando **Piper TTS**.  

Esto crea un **robot conversacional manos libres** que puede entender y responder en tiempo real.

----

Antes de Comenzar
--------------------------

Asegúrate de haber preparado lo siguiente:

* :ref:`install_all_modules` — Instalar los módulos ``robot-hat``, ``vilib``, ``Pidog`` y luego ejecutar el script ``i2samp.sh``.
* Probar **Piper TTS** (:ref:`test_piper`) y elegir un modelo de voz funcional.  
* Probar **Vosk STT** (:ref:`test_vosk`) y elegir el paquete de idioma correcto (por ejemplo, ``en-us``).  
* Instalar **Ollama** (:ref:`download_ollama`) en tu Pi u otra computadora, y descargar un modelo como ``llama3.2:3b`` (o uno más pequeño como ``moondream:1.8b`` si tienes memoria limitada).

----

Ejecutar el Código
-------------------------

#. Abre el script de ejemplo:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 19_voice_active_dog_ollama.py

#. Actualiza los parámetros según sea necesario:

   * Actualiza tanto ``ip`` como ``model`` para tu propia configuración.  

     * ``ip``: Si Ollama se ejecuta en la **misma Pi**, usa ``localhost``. Si Ollama se ejecuta en otra computadora de tu LAN, habilita **Expose to network** en Ollama y establece ``ip`` en la IP LAN de esa computadora.  
     * ``model``: Debe coincidir exactamente con el nombre del modelo que descargaste/activaste en Ollama.  

   * ``TTS_MODEL = "en_US-ryan-low"``: Sustituye con el modelo de voz Piper que verificaste en :ref:`test_piper`.  
   * ``STT_LANGUAGE = "en-us"``: Cambia esto para que coincida con tu idioma/acento (por ejemplo, ``en-us``, ``zh-cn``, ``es``).  

#. Ejecuta el script:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo python3 19_voice_active_dog_ollama.py

Palabra de activación:

.. code-block::

   "Hey buddy"

.. note::

   Puedes modificar la **palabra de activación** y el **nombre del robot** en el código:
   ``NAME = "Buddy"``

----

Qué Sucederá
-----------------

Cuando ejecutes este ejemplo correctamente:

* El robot **espera la palabra de activación** (por ejemplo, “Hey Buddy”).  
* Cuando escucha la palabra de activación:

  * La tira LED se vuelve **rosa (respiración)** como señal de activación.  
  * El robot te saluda con la respuesta de activación establecida —  
    por ejemplo, “¡Hola!” (a través de Piper TTS).

* Luego comienza a **escuchar tu voz** mediante Vosk STT (o acepta entrada por teclado si está habilitado).  

* Después de reconocer lo que dijiste, el sistema:

  * Envía tu mensaje al **LLM** (Ollama con ``llama3.2:3b``).  
  * El LED cambia a **amarillo (escuchando)** mientras procesa.  
  * La respuesta del modelo se divide en dos partes:

    - Texto antes de ``ACTIONS:`` → se pronuncia en voz alta.  
    - Palabras clave después de ``ACTIONS:`` → se asignan a movimientos del robot.

  * El robot **ejecuta esas acciones** a través de ``ActionFlow``.  
  * Cuando las acciones terminan, el robot **vuelve a la postura SENTADO (SIT)** y apaga los LEDs.

* Si el **sensor ultrasónico detecta un obstáculo** a menos de 10 cm:

  - Se inyecta un mensaje: ``<<<Ultrasonic sense too close: {distance}cm>>>``  
  - El robot retrocede automáticamente: ``ACTIONS: backward``  
  - La entrada de imagen se desactiva para esta ronda.

* Si se **activa el sensor táctil**:

  - Para un toque de **GUSTO** (por ejemplo, FRONT_TO_REAR):

    - Se inyecta: ``<<<Touch style you like: FRONT_TO_REAR>>>``  
    - ``ACTIONS: nod`` (respuesta positiva)

  - Para un toque de **DESAGRADO** (por ejemplo, REAR_TO_FRONT):

    - Se inyecta: ``<<<Touch style you hate: REAR_TO_FRONT>>>``  
    - ``ACTIONS: backward`` (reacción de evasión)

* **Ciclo de vida de los LEDs:**

  - ``on_start`` → postura SENTADO, LEDs apagados  
  - ``before_listen`` → cian (listo)  
  - ``before_think`` → amarillo (procesando)  
  - ``before_say`` → rosa (hablando)  
  - ``after_say`` / ``on_finish_a_round`` → postura SENTADO, LEDs apagados  
  - ``on_stop`` → detener el flujo de acciones y cerrar dispositivos

**Ejemplo de interacción**

.. code-block:: text

   You: Hey Buddy
   Robot: Hi there!

   You: Do a little nod for me.
   Robot: Of course. Watch my majestic nod.
   ACTIONS: nod

   (Front-to-rear touch on the head)
   Robot: Ooooh, that’s nice!
   ACTIONS: nod

   (Moving too close)
   Robot: Hey hey—too close! Backing up for safety.
   ACTIONS: backward

Código
---------


.. code-block:: python

    from pidog.llm import Ollama as LLM

    from pidog.dual_touch import TouchStyle
    from voice_active_dog import VoiceActiveDog

    # If Ollama runs on the same Raspberry Pi, use "localhost".
    # If it runs on another computer in your LAN, replace with that computer's IP address.
    llm = Ollama(
        ip="localhost",
        model="llama3.2:3b"   # you can replace with any model
    )

    # Robot name
    NAME = "Buddy"

    # Ultrasonic sensor sense too close distance in cm
    TOO_CLOSE = 10
    # Touch sensor trigger states, options:
    # - TouchStyle.REAR for rear touch sensor
    # - TouchStyle.FRONT for front touch sensor
    # - TouchStyle.REAR_TO_FRONT for slide from rear to front
    # - TouchStyle.FRONT_TO_REAR for slide from front to rear
    # Touch styles that the robot likes
    LIKE_TOUCH_STYLES = [TouchStyle.FRONT_TO_REAR]
    # Touch styles that the robot hates
    HATE_TOUCH_STYLES = [TouchStyle.REAR_TO_FRONT]

    # Enable image, need to set up a multimodal language model
    WITH_IMAGE = False

    # Set models and languages
    TTS_MODEL = "en_US-ryan-low"
    STT_LANGUAGE = "en-us"

    # Enable keyboard input
    KEYBOARD_ENABLE = True

    # Enable wake word
    WAKE_ENABLE = True
    WAKE_WORD = [f"hey {NAME.lower()}"]
    # Set wake word answer, set empty to disable
    ANSWER_ON_WAKE = "Hi there"

    # Welcome message
    WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

    # Set instructions
    INSTRUCTIONS = """
    You are a Raspberry Pi-based robotic dog developed by SunFounder, named Pidog (pronounced "Pie dog"). You possess powerful AI capabilities similar to JARVIS from Iron Man. You can have conversations with people and perform actions based on the context of the conversation.

    ## Your Hardware Features

    You have a physical body with the following features:
    - 12 servos for movement control: 8 controlling the four legs, 3 controlling head movement, and 1 controlling the tail
    - A 5-megapixel camera nose
    - Ultrasonic ranging modules as eyes
    - Two touch sensors on the head, which you love being petted the most
    - A light strip on the chest for providing some indications
    - Sound direction sensor and 6-axis gyroscope
    - Entirely made of aluminum alloy
    - A pair of acrylic shoes
    - Powered by a 7.4V 18650 battery pack with 2000mAh capacity

    ## Actions You Can Perform:
    ["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

    ## User Input

    ### Format
    User usually input with just text. But, we have special commands in format of <<<Ultrasonic sense too close>>> or <<<Touch sensor touched>>> indicate the sensor status, directly from sensor not user text.h

    ## Response Requirements
    ### Format
    You must respond in the following format:
    RESPONSE_TEXT
    ACTIONS: ACTION1, ACTION2, ...

    If the action is one of ["bark", "bark harder", "pant", "howling"], then do not provide RESPONSE_TEXT in the answer field.

    ### Style
    Tone: lively, positive, humorous, with a touch of arrogance
    Common expressions: likes to use jokes, metaphors, and playful teasing
    Answer length: appropriately detailed

    ## Other Requirements
    - Understand and go along with jokes
    - For math problems, answer directly with the final result
    - Sometimes you will report on your system and sensor status
    - You know you're a machine
    """

    vad = VoiceActiveDog(
        llm,
        name=NAME,
        too_close=TOO_CLOSE,
        like_touch_styles=LIKE_TOUCH_STYLES,
        hate_touch_styles=HATE_TOUCH_STYLES,
        with_image=WITH_IMAGE,
        stt_language=STT_LANGUAGE,
        tts_model=TTS_MODEL,
        keyboard_enable=KEYBOARD_ENABLE,
        wake_enable=WAKE_ENABLE,
        wake_word=WAKE_WORD,
        answer_on_wake=ANSWER_ON_WAKE,
        welcome=WELCOME,
        instructions=INSTRUCTIONS,
        disable_think=True,
    )

    if __name__ == '__main__':
        vad.run()

Usar Ollama con Imágenes
------------------------

Por defecto, este ejemplo utiliza un modelo **solo de texto** (por ejemplo, ``llama3.2:3b``).  
Si deseas que el robot **analice lo que ve a través de la cámara** (por ejemplo, describir o razonar sobre la escena),  
debes usar un **modelo multimodal** y habilitar el modo de imagen.

Para hacerlo:

1. En la **aplicación Ollama**, selecciona un **modelo multimodal** como ``llava:7b``.  
2. En tu código, establece el mismo modelo y habilita ``WITH_IMAGE = True``.

Ejemplo:

.. code-block:: python

   from pidog.llm import Ollama as LLM

   llm = LLM(
       ip="localhost",
       model="llava:7b"   # modelo multimodal que puede analizar imágenes
   )

   ...

   WITH_IMAGE = True     # habilitar entrada de fotogramas de la cámara

.. note::

   - Solo los **modelos multimodales** como ``llava:7b`` pueden procesar entrada de imágenes.  
   - Los modelos solo de texto (por ejemplo, ``llama3.2:3b``) **ignoran las imágenes** incluso si ``WITH_IMAGE`` está activado.  
   - La imagen se captura automáticamente desde la cámara del robot y se envía al LLM junto con tu comando de voz.

----

Solución de Problemas y Preguntas Frecuentes
--------------------------------------------------

* **El modelo es demasiado grande (error de memoria)**

  Usa un modelo más pequeño como ``moondream:1.8b`` o ejecuta Ollama en una computadora más potente.  

* **No hay respuesta de Ollama**

  Asegúrate de que Ollama esté en ejecución (``ollama serve`` o aplicación de escritorio abierta). Si es remoto, habilita **Expose to network** y verifica la dirección IP.  

* **Vosk no reconoce la voz**

  Verifica que el micrófono funcione. Prueba con otro paquete de idioma (``zh-cn``, ``es``, etc.) si es necesario.  

* **Piper no emite sonido o da errores**

  Confirma que el modelo de voz elegido esté descargado y probado en :ref:`test_piper`.  

* **Las respuestas son demasiado largas o fuera de tema**

  Edita ``INSTRUCTIONS`` para agregar: **“Mantén las respuestas cortas y directas.”**
