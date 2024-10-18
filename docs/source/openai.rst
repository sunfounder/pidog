Interacción con IA Usando GPT-4O
======================================

En nuestros proyectos anteriores, utilizamos la programación para dirigir a PiDog en tareas predefinidas, lo cual podía resultar un poco tedioso. Este proyecto introduce un emocionante salto hacia una interacción más dinámica. ¡No intentes engañar a nuestro perro mecánico, ya que ahora está equipado para entender mucho más que nunca!

Esta iniciativa detalla todos los pasos técnicos necesarios para integrar GPT-4O en tu sistema, incluyendo la configuración de entornos virtuales, la instalación de bibliotecas esenciales, y la configuración de claves API e identificadores de asistente.

.. note::

   Este proyecto requiere el uso de |link_openai_platform|, y es necesario pagar por el servicio de OpenAI. Además, la API de OpenAI se factura por separado de ChatGPT, y puedes consultar los precios en https://openai.com/api/pricing/.

   Por lo tanto, deberás decidir si continuar con este proyecto o asegurarte de que tienes fondos suficientes en la API de OpenAI.

Tanto si tienes un micrófono para comunicarte directamente como si prefieres escribir en una ventana de comandos, ¡las respuestas de PiDog, potenciadas por GPT-4O, te dejarán asombrado!

¡Vamos a sumergirnos en este proyecto y a desatar un nuevo nivel de interacción con PiDog!

.. raw:: html

   <video controls style = "max-width:90%">
     <source src="_static/video/chatgpt4o.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>


1. Instalación de paquetes y dependencias requeridas
--------------------------------------------------------------
.. note::
   
   Primero debe instalar los módulos necesarios para PiCar-X. Para más detalles, consulte: :ref:`install_all_modules`.
   
En esta sección, crearemos y activaremos un entorno virtual, instalando los paquetes y dependencias requeridos dentro de él. Esto asegura que los paquetes instalados no interfieran con el resto del sistema, manteniendo la independencia de las dependencias del proyecto y evitando conflictos con otros proyectos o paquetes del sistema.

#. Utiliza el comando ``python -m venv`` para crear un entorno virtual llamado ``my_venv``, incluyendo paquetes a nivel de sistema. La opción ``--system-site-packages`` permite que el entorno virtual acceda a los paquetes instalados a nivel de sistema, lo cual es útil cuando se necesitan bibliotecas de este nivel.

   .. code-block:: shell

      python -m venv --system-site-packages my_venv

#. Cambia al directorio ``my_venv`` y activa el entorno virtual usando el comando ``source bin/activate``. El indicador del sistema cambiará para mostrar que el entorno virtual está activo.

   .. code-block:: shell

      cd my_venv
      source bin/activate

#. Ahora, instala los paquetes de Python necesarios dentro del entorno virtual activado. Estos paquetes estarán aislados al entorno virtual y no afectarán otros paquetes del sistema.

   .. code-block:: shell

      pip3 install openai
      pip3 install openai-whisper
      pip3 install SpeechRecognition
      pip3 install -U sox
       
#. Finalmente, utiliza el comando ``apt`` para instalar dependencias a nivel del sistema, las cuales requieren privilegios de administrador.

   .. code-block:: shell

      sudo apt install python3-pyaudio
      sudo apt install sox


2. Obtención de la Clave API y el ID del Asistente
----------------------------------------------------------

**Obtener Clave API**

#. Visita |link_openai_platform| y haz clic en el botón **Create new secret key** en la esquina superior derecha.

   .. image:: img/apt_create_api_key.png
      :width: 700
      :align: center

#. Selecciona el Propietario, Nombre, Proyecto y permisos según sea necesario, y luego haz clic en **Create secret key**.

   .. image:: img/apt_create_api_key2.png
      :width: 700
      :align: center

#. Una vez generada, guarda esta clave secreta en un lugar seguro y accesible. Por razones de seguridad, no podrás verla de nuevo en tu cuenta de OpenAI. Si pierdes esta clave, deberás generar una nueva.

   .. image:: img/apt_create_api_key_copy.png
      :width: 700
      :align: center

**Obtener ID del Asistente**

#. A continuación, haz clic en **Assistants**, luego selecciona **Create**, asegurándote de estar en la página de **Dashboard**.

   .. image:: img/apt_create_assistant.png
      :width: 700
      :align: center

#. Mueve el cursor aquí para copiar el **ID del Asistente**, y pégalo en un cuadro de texto o en otro lugar seguro. Este es el identificador único de tu Asistente.

   .. image:: img/apt_create_assistant_id.png
      :width: 700
      :align: center

#. Asigna un nombre aleatorio, luego copia el siguiente contenido en el cuadro de **Instructions** para describir a tu Asistente.

   .. image:: img/apt_create_assistant_instructions.png
      :width: 700
      :align: center

   .. code-block::

      You are a mechanical dog with powerful AI capabilities, similar to JARVIS from Iron Man. Your name is Pidog. You can have conversations with people and perform actions based on the context of the conversation.

      ## actions you can do:
      ["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag_tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

      ## Response Format:
      {"actions": ["wag_tail"], "answer": "Hello, I am Pidog."}

      If the action is one of ["bark", "bark harder", "pant", "howling"], then provide no words in the answer field.

      ## Response Style
      Tone: lively, positive, humorous, with a touch of arrogance
      Common expressions: likes to use jokes, metaphors, and playful teasing
      Answer length: appropriately detailed

      ## Other
      a. Understand and go along with jokes.
      b. For math problems, answer directly with the final.
      c. Sometimes you will report on your system and sensor status.
      d. You know you're a machine.

#. PiDog está equipado con un módulo de cámara que puedes habilitar para capturar imágenes de lo que ve y subirlas a GPT usando nuestro código de ejemplo. Por ello, recomendamos elegir GPT-4O, que tiene capacidades de análisis de imágenes. Por supuesto, también puedes optar por gpt-3.5-turbo u otros modelos.

   .. image:: img/apt_create_assistant_model.png
      :width: 700
      :align: center

#. Ahora, haz clic en **Playground** para verificar si tu cuenta está funcionando correctamente.

   .. image:: img/apt_playground.png

#. Si tus mensajes o imágenes subidas se envían con éxito y recibes respuestas, significa que tu cuenta no ha alcanzado el límite de uso.

   .. image:: img/apt_playground_40.png
      :width: 700
      :align: center

#. Si encuentras un mensaje de error tras introducir información, es posible que hayas alcanzado tu límite de uso. Revisa tu panel de uso o las configuraciones de facturación.

   .. image:: img/apt_playground_40mini_3.5.png
      :width: 700
      :align: center

3. Introducir la Clave API y el ID del Asistente
----------------------------------------------------

#. Utiliza el siguiente comando para abrir el archivo ``keys.py``.

   .. code-block:: shell

      nano ~/pidog/gpt_examples/keys.py

#. Rellena los campos con la Clave API y el ID del Asistente que acabas de copiar.

   .. code-block:: shell

      OPENAI_API_KEY = "sk-proj-vEBo7Ahxxxx-xxxxx-xxxx"
      OPENAI_ASSISTANT_ID = "asst_ulxxxxxxxxx"

#. Presiona ``Ctrl + X``, ``Y`` y luego ``Enter`` para guardar el archivo y salir.

4. Ejecución del Ejemplo
----------------------------

Comunicación por Texto
^^^^^^^^^^^^^^^^^^^^^^^^^

Si tu PiDog no cuenta con un micrófono, puedes usar el teclado para interactuar con él ingresando texto mediante los siguientes comandos.

#. Ahora, ejecuta los siguientes comandos con privilegios de sudo, ya que el altavoz de PiDog no funcionará sin estos permisos. El proceso tomará un poco de tiempo en completarse.

   .. code-block:: shell

      cd ~/pidog/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_dog.py --keyboard

#. Una vez que los comandos se hayan ejecutado correctamente, verás la siguiente salida, indicando que todos los componentes de PiDog están listos.

   .. code-block:: shell

      vilib 0.3.8 launching ...
      picamera2 0.3.19
      config_file: /home/pi2/.config/pidog/pidog.conf
      robot_hat init ... done
      imu_sh3001 init ... done
      rgb_strip init ... done
      dual_touch init ... done
      sound_direction init ... done
      sound_effect init ... done
      ultrasonic init ... done

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      input:

#. También se te proporcionará un enlace para ver el video en tiempo real de la cámara de PiDog a través de tu navegador: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Ahora puedes escribir tus comandos en la ventana del terminal y presionar Enter para enviarlos. Las respuestas de PiDog podrían sorprenderte.

   .. note::
      
      PiDog necesita recibir tu entrada, enviarla a GPT para su procesamiento, recibir la respuesta y luego reproducirla mediante síntesis de voz. Todo este proceso lleva tiempo, así que ten paciencia.

   .. image:: img/apt_keyboard_input.png
      :width: 700
      :align: center

#. Si estás utilizando el modelo GPT-4O, también puedes hacer preguntas basadas en lo que PiDog observa.

Comunicación por Voz
^^^^^^^^^^^^^^^^^^^^^^^^

Si tu PiDog está equipado con un micrófono, o si has adquirido uno haciendo clic en |link_microphone|, puedes interactuar con PiDog usando comandos de voz.

#. Primero, verifica que la Raspberry Pi haya detectado el micrófono.

   .. code-block:: shell

      arecord -l

   Si tiene éxito, recibirás la siguiente información, indicando que tu micrófono ha sido detectado.

   .. code-block:: 
      
      **** List of CAPTURE Hardware Devices ****
      card 3: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

#. Ejecuta el siguiente comando y luego háblale a PiDog o emite algún sonido. El micrófono grabará los sonidos en el archivo ``op.wav``. Presiona ``Ctrl + C`` para detener la grabación.

   .. code-block:: shell

      rec op.wav

#. Finalmente, utiliza el comando a continuación para reproducir el sonido grabado y confirmar que el micrófono está funcionando correctamente.

   .. code-block:: shell

      sudo play op.wav

#. Ahora, ejecuta los siguientes comandos con sudo, ya que el altavoz de PiDog no funcionará sin estos permisos. El proceso tomará un poco de tiempo en completarse.

   .. code-block:: shell

      cd ~/pidog/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_dog.py

#. Una vez que los comandos se hayan ejecutado correctamente, verás la siguiente salida, indicando que todos los componentes de PiDog están listos.

   .. code-block:: shell
      
      vilib 0.3.8 launching ...
      picamera2 0.3.19
      config_file: /home/pi2/.config/pidog/pidog.conf
      robot_hat init ... done
      imu_sh3001 init ... done
      rgb_strip init ... done
      dual_touch init ... done
      sound_direction init ... done
      sound_effect init ... done
      ultrasonic init ... done

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      listening ...

#. También se te proporcionará un enlace para ver el video en tiempo real de la cámara de PiDog a través de tu navegador: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Ahora puedes hablarle a PiDog, y sus respuestas podrían sorprenderte.

   .. note::
      
      PiDog necesita recibir tu entrada, convertirla en texto, enviarla a GPT para su procesamiento, recibir la respuesta y luego reproducirla mediante síntesis de voz. Todo este proceso lleva tiempo, así que ten paciencia.

   .. image:: img/apt_speech_input.png
      :width: 700
      :align: center

#. Si estás utilizando el modelo GPT-4O, también puedes hacer preguntas basadas en lo que PiDog observa.

.. raw:: html

   <video controls style = "max-width:90%">
     <source src="_static/video/chatgpt4o.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>

5. Modificar parámetros [opcional]
-------------------------------------------
En el archivo ``gpt_dog.py``, localice las siguientes líneas. Puede modificar estos parámetros para configurar el idioma STT, la ganancia de volumen de TTS y el rol de la voz.

* **STT (Reconocimiento de voz a texto)** se refiere al proceso en el cual el micrófono de PiCar-X captura el habla y lo convierte en texto para ser enviado a GPT. Puede especificar el idioma para mejorar la precisión y la latencia en esta conversión.
* **TTS (Texto a voz)** es el proceso de convertir las respuestas de texto de GPT en habla, que se reproduce a través del altavoz de PiCar-X. Puede ajustar la ganancia de volumen y seleccionar un rol de voz para la salida de TTS.

.. code-block:: python

   # openai assistant init
   # =================================================================
   openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'picrawler')
   # LANGUAGE = ['zh', 'en'] # configurar código de idioma STT, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
   LANGUAGE = []
   VOLUME_DB = 3 # ganancia de volumen TTS, preferentemente menos de 5db
   # seleccionar el rol de voz TTS, puede ser "alloy, echo, fable, onyx, nova y shimmer"
   # https://platform.openai.com/docs/guides/text-to-speech/supported-languages
   TTS_VOICE = 'nova'

* Variable ``LANGUAGE``:

  * Mejora la precisión y el tiempo de respuesta del reconocimiento de voz a texto (STT).
  * ``LANGUAGE = []`` significa que admite todos los idiomas, pero esto puede reducir la precisión de STT y aumentar la latencia.
  * Se recomienda configurar un idioma específico(s) utilizando los códigos de idioma de |link_iso_language_code| para mejorar el rendimiento.

* Variable ``VOLUME_DB``:

  * Controla la ganancia aplicada a la salida de Texto a voz (TTS).
  * Aumentar el valor incrementará el volumen, pero es mejor mantener el valor por debajo de 5dB para evitar distorsiones de audio.

* Variable ``TTS_VOICE``:

  * Seleccione el rol de voz para la salida de Texto a voz (TTS).
  * Opciones disponibles: ``alloy, echo, fable, onyx, nova, shimmer``.
  * Puede experimentar con diferentes voces de |link_voice_options| para encontrar una que se adapte a su tono y audiencia deseados. Las voces disponibles están optimizadas actualmente para inglés.


