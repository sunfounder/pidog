.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_all_modules:

5. Installer tous les modules (Important)
==============================================

#. Mettez votre système à jour.

    Assurez-vous d'être connecté à Internet et mettez à jour votre système :

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt update
        sudo apt upgrade

    .. note::

        Les paquets liés à Python3 doivent être installés si vous utilisez la version Lite du système d'exploitation.

        .. raw:: html

            <run></run>

        .. code-block::
        
            sudo apt install git python3-pip python3-setuptools python3-smbus


#. Installez le module ``robot-hat``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
        cd robot-hat
        sudo python3 setup.py install


#. Installez le module ``vilib``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone -b picamera2 https://github.com/sunfounder/vilib.git
        cd vilib
        sudo python3 install.py


#. Téléchargez le code.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone https://github.com/sunfounder/pidog.git --depth 1

#. Installez le module ``pidog``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd pidog
        sudo python3 setup.py install

    Cette étape prendra un certain temps, soyez patient.

#. Exécutez le script ``i2samp.sh``.

    Enfin, vous devez exécuter le script ``i2samp.sh`` pour installer les composants nécessaires à l'amplificateur i2s, sinon le robot n'émettra aucun son.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog
        sudo bash i2samp.sh
        
    .. image:: img/i2s.png

    Tapez ``y`` et appuyez sur ``Entrée`` pour continuer à exécuter le script.

    .. image:: img/i2s2.png

    Tapez ``y`` et appuyez sur ``Entrée`` pour exécuter ``/dev/zero`` en arrière-plan.

    .. image:: img/i2s3.png

    Tapez ``y`` et appuyez sur ``Entrée`` pour redémarrer la machine.

    .. note::
        S'il n'y a pas de son après le redémarrage, il peut être nécessaire d'exécuter plusieurs fois le script ``i2samp.sh``.
