.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Sensor de Dirección de Sonido
=====================================

.. image:: img/cpn_sound.png
   :width: 400
   :align: center

Este es un módulo de reconocimiento de dirección de sonido. Está equipado con 3 micrófonos, que pueden detectar fuentes de sonido desde todas las direcciones, y cuenta con un TR16F064B, que se utiliza para procesar las señales de sonido y calcular la dirección de la fuente sonora. La unidad mínima de detección de este módulo es de 20 grados, y el rango de datos es de 0 a 360.

Proceso de transmisión de datos: el controlador principal eleva el pin BUSY, y el TR16F064B comienza a monitorear la dirección. Cuando el 064B reconoce la dirección, baja el pin BUSY. 
Cuando el controlador principal detecta que BUSY está bajo, envía datos arbitrarios de 16 bits a 064B (siguiendo la transmisión MSB) y acepta datos de 16 bits, que corresponden a la dirección del sonido procesada por el 064B.
Después de completar la transmisión, el controlador principal vuelve a elevar el pin BUSY para realizar una nueva detección de la dirección.

**Especificaciones**

* Alimentación: 3.3V
* Comunicación: SPI
* Conector: PH2.0 7P
* Rango de ángulo de reconocimiento de sonido: 360°
* Precisión angular de reconocimiento de sonido: ~10°

**Asignación de Pines**

* GND - Entrada de tierra
* VCC - Entrada de alimentación de 3.3V
* MOSI - SPI MOSI
* MISO - SPI MISO
* SCLK - Reloj SPI
* CS - Selección de chip SPI
* BUSY - Detección de ocupación

