.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, d'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

11. Jouer avec PiDog en Utilisant le Clavier
===============================================

Dans cet exemple, nous utiliserons le clavier pour contrôler PiDog. Vous pouvez appuyer sur ces touches dans le terminal pour le faire agir.

.. list-table:: 
    :widths: 25 50 25 50 25 50
    :header-rows: 1

    * - Touches
      - Fonction
      - Touches
      - Fonction
      - Touches
      - Fonction  
    * - 1
      - S'assoupir
      - q
      - Aboyer plus fort
      - a
      - Tourner à gauche
    * - 2
      - Pompes
      - w
      - Avancer
      - s
      - Reculer
    * - 3
      - Hurler
      - e
      - Haleter
      - d
      - Tourner à droite
    * - 4
      - Se tordre
      - r
      - Remuer la queue
      - f
      - Secouer la tête
    * - 5
      - Se gratter
      - t
      - Incliner la tête
      - g
      - High five
    * - u
      - Rouler la tête
      - U
      - Rouler la tête+
      - z
      - S'allonger
    * - i
      - Inclinaison de la tête
      - I
      - Inclinaison de la tête+
      - x
      - Se lever
    * - o
      - Rouler la tête
      - O
      - Rouler la tête+
      - c
      - S'asseoir
    * - j
      - Rotation de la tête
      - J
      - Rotation de la tête+
      - v
      - S'étirer
    * - k
      - Inclinaison de la tête
      - K
      - Inclinaison de la tête+
      - m
      - Réinitialiser la tête
    * - l
      - Rotation de la tête
      - L
      - Rotation de la tête+
      - W
      - Trottiner

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 11_keyboard_control.py

Une fois le programme lancé, un clavier virtuel s'affichera dans le terminal. Vous pouvez maintenant contrôler PiDog en utilisant les touches du clavier.

**Code**

Vous pouvez consulter le code sur |link_code_11_keyboard_control|.
