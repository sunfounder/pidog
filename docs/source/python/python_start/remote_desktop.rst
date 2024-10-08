.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _remote_desktop:

Accès à distance pour le Raspberry Pi
==================================================

Pour ceux qui préfèrent utiliser une interface graphique (GUI) plutôt que d'accéder via la ligne de commande, le Raspberry Pi prend en charge l'accès à distance via le bureau. Ce guide vous expliquera comment configurer et utiliser VNC (Virtual Network Computing) pour l'accès à distance.

Nous vous recommandons d'utiliser `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ pour cette tâche.

**Activer le service VNC sur le Raspberry Pi**

Le service VNC est préinstallé dans Raspberry Pi OS, mais il est désactivé par défaut. Suivez ces étapes pour l'activer :

#. Entrez la commande suivante dans le terminal du Raspberry Pi :

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Accédez à **Interfacing Options** à l'aide de la touche flèche bas, puis appuyez sur **Entrée**.

    .. image:: img/config_interface.png
        :align: center

#. Sélectionnez **VNC** parmi les options.

    .. image:: img/vnc.png
        :align: center

#. Utilisez les touches fléchées pour choisir **<Yes>** -> **<OK>** -> **<Finish>** et finalisez l'activation du service VNC.

    .. image:: img/vnc_yes.png
        :align: center

**Connexion via VNC Viewer**

#. Téléchargez et installez `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sur votre ordinateur personnel.

#. Une fois installé, lancez VNC Viewer. Entrez le nom d'hôte ou l'adresse IP de votre Raspberry Pi et appuyez sur Entrée.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Lorsque vous y êtes invité, entrez le nom d'utilisateur et le mot de passe de votre Raspberry Pi, puis cliquez sur **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Après quelques secondes, le bureau de Raspberry Pi OS s'affichera. Vous pouvez maintenant ouvrir le Terminal pour commencer à entrer des commandes.

    .. image:: img/bookwarm.png
        :align: center
