.. note::

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour enrichir vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et concours festifs** : Participez à des concours et à des promotions spéciales lors des périodes de fête.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

3. Utilisation rapide de l'application
======================================

Maintenant que votre PiDog est prêt à l'emploi, cette section est idéale pour ceux qui souhaitent explorer rapidement toutes ses fonctionnalités. Nous vous guiderons pas à pas dans l'installation de l'application, la connexion de votre PiDog à votre appareil mobile et l'activation de ses nombreuses fonctionnalités amusantes. À la fin de ce chapitre, vous serez à l'aise pour naviguer et jouer avec votre PiDog à partir de votre appareil. Commençons et plongeons dans le monde passionnant de la robotique interactive !

#. Installez le module ``sunfounder-controller``.

    Les modules robot-hat, vilib et picar-x doivent d'abord être installés. Pour plus de détails, consultez : :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Exécutez les commandes suivantes :

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/bin
        sudo bash pidog_app_install.sh

#. Redémarrez PiDog.

#. Installez `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ depuis **App Store (iOS)** ou **Google Play (Android)**.

#. Connectez-vous au réseau WLAN ``pidog``.

    Connectez votre appareil mobile au réseau local (LAN) diffusé par le PiDog. De cette manière, votre appareil mobile et le PiDog seront sur le même réseau, facilitant la communication entre les applications de votre appareil et le PiDog.

    * Trouvez ``pidog`` dans la liste WLAN de votre téléphone (ou tablette), entrez le mot de passe ``12345678`` et connectez-vous.

    * Le mode de connexion par défaut est le mode AP. Une fois connecté, un message indiquera qu'il n'y a pas d'accès à Internet sur ce réseau, choisissez de continuer la connexion.

        .. image:: img/app_no_internet.png

#. Ouvrez l'application ``Sunfounder Controller``. Cliquez sur l'icône + pour ajouter une télécommande.

        .. image:: img/app1.png

#. Des contrôleurs prédéfinis sont disponibles pour certains produits, ici nous choisissons **PiDog**. Donnez-lui un nom ou appuyez simplement sur **Confirmer**.

        .. image:: img/app_preset.jpg

#. Une fois à l'intérieur, l'application recherchera automatiquement le **Mydog**. Après quelques instants, un message indiquant « Connexion réussie » apparaîtra.

        .. image:: img/app_auto_connect.jpg

    .. note::

        * Vous pouvez également cliquer manuellement sur le bouton |app_connect|. Attendez quelques secondes, MyDog(IP) apparaîtra, cliquez dessus pour vous connecter.

            .. image:: img/sc_mydog.jpg

#. Lancer le contrôleur.

    * Lorsque le message « Connexion réussie » s'affiche, appuyez sur le bouton ▶ dans le coin supérieur droit.

    * Le flux vidéo de la caméra apparaîtra sur l'application, et vous pourrez désormais contrôler votre PiDog à l'aide des widgets.

        .. image:: img/sc_run.jpg

Voici les fonctionnalités des widgets :

* A : Mesure de la distance des obstacles via le module ultrasonique.
* C : Activer/désactiver la détection faciale.
* D : Contrôler l'inclinaison de la tête du PiDog.
* E : Faire asseoir le PiDog.
* F : Faire se lever le PiDog.
* G : Faire se coucher le PiDog.
* I : Gratter la tête du PiDog.
* N : Faire aboyer le PiDog.
* O : Faire remuer la queue.
* P : Faire haleter.
* K : Contrôler le mouvement du PiDog (avant, arrière, gauche, droite).
* Q : Contrôler l'orientation de la tête du PiDog.
* J : Passer en mode de commande vocale. Voici les commandes vocales disponibles :

    * ``forward``
    * ``backward``
    * ``turn left``
    * ``turn right``
    * ``trot``
    * ``stop``
    * ``lie down``
    * ``stand up``
    * ``sit``
    * ``bark``
    * ``bark harder``
    * ``pant``
    * ``wag tail``
    * ``shake head``
    * ``stretch``
    * ``doze off``
    * ``push-up``
    * ``howling``
    * ``twist body``
    * ``scratch``
    * ``handshake``
    * ``high five``

Configuration de l'application
---------------------------------

Vous pouvez utiliser les commandes suivantes pour modifier les paramètres de l'application.

.. code-block::

    pidog_app <OPTION> [entrée]

**OPTION**
    * ``-h`` ``help`` : afficher ce message d'aide.
    * ``start`` ``restart`` : redémarrer le service pidog_app.
    * ``stop`` : arrêter le service pidog_app.
    * ``disable`` : désactiver le démarrage automatique de l'application au lancement.
    * ``enable`` : activer le démarrage automatique de l'application au lancement.
    * ``close_ap`` : fermer le point d'accès, désactiver le démarrage automatique du point d'accès au démarrage et passer en mode STA.
    * ``open_ap`` : ouvrir le point d'accès, activer le démarrage automatique du point d'accès au démarrage.
    * ``ssid`` : définir le nom du réseau du point d'accès.
    * ``psk`` : définir le mot de passe du point d'accès.
    * ``country`` : définir le code de pays du point d'accès.
