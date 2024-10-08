.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _filezilla:

Logiciel Filezilla
==========================

.. image:: img/filezilla_icon.png

Le protocole de transfert de fichiers (FTP) est un protocole de communication standard utilisé pour le transfert de fichiers informatiques d’un serveur vers un client sur un réseau informatique.

Filezilla est un logiciel open source qui prend en charge non seulement le FTP, mais aussi le FTP via TLS (FTPS) et le SFTP. Nous pouvons utiliser Filezilla pour télécharger des fichiers locaux (tels que des images et de l’audio, etc.) vers le Raspberry Pi, ou bien télécharger des fichiers du Raspberry Pi vers un emplacement local.

**Étape 1** : Téléchargez Filezilla.

Téléchargez le client depuis le `Filezilla's official website <https://filezilla-project.org/>`_. Filezilla dispose d’un excellent tutoriel, veuillez consulter : `Documentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.

**Étape 2** : Connectez-vous au Raspberry Pi.

Après une installation rapide, ouvrez le logiciel et `connect it to an FTP server <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Il y a trois manières de se connecter, ici nous utilisons la barre **Connexion rapide**. Entrez le **nom d'hôte/IP**, **nom d’utilisateur**, **mot de passe** et **port (22)**, puis cliquez sur **Connexion rapide** ou appuyez sur **Entrée** pour vous connecter au serveur.

.. image:: img/filezilla_connect.png

.. note::

    La Connexion rapide est un bon moyen de tester vos informations de connexion. Si vous souhaitez créer une entrée permanente, vous pouvez sélectionner **Fichier** -> **Copier la connexion actuelle vers le gestionnaire de sites** après une Connexion rapide réussie, entrez le nom et cliquez sur **OK**. La prochaine fois, vous pourrez vous connecter en sélectionnant le site précédemment enregistré dans **Fichier** -> **Gestionnaire de sites**.
    
    .. image:: img/ftp_site.png

**Étape 3** : Téléversez/téléchargez des fichiers.

Vous pouvez téléverser des fichiers locaux vers le Raspberry Pi en les faisant glisser et en les déposant, ou télécharger les fichiers présents dans le Raspberry Pi vers un emplacement local.

.. image:: img/upload_ftp.png
