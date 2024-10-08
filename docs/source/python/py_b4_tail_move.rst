.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

4. Mouvement de la queue
============================

Les fonctions suivantes permettent de contrôler la queue de PiDog. Ce fonctionnement est similaire à celui du :ref:`py_b2_leg_move`.

.. code-block:: python

    Pidog.tail_move(target_angles, immediately=True, speed=50)

* ``target_angles`` : C'est un tableau bidimensionnel composé de groupes d'angles (un angle par groupe) servant à contrôler les mouvements de la queue. Si plusieurs groupes d'angles sont définis, ceux qui n'ont pas été exécutés seront stockés dans le cache.
* ``immediately`` : Lorsque ce paramètre est défini sur ``True``, le cache est immédiatement vidé pour exécuter le nouveau groupe d'angles ; si le paramètre est défini sur ``False``, le nouveau groupe d'angles est ajouté à la file d'attente d'exécution.
* ``speed`` : La vitesse d'exécution du groupe d'angles.

**Le contrôle du servomoteur de la queue de PiDog comprend également des fonctions de support :**

.. code-block:: python

    Pidog.is_tail_done()

Détermine si toutes les actions de la queue dans le cache ont été exécutées.

.. code-block:: python

    Pidog.wait_tail_done()

Attend que toutes les actions de la queue dans le cache soient exécutées.

.. code-block:: python

    Pidog.tail_stop()

Efface toutes les actions de la queue présentes dans le cache pour arrêter le servomoteur de la queue.


**Voici quelques cas d'utilisation courants :**

1. Agiter la queue pendant 10 secondes.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.tail_move([[30],[-30]], immediately=False, speed=30)

    # maintenir pendant 10 secondes
    time.sleep(10)

    my_dog.tail_stop()
