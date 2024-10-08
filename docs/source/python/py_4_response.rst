.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

4. Réaction
================

Dans ce projet, PiDog interagit avec vous de manière amusante.

Si vous approchez la tête de PiDog par l'avant, il aboiera de manière vigilante.

.. image:: img/py_4-2.gif
    :width: 430

Mais si vous l'approchez par derrière et lui caressez la tête, il montrera des signes d'appréciation.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/touch_head.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 4_response.py

Après avoir exécuté cet exemple, le module ultrasonique de PiDog détectera s'il y a un obstacle devant lui.  
S'il détecte votre main, la lumière respiratoire devient rouge, il recule et aboie.

En même temps, le capteur tactile se met en marche. Si le capteur est caressé (et non simplement touché),  
PiDog secouera la tête, remuera la queue et affichera une expression de plaisir.


**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Avant cela, vous devez vous rendre dans le répertoire source comme ``pidog\examples``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir le résultat.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from math import sin
    from preset_actions import bark_action

    my_dog = Pidog()
    sleep(0.1)

    def lean_forward():
        my_dog.speak('angry', volume=80)
        bark_action(my_dog)
        sleep(0.2)
        bark_action(my_dog)
        sleep(0.8)
        bark_action(my_dog)

    def head_nod(step):
        y = 0
        r = 0
        p = 30
        angs = []
        for i in range(20):
            r = round(10*sin(i*0.314), 2)
            p = round(20*sin(i*0.314) + 10, 2)
            angs.append([y, r, p])

        my_dog.head_move(angs*step, immediately=False, speed=80)

    def alert():
        my_dog.do_action('stand', step_count=1, speed=90)
        my_dog.rgb_strip.set_mode('breath', color='pink', bps=1, brightness=0.8)
        while True:
            print(
                f'distance.value: {round(my_dog.ultrasonic.read_distance(), 2)} cm, touch {my_dog.dual_touch.read()}')
            # alert
            if my_dog.ultrasonic.read_distance() < 15 and my_dog.ultrasonic.read_distance() > 1:
                my_dog.head_move([[0, 0, 0]], immediately=True, speed=90)
                my_dog.tail_move([[0]], immediately=True, speed=90)
                my_dog.rgb_strip.set_mode('bark', color='red', bps=2, brightness=0.8)
                my_dog.do_action('backward', step_count=1, speed=98)
                my_dog.wait_all_done()
                lean_forward()
                while len(my_dog.legs_action_buffer) > 0:
                    sleep(0.1)
                my_dog.do_action('stand', step_count=1, speed=90)
                sleep(0.5)
            # relax
            if my_dog.dual_touch.read() != 'N':
                if len(my_dog.head_action_buffer) < 2:
                    head_nod(1)
                    my_dog.do_action('wag_tail', step_count=10, speed=80)
                    my_dog.rgb_strip.set_mode('listen', color="#8A2BE2", bps=0.35, brightness=0.8)
            # calm
            else:
                my_dog.rgb_strip.set_mode('breath', color='pink', bps=1, brightness=0.8)
                my_dog.tail_stop()
            sleep(0.2)

    if __name__ == "__main__":
        try:
            alert()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()
