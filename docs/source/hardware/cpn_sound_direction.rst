.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Capteur de Direction Sonore
=====================================

.. image:: img/cpn_sound.png
   :width: 400
   :align: center

Il s'agit d'un module de reconnaissance de direction sonore. Il est équipé de 3 microphones capables de détecter les sources sonores provenant de toutes les directions, et utilise un TR16F064B pour traiter les signaux acoustiques et calculer la direction de la source sonore. L'unité de détection minimale de ce module est de 20 degrés, et la plage de données est de 0 à 360°.

Processus de transmission des données : le contrôleur principal active la broche BUSY, et le TR16F064B commence à surveiller la direction. Lorsque le 064B reconnaît la direction, il abaisse la broche BUSY ;
Lorsque le contrôleur principal détecte que BUSY est bas, il envoie des données arbitraires de 16 bits au 064B (en suivant la transmission MSB), puis reçoit des données de 16 bits, qui correspondent aux informations de direction sonore traitées par le 064B.
Une fois terminé, le contrôleur principal remet la broche BUSY à l'état haut pour détecter de nouveau la direction.

**Spécifications**

* Alimentation : 3,3V
* Communication : SPI
* Connecteur : PH2.0 7P
* Plage d'angle de reconnaissance sonore : 360°
* Précision de l'angle de reconnaissance vocale : ~10°

**Brochage**

* GND - Entrée de masse
* VCC - Entrée d'alimentation 3,3V
* MOSI - SPI MOSI
* MISO - SPI MISO
* SCLK - Horloge SPI
* CS - Sélection de la puce SPI
* BUSY - Détection d'occupation
