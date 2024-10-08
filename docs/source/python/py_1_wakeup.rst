.. note::

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_wake_up:

1. Réveil
===============

Il s'agit du premier projet de PiDog. Il réveillera votre PiDog d'un sommeil profond.

.. image:: img/py_wakeup.gif


**Exécution du Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

Après l'exécution du code, 
PiDog effectuera les actions suivantes dans l'ordre : 

S'étirer, se tordre, s'asseoir, remuer la queue, haleter.



**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Avant cela, vous devez vous rendre dans le répertoire source comme ``pidog\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir le résultat.

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
        # s'étirer
        my_dog.rgb_strip.set_mode('listen', color='yellow', bps=0.6, brightness=0.8)
        my_dog.do_action('stretch', speed=50)
        my_dog.head_move([[0, 0, 30]]*2, immediately=True)
        my_dog.wait_all_done()
        sleep(0.2)
        body_twisting(my_dog)
        my_dog.wait_all_done()
        sleep(0.5)
        my_dog.head_move([[0, 0, -30]], immediately=True, speed=90)
        # s'asseoir et remuer la queue
        my_dog.do_action('sit', speed=25)
        my_dog.wait_legs_done()
        my_dog.do_action('wag_tail', step_count=10, speed=100)
        my_dog.rgb_strip.set_mode('breath', color=[245, 10, 10], bps=2.5, brightness=0.8)
        pant(my_dog, pitch_comp=-30, volume=80)
        my_dog.wait_all_done()
        # maintenir
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

