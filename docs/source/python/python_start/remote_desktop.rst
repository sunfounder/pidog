.. _remote_desktop:

Fernzugriff auf den Raspberry Pi per Desktop
==================================================

Für diejenigen, die eine grafische Benutzeroberfläche (GUI) gegenüber dem Zugriff über die Befehlszeile bevorzugen, unterstützt der Raspberry Pi die Fernzugriffsfunktionalität per Desktop. Dieser Leitfaden führt Sie durch die Einrichtung und Verwendung von VNC (Virtual Network Computing) für den Fernzugriff.

Wir empfehlen die Verwendung von `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ für diesen Zweck.

**Aktivieren des VNC-Dienstes auf dem Raspberry Pi**

Der VNC-Dienst ist in Raspberry Pi OS vorinstalliert, aber standardmäßig deaktiviert. Folgen Sie diesen Schritten, um ihn zu aktivieren:

#. Geben Sie den folgenden Befehl im Terminal des Raspberry Pi ein:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Navigieren Sie mit der Abwärtspfeiltaste zu **Interfacing Options** und drücken Sie dann **Enter**.

    .. image:: img/config_interface.png
        :align: center

#. Wählen Sie **VNC** aus den Optionen aus.

    .. image:: img/vnc.png
        :align: center

#. Verwenden Sie die Pfeiltasten, um **<Ja>** -> **<OK>** -> **<Fertig stellen>** auszuwählen und die Aktivierung des VNC-Dienstes abzuschließen.

    .. image:: img/vnc_yes.png
        :align: center

**Anmeldung über VNC Viewer**

#. Laden Sie `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ herunter und installieren Sie es auf Ihrem persönlichen Computer.

#. Starten Sie nach der Installation den VNC Viewer. Geben Sie den Hostnamen oder die IP-Adresse Ihres Raspberry Pi ein und drücken Sie Enter.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Wenn Sie dazu aufgefordert werden, geben Sie Ihren Benutzernamen und Ihr Passwort für den Raspberry Pi ein und klicken Sie auf **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Sie haben jetzt Zugriff auf die Desktop-Oberfläche Ihres Raspberry Pi.

    .. image:: img/bullseye_desktop.png
        :align: center
