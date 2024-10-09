.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

10. Equilibrio
===================

Gracias a su módulo IMU de 6 grados de libertad (DOF), PiDog tiene un gran sentido del equilibrio.

En este ejemplo, puedes hacer que PiDog camine de manera estable sobre una mesa, e incluso si levantas un lado de la mesa, PiDog caminará sin problemas por la suave pendiente.

.. image:: img/py_10.gif

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 10_balance.py

Después de ejecutar el programa, verás un teclado impreso en el terminal.
Puedes controlar a PiDog para que camine con estabilidad en la rampa utilizando las siguientes teclas:


.. list-table:: 
    :widths: 25 25
    :header-rows: 1

    * - Teclas
      - Función
    * - W
      - Avanzar 
    * - E
      - Estar de pie 
    * - A
      - Girar a la izquierda 
    * - S
      - Retroceder 
    * - D
      - Girar a la derecha 
    * - R
      - Cada pulsación eleva ligeramente el cuerpo; se requieren varias pulsaciones para una subida notable.     
    * - F
      - Cada pulsación baja el cuerpo un poco; se necesitan varias pulsaciones para notar un descenso.


**Código**

Puedes encontrar el código en |link_code_10_balance|.

