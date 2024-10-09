.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Robot HAT
==================

|link_robot_hat_v4| es una placa de expansión multifuncional que permite convertir rápidamente la Raspberry Pi en un robot. 
Cuenta con un MCU integrado para ampliar la salida PWM y la entrada ADC de la Raspberry Pi, 
así como un chip controlador de motor, un módulo de audio I2S y un altavoz mono. 
También se incluyen los GPIOs propios de la Raspberry Pi.

Además, viene con un altavoz, 
que se puede utilizar para reproducir música de fondo, efectos de sonido e implementar funciones TTS (conversión de texto a voz) para hacer que tu proyecto sea aún más interesante.

Acepta una entrada de alimentación PH2.0 de 5 pines de 7-12V con 2 indicadores de batería, 1 indicador de carga y 1 indicador de encendido. 
La placa también cuenta con un LED y un botón para que puedas probar rápidamente algunos efectos.

.. image:: img/O1902V40RobotHAT.png

**Puerto de Alimentación**
    * Entrada de alimentación PH2.0 de 3 pines de 7-12V.
    * Alimenta simultáneamente la Raspberry Pi y el Robot HAT.

**Interruptor de Alimentación**
    * Encender/apagar la alimentación del Robot HAT.
    * Al conectar la alimentación al puerto de entrada, la Raspberry Pi se encenderá automáticamente. Sin embargo, deberás colocar el interruptor de alimentación en la posición ON para habilitar el Robot HAT.

**Puerto USB Tipo-C**
    * Inserta el cable Tipo-C para cargar la batería.
    * Al mismo tiempo, el indicador de carga se ilumina en rojo.
    * Cuando la batería está completamente cargada, el indicador de carga se apaga.
    * Si el cable USB permanece conectado durante aproximadamente 4 horas después de la carga completa, el indicador de carga parpadeará como advertencia.

**Pin Digital**
    * Pines digitales de 4 canales, D0-D3.

**Pin ADC**
    * Pines ADC de 4 canales, A0-A3.

**Pin PWM**
    * Pines PWM de 12 canales, P0-P11.

**Puerto de Motor Izquierdo/Derecho**
    * Puertos de motor de 2 canales XH2.54.
    * El puerto izquierdo está conectado al GPIO 4 y el derecho al GPIO 5.

**Pin y Puerto I2C**
    * **Pin I2C**: Interfaz de 4 pines P2.54.
    * **Puerto I2C**: Interfaz de 4 pines SH1.0, compatible con QWIIC y STEMMA QT.
    * Estas interfaces I2C están conectadas a la interfaz I2C de la Raspberry Pi a través del GPIO2 (SDA) y GPIO3 (SCL).

**Pin SPI**
    * Interfaz SPI de 7 pines P2.54.

**Pin UART**
    * Interfaz de 4 pines P2.54.

**Botón RST**
    * El botón RST, al utilizar Ezblock, actúa como un botón para reiniciar el programa Ezblock. 
    * Si no se utiliza Ezblock, el botón RST no tiene una función predefinida y puede ser completamente personalizado según tus necesidades.

**Botón USR**
    * Las funciones del Botón USR pueden ser configuradas mediante programación. (Al presionar produce una entrada “0”; al soltar, una entrada “1”).

**Indicador de Batería**
    * Dos LEDs se encienden cuando el voltaje es superior a 7.6V.
    * Un LED se enciende en el rango de 7.15V a 7.6V.
    * Por debajo de 7.15V, ambos LEDs se apagan.

**Altavoz y Puerto de Altavoz**
    * **Altavoz**: Este es un altavoz de cámara de audio 2030.
    * **Puerto de Altavoz**: El Robot HAT está equipado con una salida de audio I2S integrada, junto con un altavoz de cámara de audio 2030, proporcionando una salida de sonido mono.
