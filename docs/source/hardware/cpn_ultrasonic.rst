.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Módulo Ultrasónico
================================

.. image:: img/ultrasonic_pic.png
    :width: 400
    :align: center

* **TRIG**: Entrada de Pulso de Disparo
* **ECHO**: Salida de Pulso de Eco
* **GND**: Tierra
* **VCC**: Alimentación de 5V

Este es el sensor ultrasónico de distancia HC-SR04, que proporciona mediciones sin contacto desde 2 cm hasta 400 cm con una precisión de hasta 3 mm. El módulo incluye un transmisor ultrasónico, un receptor y un circuito de control.

Solo necesitas conectar 4 pines: VCC (alimentación), Trig (disparo), Echo (recepción) y GND (tierra) para facilitar su uso en tus proyectos de medición.

**Características**

* Voltaje de trabajo: DC 5V
* Corriente de trabajo: 16mA
* Frecuencia de trabajo: 40Hz
* Rango máximo: 500 cm
* Rango mínimo: 2 cm
* Señal de entrada del disparador: Pulso TTL de 10uS
* Señal de salida de eco: Señal de nivel TTL proporcional al rango
* Conector: XH2.54-4P
* Dimensiones: 46x20.5x15 mm

**Principio de Funcionamiento**

Los principios básicos son los siguientes:

* Utiliza el disparo de IO con una señal de nivel alto de al menos 10us.
* El módulo envía una ráfaga de 8 ciclos de ultrasonido a 40 kHz y detecta si se recibe una señal de retorno.
* Echo emitirá un nivel alto si se detecta una señal de retorno; la duración del nivel alto es el tiempo desde la emisión hasta la recepción.
* Distancia = (tiempo de nivel alto x velocidad del sonido (340M/S)) / 2

    .. image:: img/ultrasonic_prin.jpg
        :width: 800

Fórmula: 

* us / 58 = distancia en centímetros
* us / 148 = distancia en pulgadas
* distancia = tiempo de nivel alto x velocidad (340M/S) / 2

**Notas de Aplicación**

* Este módulo no debe conectarse mientras está energizado. Si es necesario, primero conecta el GND del módulo. De lo contrario, afectará el funcionamiento del módulo.
* El área del objeto a medir debe ser de al menos 0.5 metros cuadrados y lo más plana posible. De lo contrario, los resultados se verán afectados.
