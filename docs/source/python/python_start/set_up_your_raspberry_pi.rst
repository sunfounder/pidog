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

#. Versorgen Sie den Raspberry Pi mit Strom über den Stromadapter. Der Desktop des Raspberry Pi OS sollte nach einigen Sekunden auf dem Bildschirm erscheinen.

    .. image:: img/bullseye_desktop.png
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
