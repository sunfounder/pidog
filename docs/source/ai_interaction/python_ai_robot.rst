.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a los anuncios de nuevos productos y a vistas previas.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _ai_voice_assistant_robot:

20. Perro Asistente de Voz con IA
=========================================

Esta lección transforma tu Pidog en un **perro asistente de voz impulsado por IA** 🐶.  
El robot puede activarse con tu voz, entender lo que dices, responder con personalidad  
y expresar sus “sentimientos” a través de movimientos, gestos y efectos de iluminación LED.

Construirás un **compañero robótico totalmente interactivo** usando:

* **LLM**: Modelo de Lenguaje Extenso (por ejemplo, OpenAI GPT o Doubao) para conversaciones naturales.  
* **STT**: Voz a Texto para reconocimiento de voz.  
* **TTS**: Texto a Voz para respuestas vocales expresivas.  
* **Sensores + Acciones**: Sensor ultrasónico, visión por cámara (opcional), sensores táctiles y movimientos expresivos incorporados.

----

Antes de Comenzar
--------------------

Asegúrate de haber completado:

* :ref:`install_all_modules` — Instalar los módulos ``robot-hat``, ``vilib``, ``pidog`` y luego ejecutar el script ``i2samp.sh``.
* :ref:`test_piper` — Comprobar los idiomas compatibles de **Piper TTS**.  
* :ref:`test_vosk` — Comprobar los idiomas compatibles de **Vosk STT**.  
* :ref:`py_online_llm` — Este paso es **muy importante**: obtener tu clave de API de **OpenAI** o **Doubao**, o la clave de API de cualquier otro LLM compatible.

Ya deberías tener:

* Un **micrófono** y **altavoz** funcionando en tu Pidog.  
* Una **clave de API válida** guardada en ``secret.py``.  
* Una conexión de red estable (se recomienda una **conexión por cable** para mayor estabilidad).

----

Ejecutar el Ejemplo
-----------------------------

Ambas versiones de idioma están ubicadas en el mismo directorio:

.. code-block:: bash

   cd ~/pidog/examples

**Versión en inglés** (OpenAI GPT, instrucciones en inglés):

.. code-block:: bash

   sudo python3 20_voice_active_dog_gpt.py

* LLM: ``OpenAI GPT-4o-mini``  
* TTS: ``en_US-ryan-low`` (Piper)  
* STT: Vosk (``en-us``)

Palabra de activación:

.. code-block::

   "Hey buddy"


---
**Versión en chino** (Doubao, instrucciones en chino):

.. code-block:: bash

   sudo python3 20_voice_active_dog_doubao_cn.py

* LLM: ``Doubao-seed-1-6-250615``  
* TTS: ``zh_CN-huayan-x_low`` (Piper)  
* STT: Vosk (``cn``)

Palabra de activación:

.. code-block::

   "你好 旺财"

.. note::

   Puedes modificar la **palabra de activación** y el **nombre del robot** en el código:
   ``NAME = "Buddy"`` o ``NAME = "旺财"``  
   ``WAKE_WORD = ["hey buddy"]`` o ``WAKE_WORD = ["你好 旺财"]``

----

Qué Sucederá
-----------------

Cuando ejecutes este ejemplo correctamente:

* El robot **espera la palabra de activación** (por ejemplo, “Hey Buddy”，“你好 旺财”).  
* Cuando escucha la palabra de activación:

  * La tira LED se vuelve **rosa (respiración)** como señal de activación.  
  * El robot te saluda con la respuesta de activación establecida —  
    por ejemplo, “¡Hola!” (a través de Piper TTS).

* Luego comienza a **escuchar tu voz** mediante Vosk STT (o acepta entrada por teclado si está habilitado).  

* Después de reconocer lo que dijiste, el sistema:

  * Captura un **fotograma de la cámara** (porque ``WITH_IMAGE = True``) y envía tu mensaje + imagen al **LLM** (OpenAI ``gpt-4o-mini``).  
  * El LED cambia a **amarillo (escuchando/procesando)** mientras el modelo piensa.  
  * La respuesta del modelo se divide en dos partes:

    - Texto antes de ``ACTIONS:`` → se pronuncia en voz alta.  
    - Palabras clave después de ``ACTIONS:`` → se asignan a movimientos del robot.

  * El robot **ejecuta esas acciones** a través de ``ActionFlow``.  
  * Cuando las acciones terminan, el robot **vuelve a la postura SENTADO (SIT)** y apaga los LEDs.

* Si el **sensor ultrasónico detecta un obstáculo** a menos de 10 cm:

  - Se inyecta un mensaje: ``<<<Ultrasonic sense too close: {distance}cm>>>``  
  - El robot retrocede automáticamente: ``ACTIONS: backward``  
  - **La entrada de imagen se desactiva** para esta ronda.

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

   You: What do you see in front of you?
   Robot: I can see a notebook and a blue mug on the table.
   ACTIONS: think

   You: Do a little nod for me.
   Robot: Of course. Watch my majestic nod.
   ACTIONS: nod

   (Front-to-rear touch on the head)
   Robot: Ooooh, that’s nice!
   ACTIONS: nod

   (Moving too close)
   Robot: Hey hey—too close! Backing up for safety.
   ACTIONS: backward


----

Cambio a Otros LLM o TTS
------------------------------

Puedes cambiar fácilmente a otros LLM, TTS o idiomas de STT con solo unos pocos ajustes:

* LLM compatibles:

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Comprueba los idiomas compatibles con **Piper TTS**.  
* :ref:`test_vosk` — Comprueba los idiomas compatibles con **Vosk STT**.  

Para cambiar, simplemente modifica la parte de inicialización en el código:

.. code-block:: python

  from pidog.llm import OpenAI as LLM

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # Configurar modelos e idiomas
  TTS_MODEL = "en_US-ryan-low"
  STT_LANGUAGE = "en-us"

----

Solución de Problemas
------------------------------

* **El robot no responde a la palabra de activación**  

  * Verifica si el micrófono funciona.  
  * Asegúrate de que ``WAKE_ENABLE = True``.  
  * Ajusta la palabra de activación para que coincida con tu pronunciación.

* **No hay sonido en el altavoz**
 
  * Verifica la configuración del modelo TTS.  
  * Prueba Piper o Espeak manualmente.  
  * Revisa la conexión y el volumen del altavoz.

* **Error o tiempo de espera de la clave API** 
 
  * Verifica tu clave en ``secret.py``.  
  * Asegura una conexión de red estable.  
  * Confirma que el LLM sea compatible.

* **El sensor ultrasónico se activa inesperadamente.**  

  * Revisa la altura y el ángulo de instalación del sensor.  
  * Ajusta el umbral de distancia ``TOO_CLOSE`` en el código.
