.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Sumérgete más a fondo en Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte de Expertos**: Resuelve problemas postventa y supera desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y Compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede de forma anticipada a anuncios de nuevos productos y vistas previas exclusivas.
    - **Descuentos Especiales**: Aprovecha descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

11. Detección de Dirección del Sonido
==========================================

PiDog cuenta con un módulo sensor de dirección de sonido que detecta de dónde proviene el sonido, y podemos activarlo haciendo una palmada cerca de él.

**Usar este módulo es tan sencillo como llamar a las siguientes funciones.**

.. code-block:: python

    Pidog.ears.isdetected()

Devuelve ``True`` si se detecta un sonido, y ``False`` en caso contrario.

.. code-block:: python

    Pidog.ears.read()

Esta función devuelve la dirección de la fuente de sonido, en un rango de 0 a 359; si el sonido proviene del frente, devuelve 0; si proviene de la derecha, devuelve 90.

**Un ejemplo de cómo usar este módulo es el siguiente:**

.. code-block:: python

    from pidog import Pidog

    my_dog = Pidog()

    while True:
        if my_dog.ears.isdetected():
            direction = my_dog.ears.read()
            print(f"sound direction: {direction}")





