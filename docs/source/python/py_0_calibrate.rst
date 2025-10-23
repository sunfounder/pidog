.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

2. Calibración de PiDog
=============================

**Introducción**

La calibración de tu PiDog es un paso fundamental para garantizar su funcionamiento estable y eficiente. Este proceso ayuda a corregir desequilibrios o imprecisiones causadas por errores de ensamblaje o estructurales. Sigue cuidadosamente los pasos a continuación para asegurarte de que tu PiDog camine de manera fluida y funcione como se espera.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/calibrate_before.mp4" type="video/mp4">
      Tu navegador no admite la etiqueta de video.
   </video>

Si el ángulo de desviación es demasiado grande, vuelve a :ref:`py_servo_adjust`, ajusta el ángulo del servo a 0° y vuelve a ensamblar PiDog según las instrucciones.

**Video de calibración**

Para obtener una guía detallada, consulta el video completo de calibración. Este mostrará, de forma visual y paso a paso, cómo calibrar correctamente tu PiDog.

.. note::

   El kit de PiDog incluye una regla de calibración de 90° o de 60°. En el video se utiliza la regla de 90°, pero el proceso con la de 60° es muy similar. También puedes seguir la guía ilustrada paso a paso que aparece a continuación.
    
    .. image:: img/cali_ruler.png
         :width: 400
         :align: center

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/witCWeoHTdk?si=g8_RZDUkfjdwbLZu&amp;start=871&end=1160" title="Reproductor de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Pasos**

Sigue estos pasos:

#. Coloca el PiDog sobre una superficie plana.

   .. image:: img/place-pidog.JPG

#. Accede al directorio de ejemplos de PiDog y ejecuta el script ``0_calibration.py``.

   .. raw:: html

        <run></run>

   .. code-block::

        cd ~/pidog/examples
        sudo python3 0_calibration.py

#. Después de ejecutar el script, aparecerá una interfaz interactiva en la terminal. Elige el tipo de regla de calibración que tienes:  
   selecciona la opción 1 para 90° o la opción 2 para 60°.

    .. image:: img/CALI.slt.1.png

#. Una vez hecha la selección, aparecerá la siguiente interfaz de calibración:

    .. image:: img/CALI.slt.2.png

**Si estás utilizando la regla de 60°**

#. Coloca la **regla de calibración (placa acrílica en C)** como se muestra, con el borde largo apoyado en la superficie horizontal. Presiona ``1`` en la terminal y usa las teclas ``w`` y ``s`` para alinear los bordes.

    .. image:: img/CALI.60.1.JPG

#. Vuelve a colocar la **regla de calibración** como se muestra en la figura siguiente. Presiona ``2`` en la terminal y utiliza las teclas ``w`` y ``s`` para hacer un ajuste fino.

    .. image:: img/CALI.60.2.JPG

#. Repite el proceso de calibración para los servos del 3 al 8 para asegurarte de que las cuatro patas de PiDog estén correctamente calibradas.

**Si estás utilizando la regla de 90°**

#. Coloca la **regla de calibración (placa acrílica en C)** como se muestra. Presiona ``1`` en la terminal y utiliza ``w`` y ``s`` para alinear los bordes con la imagen de referencia.

    .. image:: img/CALI-1.2.png

#. Vuelve a colocar la **regla de calibración (placa acrílica en C)** como se muestra. Presiona ``2`` en la terminal y vuelve a ajustar con ``w`` y ``s``.

    .. image:: img/CALI-2.2.png

#. Repite el procedimiento de calibración para los servos del 3 al 8 para asegurarte de que las cuatro patas de PiDog estén correctamente calibradas.

**Finalización de la calibración**

- Una vez calibrados todos los servos, vuelve a ejecutar los códigos de ejemplo de caminar o de postura de PiDog para verificar que los movimientos sean fluidos.  
- Si notas alguna desviación, vuelve al programa de calibración para hacer ajustes.  
- Se recomienda completar este paso inmediatamente después del primer ensamblaje para garantizar un funcionamiento estable.

.. tip::

   Para evitar tener que recalibrar, puedes registrar los ángulos de los servos o exportar el archivo de configuración una vez finalizada la calibración. Esto te permitirá restaurar la configuración rápidamente en el futuro.
