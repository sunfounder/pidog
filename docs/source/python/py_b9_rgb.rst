.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

9. Bande RGB de PiDog
==========================

PiDog est équipé d'une bande lumineuse RGB sur son torse, qu'il utilise pour exprimer ses émotions.

Vous pouvez utiliser la fonction suivante pour la contrôler :

.. code-block:: python

    Pidog.rgb_strip.set_mode(style='breath', color='white', bps=1, brightness=1):

* ``style`` : Le mode d'affichage de la bande RGB. Les valeurs disponibles sont les suivantes :

  * ``breath``
  * ``boom``
  * ``bark``

* ``color`` : La couleur de la bande RGB. Vous pouvez utiliser des valeurs RGB hexadécimales, comme ``#a10a0a``, ou les noms de couleurs suivants :

  * ``"white"``
  * ``"black"``
  * ``"white"``
  * ``"red"``
  * ``"yellow"``
  * ``"green"``
  * ``"blue"``
  * ``"cyan"``
  * ``"magenta"``
  * ``"pink"``

* ``brightness`` : La luminosité de la bande RGB. Vous pouvez entrer une valeur décimale de 0 à 1, par exemple ``0,5``.

* ``delay`` : Valeur flottante indiquant la vitesse d'affichage de l'animation ; plus la valeur est petite, plus le changement est rapide.

Utilisez l'instruction suivante pour désactiver la bande RGB :

.. code-block:: python

    Pidog.rgb_strip.close()

Voici quelques exemples d'utilisation :

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    while True:
        # style="breath", color="pink"
        my_dog.rgb_strip.set_mode(style="breath", color='pink')
        time.sleep(3)

        # style:"bark", color="#a10a0a"
        my_dog.rgb_strip.set_mode(style="bark", color="#a10a0a")
        time.sleep(3)

        # style:"boom", color="#a10a0a", brightness=0.5, bps=2.5
        my_dog.rgb_strip.set_mode(style="boom", color="#a10a0a", bps=2.5, brightness=0.5)
        time.sleep(3)

        # close
        my_dog.rgb_strip.close()
        time.sleep(2)

