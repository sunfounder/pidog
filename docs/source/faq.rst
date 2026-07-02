.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook!
    Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

FAQ
==========

Q1: ¿Qué versiones de PiDog están disponibles?
------------------------------------------------------

PiDog está disponible en versiones **V1** y **V2**:

* **Versión V1**: Compatible con Raspberry Pi 3B+/4B/Zero 2W, **no** compatible con Raspberry Pi 5.
* **Versión V2**: Compatible con Raspberry Pi 3/4/5 y Zero 2W. Mejora el HAT del robot y los circuitos del controlador de servos, y proporciona mejor soporte de energía para la Pi 5.
* **Alimentación**: V2 cuenta con una mejor gestión de energía para aplicaciones de mayor consumo.

----

Q2: ¿Cómo instalo los módulos necesarios?
--------------------------------------------------

.. code-block:: bash

    # Robot HAT
    git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
    cd robot-hat && sudo python3 install.py

    # Vilib
    git clone https://github.com/sunfounder/vilib.git
    cd vilib && sudo python3 install.py

    # PiDog
    git clone https://github.com/sunfounder/pidog.git --depth 1
    cd pidog && sudo pip3 install . --break

Si no hay sonido:

.. code-block:: bash

    # Audio I2S
    cd ~/robot-hat
    sudo bash i2samp.sh

Ejecuta varias veces si es necesario.

----

Q3: Why do I get a "piper-tts" error during installation?
----------------------------------------------------------

.. important::

   If you see this error during ``pip3 install``:

   .. code-block:: text

       ERROR: Could not find a version that satisfies the requirement piper-tts==1.3.0
       ERROR: No matching distribution found for piper-tts==1.3.0

   It means you are using a **32-bit** Raspberry Pi OS. The ``piper-tts`` package only provides pre-built wheels for **64-bit** systems. Reinstall the OS using the **64-bit** version of Raspberry Pi OS and the installation will succeed.

----

Q4: ¿Cómo ejecuto la primera demostración?
-------------------------------------------------------------------

.. code-block:: bash

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

PiDog se despertará, se sentará y moverá la cola.

----

Q5: ¿Qué acciones y sonidos integrados están disponibles?
------------------------------------------------------------

* Acciones: ``stand``, ``sit``, ``wag_tail``, ``trot``, etc.
* Sonidos: ``bark``, ``howling``, ``pant``, etc.

Ejecuta:

.. code-block:: bash

    sudo python3 2_function_demonstration.py

Introduce números para activar las acciones.

----

Q6: ¿Cómo utiliza PiDog los sensores?
-------------------------------------

* **Ultrasonido**: evita obstáculos y patrulla.
* **Táctil**: toque frontal = alerta; toque trasero = disfrute.
* **Dirección del sonido**: responde a la dirección del sonido.

----

Q7: ¿Qué funciones de IA admite PiDog?
------------------------------------------------------

PiDog se integra con **TTS**, **STT** y **LLM**:

* **TTS**: Espeak, Pico2Wave, Piper, OpenAI.
* **STT**: Vosk (sin conexión).
* **LLM**: Ollama (local), OpenAI (en línea).

----

Q8: ¿Es necesario calibrar los servos?
---------------------------------------------

Sí — **la calibración de los servos es obligatoria tanto para la versión V1 como para la V2** para garantizar un movimiento estable y evitar daños.

**Versión V2**

The Robot HAT on the V2 version has a **zeroing button**. Press it to automatically set all servos to 0° — no script needed.

If your PiDog V2's legs are in the wrong position after assembly (for example, servos appear at strange angles or the robot cannot stand properly), you can use the zero button to fix this:

#. Power on the PiDog.
#. Press the **zero button** on the Robot HAT — all servos will forcibly return to 0°.
#. Reassemble the legs in the correct orientation following the assembly instructions.

For a step-by-step demonstration, watch the video below:

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zmN_mGxTKuU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Versión V1**

The V1 version uses a script to zero the servos. Run the following command — it will set all servos to 0°:

.. code-block:: bash

   cd ~/pidog/examples
   sudo python3 servo_zeroing.py

This should be done **before installation** to ensure each servo starts from the correct zero position. If your PiDog V1's legs are in the wrong position after assembly, re-run this script to reset all servos to 0°, then reassemble the legs correctly.


----

Q9: ¿Por qué mi PiDog camina de forma inestable?
---------------------------------------------------

* Confirma que todos los servos estén instalados en 0°.
* Asegúrate de que los ángulos de los servos coincidan con la regla de calibración (60°/90°).
* Verifica que la batería esté completamente cargada.
* Aprieta todos los tornillos de los servos.

----

Q10: Servo zeroing works, but calibration example doesn't move any servo?
--------------------------------------------------------------------------

If pressing the zeroing button moves all servos to 0° normally, but the calibration script cannot control any servo, the problem is likely a hardware connection issue between the Raspberry Pi and the Robot HAT.

.. note::

   The zeroing button is only available on **PiDog V2** (which uses Robot HAT V5). PiDog V1 does not have this feature and must use the ``servo_zeroing.py`` script instead.

**Why this happens**

* Servo zeroing is handled **directly by the Robot HAT** — it works independently without the Raspberry Pi.
* Running calibration or any servo control from code requires the Raspberry Pi to communicate with the Robot HAT through the **GPIO header pins**.

**How to diagnose**

This is often caused by poor soldering on either side of the GPIO connection:

* The **Raspberry Pi's 40-pin GPIO header** (especially on Zero 2W, where the header must be soldered on by the user).
* The **Robot HAT's female header pins**.

Take clear, well-lit photos of both sets of pins and send them to SunFounder support at service@sunfounder.com. The team will help identify whether resoldering is needed.

----

Q11: ¿Por qué no funciona mi cámara?
--------------------------------------

* Asegúrate de que el cable de la cámara esté **firmemente insertado** en la interfaz CSI y que la pestaña negra esté bien asegurada.
* **Apaga** la Raspberry Pi antes de conectar o desconectar la cámara para evitar daños.
* Prueba la cámara con ``libcamera-hello`` o ``raspistill`` para verificar que haya salida de imagen.
* Vuelve a insertar el cable si está flojo o mal instalado.

----

Q12: ¿Por qué no funciona el altavoz?
--------------------------------------

* Asegúrate de que el altavoz del Robot HAT esté activado. Si aún no has ejecutado ningún código de ejemplo de PiDog, actívalo primero:

  .. code-block:: bash

     robot_hat enable_speaker

  Esto solo necesita hacerse una vez por arranque. Ejecutar cualquier ejemplo de PiDog (que inicializa ``Pidog()``) lo hace automáticamente.

* Asegúrate de que el volumen no esté silenciado y de que el controlador de audio I2S esté instalado.
* Si no hay sonido, vuelve a configurar I2S con:

.. code-block:: bash

    cd ~/robot-hat
    sudo bash i2samp.sh

* Reinicia la Raspberry Pi después de ejecutar el script.

----

Q13: ¿Por qué no funciona el micrófono?
-------------------------------------------

* Comprueba si el sistema reconoce el micrófono con:

.. code-block:: bash

    arecord -l

* Prueba la función de grabación con:

.. code-block:: bash

    arecord -D plughw:1,0 -f cd test.wav

* Si no se graba audio, selecciona el dispositivo de entrada correcto en la configuración de audio o usa ``alsamixer`` para ajustar el volumen de entrada.
* Asegúrate de que ningún otro proceso esté ocupando el dispositivo de entrada de audio.

----

Q14: ¿Por qué no funciona el sensor de dirección del sonido?
---------------------------------------------------------------------

* Asegúrate de que el sensor esté conectado a la interfaz SPI correcta.
* Verifica que todos los cables estén bien conectados y no invertidos.
* Asegúrate de que la fuente de alimentación sea estable y que el sensor no esté obstruido.
* Reinicia el dispositivo y vuelve a ejecutar el script de ejemplo del sensor.

----

Q15: ¿Por qué no responde el sensor táctil?
----------------------------------------------

* Asegúrate de que todos los cables del sensor táctil estén firmemente conectados.
* Recuerda: una señal **LOW** significa que el sensor está siendo tocado.
* Prueba el pin GPIO con ``gpio readall`` o código en Python para confirmar la detección de señal.
* Verifica nuevamente el cableado y la orientación.

----

Q16: Why is the ultrasonic sensor not working?
-----------------------------------------------

#. Run the ultrasonic test to check the reading:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 ultrasonic_test.py

   If the reading shows **-1**, the sensor is not functioning correctly.

#. Verify the wiring:

   * **White wire** → GPIO **17**
   * **Yellow wire** → GPIO **4**

#. If the wiring is correct and the reading is still -1, contact SunFounder support at service@sunfounder.com for further assistance.

----

Q17: ¿Por qué la placa LED no enciende o parpadea incorrectamente?
---------------------------------------------------------------------

* Verifica que la placa LED esté alimentada con **3.3V** y conectada al puerto I2C.
* Asegúrate de que **I2C esté habilitado** en la Raspberry Pi.
* Ejecuta el siguiente comando para comprobar si la placa es reconocida:

.. code-block:: bash

    i2cdetect -y 1

* Si no aparece ningún dispositivo, revisa el cableado y reinicia la Pi.

----

Q18: Why are the 6-DOF IMU and 11-channel RGB board not working?
-----------------------------------------------------------------

If both the 6-DOF IMU and the 11-channel RGB LED board are not responding, the issue is likely with the shared I2C connection:

#. First, check whether the devices are detected on the I2C bus:

   .. code-block:: bash

       sudo i2cdetect -y 1

   The expected addresses are:

   * **0x36** — 6-DOF IMU
   * **0x74** — 11-channel RGB LED board

   If one or both addresses are missing, the corresponding device is not properly connected.

#. Try connecting the 6-DOF IMU to a different port and test again.
#. Connect the 6-DOF IMU directly to the Robot HAT's I2C port, then run the test:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 imu_test.py

#. If the IMU works when connected directly, the problem is with the 11-channel RGB board's pass-through port.
#. To confirm, connect the 11-channel RGB board directly to the I2C port and test:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 rgb_strip_test.py

----

Q19: ¿Cómo se alimenta PiDog?
------------------------------------------

* Usa un adaptador de corriente Type-C de 5V 3A.
* Luz roja = cargando, apagada = completamente cargada.
* Puedes alimentarlo mientras se carga.
* Si el indicador no se enciende, cárgalo primero.

----
