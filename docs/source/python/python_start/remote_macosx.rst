.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Pour les utilisateurs de Mac OS X
======================================

Pour les utilisateurs de Mac OS X, SSH (Secure Shell) offre un moyen sécurisé et pratique pour accéder à distance au Raspberry Pi et le contrôler. C'est particulièrement utile lorsque vous travaillez sur le Raspberry Pi à distance ou lorsqu'il n'est pas connecté à un écran. En utilisant l'application Terminal sur un Mac, vous pouvez établir cette connexion sécurisée. Le processus consiste à utiliser une commande SSH incluant le nom d'utilisateur et le nom d'hôte du Raspberry Pi. Lors de la première connexion, une invite de sécurité demandera de confirmer l'authenticité du Raspberry Pi.

#. Pour vous connecter au Raspberry Pi, saisissez la commande SSH suivante :

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac-ping.png

#. Un message de sécurité apparaîtra lors de votre première connexion. Répondez par **yes** pour continuer.

    .. code-block::

        L'authenticité de l'hôte 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' ne peut pas être établie.
        L'empreinte de la clé ED25519 est SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Êtes-vous sûr de vouloir continuer la connexion (yes/no/[empreinte]) ?

#. Entrez le mot de passe de votre Raspberry Pi. Notez que le mot de passe ne s'affichera pas à l'écran lors de la saisie, ce qui est une fonctionnalité de sécurité standard.

    .. code-block::

        Mot de passe pour pi@raspberrypi.local : 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Ven 26 Août 11:16:44 BST 2022 aarch64

        Les programmes inclus dans le système Debian GNU/Linux sont des logiciels libres ;
        les conditions de distribution exactes pour chaque programme sont décrites dans les fichiers
        individuels situés dans /usr/share/doc/*/copyright.

        Debian GNU/Linux est fourni SANS AUCUNE GARANTIE, dans les limites
        autorisées par la loi applicable.
        Dernière connexion : jeu. 22 sept. 2022, 12:18:22
        pi@raspberrypi:~ $ 

