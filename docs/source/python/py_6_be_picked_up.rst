.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers du Raspberry Pi, d'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

6. Être Soulevé
===================

Essayez de soulever votre PiDog du sol, il aura l'impression de pouvoir voler et adoptera une pose de super-héros tout en s'exclamant de joie.

.. image:: img/py_6.gif

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 6_be_picked_up.py

Après avoir lancé le programme, le module IMU 6-DOF calculera en permanence l'accélération dans la direction verticale.  
Si PiDog est détecté dans un état d'apesanteur, il prendra une pose de super-héros et se réjouira.  
Sinon, il considérera être sur un terrain plat et adoptera une posture debout.


**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Avant cela, vous devez vous rendre dans le répertoire source comme ``pidog\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir le résultat.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep

    my_dog = Pidog()
    sleep(0.1)


    def fly():
        my_dog.rgb_strip.set_mode('boom', color='red', bps=3)
        my_dog.legs.servo_move([45, -45, 90, -80, 90, 90, -90, -90], speed=60)
        my_dog.do_action('wag_tail', step_count=10, speed=100)
        my_dog.speak('woohoo', volume=80)
        my_dog.wait_legs_done()
        sleep(1)

    def stand():
        my_dog.rgb_strip.set_mode('breath', color='green', bps=1)
        my_dog.do_action('stand', speed=60)
        my_dog.wait_legs_done()
        sleep(1)

    def be_picked_up():
        isUp = False
        upflag = False
        downflag = False

        stand()

        while True:
            ax = my_dog.accData[0]
            print('ax: %s, is up: %s' % (ax, isUp))

            # gravité : 1G = -16384
            if ax < -18000:  # si vers le bas, l'accélération est dans la même direction que la gravité, ax < -1G
                my_dog.body_stop()
                if upflag == False:
                    upflag = True
                if downflag == True:
                    isUp = False
                    downflag = False
                    stand()

            if ax > -13000:  # si vers le haut, l'accélération est opposée à la gravité, ax sera > -1G
                my_dog.body_stop()
                if upflag == True:
                    isUp = True
                    upflag = False
                    fly()
                if downflag == False:
                    downflag = True

            sleep(0.02)


    if __name__ == "__main__":
        try:
            be_picked_up()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()