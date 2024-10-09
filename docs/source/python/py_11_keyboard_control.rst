.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

11. Juega con PiDog usando el Teclado
==========================================

En este ejemplo, utilizaremos el teclado para controlar a PiDog. Puedes presionar las siguientes teclas en el terminal para que realice diferentes acciones.

.. list-table:: 
    :widths: 25 50 25 50 25 50
    :header-rows: 1

    * - Teclas
      - Función
      - Teclas
      - Función
      - Teclas
      - Función  
    * - 1
      - Dormitar
      - q
      - Ladrar fuerte
      - a
      - Girar a la izquierda
    * - 2
      - Flexiones
      - w
      - Avanzar
      - s
      - Retroceder
    * - 3
      - Aullido
      - e
      - Jadear
      - d
      - Girar a la derecha
    * - 4
      - Torcer el cuerpo
      - r
      - Mover la cola
      - f
      - Sacudir la cabeza
    * - 5
      - Rascarse
      - t
      - Sacudir la cabeza
      - g
      - Chocar los cinco
    * - u
      - Rodar la cabeza
      - U
      - Rodar la cabeza+
      - z
      - Acostarse
    * - i
      - Inclinar la cabeza
      - I
      - Inclinar la cabeza+
      - x
      - Levantarse
    * - o
      - Girar la cabeza
      - O
      - Girar la cabeza+
      - c
      - Sentarse
    * - j
      - Rotar la cabeza (yaw)
      - J
      - Rotar la cabeza (yaw)+
      - v
      - Estirarse
    * - k
      - Inclinar la cabeza
      - K
      - Inclinar la cabeza+
      - m
      - Resetear cabeza
    * - l
      - Rotar la cabeza (yaw)
      - L
      - Rotar la cabeza (yaw)+
      - W
      - Trote

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 11_keyboard_control.py

Después de ejecutar el programa, verás un teclado impreso en el terminal. Ahora puedes controlar a PiDog usando el teclado desde la terminal.


**Código**

Puedes encontrar el código en |link_code_11_keyboard_control|.

