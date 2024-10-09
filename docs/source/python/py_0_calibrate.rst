.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

2. Calibrar el PiDog
=============================

**Introducción**

Calibrar tu PiDog es un paso esencial para garantizar su operación estable y eficiente. Este proceso ayuda a corregir cualquier desequilibrio o imprecisión que pueda haber surgido durante el ensamblaje o por problemas estructurales. Sigue estos pasos con cuidado para asegurarte de que tu PiDog camine de manera firme y funcione como se espera.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/calibrate_before.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>


Si el ángulo de desviación es demasiado grande, deberás volver a :ref:`py_servo_adjust` para ajustar el ángulo del servomotor a 0° y luego seguir las instrucciones para volver a ensamblar el PiDog.


**Video de calibración**

Para obtener una guía completa, consulta el video de calibración. Este proporciona un proceso visual detallado para calibrar con precisión tu PiDog.

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/witCWeoHTdk?si=g8_RZDUkfjdwbLZu&amp;start=871&end=1160" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Pasos**

Los pasos específicos son los siguientes:

#. Coloca el PiDog sobre la base.

    .. image:: img/place-pidog.JPG

#. Navega al directorio de ejemplos de PiDog y ejecuta el script ``0_calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 0_calibration.py
        
    Al ejecutar el script, aparecerá una interfaz de usuario en tu terminal.

    .. image:: img/CALI.slt.1.png

#. Aquí debes seleccionar tu regla de calibración (60° o 90°). Si tu kit tiene una regla de calibración de 90°, selecciona la primera opción; si es una de 60°, selecciona la segunda opción. Después de seleccionar, ingresarás a la siguiente interfaz:

.. image:: img/CALI.slt.2.png


Regla de 90°
------------------------------

#. Coloca la **Regla de Calibración** (Acrílico C) como se muestra en la imagen proporcionada. En la terminal, presiona ``1``, seguido de las teclas ``w`` y ``s`` para alinear los bordes como se indica en la imagen.

    .. image:: img/CALI-1.2.png

#. Reposiciona la **Regla de Calibración** (Acrílico C) como se ilustra en la siguiente imagen. Presiona ``2`` en la terminal, luego usa ``w`` y ``s`` para alinear los bordes como se muestra.

    .. image:: img/CALI-2.2.png

#. Repite el proceso de calibración para los servomotores restantes (del 3 al 8). Asegúrate de calibrar las cuatro patas del PiDog.


Regla de 60°
------------------------------

#. Coloca la **Regla de Calibración** (Acrílico C) como se muestra en la imagen proporcionada. Coloca su lado largo sobre una superficie nivelada. En la terminal, presiona ``1``, seguido de las teclas ``w`` y ``s`` para alinear los bordes como se indica en la imagen.

    .. image:: img/CALI.60.1.JPG

#. Reposiciona la **Regla de Calibración** (Acrílico C) como se ilustra en la siguiente imagen. Presiona ``2`` en la terminal, luego usa ``w`` y ``s`` para alinear los bordes como se muestra.

    .. image:: img/CALI.60.2.JPG

#. Repite el proceso de calibración para los servomotores restantes (del 3 al 8). Asegúrate de calibrar las cuatro patas del PiDog.

