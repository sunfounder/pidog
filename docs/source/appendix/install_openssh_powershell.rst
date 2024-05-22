.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _openssh_powershell:

OpenSSH über Powershell installieren
------------------------------------------------------

Wenn Sie ``ssh <username>@<hostname>.local`` (oder ``ssh <username>@<IP address>``) verwenden, um eine Verbindung zu Ihrem Raspberry Pi herzustellen, und folgende Fehlermeldung erscheint:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.

Dies bedeutet, dass Ihr Computersystem zu alt ist und `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ nicht vorinstalliert hat. Sie müssen der folgenden Anleitung folgen, um es manuell zu installieren.

#. Geben Sie ``powershell`` in das Suchfeld Ihres Windows-Desktops ein, klicken Sie mit der rechten Maustaste auf die ``Windows PowerShell`` und wählen Sie ``Als Administrator ausführen`` aus dem erscheinenden Menü.

    .. image:: img/powershell_ssh.png
        :align: center

#. Verwenden Sie den folgenden Befehl, um ``OpenSSH.Client`` zu installieren.

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Nach der Installation wird die folgende Ausgabe zurückgegeben.

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Überprüfen Sie die Installation mit dem folgenden Befehl.

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Es zeigt Ihnen jetzt an, dass ``OpenSSH.Client`` erfolgreich installiert wurde.

    .. code-block::

        Name : OpenSSH.Client~~~~0.0.1.0
        State: Installed
        Name : OpenSSH.Server~~~~0.0.1.0
        State: NotPresent

    .. warning:: 
        Wenn der obige note nicht erscheint, bedeutet das, dass Ihr Windows-System immer noch zu alt ist, und es wird empfohlen, ein Drittanbieter-SSH-Tool zu installieren, wie :ref:`login_windows`.

#. Starten Sie nun PowerShell neu und führen Sie es weiterhin als Administrator aus. Zu diesem Zeitpunkt können Sie sich mit dem ``ssh``-Befehl in Ihren Raspberry Pi einloggen, wobei Sie aufgefordert werden, das zuvor eingerichtete Passwort einzugeben.

    .. image:: img/powershell_login.png
