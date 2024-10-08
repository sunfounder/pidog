.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_os_sd:

2. Installation du Système d'Exploitation
============================================================


**Composants Nécessaires**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur de carte

1. Installer Raspberry Pi Imager
----------------------------------

#. Rendez-vous sur la page de téléchargement du logiciel Raspberry Pi à l'adresse `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Choisissez la version de l'Imager compatible avec votre système d'exploitation. Téléchargez le fichier et ouvrez-le pour démarrer l'installation.

    .. image:: img/os_install_imager.png
        :align: center

#. Une alerte de sécurité peut apparaître pendant l'installation, selon votre système d'exploitation. Par exemple, Windows pourrait afficher un message d'avertissement. Dans ce cas, sélectionnez **Plus d'infos**, puis **Exécuter quand même**. Suivez les instructions à l'écran pour terminer l'installation de Raspberry Pi Imager.

    .. image:: img/os_info.png
        :align: center

#. Lancez l'application Raspberry Pi Imager en cliquant sur son icône ou en tapant ``rpi-imager`` dans votre terminal.

    .. image:: img/os_open_imager.png
        :align: center

2. Installation du Système d'Exploitation sur la carte Micro SD
----------------------------------------------------------------------

#. Insérez votre carte SD dans votre ordinateur ou votre portable à l'aide d'un lecteur de carte.

#. Dans l'Imager, cliquez sur **Raspberry Pi Device** et sélectionnez le modèle de Raspberry Pi dans la liste déroulante.

    .. image:: img/os_choose_device.png
        :align: center

#. Sélectionnez **Système d'Exploitation** et optez pour la version recommandée.

    .. image:: img/os_choose_os.png
        :align: center

#. Cliquez sur **Choisir le stockage** et sélectionnez le périphérique de stockage approprié pour l'installation.

    .. note::

        Assurez-vous de sélectionner le bon périphérique de stockage. Pour éviter toute confusion, déconnectez les périphériques de stockage supplémentaires si plusieurs sont connectés.

    .. image:: img/os_choose_sd.png
        :align: center

#. Cliquez sur **Suivant** puis sur **Modifier les paramètres** pour personnaliser votre système d'exploitation.

    .. note::

        Si vous disposez d'un écran pour votre Raspberry Pi, vous pouvez ignorer les étapes suivantes et cliquer sur 'Oui' pour commencer l'installation. Vous pourrez ajuster les autres paramètres plus tard sur l'écran.

    .. image:: img/os_enter_setting.png
        :align: center

#. Définissez un **nom d'hôte** pour votre Raspberry Pi.

    .. note::

        Le nom d'hôte est l'identifiant réseau de votre Raspberry Pi. Vous pourrez accéder à votre Pi en utilisant ``<hostname>.local`` ou ``<hostname>.lan``.

    .. image:: img/os_set_hostname.png
        :align: center

#. Créez un **Nom d'utilisateur** et un **Mot de passe** pour le compte administrateur du Raspberry Pi.

    .. note::

        La création d'un nom d'utilisateur et d'un mot de passe uniques est essentielle pour sécuriser votre Raspberry Pi, qui n'a pas de mot de passe par défaut.

    .. image:: img/os_set_username.png
        :align: center

#. Configurez le réseau sans fil (LAN) en renseignant le **SSID** et le **Mot de passe** de votre réseau.

    .. note::

        Réglez le ``Pays du réseau sans fil`` selon le code `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ correspondant à votre pays.

    .. image:: img/os_set_wifi.png
        :align: center

#. Pour vous connecter à distance à votre Raspberry Pi, activez SSH dans l'onglet Services.

    * Pour une **authentification par mot de passe**, utilisez le nom d'utilisateur et le mot de passe définis dans l'onglet Général.
    * Pour une authentification par clé publique, choisissez "Autoriser uniquement l'authentification par clé publique". Si vous possédez une clé RSA, elle sera utilisée. Sinon, cliquez sur "Exécuter SSH-keygen" pour générer une nouvelle paire de clés.

    .. image:: img/os_enable_ssh.png
        :align: center

#. Le menu **Options** vous permet de configurer le comportement de l'Imager lors de l'écriture, comme la lecture d'un son à la fin, l'éjection automatique du média à la fin, et l'activation de la télémétrie.

    .. image:: img/os_options.png
        :align: center

#. Lorsque vous avez terminé de personnaliser les paramètres, cliquez sur **Enregistrer** pour sauvegarder vos modifications. Ensuite, cliquez sur **Oui** pour les appliquer lors de l'écriture de l'image.

    .. image:: img/os_click_yes.png
        :align: center

#. Si la carte SD contient déjà des données, assurez-vous de les sauvegarder pour éviter toute perte. Cliquez sur **Oui** si aucune sauvegarde n'est nécessaire.

    .. image:: img/os_continue.png
        :align: center

#. Lorsque le message "Écriture réussie" s'affiche, votre image a été complètement écrite et vérifiée. Vous êtes maintenant prêt à démarrer votre Raspberry Pi à partir de la carte Micro SD !

    .. image:: img/os_finish.png
        :align: center

#. Vous pouvez maintenant insérer la carte SD configurée avec Raspberry Pi OS dans le logement microSD situé sous le Raspberry Pi.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center
