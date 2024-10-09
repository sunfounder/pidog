.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de Expertos**: Resuelve problemas postventa y supera desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y Compartir**: Intercambia consejos y tutoriales para perfeccionar tus habilidades.
    - **Avances Exclusivos**: Accede de forma anticipada a anuncios de nuevos productos y vistas previas exclusivas.
    - **Descuentos Especiales**: Aprovecha descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Especiales**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

4. Movimiento de la Cola
============================

A continuación se presentan las funciones que controlan la cola de PiDog. Esta función es similar a :ref:`py_b2_leg_move`.


.. code-block:: python

    Pidog.tail_move(target_angles, immediately=True, speed=50)

* ``target_angles`` : Es un array bidimensional compuesto por un conjunto de 1 ángulo para el servo (denominado grupo de ángulos). Estos grupos se utilizarán para controlar los ángulos de los 8 servos de las patas. Si se escriben varios grupos de ángulos, los grupos no ejecutados se almacenarán en la memoria intermedia.
* ``immediately`` : Si se establece este parámetro en ``True`` al llamar a la función, la memoria intermedia se vaciará de inmediato para ejecutar el nuevo grupo de ángulos escrito; si el parámetro se establece en ``False``, el nuevo grupo de ángulos se añadirá a la cola de ejecución.
* ``speed`` : Velocidad a la que se ejecutará el grupo de ángulos.

**El control del servo de la cola de PiDog también cuenta con funciones de soporte adicionales:**


.. code-block:: python

    Pidog.is_tail_done()

Indica si todas las acciones de la cola en el búfer han sido ejecutadas.

.. code-block:: python

    Pidog.wait_tail_done()

Espera hasta que todas las acciones de la cola en el búfer hayan sido ejecutadas.

.. code-block:: python

    Pidog.tail_stop()

Limpia todas las acciones de la cola en el búfer para detener el servo de la cola.


**A continuación, se presentan algunos casos de uso comunes:**

1. Mover la cola durante 10 segundos.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.tail_move([[30],[-30]], immediately=False, speed=30)

    # mantener durante 10 segundos
    time.sleep(10)

    my_dog.tail_stop()
