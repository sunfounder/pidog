.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _py_wake_up:

1. Despertar
===============

Este es el primer proyecto de PiDog. Consiste en despertar a tu PiDog de un sueño profundo.

.. image:: img/py_wakeup.gif


**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

Después de ejecutar el código, 
PiDog realizará las siguientes acciones en secuencia:

Estirarse, girar el cuerpo, sentarse, mover la cola y jadear.


**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de eso, necesitas ir a la ruta del código fuente como ``pidog\examples``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import pant
    from preset_actions import body_twisting

    my_dog = Pidog(head_init_angles=[0, 0, -30])
    sleep(1)

    def wake_up():
        # estirarse
        my_dog.rgb_strip.set_mode('listen', color='yellow', bps=0.6, brightness=0.8)
        my_dog.do_action('stretch', speed=50)
        my_dog.head_move([[0, 0, 30]]*2, immediately=True)
        my_dog.wait_all_done()
        sleep(0.2)
        body_twisting(my_dog)
        my_dog.wait_all_done()
        sleep(0.5)
        my_dog.head_move([[0, 0, -30]], immediately=True, speed=90)
        # sentarse y mover la cola
        my_dog.do_action('sit', speed=25)
        my_dog.wait_legs_done()
        my_dog.do_action('wag_tail', step_count=10, speed=100)
        my_dog.rgb_strip.set_mode('breath', color=[245, 10, 10], bps=2.5, brightness=0.8)
        pant(my_dog, pitch_comp=-30, volume=80)
        my_dog.wait_all_done()
        # mantener
        my_dog.do_action('wag_tail', step_count=10, speed=30)
        my_dog.rgb_strip.set_mode('breath', 'pink', bps=0.5)
        while True:
            sleep(1)

    if __name__ == "__main__":
        try:
            wake_up()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()

