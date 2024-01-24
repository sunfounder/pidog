.. _install_all_modules:

5. Installieren Sie alle Module (Wichtig)
==============================================

#. Aktualisieren Sie Ihr System.

    Stellen Sie sicher, dass Sie mit dem Internet verbunden sind und aktualisieren Sie Ihr System:

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt update
        sudo apt upgrade

    .. note::

        Python3-bezogene Pakete müssen installiert werden, wenn Sie die Lite-Version des Betriebssystems installieren.

        .. raw:: html

            <run></run>

        .. code-block::
        
            sudo apt install git python3-pip python3-setuptools python3-smbus


#. Installieren Sie das ``robot-hat``-Modul.


    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
        cd robot-hat
        sudo python3 setup.py install



#. Installieren Sie das ``vilib``-Modul.


    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone -b picamera2 https://github.com/sunfounder/vilib.git
        cd vilib
        sudo python3 install.py




#. Laden Sie den Code herunter.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone https://github.com/sunfounder/pidog.git

#. Installieren Sie das ``pidog``-Modul.

    .. raw:: html

        <run></run>

    .. code-block::

        cd pidog
        sudo python3 setup.py install

    Dieser Schritt wird etwas Zeit in Anspruch nehmen, also bitte Geduld haben.

#. Führen Sie das Skript ``i2samp.sh`` aus.

    Schließlich müssen Sie das Skript ``i2samp.sh`` ausführen, um die Komponenten zu installieren, die der i2s-Verstärker benötigt, sonst hat der Roboter keinen Ton.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog
        sudo bash i2samp.sh
        
    .. image:: img/i2s.png

    Geben Sie ``y`` ein und drücken Sie ``Enter``, um das Skript weiter auszuführen.

    .. image:: img/i2s2.png

    Geben Sie ``y`` ein und drücken Sie ``Enter``, um ``/dev/zero`` im Hintergrund laufen zu lassen.

    .. image:: img/i2s3.png

    Geben Sie ``y`` ein und drücken Sie ``Enter``, um den Computer neu zu starten.

    .. note::
        Wenn nach dem Neustart kein Ton zu hören ist, müssen Sie möglicherweise das Skript ``i2samp.sh`` mehrmals ausführen.
