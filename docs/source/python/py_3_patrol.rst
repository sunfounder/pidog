.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

3. Patrullaje
=================

En este proyecto, PiDog ejecuta un comportamiento dinámico: patrullar.

PiDog caminará hacia adelante y, si hay un obstáculo frente a él, se detendrá y ladrará.

.. image:: img/py_3.gif

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 3_patrol.py

Después de ejecutar este ejemplo, PiDog moverá su cola, escaneará a la izquierda y a la derecha, y comenzará a caminar hacia adelante.


**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de eso, necesitas ir a la ruta del código fuente como ``pidog\examples``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.

.. raw:: html

    <run></run>

.. code-block:: python


    #!/usr/bin/env python3
    import time
    from pidog import Pidog
    from preset_actions import bark

    t = time.time()
    my_dog = Pidog()
    my_dog.do_action('stand', speed=80)
    my_dog.wait_all_done()
    time.sleep(.5)

    DANGER_DISTANCE = 15

    stand = my_dog.legs_angle_calculation([[0, 80], [0, 80], [30, 75], [30, 75]])

    def patrol():
        distance = round(my_dog.ultrasonic.read_distance(), 2)
        print(f"distance: {distance} cm", end="", flush=True)

        # peligro
        if distance < DANGER_DISTANCE:
            print("\033[0;31m DANGER !\033[m")
            my_dog.body_stop()
            head_yaw = my_dog.head_current_angles[0]
            # my_dog.rgb_strip.set_mode('boom', 'red', bps=2)
            my_dog.rgb_strip.set_mode('bark', 'red', bps=2)
            my_dog.tail_move([[0]], speed=80)
            my_dog.legs_move([stand], speed=70)
            my_dog.wait_all_done()
            time.sleep(0.5)
            bark(my_dog, [head_yaw, 0, 0])

            while distance < DANGER_DISTANCE:
                distance = round(my_dog.ultrasonic.read_distance(), 2)
                if distance < DANGER_DISTANCE:
                    print(f"distance: {distance} cm \033[0;31m DANGER !\033[m")
                else:
                    print(f"distance: {distance} cm", end="", flush=True)
                time.sleep(0.01)
        # seguro
        else:
            print("")
            my_dog.rgb_strip.set_mode('breath', 'white', bps=0.5)
            my_dog.do_action('forward', step_count=2, speed=98)
            my_dog.do_action('shake_head', step_count=1, speed=80)
            my_dog.do_action('wag_tail', step_count=5, speed=99)


    if __name__ == "__main__":
        try:
            while True:
                patrol()
                time.sleep(0.01)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()