.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez au cœur de l'univers du Raspberry Pi, d'Arduino et d'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

10. Équilibre
=================

Grâce à son module IMU 6-DOF, PiDog possède un excellent sens de l'équilibre.

Dans cet exemple, vous pouvez faire marcher PiDog en douceur sur une table. Même si vous soulevez un côté de la table, PiDog continuera à marcher en toute stabilité sur la pente douce.

.. image:: img/py_10.gif

**Exécution du Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 10_balance.py

Une fois le programme lancé, un clavier virtuel s'affichera dans le terminal.
Vous pouvez contrôler PiDog pour qu'il marche en douceur sur la rampe en utilisant les touches suivantes :

.. list-table:: 
    :widths: 25 25
    :header-rows: 1

    * - Touches
      - Fonction
    * -  W
      -  Avancer 
    * -  E
      -  Se tenir debout 
    * -  A
      -  Tourner à gauche 
    * -  S
      -  Reculer 
    * -  D
      -  Tourner à droite 
    * -  R
      -  Chaque pression soulève légèrement le corps ; plusieurs appuis sont nécessaires pour observer une montée notable.
    * -  F
      -  Chaque pression abaisse légèrement le corps ; plusieurs appuis sont nécessaires pour observer une descente notable.
    

**Code**

Vous pouvez consulter le code sur |link_code_10_balance|.
