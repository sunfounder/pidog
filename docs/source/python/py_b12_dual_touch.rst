.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

12. Caresser la tête du PiDog
================================

Le capteur tactile situé sur la tête de PiDog peut détecter la manière dont vous le touchez. Vous pouvez utiliser les fonctions suivantes pour exploiter ce module.

.. code-block:: python

   Pidog.dual_touch.read()

* Si vous touchez le module de la gauche vers la droite (de l'avant vers l'arrière par rapport à l'orientation de PiDog), il renverra ``"LS"``.
* Si vous touchez le module de la droite vers la gauche, il renverra ``"RS"``.
* Si vous touchez seulement le côté gauche du module, il renverra ``"L"``.
* Si vous touchez seulement le côté droit du module, il renverra ``"R"``.
* Si le module n'est pas touché, il renverra ``"N"``.

**Voici un exemple d'utilisation :**

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()
    while True:
        touch_status = my_dog.dual_touch.read()
        print(f"touch_status: {touch_status}")
        time.sleep(0.5)

