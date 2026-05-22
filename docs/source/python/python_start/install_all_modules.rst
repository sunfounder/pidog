.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support expert** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez et partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-goûts.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos tout nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions de vacances.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_all_modules:

Installer tous les modules (Important)
==============================================

.. note::

    Les packages liés à Python3 doivent être installés si vous installez la version Lite du système d'exploitation.

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt install git python3-pip python3-setuptools python3-smbus


#. Installez le module ``robot-hat``.


   .. raw:: html

       <run></run>

   .. code-block::

       cd ~/
       git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
       cd robot-hat
       sudo python3 install.py

#. Installez le module ``vilib``.

   .. raw:: html

       <run></run>

   .. code-block::

       cd ~/
       git clone https://github.com/sunfounder/vilib.git
       cd vilib
       sudo python3 install.py

#. Installez le module ``pidog``.

   .. raw:: html

       <run></run>

   .. code-block::

       cd ~/
       git clone https://github.com/sunfounder/pidog.git --depth 1
       cd pidog
       sudo pip3 install . --break

   Cette étape prendra un peu de temps, veuillez donc être patient.

#. Exécutez le script ``i2samp.sh``.

   Enfin, vous devez exécuter le script ``i2samp.sh`` pour installer les composants requis par l'amplificateur I2S, sinon le robot n'aura pas de son.

   .. raw:: html

       <run></run>

   .. code-block::

       cd ~/robot-hat
       sudo bash i2samp.sh

   Tapez y et appuyez trois fois sur Entrée pour continuer le script, démarrez /dev/zero en arrière-plan, puis redémarrez la machine.

   .. note::
       Si le son ne fonctionne pas après le redémarrage, vous devrez peut-être exécuter le script ``i2samp.sh`` plusieurs fois.
