.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Module Ultrasonique
================================

.. image:: img/ultrasonic_pic.png
    :width: 400
    :align: center

* **TRIG** : Entrée du signal de déclenchement
* **ECHO** : Sortie du signal d'écho
* **GND** : Masse
* **VCC** : Alimentation 5V

Il s'agit du capteur de distance ultrasonique HC-SR04, permettant des mesures sans contact de 2 cm à 400 cm avec une précision de l'ordre de 3 mm. Le module comprend un émetteur ultrasonique, un récepteur et un circuit de contrôle.

Il suffit de connecter 4 broches : VCC (alimentation), Trig (déclenchement), Echo (réception) et GND (masse) pour l'utiliser facilement dans vos projets de mesure.

**Caractéristiques**

* Tension de fonctionnement : DC5V
* Courant de fonctionnement : 16mA
* Fréquence de travail : 40Hz
* Portée maximale : 500 cm
* Portée minimale : 2 cm
* Signal d'entrée de déclenchement : impulsion TTL de 10 µS
* Signal de sortie d'écho : signal de niveau TTL en proportion avec la distance mesurée
* Connecteur : XH2.54-4P
* Dimensions : 46 x 20,5 x 15 mm

**Principe**

Les principes de base sont les suivants :

* Utilisez un déclencheur IO avec un signal de niveau haut d'au moins 10 µs.
* Le module envoie une rafale de 8 cycles d'ultrasons à 40 kHz et détecte si un signal de retour est reçu.
* Echo émet un signal de niveau haut si un signal est renvoyé ; la durée de ce niveau haut correspond au temps écoulé entre l'émission et le retour.
* Distance = (durée du niveau haut x vitesse du son (340 m/s)) / 2

    .. image:: img/ultrasonic_prin.jpg
        :width: 800

Formule : 

* µs / 58 = distance en centimètres
* µs / 148 = distance en pouces
* distance = durée du niveau haut x vitesse (340 m/s) / 2

**Notes d'application**

* Ce module ne doit pas être connecté sous tension ; si nécessaire, connectez d'abord le GND du module. Sinon, cela pourrait affecter son fonctionnement.
* La surface de l'objet à mesurer doit être d'au moins 0,5 mètre carré et aussi plane que possible. Sinon, cela pourrait fausser les résultats.
