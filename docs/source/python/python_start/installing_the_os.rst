.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

2. Betriebssystem installieren
========================================

**Benötigte Komponenten**

* Raspberry Pi 5B
* Ein Personal Computer
* Eine Micro-SD-Karte

**Installationsschritte**

#. Besuchen Sie die Software-Download-Seite von Raspberry Pi unter `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Wählen Sie die Imager-Version, die mit Ihrem Betriebssystem kompatibel ist. Laden Sie die Datei herunter und öffnen Sie sie, um die Installation zu starten.

    .. image:: img/os_install_imager.png

#. Während der Installation kann je nach Betriebssystem eine Sicherheitsaufforderung erscheinen. Zum Beispiel könnte Windows eine Warnmeldung anzeigen. Wählen Sie in solchen Fällen **Weitere Informationen** und dann **Trotzdem ausführen**. Folgen Sie den Anweisungen auf dem Bildschirm, um die Installation des Raspberry Pi Imager abzuschließen.

    .. image:: img/os_info.png

#. Legen Sie Ihre SD-Karte in den SD-Kartensteckplatz Ihres Computers oder Laptops ein.

#. Starten Sie die Raspberry Pi Imager-Anwendung, indem Sie auf das Symbol klicken oder ``rpi-imager`` in Ihrem Terminal eingeben.

    .. image:: img/os_open_imager.png

#. Klicken Sie auf **GERÄT AUSWÄHLEN** und wählen Sie Ihr spezifisches Raspberry Pi-Modell aus der Liste aus (note: Raspberry Pi 5 ist nicht anwendbar).

    .. image:: img/os_choose_device.png

#. Wählen Sie **BETRIEBSSYSTEM AUSWÄHLEN** und dann **Raspberry Pi OS (Legacy)**.

    .. warning::

        * Bitte installieren Sie nicht die **Bookworm**-Version, da der Lautsprecher nicht funktionieren wird.
        * Sie müssen die **Raspberry Pi OS (Legacy)**-Version - **Debian Bullseye** installieren.

            .. image:: img/os_choose_os.png

#. Klicken Sie auf **Speicher auswählen** und wählen Sie das entsprechende Speichergerät für die Installation aus.

    .. note::

        Stellen Sie sicher, dass Sie das richtige Speichergerät auswählen. Um Verwechslungen zu vermeiden, trennen Sie alle zusätzlichen Speichergeräte, wenn mehrere angeschlossen sind.

    .. image:: img/os_choose_sd.png

#. Klicken Sie auf **WEITER** und dann auf **EINSTELLUNGEN BEARBEITEN**, um Ihre Betriebssystemeinstellungen anzupassen. Wenn Sie einen Monitor für Ihren Raspberry Pi haben, können Sie die nächsten Schritte überspringen und auf 'Ja' klicken, um mit der Installation zu beginnen. Passen Sie andere Einstellungen später am Monitor an.

    .. image:: img/os_enter_setting.png

#. Definieren Sie einen **Hostnamen** für Ihren Raspberry Pi.

    .. note::

        Der Hostname ist der Netzwerkidentifikator Ihres Raspberry Pi. Sie können auf Ihren Pi über ``<hostname>.local`` oder ``<hostname>.lan`` zugreifen.

    .. image:: img/os_set_hostname.png

#. Erstellen Sie einen **Benutzernamen** und ein **Passwort** für das Administratorkonto des Raspberry Pi.

    .. note::

        Die Einrichtung eines einzigartigen Benutzernamens und Passworts ist entscheidend für die Sicherheit Ihres Raspberry Pi, der kein Standardpasswort hat.

    .. image:: img/os_set_username.png

#. Konfigurieren Sie das WLAN, indem Sie die **SSID** und das **Passwort** Ihres Netzwerks angeben.

    .. note::

        Setzen Sie das ``Wireless LAN-Land`` auf den zweistelligen `ISO/IEC alpha2-Code <https://de.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_, der Ihrem Standort entspricht.

    .. image:: img/os_set_wifi.png

#. Klicken Sie auf **DIENSTE** und aktivieren Sie **SSH** für sicheren, passwortgeschützten Fernzugriff. Denken Sie daran, Ihre Einstellungen zu speichern.

    .. image:: img/os_enable_ssh.png

#. Bestätigen Sie Ihre ausgewählten Einstellungen, indem Sie auf **Ja** klicken.

    .. image:: img/os_click_yes.png

#. Wenn die SD-Karte vorhandene Daten enthält, stellen Sie sicher, dass Sie diese sichern, um Datenverlust zu vermeiden. Fahren Sie mit **Ja** fort, wenn keine Sicherung benötigt wird.

    .. image:: img/os_continue.png

#. Der Installationsprozess des Betriebssystems beginnt auf der SD-Karte. Ein Bestätigungsdialog erscheint nach Abschluss.

    .. image:: img/os_finish.png
        :align: center


#. Stecken Sie die mit dem Raspberry Pi OS eingerichtete SD-Karte in den microSD-Kartensteckplatz, der sich auf der Unterseite des Raspberry Pi befindet.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center
