.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a los anuncios de nuevos productos y a vistas previas.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

14. TTS con Espeak y Pico2Wave
=================================================

En esta lección, usaremos dos motores integrados de texto a voz (TTS) en Raspberry Pi — **Espeak** y **Pico2Wave** — para hacer que el Pidog hable.  

Estos dos motores son simples y funcionan sin conexión, pero suenan bastante diferentes:

* **Espeak**: muy ligero y rápido, pero la voz es robótica. Puedes ajustar la velocidad, el tono y el volumen.  
* **Pico2Wave**: produce una voz más suave y natural que Espeak, pero ofrece menos opciones de configuración.  

Podrás notar la diferencia en la **calidad de voz** y en las **características**.  

----

Antes de Comenzar
-------------------------

Asegúrate de haber completado:

* :ref:`install_all_modules` — Instalar los módulos ``robot-hat``, ``vilib``, ``pidog`` y luego ejecutar el script ``i2samp.sh``.

Probar Espeak
--------------------

Espeak es un motor de TTS ligero incluido en Raspberry Pi OS.  
Su voz suena robótica, pero es altamente configurable: puedes ajustar el volumen, tono, velocidad y más.  

**Pasos para probarlo**:

* Crea un nuevo archivo con el comando:

  .. code-block:: bash
  
      cd ~/pidog/examples
      sudo nano test_tts_espeak.py

* Luego copia el código de ejemplo en él. Presiona ``Ctrl+X``, luego ``Y`` y finalmente ``Enter`` para guardar y salir.

  .. code-block:: python
  
      from pidog.tts import Espeak

      tts = Espeak()
  
      # Ajustes opcionales de voz
      # tts.set_amp(100)   # 0 a 200
      # tts.set_speed(150) # 80 a 260
      # tts.set_gap(5)     # 0 a 200
      # tts.set_pitch(50)  # 0 a 99

      # Saludo rápido (prueba básica)
      tts.say("Hello! I'm Espeak TTS.")
  
* Ejecuta el programa con:

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* Deberías escuchar al Pidog decir: “Hello! I'm Espeak TTS.”  
* Descomenta las líneas de ajuste de voz en el código para experimentar cómo ``amp``, ``speed``, ``gap`` y ``pitch`` afectan el sonido.

----

Probar Pico2Wave
---------------------

Pico2Wave produce una voz más natural y humana que Espeak.  
Es más simple de usar pero menos flexible: solo puedes cambiar el idioma, no el tono ni la velocidad.

**Pasos para probarlo**:

* Crea un nuevo archivo con el comando:

  .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_pico2wave.py

* Luego copia el código de ejemplo en él. Presiona ``Ctrl+X``, luego ``Y`` y finalmente ``Enter`` para guardar y salir.

  .. code-block:: python
  
      from pidog.tts import Pico2Wave
  
      tts = Pico2Wave()
  
      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
      # Saludo rápido (prueba básica)
      tts.say("Hello! I'm Pico2Wave TTS.")

* Ejecuta el programa con:

  .. code-block:: bash

    sudo python3 test_tts_pico2wave.py

* Deberías escuchar al Pidog decir: “Hello! I'm Pico2Wave TTS.”  
* Prueba cambiando el idioma (por ejemplo, ``es-ES`` para español) y escucha la diferencia.

----

Solución de Problemas
----------------------------

* **No hay sonido al usar Espeak o Pico2Wave**

  * Verifica que tus altavoces o auriculares estén conectados y que el volumen no esté silenciado.  
  * Realiza una prueba rápida en la terminal:

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  Si no escuchas nada, el problema está en la salida de audio, no en tu código de Python.

* **La voz de Espeak suena demasiado rápida o robótica**

  * Intenta ajustar los parámetros en tu código:

    .. code-block:: python

       tts.set_speed(120)   # más lento
       tts.set_pitch(60)    # tono diferente

* **“Permission denied” al ejecutar el código**

  * Intenta ejecutar con ``sudo``:

    .. code-block:: bash

       sudo python3 test_tts_espeak.py


Comparación: Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Característica
     - Espeak
     - Pico2Wave
   * - Calidad de voz
     - Robótica, sintética
     - Más natural, tipo humano
   * - Idiomas
     - Inglés por defecto
     - Menos idiomas, pero comunes
   * - Ajustable
     - Sí (velocidad, tono, etc.)
     - No (solo idioma)
   * - Rendimiento
     - Muy rápido y ligero
     - Un poco más lento y pesado

