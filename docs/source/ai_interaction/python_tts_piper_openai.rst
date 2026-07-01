.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a los anuncios de nuevos productos y a vistas previas.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

15. TTS con Piper y OpenAI
========================================================

En la lección anterior, probamos dos motores TTS integrados en Raspberry Pi (**Espeak** y **Pico2Wave**).  
Ahora exploraremos dos opciones más potentes: **Piper** (sin conexión, basado en redes neuronales) y **OpenAI TTS** (en línea, basado en la nube).

* **Piper**: un motor TTS local que funciona sin conexión en Raspberry Pi.  
* **OpenAI TTS**: un servicio en línea que ofrece voces muy naturales y humanas.  

Antes de Comenzar
-------------------------

Asegúrate de haber completado:

* :ref:`install_all_modules` — Instalar los módulos ``robot-hat``, ``vilib``, ``pidog`` y luego ejecutar el script ``i2samp.sh``.

.. _test_piper:

Probar Piper
------------------

**Pasos para probarlo**:

#. Crea un nuevo archivo:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_piper.py

#. Copia el siguiente código de ejemplo en el archivo. Presiona ``Ctrl+X``, luego ``Y`` y finalmente ``Enter`` para guardar y salir.

   .. code-block:: python

       from pidog.tts import Piper

       tts = Piper()

       # Listar idiomas compatibles
       print(tts.available_countrys())

       # Listar modelos para inglés (en_us)
       print(tts.available_models('en_us'))

       # Establecer un modelo de voz (se descarga automáticamente si no está presente)
       tts.set_model("en_US-amy-low")

       # Decir algo
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()``: imprime los idiomas compatibles.  
   * ``available_models()``: lista los modelos disponibles para ese idioma.  
   * ``set_model()``: establece el modelo de voz (se descarga automáticamente si falta).  
   * ``say()``: convierte texto en voz y lo reproduce.

#. Ejecuta el programa:

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. La primera vez que lo ejecutes, el modelo de voz seleccionado se descargará automáticamente. 

   * Luego deberías escuchar al Pidog decir: ``Hello! I'm Piper TTS.``

   * Puedes cambiar a otro idioma o voz llamando a ``set_model()`` con otro nombre.

----

Probar OpenAI TTS
-------------------------------

**Obtener y guardar tu Clave API**

#. Ve a |link_openai_platform| e inicia sesión. En la página **API keys**, haz clic en **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Completa los detalles (propietario, nombre, proyecto y permisos si es necesario), luego haz clic en **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Una vez creada la clave, cópiala de inmediato — no podrás verla de nuevo. Si la pierdes, deberás generar una nueva.

   .. image:: img/llm_openai_copy.png

#. En tu carpeta del proyecto (por ejemplo: ``/pidog/examples``), crea un archivo llamado ``secret.py``:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Pega tu clave en el archivo de esta forma:

   .. code-block:: python

       # secret.py
       # Guarda las claves aquí. Nunca subas este archivo a Git.
       OPENAI_API_KEY = "sk-xxx"

**Escribir y ejecutar un programa de prueba**

#. Crea un nuevo archivo:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano test_tts_openai.py

#. Copia el siguiente código de ejemplo en el archivo. Presiona ``Ctrl+X``, luego ``Y`` y finalmente ``Enter`` para guardar y salir.

   .. code-block:: python

      from pidog.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # o usa la versión try/except mostrada antes

      # Inicializar OpenAI TTS
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # modelo TTS de baja latencia
      tts.set_voice('alloy')            # selecciona una voz

      # Saludo rápido (prueba básica)
      tts.say("Hello! I'm OpenAI TTS.")

#. Ejecuta el programa:

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. Deberías escuchar al Pidog decir:
 

   ``Hello! I'm OpenAI TTS.``

----

Solución de Problemas
----------------------------

* **No module named 'secret'**

  Esto significa que ``secret.py`` no está en la misma carpeta que tu archivo Python.  
  Mueve ``secret.py`` al mismo directorio desde donde ejecutas el script, por ejemplo:

  .. code-block:: bash

     ls ~/pidog/examples
     # Asegúrate de ver: secret.py y tu archivo .py

* **OpenAI: Invalid API key / 401**

  * Verifica que hayas pegado toda la clave (comienza con ``sk-``) y que no tenga espacios o saltos de línea extra.  
  * Asegúrate de importarla correctamente en tu código:

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Confirma que tu Raspberry Pi tenga acceso a internet (prueba con ``ping api.openai.com``).

* **OpenAI: Quota exceeded / billing error**

  * Es posible que debas agregar un método de pago o aumentar el límite de uso en tu panel de OpenAI.  
  * Intenta nuevamente después de resolver el problema de cuenta/facturación.

* **Piper: tts.say() se ejecuta pero no hay sonido**

  * Asegúrate de que el modelo de voz esté realmente presente:

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * Confirma que el nombre del modelo coincida exactamente en tu código:

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Asegúrate de que el altavoz del Robot HAT esté activado. Si aún no has ejecutado ningún código de ejemplo de PiDog, actívalo:

    .. code-block:: bash

       robot_hat enable_speaker

    Esto solo necesita hacerse una vez por arranque.

  * Verifica la salida de audio y volumen en tu Raspberry Pi (``alsamixer``) y que los altavoces estén conectados y con energía.

* **Errores ALSA / de dispositivo de sonido (por ejemplo, “Audio device busy” o “No such file or directory”)**

  * Cierra otros programas que estén usando audio.  
  * Reinicia la Raspberry Pi si el dispositivo sigue ocupado.  
  * Si estás usando HDMI o la salida de auriculares, selecciona el dispositivo correcto en la configuración de audio de Raspberry Pi OS.

* **Permission denied al ejecutar Python**

  * Si tu entorno lo requiere, intenta con ``sudo``:

    .. code-block:: bash

       sudo python3 test_tts_piper.py

Comparación de Motores TTS
-------------------------------

.. list-table:: Comparación de funciones: Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - Elemento
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - Se ejecuta en
     - Integrado en Raspberry Pi (sin conexión)
     - Integrado en Raspberry Pi (sin conexión)
     - Raspberry Pi / PC (sin conexión, necesita modelo)
     - Nube (en línea, necesita clave API)
   * - Calidad de voz
     - Robótica
     - Más natural que Espeak
     - Natural (TTS neuronal)
     - Muy natural / similar a humana
   * - Controles
     - Velocidad, tono, volumen
     - Controles limitados
     - Elegir diferentes voces/modelos
     - Elegir modelo y voces
   * - Idiomas
     - Muchos (la calidad varía)
     - Conjunto limitado
     - Muchos idiomas y voces disponibles
     - Mejor en inglés (otros dependen de disponibilidad)
   * - Latencia / velocidad
     - Muy rápida
     - Rápida
     - Tiempo real en Pi 4/5 con modelos “low”
     - Depende de la red (generalmente baja latencia)
   * - Configuración
     - Mínima
     - Mínima
     - Descargar modelos ``.onnx`` + ``.onnx.json``
     - Crear clave API, instalar cliente
   * - Mejor para
     - Pruebas rápidas, mensajes básicos
     - Voz offline ligeramente mejor
     - Proyectos locales con mejor calidad
     - Máxima calidad y opciones de voz
