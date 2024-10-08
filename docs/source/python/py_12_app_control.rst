.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, d'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

12. Jouer avec PiDog à l'aide de l'APP
==========================================

Dans cet exemple, nous allons utiliser l'application SunFounder Controller pour contrôler PiDog.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/app_control.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

Vous devez d'abord télécharger l'application sur votre téléphone ou tablette, puis vous connecter au hotspot émis par PiDog et, enfin, créer votre propre télécommande sur SunFounder Controller pour contrôler PiDog.

Contrôler PiDog avec l'APP
-----------------------------

#. Installez `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ depuis **APP Store (iOS)** ou **Google Play (Android)**.

#. Installez le module ``sunfounder-controller``.

    Les modules ``robot-hat``, ``vilib`` et ``picar-x`` doivent être installés au préalable. Pour plus de détails, voir :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Exécutez le code.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 12_app_control.py

    Après l'exécution du code, vous verrez l'invite suivante, indiquant que PiDog a bien démarré la communication réseau.

    .. code-block:: 

        Running on: http://192.168.18.138:9000/mjpg

        * Serving Flask app "vilib.vilib" (lazy loading)
        * Environment: development
        * Debug mode: off
        * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)       

#. Connectez ``PiDog`` et ``Sunfounder Controller``.

    * Connectez votre tablette ou téléphone au réseau WLAN de PiDog.

    * Ouvrez l'application ``Sunfounder Controller``. Cliquez sur l'icône + pour ajouter une télécommande.

        .. image:: img/app1.png
       
    * Des télécommandes prédéfinies sont disponibles pour certains produits. Ici, nous choisissons **PiDog**. Donnez-lui un nom ou appuyez simplement sur **Confirmer**.

        .. image:: img/app_preset.jpg

    * Une fois à l'intérieur, l'application recherchera automatiquement **Mydog**. Après quelques instants, vous verrez un message indiquant "Connecté avec succès".

        .. image:: img/app_auto_connect.jpg

    .. note::

        * Vous pouvez également cliquer manuellement sur le bouton |app_connect|. Attendez quelques secondes, MyDog(IP) apparaîtra. Cliquez dessus pour vous connecter.

            .. image:: img/sc_mydog.jpg

#. Lancer le contrôleur.

    * Lorsque le message "Connecté avec succès" apparaît, appuyez sur le bouton ▶ dans le coin supérieur droit.

    * L'image capturée par la caméra s'affichera dans l'application, et vous pourrez désormais contrôler PiDog avec ces widgets.

        .. image:: img/sc_run.jpg

Voici les fonctions des widgets :

* A : Détection de distance des obstacles, c'est-à-dire la lecture du module à ultrasons.
* C : Activer/désactiver la détection faciale.
* D : Contrôle de l'inclinaison de la tête de PiDog.
* E : Assis.
* F : Debout.
* G : Allongé.
* I : Gratter la tête de PiDog.
* N : Aboyer.
* O : Remuer la queue.
* P : Haleter.
* K : Contrôler les mouvements de PiDog (avant, arrière, gauche et droite).
* Q : Contrôler l'orientation de la tête de PiDog.
* J : Passer en mode commande vocale. Les commandes vocales prises en charge sont :

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

Démarrage automatique au démarrage
----------------------------------------

Lors du contrôle de PiDog via l'application, il n'est pas pratique de se connecter au Raspberry Pi et d'exécuter manuellement ``12_app_control.py`` à chaque fois avant de se connecter à l'APP.

Il existe une solution plus simple : vous pouvez configurer PiDog pour qu'il exécute automatiquement ``12_app_control.py`` à chaque démarrage. Ainsi, vous pourrez vous connecter directement à PiDog depuis l'APP et le contrôler sans effort.

Comment configurer cela ?

#. Exécutez les commandes suivantes pour installer et configurer l'application ``pidog_app`` et configurer le WiFi pour PiDog.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/bin
        sudo bash pidog_app_install.sh

#. À la fin, entrez ``y`` pour redémarrer PiDog.

    .. image:: img/auto_start.png

#. Par la suite, vous pourrez simplement allumer PiDog et le contrôler directement depuis l'APP.

.. warning::

    Si vous souhaitez exécuter d'autres scripts, exécutez d'abord la commande ``pidog_app disable`` pour désactiver la fonctionnalité de démarrage automatique.


Configuration de l'application
----------------------------------

Vous pouvez entrer les commandes suivantes pour modifier les paramètres de l'APP.

.. code-block::

    pidog_app <OPTION> [input]

**OPTION**
    * ``-h`` ``help`` : aide, afficher ce message
    * ``start`` ``restart`` : redémarrer le service ``pidog_app``
    * ``stop`` : arrêter le service ``pidog_app``
    * ``disable`` : désactiver le démarrage automatique du programme ``app_controller`` au démarrage
    * ``enable`` : activer le démarrage automatique du programme ``app_controller`` au démarrage
    * ``close_ap`` : fermer le hotspot, désactiver le démarrage automatique du hotspot au démarrage et passer en mode ``sta``
    * ``open_ap`` : ouvrir le hotspot, activer le démarrage automatique du hotspot au démarrage
    * ``ssid`` : définir le nom du réseau (SSID) du hotspot
    * ``psk`` : définir le mot de passe du hotspot
    * ``country`` : définir le code de pays pour le hotspot
