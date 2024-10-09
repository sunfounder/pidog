.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el fascinante mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

1. Inicialización de PiDog
===============================

Las funciones de PiDog están escritas en la clase ``Pidog``, cuyo prototipo se muestra a continuación.

.. code-block:: python

    Class: Pidog()

    __init__(leg_pins=DEFAULT_LEGS_PINS, 
            head_pins=DEFAULT_HEAD_PINS,
            tail_pin=DEFAULT_TAIL_PIN,
            leg_init_angles=None,
            head_init_angles=None,
            tail_init_angle=None)


PiDog debe ser instanciado de varias formas, como se muestra a continuación.

1. A continuación se muestran los pasos más simples para inicializarlo.

.. code-block:: python

    # Importar la clase Pidog
    from pidog import Pidog

    # Instanciar un objeto Pidog
    my_dog = Pidog()

2. PiDog cuenta con 12 servos, que se pueden inicializar al momento de su instanciación.

.. code-block:: python

    # Importar la clase Pidog
    from pidog import Pidog

    # Instanciar un objeto Pidog con ángulos de servos personalizados
    my_dog = Pidog(leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )

En la clase ``Pidog``, los servos se dividen en tres grupos:

* ``leg_init_angles``: Este array contiene 8 valores que determinan los ángulos de ocho servos, correspondientes a los servos (números de pin) ``2, 3, 7, 8, 0, 1, 10, 11``. En el esquema de ensamblaje puedes ver la ubicación de estos servos.

* ``head_init_angles``: Este array contiene 3 valores que controlan los servos de la cabeza de PiDog, encargados del yaw, roll y pitch (``no. 4, 6, 5``), los cuales reaccionan a la orientación o inclinación del cuerpo.

* ``tail_init_angle``: Este array contiene un solo valor dedicado a controlar el servo de la cola, que corresponde al pin ``9``.

3. ``Pidog`` permite redefinir el número de serie de los servos al instanciar el robot si el orden de tus servos es diferente.

.. code-block:: python

    # Importar la clase Pidog
    from pidog import Pidog

    # Instanciar un objeto Pidog con pines y ángulos de servos personalizados
    my_dog = Pidog(leg_pins=[2, 3, 7, 8, 0, 1, 10, 11], 
                    head_pins=[4, 6, 5],
                    tail_pin=[9],
                    leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )