.. note::

   Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

   **Pourquoi rejoindre ?**

   - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
   - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
   - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
   - **Remises spéciales** : Profitez de remises exclusives sur nos tout nouveaux produits.
   - **Promotions festives et cadeaux** : Participez à des concours et à des promotions de vacances.

   👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

12. Jouer avec PiDog via l'APP
=================================

Dans cette leçon, vous apprendrez à utiliser l'application **SunFounder Controller** pour contrôler votre PiDog. Cette approche rend le contrôle de votre chien robotique plus intuitif et interactif.

.. raw:: html

   <video width="600" loop autoplay muted>
     <source src="../_static/video/app_control.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>


Vous devez d'abord télécharger l'APP sur votre téléphone/tablette, puis vous connecter au WLAN de PiDog, et enfin créer votre propre télécommande sur SunFounder Controller pour contrôler PiDog.

.. _app_control:

Contrôler PiDog avec l'App
----------------------------



Pour contrôler PiDog via l'application SunFounder Controller, suivez ces étapes :

#. Installez `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ depuis l'**APP Store (iOS)** ou **Google Play (Android)**.

#. Installez les modules requis.

   * Les modules ``robot-hat``, ``vilib`` et ``pidog`` doivent d'abord être installés, pour plus de détails voir la section :ref:`install_all_modules`.

     *  ``robot-hat``
     *  ``vilib``
     *  ``pidog``

   * Ensuite, installez le module ``sunfounder-controller`` :

     .. raw:: html

         <run></run>

     .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Exécutez les commandes suivantes pour lancer le script de contrôle :

   .. raw:: html

        <run></run>

   .. code-block::

        cd ~/pidog/examples
        sudo python3 12_app_control.py

   Une fois le script exécuté avec succès, vous verrez une invite comme celle-ci :

   .. code-block::

        Running on: http://192.168.18.138:9000/mjpg

        * Serving Flask app "vilib.vilib" (lazy loading)
        * Environment: development
        * Debug mode: off
        * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

   Cela indique que votre PiDog est prêt pour la communication réseau.

#. Connectez PiDog et Sunfounder Controller.

   * Connectez votre téléphone/tablette au même WLAN que PiDog.

   * Ouvrez l'APP **Sunfounder Controller**. Cliquez sur l'icône + pour ajouter un contrôleur.

     .. image:: img/app1.png


   * Des contrôleurs prédéfinis sont disponibles pour certains produits, ici nous choisissons **PiDog**. Donnez-lui un nom, ou appuyez simplement sur **Confirmer**.

     .. image:: img/app_preset.jpg


   * Une fois à l'intérieur, l'application recherchera automatiquement le **Mydog**. Après un moment, vous verrez une notification indiquant « Connecté avec succès ».

     .. image:: img/app_auto_connect.jpg

     .. note::

        * Vous pouvez également cliquer manuellement sur le bouton |app_connect|. Attendez quelques secondes, MyDog (IP) apparaîtra, cliquez dessus pour vous connecter.

        .. image:: img/sc_mydog.jpg

#. Exécutez le Contrôleur.

   * Lorsque la notification « Connecté avec succès » apparaît, appuyez sur le bouton ▶ dans le coin supérieur droit.

   * L'image prise par la caméra apparaîtra sur l'APP, et vous pouvez maintenant contrôler votre PiDog avec ces widgets.

   .. image:: img/sc_run.jpg


Here are the functions of the widgets.

* A: Detect the obstacle distance, that is, the reading of the ultrasonic module.
* C: Turn on/off face detection.
* D: Control PiDog's head tilt angle (tilt head).
* E: Sit.
* F: Stand.
* G: Lie.
* I: Scratch PiDog's head.
* N: Bark.
* O: Wag tail.
* P: Pant.
* K: Control PiDog's movement (forward, backward, left and right).
* Q: Controls the orientation of PiDog's head.
* J: Switch to voice control mode. It supports the following voice commands:

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

Démarrage automatique de PiDog au boot
-----------------------------------------

Pour éviter d'exécuter manuellement le script 12_app_control.py à chaque fois, vous pouvez configurer PiDog pour lancer le script automatiquement au démarrage :

Comment configurer cela ?

#. Exécutez les commandes suivantes pour installer et configurer l'application ``pidog_app`` :

   .. raw:: html

        <run></run>

   .. code-block::

        cd ~/pidog/bin
        sudo bash pidog_app_install.sh

#. Lorsque vous y êtes invité, saisissez ``y`` pour redémarrer PiDog.

   .. image:: img/auto_start.png

#. Après le redémarrage, PiDog lancera automatiquement le script de contrôle. Vous pouvez alors :ref:`app_control`.

.. warning::

   Si vous souhaitez exécuter d'autres scripts, exécutez d'abord ``pidog_app disable`` pour désactiver le démarrage automatique.


.. Configuration du programme APP
.. -----------------------------

.. Vous pouvez saisir les commandes suivantes pour modifier les paramètres du mode APP.

.. .. code-block::

..    pidog_app <OPTION> [input]

.. **OPTION**
..    * ``-h`` ``help``: aide, affiche ce message
..    * ``start`` ``restart``: redémarre le service ``pidog_app``
..    * ``stop``: arrête le service ``pidog_app``
..    * ``disable``: désactive le démarrage automatique du programme ``app_controller`` au démarrage
..    * ``enable``: active le démarrage automatique du programme ``app_controller`` au démarrage
..    * ``close_ap``: ferme le point d'accès, désactive le démarrage automatique du point d'accès et passe en mode station
..    * ``open_ap``: ouvre le point d'accès, active le démarrage automatique du point d'accès au démarrage
..    * ``ssid``: définit le SSID (nom du réseau) du point d'accès
..    * ``psk``: définit le mot de passe du point d'accès
..    * ``country``: définit le code pays du point d'accès
