.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

3. Fuente de alimentación para Raspberry Pi (Importante)
===============================================================

Carga
-------------------

Conecta el cable de la batería. A continuación, conecta el cable USB-C para cargar la batería. Deberás usar tu propio cargador; recomendamos un cargador de 5V 3A o, en su defecto, puedes utilizar el cargador de tu smartphone habitual.

.. image:: img/BTR_IMG_1096.png

.. note::
    Conecta una fuente de alimentación externa Type-C al puerto Type-C en el robot HAT; la batería comenzará a cargarse de inmediato, y se encenderá un indicador rojo.
    Cuando la batería esté completamente cargada, la luz roja se apagará automáticamente.


Encendido
----------------------

Enciende el interruptor de alimentación. Se iluminarán el indicador de energía y el indicador de nivel de batería.

.. image:: img/BTR_IMG_1097.png

Espera unos segundos y escucharás un pequeño pitido, lo que indica que la Raspberry Pi se ha iniciado con éxito.

.. note::
    Si ambos indicadores de nivel de batería están apagados, por favor carga la batería.
    Si necesitas realizar sesiones prolongadas de programación o depuración, puedes mantener la Raspberry Pi en funcionamiento conectando simultáneamente el cable USB-C para cargar la batería.

Batería 18650
-----------------------------------

.. image:: img/5pin_battery.jpg

* VCC: Terminal positivo de la batería; aquí hay dos conjuntos de VCC y GND para aumentar la corriente y reducir la resistencia.
* Medio: Para equilibrar el voltaje entre las dos celdas y así proteger la batería.
* GND: Terminal negativo de la batería.

Este es un paquete de baterías personalizado fabricado por SunFounder, compuesto por dos baterías 18650 con una capacidad de 2000mAh. El conector es XH2.54 5P, lo que permite cargarlo directamente al insertarlo en la tarjeta de expansión.

**Características**

* Carga de la batería: 5V/2A
* Salida de la batería: 5V/5A
* Capacidad de la batería: 3.7V 2000mAh x 2
* Duración de la batería: 90 min
* Tiempo de carga de la batería: 130 min
* Conector: XH2.54 5P
