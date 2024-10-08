.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

7. Suivi de Visage
======================

PiDog s'assiéra tranquillement en place. Si vous applaudissez, il tournera la tête dans votre direction et, s'il vous voit, il vous saluera.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/face_track.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 7_face_track.py

Après avoir exécuté ce code, PiDog activera la caméra et la fonction de détection de visage.  
Vous pouvez visiter ``http://+ l'IP de PiDog +/mjpg`` (par exemple, ``http://192.168.18.138:9000/mjpg``) dans votre navigateur pour voir l'image de la caméra.

Ensuite, PiDog s'assiéra et activera le module de détection de direction sonore pour capter l'origine de vos applaudissements.  
Quand PiDog entend des applaudissements (ou tout autre bruit), il tournera la tête vers la source sonore pour tenter de vous repérer.

S'il vous voit (la détection faciale identifie un objet), il agitera la queue et aboiera pour vous saluer.


**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Avant cela, vous devez vous rendre dans le répertoire source comme ``pidog\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir le résultat.

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

    def face_track():
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=True, web=True)
        Vilib.human_detect_switch(True)
        sleep(0.2)
        print('start')
        yaw = 0
        roll = 0
        pitch = 0
        flag = False
        direction = 0

        my_dog.do_action('sit', speed=50)
        my_dog.head_move([[yaw, 0, pitch]], pitch_comp=-40, immediately=True, speed=80)
        my_dog.wait_all_done()
        sleep(0.5)

        if my_dog.ears.isdetected():    
            direction = my_dog.ears.read()

        while True:
            if flag == False:
                my_dog.rgb_strip.set_mode('breath', 'pink', bps=1)
            # If heard somthing, turn to face it
            if my_dog.ears.isdetected():
                flag = False
                direction = my_dog.ears.read()
                pitch = 0
                if direction > 0 and direction < 160:
                    yaw = -direction
                    if yaw < -80:
                        yaw = -80
                elif direction > 200 and direction < 360:
                    yaw = 360 - direction
                    if yaw > 80:
                        yaw = 80
                my_dog.head_move([[yaw, 0, pitch]], pitch_comp=-40, immediately=True, speed=80)
                my_dog.wait_head_done()
                sleep(0.05)

            ex = Vilib.detect_obj_parameter['human_x'] - 320
            ey = Vilib.detect_obj_parameter['human_y'] - 240
            people = Vilib.detect_obj_parameter['human_n']

            # If see someone, bark at him/her
            if people > 0 and flag == False:
                flag = True
                my_dog.do_action('wag_tail', step_count=2, speed=100)
                bark(my_dog, [yaw, 0, 0], pitch_comp=-40, volume=80)
                if my_dog.ears.isdetected():
                    direction = my_dog.ears.read()

            if ex > 15 and yaw > -80:
                yaw -= 0.5 * int(ex/30.0+0.5)

            elif ex < -15 and yaw < 80:
                yaw += 0.5 * int(-ex/30.0+0.5)

            if ey > 25:
                pitch -= 1*int(ey/50+0.5)
                if pitch < - 30:
                    pitch = -30
            elif ey < -25:
                pitch += 1*int(-ey/50+0.5)
                if pitch > 30:
                    pitch = 30

            print('direction: %s |number: %s | ex, ey: %s, %s | yrp: %s, %s, %s '
                % (direction, people, ex, ey, round(yaw, 2), round(roll, 2), round(pitch, 2)),
                end='\r',
                flush=True,
                )
            my_dog.head_move([[yaw, 0, pitch]], pitch_comp=-40, immediately=True, speed=100)
            sleep(0.05)


    if __name__ == "__main__":
        try:
            face_track()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            Vilib.camera_close()
            my_dog.close()
