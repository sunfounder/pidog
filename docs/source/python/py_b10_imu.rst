.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Sumérgete más a fondo en Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirte?**

    - **Soporte de Expertos**: Resuelve problemas postventa y supera desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y Compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede de forma anticipada a anuncios de nuevos productos y vistas previas exclusivas.
    - **Descuentos Especiales**: Aprovecha descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

10. Lectura del IMU
=======================

A través del Módulo IMU de 6 grados de libertad (6-DOF), PiDog puede detectar si está en una pendiente o si ha sido levantado.

El Módulo IMU de 6-DOF está equipado con un acelerómetro de 3 ejes y un giroscopio de 3 ejes, lo que permite medir la aceleración y la velocidad angular en tres direcciones.

.. note::

    Antes de utilizar el módulo, asegúrate de que esté correctamente ensamblado. La etiqueta en el módulo te indicará si está colocado al revés.

**Puedes leer su aceleración con:**

.. code-block:: python

   ax, ay, az = Pidog.accData

Si PiDog está colocado horizontalmente, la aceleración en el eje x (es decir, ax) debería ser cercana a la aceleración de la gravedad (1g), con un valor de -16384.
Los valores de los ejes y y z estarán cerca de 0.

**Usa el siguiente método para leer la velocidad angular:**

.. code-block:: python

   gx, gy, gz = my_dog.gyroData

En el caso de que PiDog esté colocado horizontalmente, los tres valores deberían estar cerca de 0.


**A continuación, algunos ejemplos de cómo utilizar el módulo de 6-DOF:**

1. Leer aceleración y velocidad angular en tiempo real.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    my_dog.do_action("pushup", step_count=10, speed=20)

    while True:
        ax, ay, az = my_dog.accData
        gx, gy, gz = my_dog.gyroData
        print(f"accData: {ax/16384:.2f} g ,{ay/16384:.2f} g, {az/16384:.2f} g       gyroData: {gx} °/s, {gy} °/s, {gz} °/s")
        time.sleep(0.2)
        if my_dog.is_legs_done():
            break

    my_dog.stop_and_lie()

    my_dog.close()

2. Calcular el ángulo de inclinación del cuerpo de PiDog.

.. code-block:: python

    from pidog import Pidog
    import time
    import math

    my_dog = Pidog()

    while True:
        ax, ay, az = my_dog.accData
        body_pitch = math.atan2(ay,ax)/math.pi*180%360-180
        print(f"Body Degree: {body_pitch:.2f} °" )
        time.sleep(0.2)

    my_dog.close()

3. Mantener la cabeza nivelada mientras PiDog está inclinado.

.. code-block:: python

    from pidog import Pidog
    import time
    import math

    my_dog = Pidog()

    while True:
        ax, ay, az = my_dog.accData
        body_pitch = math.atan2(ay,ax)/math.pi*180%360-180
        my_dog.head_move([[0, 0, 0]], pitch_comp=-body_pitch, speed=80)
        time.sleep(0.2)

    my_dog.close()