.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

1. Initialisation de PiDog
=============================

Les fonctionnalités de PiDog sont regroupées dans la classe ``Pidog``, dont le prototype est présenté ci-dessous.

.. code-block:: python

    Class: Pidog()

    __init__(leg_pins=DEFAULT_LEGS_PINS, 
            head_pins=DEFAULT_HEAD_PINS,
            tail_pin=DEFAULT_TAIL_PIN,
            leg_init_angles=None,
            head_init_angles=None,
            tail_init_angle=None)


PiDog doit être instancié de plusieurs manières, comme indiqué ci-dessous.

1. Voici les étapes les plus simples d'initialisation.

.. code-block:: python

    # Importation de la classe Pidog
    from pidog import Pidog

    # Instanciation d'un Pidog
    my_dog = Pidog()

2. PiDog dispose de 12 servomoteurs, qui peuvent être initialisés lors de l'instanciation.

.. code-block:: python

    # Importation de la classe Pidog
    from pidog import Pidog

    # Instanciation d'un Pidog avec des angles de servos personnalisés
    my_dog = Pidog(leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )

Dans la classe ``Pidog``, les servomoteurs sont divisés en trois groupes :

* ``leg_init_angles`` : Dans ce tableau, 8 valeurs définissent les angles des huit servos, contrôlant les servos (numéros de broche) ``2, 3, 7, 8, 0, 1, 10, 11``. À partir du schéma de déploiement, vous pouvez voir où ces servos sont situés.

* ``head_init_angles`` : Ce tableau contient 3 valeurs, correspondant aux servos de direction (yaw), de roulis (roll) et de tangage (pitch) de la tête de PiDog (``no. 4, 6, 5``) qui réagissent aux mouvements de la tête ou aux déviations du corps.

* ``tail_init_angle`` : Ce tableau ne contient qu'une seule valeur, dédiée au contrôle du servo de la queue, qui est ``9``.

3. ``Pidog`` permet de redéfinir l'ordre des servos lors de l'instanciation si votre configuration est différente.

.. code-block:: python

    # Importation de la classe Pidog
    from pidog import Pidog

    # Instanciation d'un Pidog avec des broches et des angles de servos personnalisés
    my_dog = Pidog(leg_pins=[2, 3, 7, 8, 0, 1, 10, 11], 
                    head_pins=[4, 6, 5],
                    tail_pin=[9],
                    leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )