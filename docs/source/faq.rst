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

P1: ¿Qué versiones de PiDog están disponibles?
------------------------------------------------------

PiDog está disponible en versiones **Estándar** y **V2**:

* **Versión Estándar**: Compatible con Raspberry Pi 3B+/4B/Zero 2W, **no** compatible con Raspberry Pi 5.  
* **Versión V2**: Compatible con Raspberry Pi 3/4/5 y Zero 2W. Mejora el HAT del robot y los circuitos del controlador de servos, y proporciona mejor soporte de energía para la Pi 5.  
* **Alimentación**: V2 cuenta con una mejor gestión de energía para aplicaciones de mayor consumo.

P2: ¿Cómo instalo los módulos necesarios?
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

P3: ¿Cómo ejecuto la primera demostración?
-------------------------------------------------------------------

.. code-block:: bash

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

PiDog se despertará, se sentará y moverá la cola.

----

P4: ¿Qué acciones y sonidos integrados están disponibles?
------------------------------------------------------------

* Acciones: ``stand``, ``sit``, ``wag_tail``, ``trot``, etc.  
* Sonidos: ``bark``, ``howling``, ``pant``, etc.

Ejecuta:

.. code-block:: bash

    sudo python3 2_function_demonstration.py

Introduce números para activar las acciones.

----

P5: ¿Cómo utiliza PiDog los sensores?
-------------------------------------

* **Ultrasonido**: evita obstáculos y patrulla.  
* **Táctil**: toque frontal = alerta; toque trasero = disfrute.  
* **Dirección del sonido**: responde a la dirección del sonido.

----

P6: ¿Qué funciones de IA admite PiDog?
------------------------------------------------------

PiDog se integra con **TTS**, **STT** y **LLM**:

* **TTS**: Espeak, Pico2Wave, Piper, OpenAI.  
* **STT**: Vosk (sin conexión).  
* **LLM**: Ollama (local), OpenAI (en línea).

----

P7: ¿Es necesario calibrar los servos?
---------------------------------------------

Sí — **la calibración de los servos es obligatoria tanto para la versión Estándar como para la V2** para garantizar un movimiento estable y evitar daños.

**Versión V2**  

Presiona el **botón de cero** en el Robot HAT para establecer automáticamente todos los servos en 0°. Esto simplifica el proceso sin necesidad de ejecutar un script.

**Versión Estándar** 

Ejecuta el script de calibración **antes de la instalación**:

.. code-block:: bash

   cd ~/pidog/examples
   sudo python3 servo_zeroing.py

Después de la instalación (en ambas versiones), verifica y ajusta manualmente los ángulos de los servos para alinear cada extremidad con la regla de calibración. Esto evita inestabilidad, bloqueos o estrés mecánico, y garantiza un movimiento suave y un control preciso de la postura.

----

P8: ¿Por qué mi PiDog camina de forma inestable?
---------------------------------------------------

* Confirma que todos los servos estén instalados en 0°.  
* Asegúrate de que los ángulos de los servos coincidan con la regla de calibración (60°/90°).  
* Verifica que la batería esté completamente cargada.  
* Aprieta todos los tornillos de los servos.

----

P9: ¿Por qué no funciona mi cámara?
--------------------------------------

* Asegúrate de que el cable de la cámara esté **firmemente insertado** en la interfaz CSI y que la pestaña negra esté bien asegurada.  
* **Apaga** la Raspberry Pi antes de conectar o desconectar la cámara para evitar daños.  
* Prueba la cámara con ``libcamera-hello`` o ``raspistill`` para verificar que haya salida de imagen.  
* Vuelve a insertar el cable si está flojo o mal instalado.

----

P10: ¿Por qué no funciona el altavoz?
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

P11: ¿Por qué no funciona el micrófono?
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

P12: ¿Por qué no funciona el sensor de dirección del sonido?
---------------------------------------------------------------------

* Asegúrate de que el sensor esté conectado a la interfaz SPI correcta.  
* Verifica que todos los cables estén bien conectados y no invertidos.  
* Asegúrate de que la fuente de alimentación sea estable y que el sensor no esté obstruido.  
* Reinicia el dispositivo y vuelve a ejecutar el script de ejemplo del sensor.

----

P13: ¿Por qué no responde el sensor táctil?
----------------------------------------------

* Asegúrate de que todos los cables del sensor táctil estén firmemente conectados.  
* Recuerda: una señal **LOW** significa que el sensor está siendo tocado.  
* Prueba el pin GPIO con ``gpio readall`` o código en Python para confirmar la detección de señal.  
* Verifica nuevamente el cableado y la orientación.

----

P14: ¿Por qué la placa LED no enciende o parpadea incorrectamente?
---------------------------------------------------------------------

* Verifica que la placa LED esté alimentada con **3.3V** y conectada al puerto I2C.  
* Asegúrate de que **I2C esté habilitado** en la Raspberry Pi.  
* Ejecuta el siguiente comando para comprobar si la placa es reconocida:

.. code-block:: bash

    i2cdetect -y 1

* Si no aparece ningún dispositivo, revisa el cableado y reinicia la Pi.

----

P15: ¿Cómo se alimenta PiDog?
------------------------------------------

* Usa un adaptador de corriente Type-C de 5V 3A.  
* Luz roja = cargando, apagada = completamente cargada.  
* Puedes alimentarlo mientras se carga.  
* Si el indicador no se enciende, cárgalo primero.
