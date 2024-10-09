.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Sumérgete más a fondo en Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte de Expertos**: Resuelve problemas postventa y supera desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y Compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede de forma anticipada a anuncios de nuevos productos y vistas previas exclusivas.
    - **Descuentos Especiales**: Aprovecha descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

12. Acariciar la Cabeza de PiDog
=========================================

El interruptor táctil en la cabeza de PiDog puede detectar cómo lo tocas. Puedes usar las siguientes funciones para interactuar con él.

.. code-block:: python

    Pidog.dual_touch.read()

* Si tocas el módulo de izquierda a derecha (de frente hacia atrás en la orientación de PiDog), devolverá ``"LS"``.
* Si lo tocas de derecha a izquierda, devolverá ``"RS"``.
* Si solo se toca el lado izquierdo del módulo, devolverá ``"L"``.
* Si solo se toca el lado derecho del módulo, devolverá ``"R"``.
* Si no se toca el módulo, devolverá ``"N"``.

**A continuación, un ejemplo de su uso:**

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()
    while True:
        touch_status = my_dog.dual_touch.read()
        print(f"touch_status: {touch_status}")
        time.sleep(0.5)

