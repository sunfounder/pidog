.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_ball_track:

13. Suivi de la balle
==========================

PiDog reste tranquillement assis sur place.  
Placez une balle rouge devant lui, il se lèvera et commencera à la suivre.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/bull_track.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 13_ball_track.py

Après avoir exécuté ce code, PiDog démarrera la caméra.  
Vous pouvez visiter ``http://+ PiDog's IP +/mjpg`` (par exemple, ``http://192.168.18.138:9000/mjpg``) dans votre navigateur pour voir l'image de la caméra.

**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Avant cela, vous devez vous rendre dans le répertoire source comme ``pidog\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour observer le résultat.

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
