.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a los anuncios de nuevos productos y a vistas previas.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

16. STT con Vosk (Offline)
==============================================

Vosk es un motor de reconocimiento de voz a texto (STT) ligero que admite muchos idiomas y funciona completamente **sin conexión** en Raspberry Pi.  
Solo necesitas acceso a internet una vez para descargar un modelo de idioma. Después de eso, todo funciona sin conexión a la red.  

En esta lección, vamos a:  

* Verificar el micrófono en la Raspberry Pi.  
* Instalar y probar Vosk con un modelo de idioma seleccionado.  

Antes de Comenzar
--------------------------

Asegúrate de haber completado:

* :ref:`install_all_modules` — Instalar los módulos ``robot-hat``, ``vilib``, ``pidog`` y luego ejecutar el script ``i2samp.sh``.

1. Verifica Tu Micrófono
--------------------------

Antes de usar el reconocimiento de voz, asegúrate de que tu micrófono USB funcione correctamente.

#. Lista los dispositivos de grabación disponibles:

   .. code-block:: bash

      arecord -l

   Busca una línea como ``card 1: ... device 0``.  

#. Graba una muestra corta (reemplaza ``1,0`` con los números que encontraste):

   .. code-block:: bash

      arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

   * Ejemplo: si tu dispositivo es ``card 2, device 0``, usa:

   .. code-block:: bash

      arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

#. Reproduce la grabación para confirmar:

   .. important::

      El altavoz del Robot HAT debe estar activado antes de reproducir audio. Si aún no has ejecutado ningún código de ejemplo de PiDog, actívalo primero:

      .. code-block:: bash

         robot_hat enable_speaker

      Esto solo necesita hacerse una vez por arranque. Ejecutar cualquier ejemplo de PiDog (que inicializa ``Pidog()``) lo hace automáticamente.

   .. code-block:: bash

      aplay test.wav

#. Ajusta el volumen del micrófono si es necesario:

   .. code-block:: bash

      alsamixer

   * Presiona **F6** para seleccionar tu micrófono USB.  
   * Busca el canal **Mic** o **Capture**.  
   * Asegúrate de que no esté silenciado (**[MM]** significa silencio; presiona ``M`` para activar → debería mostrar **[OO]**).  
   * Usa las flechas ↑ / ↓ para cambiar el volumen de grabación.


.. _test_vosk:

2. Probar Vosk
--------------------------

**Pasos para probarlo**:

#. Crea un nuevo archivo:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_stt_vosk.py

#. Copia el código de ejemplo dentro. Presiona ``Ctrl+X``, luego ``Y`` y ``Enter`` para guardar y salir.

   .. code-block:: python

      from pidog.stt import Vosk

      vosk = Vosk(language="en-us")

      print(vosk.available_languages)

      while True:
          print("Say something")
          result = vosk.listen(stream=False)
          print(result)

#. Ejecuta el programa:

   .. code-block:: bash

      sudo python3 test_stt_vosk.py

#. La primera vez que ejecutes este código con un nuevo idioma, Vosk **descargará automáticamente el modelo de idioma** (por defecto descargará la versión **pequeña**).  
   Al mismo tiempo, imprimirá la lista de idiomas compatibles. Luego verás:

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   Esto significa:

   * El archivo del modelo (``vosk-model-small-en-us-0.15``) se ha descargado.  
   * Se ha impreso la lista de idiomas admitidos.  
   * El sistema ahora está escuchando: habla por el micrófono de Pidog y el texto reconocido aparecerá en la terminal.

   **Consejos**:

   * Mantén el micrófono a unos 15–30 cm de distancia.  
   * Elige un modelo que coincida con tu idioma y acento.  

**Modo Streaming (opcional)**

También puedes transmitir voz de forma continua para ver resultados parciales mientras hablas:

.. code-block:: python

   from pidog.stt import Vosk

   vosk = Vosk(language="en-us")

   while True:
       print("Say something")
       for result in vosk.listen(stream=True):
           if result["done"]:
               print(f"final:   {result['final']}")
           else:
               print(f"partial: {result['partial']}", end="\r", flush=True)

Solución de Problemas
---------------------------

* **No such file or directory (al ejecutar `arecord`)**

  Es posible que hayas usado un número de tarjeta/dispositivo incorrecto.  
  Ejecuta:

  .. code-block:: bash

     arecord -l

  y reemplaza ``1,0`` con los números que aparezcan para tu micrófono USB.

* **El archivo grabado no tiene sonido**

  Abre el mezclador y verifica el volumen del micrófono:

  .. code-block:: bash

     alsamixer

  * Presiona **F6** para seleccionar tu micrófono USB.  
  * Asegúrate de que **Mic/Capture** no esté silenciado (**[OO]** en lugar de **[MM]**).  
  * Aumenta el volumen con ↑.

* **Vosk no reconoce la voz**

  * Asegúrate de que el **código de idioma** coincida con tu modelo (por ejemplo, ``en-us`` para inglés, ``zh-cn`` para chino).  
  * Mantén el micrófono a 15–30 cm y evita el ruido de fondo.  
  * Habla con claridad y despacio.

* **Alta latencia / reconocimiento lento**

  * La descarga automática por defecto es un **modelo pequeño** (más rápido, pero menos preciso).  
  * Si sigue siendo lento, cierra otros programas para liberar CPU.
