.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _i2c_spi_config:

6. Vérifier l'interface I2C et SPI
========================================

Nous allons utiliser les interfaces I2C et SPI du Raspberry Pi. Ces interfaces devraient avoir été activées lors de l'installation du module ``robot-hat`` précédemment. Pour vérifier que tout est en ordre, voyons si elles sont bien activées.

#. Saisissez la commande suivante :

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Choisissez **Interfacing Options** en appuyant sur la touche flèche bas de votre clavier, puis appuyez sur la touche **Entrée**.

    .. image:: img/image282.png
        :align: center

#. Sélectionnez ensuite **I2C**.

    .. image:: img/image283.png
        :align: center

#. Utilisez les flèches du clavier pour sélectionner **<Yes>** -> **<OK>** afin de terminer la configuration de l'I2C.

    .. image:: img/image284.png
        :align: center

#. Retournez dans **Interfacing Options** et sélectionnez **SPI**.

    .. image:: img/image-spi1.png
        :align: center

#. Utilisez les flèches du clavier pour sélectionner **<Yes>** -> **<OK>** afin de terminer la configuration du SPI.

    .. image:: img/image-spi2.png
        :align: center
