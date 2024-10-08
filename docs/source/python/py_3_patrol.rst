.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

3. Patrouille
==================

Dans ce projet, PiDog exécute un comportement dynamique : la patrouille.

PiDog avance, et si un obstacle se trouve devant lui, il s'arrête et aboie.

.. image:: img/py_3.gif

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 3_patrol.py

Après avoir exécuté cet exemple, PiDog remue la queue, scanne de gauche à droite, puis avance.


**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Avant cela, vous devez vous rendre dans le répertoire source comme ``pidog\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir le résultat.

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

        # danger
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
        # sûr
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