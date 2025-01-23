.. note::

    Bonjour et bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes post-achat et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions et cadeaux festifs** : Participez à des tirages au sort et à des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

FAQ
===========================

Q1 : À propos de l'erreur "pinctrl: not found"
-------------------------------------------------------------------

Si vous rencontrez l'erreur suivante :

.. code-block::

    pinctrl: not found

Cela indique que vous avez installé le système Bullseye. Il est recommandé d'installer plutôt le système **Bookworm**.

Q2 : À propos du chargeur de batterie
-------------------------------------------------------------------

Pour charger la batterie, il suffit de connecter une alimentation Type-C de 5V/2A au port d'alimentation du Robot Hat. Il n'est pas nécessaire d'allumer l'interrupteur d'alimentation du Robot Hat pendant le chargement.
Vous pouvez également utiliser l'appareil pendant la charge de la batterie.

.. image:: img/robot_hat_pic.png
    :align: center
    :width: 500

Pendant la charge, la puissance d'entrée est amplifiée par la puce de charge pour recharger la batterie tout en alimentant simultanément le convertisseur DC-DC pour un usage externe. La puissance de charge est d'environ 10 W.
Si la consommation électrique externe reste élevée sur une longue période, la batterie peut compléter l'alimentation, de manière similaire à l'utilisation d'un téléphone en charge. Cependant, veillez à ne pas épuiser complètement la capacité de la batterie lors d'une utilisation et d'une charge simultanées.
