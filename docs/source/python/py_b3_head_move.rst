.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

3. Mouvement de la tête
===========================

Le contrôle des servomoteurs de la tête de PiDog est réalisé par les fonctions suivantes :

.. code-block:: python

    Pidog.head_move(target_yrps, roll_comp=0, pitch_comp=0, immediately=True, speed=50)

* ``target_yrps`` : C'est un tableau bidimensionnel composé de plusieurs groupes d'angles de 3 servomoteurs (appelés groupes d'angles). Ces groupes seront utilisés pour contrôler les angles des servos de la tête. Si plusieurs groupes d'angles sont définis, ceux qui n'ont pas été exécutés seront stockés dans le cache.
* ``roll_comp`` : Compensation angulaire sur l'axe de roulis.
* ``pitch_comp`` : Compensation angulaire sur l'axe de tangage.
* ``immediately`` : Lorsque ce paramètre est défini sur ``True``, le cache est immédiatement vidé pour exécuter le nouveau groupe d'angles ; si le paramètre est défini sur ``False``, le nouveau groupe d'angles est ajouté à la file d'attente d'exécution.
* ``speed`` : La vitesse d'exécution du groupe d'angles.

**Le contrôle des servomoteurs de la tête de PiDog comprend également des fonctions de support :**

.. code-block:: python

    Pidog.is_head_done()

Détermine si toutes les actions de la tête dans le cache ont été exécutées.

.. code-block:: python

    Pidog.wait_head_done()

Attend que toutes les actions de la tête dans le cache soient exécutées.

.. code-block:: python

    Pidog.head_stop()

Efface toutes les actions de la tête présentes dans le cache pour arrêter les servomoteurs de la tête.


**Voici quelques cas d'utilisation courants :**

1. Hochement de tête cinq fois.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(5):
        my_dog.head_move([[0, 0, 30],[0, 0, -30]], speed=80)
        my_dog.wait_head_done()
        time.sleep(0.5)

2. Secouer la tête pendant 10 secondes.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.head_move([[30, 0, 0],[-30, 0, 0]], immediately=False, speed=30)

    # maintenir pendant 10 secondes
    time.sleep(10)

    my_dog.head_move([[0, 0, 0]], immediately=True, speed=80)

3. PiDog garde la tête horizontale lorsqu'il secoue la tête, qu'il soit assis ou en demi-position debout.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # liste d'actions
    shake_head = [[30, 0, 0],[-30, 0, 0]]
    half_stand_leg = [[45, 10, -45, -10, 45, 10, -45, -10]]
    sit_leg = [[30, 60, -30, -60, 80, -45, -80, 45]]

    while True:
        # secouer la tête en demi-position debout
        my_dog.legs_move(half_stand_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=0, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)

        # secouer la tête en position assise
        my_dog.legs_move(sit_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=-30, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)
