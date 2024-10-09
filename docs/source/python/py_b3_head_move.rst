.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Sumérgete más profundamente en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de Expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y Compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

3. Movimiento de la Cabeza
================================

El control del servo de la cabeza de PiDog se implementa a través de las siguientes funciones.

.. code-block:: python

    Pidog.head_move(target_yrps, roll_comp=0, pitch_comp=0, immediately=True, speed=50)

* ``target_angles`` : Es un array bidimensional compuesto por un conjunto de 3 ángulos para los servos (denominado grupo de ángulos). Estos grupos se utilizarán para controlar los ángulos de los 8 servos de las patas. Si se escriben varios grupos de ángulos, los grupos no ejecutados se almacenarán en la memoria intermedia.
* ``roll_comp`` : Proporciona compensación angular en el eje de balanceo.
* ``pitch_comp`` : Proporciona compensación angular en el eje de cabeceo.
* ``immediately`` : Si se establece este parámetro en ``True`` al llamar a la función, la memoria intermedia se vaciará de inmediato para ejecutar el nuevo grupo de ángulos escrito; si el parámetro se establece en ``False``, el nuevo grupo de ángulos se añadirá a la cola de ejecución.
* ``speed`` : Velocidad a la que se ejecutará el grupo de ángulos.

**El control del servo de la cabeza de PiDog también cuenta con funciones de soporte adicionales:**


.. code-block:: python

    Pidog.is_head_done()

Indica si todas las acciones de la cabeza en el búfer han sido ejecutadas.

.. code-block:: python

    Pidog.wait_head_done()

Espera hasta que todas las acciones de la cabeza en el búfer hayan sido ejecutadas.

.. code-block:: python

    Pidog.head_stop()

Limpia todas las acciones de la cabeza en el búfer para detener los servos de la cabeza.


**A continuación, se presentan algunos casos de uso comunes:**

1. Asentir cinco veces.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(5):
        my_dog.head_move([[0, 0, 30],[0, 0, -30]], speed=80)
        my_dog.wait_head_done()
        time.sleep(0.5)

2. Mover la cabeza de un lado a otro durante 10 segundos.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.head_move([[30, 0, 0],[-30, 0, 0]], immediately=False, speed=30)

    # mantener durante 10 segundos
    time.sleep(10)

    my_dog.head_move([[0, 0, 0]], immediately=True, speed=80)

3. Mantener la cabeza nivelada mientras PiDog está sentado o medio erguido al moverla de un lado a otro.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # lista de acciones
    shake_head = [[30, 0, 0],[-30, 0, 0]]
    half_stand_leg = [[45, 10, -45, -10, 45, 10, -45, -10]]
    sit_leg = [[30, 60, -30, -60, 80, -45, -80, 45]]

    while True:
        # mover la cabeza en posición semi-erguida
        my_dog.legs_move(half_stand_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=0, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)

        # mover la cabeza en posición de sentado
        my_dog.legs_move(sit_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=-30, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)

