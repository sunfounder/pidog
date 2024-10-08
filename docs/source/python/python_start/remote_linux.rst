.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Pour les utilisateurs Linux/Unix
=========================================

#. Localisez et ouvrez le **Terminal** sur votre système Linux/Unix.

#. Assurez-vous que votre Raspberry Pi est connecté au même réseau. Vérifiez cela en tapant `ping <hostname>.local`. Par exemple :

    .. code-block::

        ping raspberrypi.local

    Vous devriez voir l'adresse IP de votre Raspberry Pi s'afficher s'il est bien connecté au réseau.

    * Si le terminal affiche un message tel que ``La requête Ping n'a pas pu trouver l'hôte pi.local. Veuillez vérifier le nom et réessayer.``, vérifiez à nouveau le nom d'hôte que vous avez saisi.
    * Si vous ne parvenez toujours pas à récupérer l'adresse IP, vérifiez les paramètres réseau ou Wi-Fi de votre Raspberry Pi.

#. Établissez une connexion SSH en tapant ``ssh <nom_utilisateur>@<hostname>.local`` ou ``ssh <nom_utilisateur>@<adresse_IP>``. Par exemple :

    .. code-block::

        ssh pi@raspberrypi.local

#. Lors de votre première connexion, vous verrez un message de sécurité. Tapez ``yes`` pour continuer.

    .. code-block::

        L'authenticité de l'hôte 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' ne peut pas être établie.
        L'empreinte de la clé ED25519 est SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Êtes-vous sûr de vouloir continuer la connexion (yes/no/[fingerprint])?

#. Entrez le mot de passe que vous avez défini précédemment. Notez que, pour des raisons de sécurité, le mot de passe ne sera pas visible pendant la saisie.

    .. note::
        Il est normal que les caractères du mot de passe ne s'affichent pas dans le terminal. Assurez-vous simplement d'entrer le mot de passe correct.

#. Une fois connecté avec succès, votre Raspberry Pi est maintenant opérationnel et prêt pour la prochaine étape.
