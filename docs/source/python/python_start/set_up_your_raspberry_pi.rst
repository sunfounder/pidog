.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

4. Einrichten Ihres Raspberry Pi
=====================================

Einrichten mit einem Bildschirm
--------------------------------------

Mit einem Bildschirm wird das Arbeiten mit Ihrem Raspberry Pi erheblich vereinfacht.

**Benötigte Komponenten**

* Raspberry Pi 5 Modell B
* Stromadapter
* Micro-SD-Karte
* Stromadapter für den Bildschirm
* HDMI-Kabel
* Bildschirm
* Maus
* Tastatur

**Schritte**:

#. Schließen Sie die Maus und die Tastatur an den Raspberry Pi an.

#. Verwenden Sie das HDMI-Kabel, um den Bildschirm mit dem HDMI-Port des Raspberry Pi zu verbinden. Stellen Sie sicher, dass der Bildschirm an eine Stromquelle angeschlossen und eingeschaltet ist.

#. Versorgen Sie den Raspberry Pi mit Strom über den Stromadapter. 

#. Nach einigen Sekunden wird der Desktop von Raspberry Pi OS angezeigt. Nun können Sie das Terminal öffnen, um mit der Eingabe von Befehlen zu beginnen.

    .. image:: img/bookwarm.png
        :align: center

Einrichten ohne Bildschirm
------------------------------

Wenn Sie keinen Monitor haben, ist der Fernzugriff eine praktikable Option.

**Benötigte Komponenten**

* Raspberry Pi 5 Modell B
* Stromadapter
* Micro-SD-Karte

Mit SSH können Sie auf die Bash-Shell des Raspberry Pi zugreifen, die die Standard-Linux-Shell ist. Bash bietet eine Befehlszeilenschnittstelle für die Durchführung verschiedener Aufgaben.

Für diejenigen, die eine grafische Benutzeroberfläche (GUI) bevorzugen, ist die Fernzugriffsfunktionalität per Desktop eine bequeme Alternative für die Verwaltung von Dateien und Operationen.

Für detaillierte Einrichtungsanleitungen, die auf Ihrem Betriebssystem basieren, siehe die folgenden Abschnitte:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop
