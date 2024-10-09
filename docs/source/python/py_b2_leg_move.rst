.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el fascinante mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _py_b2_leg_move:

2. Movimiento de las patas
===============================

Los movimientos de las patas de PiDog se implementan mediante las siguientes funciones.

.. code-block:: python

    Pidog.legs_move(target_angles, immediately=True, speed=50)

* ``target_angles``: Es un array bidimensional compuesto por un array de 8 ángulos de servos (conocido como grupo de ángulos). Estos grupos de ángulos se utilizan para controlar los 8 servos de las patas. Si se escriben varios grupos de ángulos, los que no se han ejecutado se almacenan en la memoria temporal.
* ``immediately``: Al llamar la función, si este parámetro se establece en ``True``, la memoria temporal se borrará de inmediato para ejecutar el nuevo grupo de ángulos; si se establece en ``False``, el nuevo grupo de ángulos se añadirá a la cola de ejecución.
* ``speed``: La velocidad a la que se ejecuta el grupo de ángulos.

**A continuación, se presentan algunos usos comunes:**

1. Ejecutar la acción de inmediato.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # medio apoyo
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)   


2. Añadir varios grupos de ángulos a la cola de ejecución.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # medio apoyo
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # múltiples acciones
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70],
                        [90, -30, -90, 30, 80, 70, -80, -70],
                        [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   


3. Realizar repeticiones durante 10 segundos.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # medio apoyo
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # preparación para flexiones
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], immediately=False, speed=20)

    # flexiones
    for _ in range(99):
        my_dog.legs_move([[90, -30, -90, 30, 80, 70, -80, -70],
                            [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   

    # mantener durante 10 segundos
    time.sleep(10)

    # detenerse y medio apoyo
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], immediately=True, speed=50)  


**El control de las patas de PiDog también cuenta con las siguientes funciones que se pueden utilizar conjuntamente:**

.. code-block:: python

    Pidog.is_legs_done()

Esta función se utiliza para determinar si el grupo de ángulos en la memoria temporal ha sido ejecutado. Si es así, devuelve ``True``; de lo contrario, devuelve ``False``.

.. code-block:: python

    Pidog.wait_legs_done()

Suspende el programa hasta que los grupos de ángulos en la memoria temporal se hayan ejecutado.

.. code-block:: python

    Pidog.legs_stop() 

Vacía el grupo de ángulos en la memoria temporal.
