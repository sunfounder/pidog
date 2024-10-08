.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Pour les utilisateurs de Windows
=======================================

Pour les utilisateurs de Windows 10 ou versions supérieures, la connexion à distance à un Raspberry Pi peut être effectuée via les étapes suivantes :

#. Recherchez ``powershell`` dans la barre de recherche Windows. Faites un clic droit sur ``Windows PowerShell`` et sélectionnez ``Exécuter en tant qu'administrateur``.

    .. image:: img/powershell_ssh.png
        :align: center

#. Déterminez l'adresse IP de votre Raspberry Pi en tapant ``ping -4 <hostname>.local`` dans PowerShell.

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    L'adresse IP de votre Raspberry Pi s'affichera une fois qu'il sera connecté au réseau.

    * Si le terminal affiche ``La requête Ping n'a pas pu trouver l'hôte pi.local. Veuillez vérifier le nom et réessayer.``, assurez-vous que le nom d'hôte que vous avez saisi est correct.
    * Si l'adresse IP n'est toujours pas récupérable, vérifiez les paramètres réseau ou Wi-Fi de votre Raspberry Pi.

#. Une fois l'adresse IP confirmée, connectez-vous à votre Raspberry Pi en utilisant ``ssh <nom_utilisateur>@<hostname>.local`` ou ``ssh <nom_utilisateur>@<adresse_IP>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Si une erreur apparaît indiquant ``Le terme 'ssh' n'est pas reconnu comme le nom d'une cmdlet...``, cela signifie que votre système ne dispose pas des outils SSH préinstallés. Dans ce cas, vous devez installer manuellement OpenSSH en suivant :ref:`openssh_powershell`, ou utiliser un outil tiers comme décrit dans :ref:`login_windows`.

#. Un message de sécurité apparaîtra lors de votre première connexion. Entrez ``yes`` pour continuer.

    .. code-block::

        L'authenticité de l'hôte 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' ne peut pas être établie.
        L'empreinte de la clé ED25519 est SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Êtes-vous sûr de vouloir continuer la connexion (yes/no/[fingerprint])?

#. Entrez le mot de passe que vous avez défini précédemment. Notez que les caractères du mot de passe ne s'afficheront pas à l'écran, ce qui est une fonctionnalité de sécurité standard.

    .. note::
        L'absence de caractères visibles lors de la saisie du mot de passe est normale. Assurez-vous d'entrer le mot de passe correct.

#. Une fois connecté, votre Raspberry Pi est prêt pour les opérations à distance.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center
