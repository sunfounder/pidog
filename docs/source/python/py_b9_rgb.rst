.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Sumérgete más a fondo en Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte de Expertos**: Resuelve problemas postventa y supera desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y Compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede de forma anticipada a anuncios de nuevos productos y vistas previas exclusivas.
    - **Descuentos Especiales**: Aprovecha descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

9. Tira RGB de PiDog
=======================

PiDog cuenta con una tira RGB en su pecho, la cual puede usar para expresar diferentes emociones.

Puedes controlarla usando la siguiente función.

.. code-block:: python

    Pidog.rgb_strip.set_mode(style='breath', color='white', bps=1, brightness=1):

* ``style`` : El modo de visualización de la tira RGB. Los valores disponibles son:

  * ``breath``
  * ``boom``
  * ``bark``

* ``color`` : Color que mostrará la tira RGB. Puedes ingresar valores RGB de 16 bits, como ``#a10a0a``, o usar los siguientes nombres de colores:

  * ``"white"``
  * ``"black"``
  * ``"white"``
  * ``"red"``
  * ``"yellow"``
  * ``"green"``
  * ``"blue"``
  * ``"cyan"``
  * ``"magenta"``
  * ``"pink"``

* ``brightness`` : Brillo de la tira RGB. Puedes ingresar un valor de punto flotante de 0 a 1, como ``0.5``.

* ``delay`` : Velocidad de la animación, cuanto menor sea el valor, más rápida será la transición.

Usa la siguiente instrucción para desactivar la tira RGB.

.. code-block:: python

    Pidog.rgb_strip.close()

A continuación, algunos ejemplos de uso

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    while True:
        # style="breath", color="pink"
        my_dog.rgb_strip.set_mode(style="breath", color='pink')
        time.sleep(3)

        # style="bark", color="#a10a0a"
        my_dog.rgb_strip.set_mode(style="bark", color="#a10a0a")
        time.sleep(3)

        # style="boom", color="#a10a0a", brightness=0.5, bps=2.5
        my_dog.rgb_strip.set_mode(style="boom", color="#a10a0a", bps=2.5, brightness=0.5)
        time.sleep(3)

        # cerrar
        my_dog.rgb_strip.close()
        time.sleep(2)

