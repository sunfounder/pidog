.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers du Raspberry Pi, d'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

5. Repos
=============

Dans ce projet, PiDog se couchera et s'endormira. Lorsqu'il détecte un son autour de lui, il se lèvera, confus, pour voir qui l'a réveillé.

.. image:: img/py_5.gif

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 5_rest.py

Après avoir lancé le programme, PiDog s'allongera au sol, secouera la tête et remuera la queue comme s'il somnolait.  
Pendant ce temps, son module de détection de direction sonore sera activé. Si PiDog entend un bruit, il se lèvera, regardera autour de lui et affichera un air perplexe.  
Ensuite, il se recouchera pour se rendormir.


**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Avant cela, vous devez vous rendre dans le répertoire source comme ``pidog\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir le résultat.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import shake_head

    my_dog = Pidog()
    sleep(0.1)

    def loop_around(amplitude=60, interval=0.5, speed=100):
        my_dog.head_move([[amplitude,0,0]], immediately=True, speed=speed)
        my_dog.wait_all_done()
        sleep(interval)
        my_dog.head_move([[-amplitude,0,0]], immediately=True, speed=speed)
        my_dog.wait_all_done()
        sleep(interval)
        my_dog.head_move([[0,0,0]], immediately=True, speed=speed)
        my_dog.wait_all_done()

    def is_sound():
        if my_dog.ears.isdetected():
            direction = my_dog.ears.read()
            if direction != 0:
                return True
            else:
                return False
        else:
            return False

    def rest():
        my_dog.wait_all_done()
        my_dog.do_action('lie', speed=50)
        my_dog.wait_all_done()

        while True:
            # Sommeil
            my_dog.rgb_strip.set_mode('breath', 'pink', bps=0.3)
            my_dog.head_move([[0,0,-40]], immediately=True, speed=5)
            my_dog.do_action('doze_off', speed=92)
            # Réinitialisation de la détection sonore
            sleep(1)
            is_sound()

            # Continue de dormir
            while detecter_son() is False:
                my_dog.do_action('doze_off', speed=92)
                sleep(0.2)

            # Si un bruit est détecté, se réveiller
            # Allumer la lumière en jaune et se lever
            my_dog.rgb_strip.set_mode('boom', 'yellow', bps=1)
            my_dog.body_stop()
            my_dog.do_action('stand', speed=90)
            my_dog.head_move([[0, 0, 0]], immediately=True, speed=80)
            my_dog.wait_all_done()
            # Regarder autour
            loop_around(60, 1, 60)
            sleep(0.5)
            # Pencher la tête et afficher un air confus
            my_dog.speak('confused_3', volume=80)
            my_dog.do_action('tilting_head_left', speed=80)
            my_dog.wait_all_done()
            sleep(1.2)
            my_dog.head_move([[0, 0, -10]], immediately=True, speed=80)
            my_dog.wait_all_done()
            sleep(0.4)
            # Secouer la tête, signifiant qu'il ignore le bruit
            shake_head(my_dog)
            sleep(0.2)

            # Se recoucher
            my_dog.rgb_strip.set_mode('breath', 'pink', bps=1)
            my_dog.do_action('lie', speed=50)
            my_dog.wait_all_done()
            sleep(1)

    if __name__ == "__main__":
        try:
            rest()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()