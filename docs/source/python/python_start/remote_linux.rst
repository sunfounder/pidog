Für Linux/Unix-Benutzer
==========================

#. Suchen und öffnen Sie das **Terminal** auf Ihrem Linux/Unix-System.

#. Stellen Sie sicher, dass Ihr Raspberry Pi mit demselben Netzwerk verbunden ist. Überprüfen Sie dies, indem Sie `ping <hostname>.local` eingeben. Zum Beispiel:

    .. code-block::

        ping raspberrypi.local

    Sie sollten die IP-Adresse des Raspberry Pi sehen, wenn er mit dem Netzwerk verbunden ist.

    * Wenn das Terminal eine Meldung wie ``Ping request could not find host pi.local. Please check the name and try again.`` anzeigt, überprüfen Sie den eingegebenen Hostnamen.
    * Wenn Sie die IP-Adresse nicht abrufen können, überprüfen Sie Ihre Netzwerk- oder WLAN-Einstellungen auf dem Raspberry Pi.

#. Initiieren Sie eine SSH-Verbindung, indem Sie ``ssh <Benutzername>@<Hostname>.local`` oder ``ssh <Benutzername>@<IP-Adresse>`` eingeben. Zum Beispiel:

    .. code-block::

        ssh pi@raspberrypi.local

#. Bei Ihrer ersten Anmeldung stoßen Sie auf eine Sicherheitsmeldung. Geben Sie ``yes`` ein, um fortzufahren.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Geben Sie das Passwort ein, das Sie zuvor festgelegt haben. Beachten Sie, dass das Passwort aus Sicherheitsgründen beim Tippen nicht sichtbar ist.

    .. note::
        Es ist normal, dass die Passwortzeichen im Terminal nicht angezeigt werden. Stellen Sie einfach sicher, dass Sie das richtige Passwort eingeben.

#. Sobald Sie sich erfolgreich eingeloggt haben, ist Ihr Raspberry Pi jetzt verbunden, und Sie sind bereit, zum nächsten Schritt überzugehen.
