.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

11. Détection de la Direction du Son
=======================================

PiDog est équipé d'un module de détection de direction sonore capable de déterminer d'où provient le son, et nous pouvons le déclencher en applaudissant près de lui.

**L'utilisation de ce module est très simple, il suffit d'appeler les fonctions suivantes :**

.. code-block:: python

    Pidog.ears.isdetected()

Renvoie ``True`` si un son est détecté, ``False`` sinon.

.. code-block:: python

    Pidog.ears.read()

Cette fonction renvoie la direction de la source sonore, avec une plage allant de 0 à 359 ; si le son provient de l'avant, la fonction renverra 0 ; s'il provient de la droite, elle renverra 90.

**Voici un exemple d'utilisation de ce module :**

.. code-block:: python

    from pidog import Pidog

    my_dog = Pidog()

    while True:
        if my_dog.ears.isdetected():
            direction = my_dog.ears.read()
            print(f"sound direction: {direction}")





