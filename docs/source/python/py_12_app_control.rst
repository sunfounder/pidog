12. PiDog mit der APP spielen
================================

In diesem Beispiel verwenden wir die SunFounder Controller APP, um PiDog zu steuern.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/app_control.mp4" type="video/mp4">
      Ihr Browser unterstützt das Video-Tag nicht.
   </video>

Sie müssen zuerst die APP auf Ihrem Telefon/Tablet herunterladen, dann eine Verbindung zum von PiDog gesendeten Hotspot herstellen und schließlich Ihren eigenen Fernbedienung auf SunFounder Controller erstellen, um PiDog zu steuern.

PiDog mit der App steuern
----------------------------

#. Installieren Sie `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ aus dem **APP Store(iOS)** oder **Google Play(Android)**.

#. Installieren Sie das Modul ``sunfounder-controller``.

    Die Module ``robot-hat``, ``vilib`` und ``picar-x`` müssen zuerst installiert werden, siehe: :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Führen Sie den Code aus.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 12_app_control.py

    Nachdem der Code ausgeführt wurde, sehen Sie die folgende Aufforderung, was bedeutet, dass Ihr PiDog erfolgreich mit dem Netzwerk kommuniziert.

    .. code-block:: 

        Running on: http://192.168.18.138:9000/mjpg

        * Serving Flask app "vilib.vilib" (lazy loading)
        * Environment: development
        * Debug mode: off
        * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)       

#. Verbinden Sie ``PiDog`` und ``Sunfounder Controller``.

    * Verbinden Sie Ihr Tablet/Telefon mit dem WLAN, in dem sich PiDog befindet.

    * Öffnen Sie die ``Sunfounder Controller`` APP. Klicken Sie auf das + Symbol, um einen Controller hinzuzufügen.

        .. image:: img/app1.png
      

    * Für einige Produkte sind voreingestellte Controller verfügbar, hier wählen wir **PiDog**. Geben Sie ihm einen Namen oder tippen Sie einfach auf **Bestätigen**.

        .. image:: img/app_preset.jpg


    * Sobald Sie drinnen sind, sucht die App automatisch nach dem **Mydog**. Nach einem Moment sehen Sie eine Aufforderung, die besagt, dass die Verbindung erfolgreich war.

        .. image:: img/app_auto_connect.jpg

    .. note::

        * Sie können auch manuell auf den |app_connect| Button klicken. Warten Sie einige Sekunden, MyDog(IP) wird erscheinen, klicken Sie darauf, um sich zu verbinden.

            .. image:: img/sc_mydog.jpg

#. Führen Sie den Controller aus.

    * Wenn die Aufforderung "Connected Successfully" erscheint, tippen Sie auf die ▶ Taste in der oberen rechten Ecke.

    * Das Bild der Kamera erscheint in der APP, und jetzt können Sie Ihren PiDog mit diesen Widgets steuern.

        .. image:: img/sc_run.jpg
    

Hier sind die Funktionen der Widgets.

* A: Erkennt die Hindernisentfernung, also die Messung des Ultraschallmoduls.
* C: Gesichtserkennung ein-/ausschalten.
* D: Steuert den Neigungswinkel von PiDogs Kopf (Kopf neigen).
* E: Sitzen.
* F: Stehen.
* G: Liegen.
* I: PiDogs Kopf kraulen.
* N: Bellen.
* O: Schwanz wedeln.
* P: Hecheln.
* K: Steuert PiDogs Bewegungen (vorwärts, rückwärts, links und rechts).
* Q: Steuert die Ausrichtung von PiDogs Kopf.
* J: Wechselt in den Sprachsteuerungsmodus. Es unterstützt die folgenden Sprachbefehle: 

    * ``forward``
    * ``backward``
    * ``turn left``
    * ``turn right``
    * ``trot``
    * ``stop``
    * ``lie down`` 
    * ``stand up``
    * ``sit``
    * ``bark``
    * ``bark harder``
    * ``pant``
    * ``wag tail``
    * ``shake head``
    * ``stretch``
    * ``doze off``
    * ``push-up``
    * ``howling``
    * ``twist body``
    * ``scratch``
    * ``handshake``
    * ``high five``

Autostart beim Booten
-------------------------------
Wenn Sie PiDog über die APP steuern, möchten Sie nicht zuerst in den Raspberry Pi einloggen und ``12_app_control.py`` laufen lassen, bevor Sie die Verbindung mit der APP herstellen.

Es gibt einen effizienteren Ansatz. Sie können PiDog so einstellen, dass es ``12_app_control.py`` automatisch ausführt, jedes Mal, wenn es eingeschaltet wird. Danach können Sie direkt mit der APP eine Verbindung zu PiDog herstellen und Ihren Roboterhund bequem steuern.

Wie richten Sie das ein?

#. Führen Sie die folgenden Befehle aus, um die ``pidog_app``-Anwendung zu installieren und zu konfigurieren und WLAN für PiDog einzurichten.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/bin
        sudo bash pidog_app_install.sh

#. Geben Sie am Ende ``y`` ein, um PiDog neu zu starten.

    .. image:: img/auto_start.png

#. Ab dann können Sie PiDog einfach einschalten und direkt mit der APP steuern.

.. warning::

    Wenn Sie andere Skripte ausführen möchten, führen Sie zuerst ``pidog_app disable`` aus, um die Autostart-Funktion auszuschalten.


APP-Programmkonfiguration
-----------------------------

Sie können die folgenden Befehle eingeben, um die Einstellungen des APP-Modus zu ändern.

.. code-block::

    pidog_app <OPTION> [input]

**OPTION**
    * ``-h`` ``help``: Hilfe, diese Nachricht anzeigen
    * ``start`` ``restart``: ``pidog_app``-Dienst neu starten
    * ``stop``: ``pidog_app``-Dienst stoppen
    * ``disable``: Autostart-Programm ``app_controller`` beim Booten deaktivieren
    * ``enable``: Autostart-Programm ``app_controller`` beim Booten aktivieren
    * ``close_ap``: Hotspot schließen, Autostart-Hotspot beim Booten deaktivieren und in den STA-Modus wechseln
    * ``open_ap``: Hotspot öffnen, Autostart-Hotspot beim Booten aktivieren
    * ``ssid``: SSID (Netzwerkname) des Hotspots festlegen
    * ``psk``: Passwort des Hotspots festlegen
    * ``country``: Ländercode des Hotspots festlegen
