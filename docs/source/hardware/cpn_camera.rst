.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Module Caméra
====================================

**Description**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Il s'agit d'un module caméra 5MP pour Raspberry Pi avec capteur OV5647. Il est prêt à l'emploi : connectez le câble ruban fourni au port CSI (Camera Serial Interface) de votre Raspberry Pi et c'est parti.

La carte est petite, environ 25mm x 23mm x 9mm, et ne pèse que 3g, ce qui la rend idéale pour des applications mobiles ou d'autres projets où la taille et le poids sont critiques. Le module caméra a une résolution native de 5 mégapixels et dispose d'un objectif à mise au point fixe qui capture des images fixes à 2592 x 1944 pixels. Il prend également en charge la vidéo en 1080p30, 720p60 et 640x480p90.

.. note:: 

   Le module ne peut capturer que des images et des vidéos, pas de son.

**Spécifications**

* **Résolution des images statiques** : 2592×1944 
* **Résolution vidéo prise en charge** : Enregistrement vidéo 1080p/30 ips, 720p/60 ips et 640 x480p 60/90 
* **Ouverture (F)** : 1.8 
* **Angle de vue** : 65 degrés 
* **Dimensions** : 24mm x 23,5mm x 8mm 
* **Poids** : 3g 
* **Interface** : Connecteur CSI 
* **Systèmes d'exploitation supportés** : Raspberry Pi OS (dernière version recommandée)


**Assemblage du module caméra**

Sur le module caméra ou le Raspberry Pi, vous trouverez un connecteur en plastique plat. Tirez délicatement sur le commutateur de fixation noir jusqu'à ce qu'il soit partiellement ouvert. Insérez le câble FFC dans le connecteur plastique dans le sens indiqué et repoussez le commutateur de fixation pour le verrouiller.

Si le câble FFC est correctement installé, il restera droit et ne se déconnectera pas lorsque vous le tirerez doucement. Si ce n'est pas le cas, réinstallez-le correctement.

.. image:: img/connect_ffc.png
.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   N'installez pas la caméra lorsque l'alimentation est sous tension, cela pourrait endommager votre caméra.

.. **Enable the Camera Interface**

.. Run the following command to enable the camera interface of your Raspberry Pi. If you have enabled it, skip this; if you do not know whether you have done that or not, please continue.

.. .. raw:: html

..    <run></run>

.. .. code-block::

..    sudo raspi-config

.. **3 Interfacing options**

.. .. image:: img/image282.png
..    :align: center

.. **P1 Camera**

.. .. image:: img/camera_config1.png
..    :align: center

.. **<Yes>, then <Ok> -> <Finish>**

.. .. image:: img/camera_config2.png
..    :align: center

.. After the configuration is complete, it is recommended to reboot the Raspberry Pi.

.. .. raw:: html

..    <run></run>

.. .. code-block::

..    sudo reboot