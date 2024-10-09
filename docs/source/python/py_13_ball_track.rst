.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _py_ball_track:

13. Seguimiento de Pelota
===============================

PiDog se quedará sentado en silencio. Si pones una pelota roja frente a él, se 
levantará y comenzará a perseguirla.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/bull_track.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 13_ball_track.py

Después de ejecutar este código, PiDog activará la cámara. Puedes acceder a la 
dirección ``http://+ PiDog's IP +/mjpg`` (por ejemplo, en mi caso es ``http://192.168.18.138:9000/mjpg``) en tu navegador para ver la transmisión de la cámara.

**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de hacerlo, debes ir a la ruta del código fuente, como ``pidog\examples``. Después de modificar el código, podrás ejecutarlo directamente para ver los resultados.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from vilib import Vilib
    from preset_actions import bark

    my_dog = Pidog()

    sleep(0.1)

    STEP = 0.5

    def delay(time):
        my_dog.wait_legs_done()
        my_dog.wait_head_done()
        sleep(time)

    def ball_track():
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=True, web=True)
        Vilib.color_detect_switch(True)
        sleep(0.2)
        print('start')
        yaw = 0
        roll = 0
        pitch = 0
        flag = False
        direction = 0

        my_dog.do_action('stand', speed=50)
        my_dog.head_move([[yaw, 0, pitch]], immediately=True, speed=80)
        delay(0.5)

        while True:

            ball_x = Vilib.detect_obj_parameter['color_x'] - 320
            ball_y = Vilib.detect_obj_parameter['color_y'] - 240
            width = Vilib.detect_obj_parameter['color_w']

            if ball_x > 15 and yaw > -80:
                yaw -= STEP

            elif ball_x < -15 and yaw < 80:
                yaw += STEP

            if ball_y > 25:
                pitch -= STEP
                if pitch < - 40:
                    pitch = -40
            elif ball_y < -25:
                pitch += STEP
                if pitch > 20:
                    pitch = 20

            print(f"yaw: {yaw}, pitch: {pitch}, width: {width}")

            my_dog.head_move([[yaw, 0, pitch]], immediately=True, speed=100)
            if width == 0:
                pitch = 0
                yaw = 0
            elif width < 300:
                if my_dog.is_legs_done():
                    if yaw < -30:
                        print("turn right")
                        my_dog.do_action('turn_right', speed=98)
                    elif yaw > 30:
                        print("turn left")
                        my_dog.do_action('turn_left', speed=98)
                    else:
                        my_dog.do_action('forward', speed=98)
            sleep(0.02)


    if __name__ == "__main__":
        try:
            ball_track()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            Vilib.camera_close()
            my_dog.close()
