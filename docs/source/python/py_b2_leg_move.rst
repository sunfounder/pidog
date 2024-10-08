.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_b2_leg_move:

2. Mouvement des pattes
===========================

Les mouvements des pattes de PiDog sont implémentés par les fonctions suivantes.

.. code-block:: python

    Pidog.legs_move(target_angles, immediately=True, speed=50)

* ``target_angles`` : C'est un tableau bidimensionnel composé de plusieurs groupes de 8 angles de servomoteurs (appelés groupes d'angles). Ces groupes seront utilisés pour contrôler les angles des 8 servos des pattes. Si plusieurs groupes d'angles sont définis, ceux qui n'ont pas été exécutés seront stockés dans le cache.
* ``immediately`` : Lorsque ce paramètre est défini sur ``True``, le cache est immédiatement vidé pour exécuter le nouveau groupe d'angles ; si le paramètre est défini sur ``False``, le nouveau groupe d'angles est ajouté à la file d'attente d'exécution.
* ``speed`` : La vitesse à laquelle le groupe d'angles est exécuté.

**Quelques utilisations courantes sont listées ci-dessous :**

1. Exécution immédiate de l'action.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # demi-position debout
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)   


2. Ajouter des groupes d'angles à la file d'attente d'exécution.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # demi-position debout
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # actions multiples
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70],
                        [90, -30, -90, 30, 80, 70, -80, -70],
                        [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   

3. Effectuer des répétitions pendant 10 secondes.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # demi-position debout
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # préparation pour les pompes
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], immediately=False, speed=20)

    # exécution des pompes
    for _ in range(99):
        my_dog.legs_move([[90, -30, -90, 30, 80, 70, -80, -70],
                            [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   

    # maintien pendant 10 secondes
    time.sleep(10)

    # arrêt et demi-position debout
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], immediately=True, speed=50)  


**Le contrôle des pattes de PiDog dispose également des fonctions suivantes, utilisables conjointement :**

.. code-block:: python

    Pidog.is_legs_done()

Cette fonction permet de déterminer si les groupes d'angles dans le cache ont été exécutés. Si oui, retourne ``True`` ; sinon, retourne ``False``.

.. code-block:: python

    Pidog.wait_legs_done()

Suspend le programme jusqu'à ce que les groupes d'angles dans le cache soient exécutés.

.. code-block:: python

    Pidog.legs_stop() 

Vide le cache des groupes d'angles.
