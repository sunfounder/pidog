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

Alle Module installieren (Wichtig)
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
   
   .. code-block::
   
       cd ~/
       git clone https://github.com/sunfounder/pidog.git --depth 1
       cd pidog
       sudo pip3 install . --break
   
   Dieser Schritt dauert ein wenig – bitte habe etwas Geduld.

#. Führe das Skript ``i2samp.sh`` aus.

   Zum Schluss musst du das Skript ``i2samp.sh`` ausführen, um die Komponenten zu installieren, die für den i2s-Verstärker erforderlich sind.  
   Andernfalls gibt der Roboter keinen Ton aus.
   
   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/robot-hat
       sudo bash i2samp.sh
        
   Geben Sie dreimal ``y`` ein und drücken Sie **Enter**, um das Skript fortzusetzen, ``/dev/zero`` im Hintergrund zu starten und anschließend den Rechner neu zu starten.

   .. note::
        Wenn nach dem Neustart kein Ton zu hören ist, musst du das Skript ``i2samp.sh`` möglicherweise mehrmals ausführen.

        Wenn du außerdem versuchst, Audio direkt abzuspielen (z. B. mit ``aplay``), ohne vorher ein PiDog-Beispiel auszuführen, musst du den Lautsprecher manuell aktivieren:

        .. code-block:: bash

           robot_hat enable_speaker

        Dies muss nur einmal pro Systemstart durchgeführt werden. Das Ausführen eines beliebigen PiDog-Beispiels (das ``Pidog()`` initialisiert) erledigt dies automatisch.
