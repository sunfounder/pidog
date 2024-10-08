.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Robot HAT
==================

|link_robot_hat_v4| est une carte d'extension multifonctionnelle qui permet de transformer rapidement un Raspberry Pi en robot. 
Un microcontrôleur (MCU) est intégré pour étendre les sorties PWM et les entrées ADC du Raspberry Pi, 
ainsi qu'une puce de pilotage moteur, un module audio I2S et un haut-parleur mono. 
Elle inclut également les GPIO du Raspberry Pi.

Le module est livré avec un haut-parleur, 
qui peut être utilisé pour jouer de la musique de fond, des effets sonores et implémenter des fonctions TTS afin de rendre votre projet plus interactif.

Il accepte une alimentation de 7-12V via un connecteur PH2.0 5 broches avec 2 indicateurs de batterie, 1 indicateur de charge et 1 indicateur d'alimentation. 
La carte comprend également une LED utilisateur disponible et un bouton permettant de tester rapidement certains effets.

.. image:: img/O1902V40RobotHAT.png

**Port d'Alimentation**
    * Entrée d'alimentation PH2.0 3 broches, 7-12V.
    * Alimente le Raspberry Pi et le Robot HAT en même temps.

**Interrupteur d'Alimentation**
    * Permet d'allumer/éteindre le Robot HAT.
    * Lorsque vous connectez l'alimentation au port d'alimentation, le Raspberry Pi démarre automatiquement. Cependant, vous devrez passer l'interrupteur sur ON pour activer le Robot HAT.

**Port USB Type-C**
    * Insérez le câble Type-C pour charger la batterie.
    * L'indicateur de charge s'allume en rouge pendant le chargement.
    * Une fois la batterie complètement chargée, l'indicateur de charge s'éteint.
    * Si le câble USB reste connecté environ 4 heures après une charge complète, l'indicateur de charge clignote pour avertir.

**Broches Numériques**
    * 4 broches numériques, D0-D3.

**Broches ADC**
    * 4 broches ADC, A0-A3.

**Broches PWM**
    * 12 broches PWM, P0-P11.

**Ports Moteur Gauche/Droite**
    * 2 ports moteur XH2.54.
    * Le port gauche est connecté au GPIO 4 et le port droit au GPIO 5.

**Broches et Port I2C**
    * **Broches I2C** : Interface P2.54 à 4 broches.
    * **Port I2C** : Interface SH1.0 à 4 broches, compatible avec QWIIC et STEMMA QT. 
    * Ces interfaces I2C sont reliées aux broches I2C du Raspberry Pi via les GPIO2 (SDA) et GPIO3 (SCL).

**Broches SPI**
    * Interface SPI P2.54 à 7 broches.

**Broches UART**
    * Interface UART P2.54 à 4 broches.

**Bouton RST**
    * Le bouton RST sert à redémarrer le programme Ezblock lorsque vous utilisez Ezblock. 
    * Si vous n'utilisez pas Ezblock, le bouton RST n'a pas de fonction prédéfinie et peut être entièrement personnalisé selon vos besoins.

**Bouton USR**
    * Les fonctions du bouton USR peuvent être définies par votre programmation. (Appuyer active une entrée “0” ; relâcher produit une entrée “1”.) 

**Indicateur de Batterie**
    * Deux LEDs s'allument lorsque la tension est supérieure à 7,6V.
    * Une LED s'allume lorsque la tension est comprise entre 7,15V et 7,6V. 
    * En dessous de 7,15V, les deux LEDs s'éteignent.

**Haut-parleur et Port Haut-parleur**
    * **Haut-parleur** : Haut-parleur mono de chambre acoustique 2030.
    * **Port Haut-parleur** : Le Robot HAT est équipé d'une sortie audio I2S intégrée et d'un haut-parleur de chambre acoustique 2030, offrant une sortie audio mono.
