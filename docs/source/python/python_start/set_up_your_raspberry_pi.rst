.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

4. Configuration de votre Raspberry Pi
===========================================

Configuration avec un écran
-----------------------------

Utiliser un écran simplifie le processus de configuration et de travail avec votre Raspberry Pi.

**Composants nécessaires**

* Raspberry Pi 5
* Adaptateur d'alimentation
* Carte Micro SD
* Adaptateur d'alimentation de l'écran
* Câble HDMI
* Écran
* Souris
* Clavier

**Étapes** :

#. Connectez la souris et le clavier au Raspberry Pi.

#. Utilisez le câble HDMI pour relier l’écran au port HDMI du Raspberry Pi. Assurez-vous que l’écran est branché à une source d’alimentation et allumé.

#. Alimentez le Raspberry Pi avec l’adaptateur d’alimentation.

#. Après quelques secondes, le bureau de Raspberry Pi OS s'affichera. Vous pouvez maintenant ouvrir le Terminal pour commencer à entrer des commandes.

    .. image:: img/bookwarm.png
        :align: center

Configuration sans écran
---------------------------

Si vous n'avez pas de moniteur, la connexion à distance est une option viable.

**Composants nécessaires**

* Raspberry Pi 5
* Adaptateur d'alimentation
* Carte Micro SD

En utilisant SSH, vous pouvez accéder au shell Bash de votre Raspberry Pi, qui est le shell par défaut de Linux. Bash propose une interface en ligne de commande pour effectuer diverses tâches.

Pour ceux qui préfèrent une interface graphique (GUI), la fonctionnalité de bureau à distance est une alternative pratique pour gérer les fichiers et les opérations.

Pour des tutoriels de configuration détaillés selon votre système d'exploitation, référez-vous aux sections suivantes :

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop

