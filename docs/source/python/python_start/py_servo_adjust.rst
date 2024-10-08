.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_servo_adjust:

7. Réglage des Servomoteurs (Important)
===========================================

La plage d'angle du servomoteur est de -90 à 90°, mais l'angle défini en usine est aléatoire : il peut être de 0°, de 45° ou autre. Si nous l’assemblons avec cet angle par défaut, cela peut entraîner un comportement chaotique lorsque le robot exécute le code, voire pire, bloquer le servomoteur et provoquer sa surchauffe.

Nous devons donc régler tous les angles des servomoteurs à 0° avant de les installer, afin que l’angle de chaque servo soit au centre, quelle que soit la direction de rotation.

#. Pour vous assurer que le servomoteur est bien réglé à 0°, insérez d'abord le bras du servomoteur dans l'arbre du servo, puis tournez doucement le bras du servomoteur à différents angles. Ce bras n’est là que pour vous permettre de visualiser clairement la rotation du servo.

    .. image:: img/servo_arm.png
        :align: center

#. Lancez maintenant ``servo_zeroing.py`` dans le dossier ``examples/``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 servo_zeroing.py

    .. note::
        Si une erreur se produit, essayez de réactiver le port I2C du Raspberry Pi, consultez : :ref:`i2c_spi_config`.

#. Ensuite, branchez le câble du servomoteur sur le port P11 comme suit. Vous verrez le bras du servomoteur se déplacer vers une position (il s'agit de la position 0°, qui est aléatoire et peut ne pas être verticale ou parallèle).

    .. image:: img/servo_pin11.jpg

#. Retirez maintenant le bras du servomoteur tout en veillant à ce que le câble reste connecté, et ne coupez pas l'alimentation. Continuez ensuite l'assemblage en suivant les instructions du manuel.

.. note::

    * Ne débranchez pas ce câble de servomoteur avant de l'avoir fixé avec la vis de servo ; vous pourrez le débrancher après l'avoir fixé.
    * Ne faites pas tourner le servomoteur lorsqu'il est sous tension pour éviter tout dommage ; si l'axe du servomoteur n'est pas inséré dans le bon angle, retirez le servo et réinsérez-le.
    * Avant d'assembler chaque servomoteur, branchez le câble du servomoteur sur la broche PWM et allumez l'alimentation pour régler son angle à 0°.
