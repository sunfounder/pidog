.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _install_all_modules:

5. Alle Module installieren (Wichtig)
==============================================

.. note::

    Python3-bezogene Pakete müssen installiert werden, wenn du die Lite-Version des Betriebssystems verwendest.

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt install git python3-pip python3-setuptools python3-smbus


#. Installiere das Modul ``robot-hat``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
        cd robot-hat
        sudo python3 install.py


#. Installiere das Modul ``vilib``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone https://github.com/sunfounder/vilib.git
        cd vilib
        sudo python3 install.py

#. Installiere das Modul ``pidog``.

    .. raw:: html

        <run></run>

    .. code-block:: bash

        cd ~/
        git clone https://github.com/sunfounder/pidog.git --depth 1
        cd pidog
        sudo python3 setup.py install

    Dieser Schritt dauert ein wenig – bitte habe etwas Geduld.

#. Führe das Skript ``i2samp.sh`` aus.

    Zum Schluss musst du das Skript ``i2samp.sh`` ausführen, um die Komponenten zu installieren, die für den i2s-Verstärker erforderlich sind.  
    Andernfalls gibt der Roboter keinen Ton aus.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/robot-hat
        sudo bash i2samp.sh
        
    .. image:: img/i2s.png

    Tippe ``y`` und drücke ``Enter``, um das Skript fortzusetzen.

    .. image:: img/i2s2.png

    Tippe ``y`` und drücke ``Enter``, um ``/dev/zero`` im Hintergrund auszuführen.

    .. image:: img/i2s3.png

    Tippe ``y`` und drücke ``Enter``, um den Raspberry Pi neu zu starten.

    .. note::
        Wenn nach dem Neustart kein Ton zu hören ist, musst du das Skript ``i2samp.sh`` möglicherweise mehrmals ausführen.
