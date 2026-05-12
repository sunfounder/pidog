.. _pidog_skill:

.. start_using_pidog

21. Verwenden von OpenClaw zur Steuerung von PiDog
==========================================================================

**Was ist OpenClaw?**

Stellen Sie es sich als eine erweiterte Version von ChatGPT vor. Während traditionelle Chatbots nur sprechen (Text generieren) können, kann OpenClaw handeln. Es versteht Ihre Anweisungen in natürlicher Sprache und kann tatsächlich Operationen auf Ihrem Computer ausführen, wie z. B. Befehle ausführen, Dateien verwalten und verschiedene Werkzeuge aufrufen.

Hier sind einige fantastische Anwendungsszenarien:

* **Persönlicher Allround-Assistent:** Lassen Sie es Ihnen helfen, Ihren Zeitplan zu verwalten, Erinnerungen zu setzen und Aufgaben zu verfolgen. Sie müssen es ihm nur in einer Chat-App (wie Telegram, WhatsApp) sagen, und es wird sich erinnern und ausführen.
* **Automatisierungs-„Kleber“:** Es kann als Bindeglied für Ihre verschiedenen Dienste fungieren. Sie können es zum Beispiel eine Website auf Preisänderungen überwachen lassen. Sobald ein Preisverfall erkannt wird, kann es automatisch einen n8n-Automatisierungs-Workflow auslösen, um Ihnen eine E-Mail-Benachrichtigung zu senden.
* **Dedizierter Entwicklungsassistent:** Lassen Sie es Ihnen bei der Verwaltung von Servern, dem Ausführen von Skripten und dem Überprüfen von Protokollen helfen. Sie können einfach sagen: „Überprüfe die Systemauslastung für mich“, und es kann per SSH auf Ihren Server zugreifen, den Befehl ausführen und die Ergebnisse zurückliefern.
* **Hardware-„Spielkamerad“:** Dies ist ein sehr interessanter Anwendungsfall. Sie können OpenClaw Hardware steuern lassen, die an einen Raspberry Pi angeschlossen ist. Ein Entwickler hat es zum Beispiel verwendet, um einen Roboter-Staubsauger mit einem mechanischen Arm zu steuern, oder es sogar dazu gebracht, Renndaten zu analysieren und auf einem LED-Bildschirm anzuzeigen. Das offizielle Raspberry Pi-Team hat es sogar verwendet, um eine automatische Fotobox für eine Hochzeit zu bauen – nur durch Konversation, ohne eine einzige Zeile Code zu schreiben!


.. important::

   Der Raspberry Pi Zero 2W hat nur 512 MB RAM, während OpenClaw mindestens 1 GB benötigt. Daher kann es nicht richtig laufen. Ein Raspberry Pi 4/5 oder höher wird empfohlen.

Quick Start OpenClaw
------------------------------

Wenn Sie die Leistungsfähigkeit von OpenClaw so schnell wie möglich erleben möchten, verwenden Sie diese Methode. Sie wird den interaktiven Einrichtungsassistenten automatisch installieren und starten.

1.  Öffnen Sie das Terminal auf Ihrem Raspberry Pi und führen Sie den folgenden Befehl direkt aus. Dieser Befehl lädt das Installationsskript von der offiziellen Website herunter und führt es aus:

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash

    .. note:: Aufgrund schneller Aktualisierungen neuer Versionen ist es normal, wenn Ihre Installationsschritte leicht abweichen.

2.  Das Skript lädt OpenClaw automatisch herunter und installiert es.

    .. image:: /img/openclaw/install_open_claw.png

3.  Sie sehen dann eine Sicherheitsabfrage, ob Sie OpenClaw vertrauen. Wenn Sie sicher sind, dass es sicher und zuverlässig ist, navigieren Sie mit den Pfeiltasten zu „Yes“ und drücken Sie die Eingabetaste.

    .. image:: /img/openclaw/security_open_claw.png

4.  Wählen Sie Quick Start und drücken Sie dann die Eingabetaste.

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  Wählen Sie Ihr Model und drücken Sie dann die Eingabetaste. Hier verwenden wir OpenAI als Beispiel.

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  Wählen Sie OpenAI API Key.

    .. image:: /img/openclaw/api_key_open_claw.png

7.  Fügen Sie jetzt den API-Schlüssel ein.

    .. image:: /img/openclaw/paste_api_key_open_claw.png

.. |link_openai_platform| raw:: html

    <a href="https://platform.openai.com/settings/organization/api-keys" target="_blank">OpenAI Platform</a>

8.  Gehen Sie zu |link_openai_platform| und melden Sie sich an. Klicken Sie auf der Seite **API keys** auf **Create new secret key**.

    .. image:: /img/openclaw/llm_openai_create.png

9.  Füllen Sie die Details aus (Owner, Name, Projekt und Berechtigungen, falls erforderlich) und klicken Sie dann auf **Create secret key**.

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. Sobald der Schlüssel erstellt ist, kopieren Sie ihn sofort – Sie werden ihn nicht wieder sehen können. Wenn Sie ihn verlieren, müssen Sie einen neuen generieren.

    .. image:: /img/openclaw/llm_openai_copy.png

11. Fügen Sie den Schlüssel in die OpenClaw-Konfiguration ein.

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. Wählen Sie das Model aus, das Sie verwenden möchten. In diesem Beispiel verwenden wir **Keep current**.

    .. image:: /img/openclaw/model_config_open_claw.png

13. Als Nächstes folgt die Kanalauswahl. Kanäle beziehen sich auf die von OpenClaw unterstützten Kommunikationsdienste, wie Telegram, WhatsApp, Discord und mehr. Verwenden Sie die Abwärtspfeiltaste, um die Option „Skip for now“ auszuwählen, und drücken Sie dann die Eingabetaste.

    .. image:: /img/openclaw/channel_open_claw.png

14. Als Nächstes werden Sie gefragt, ob Sie sofort Fähigkeiten (Skills) konfigurieren möchten. Wählen Sie „Yes“ und drücken Sie die Eingabetaste.

    .. image:: /img/openclaw/config_skill_open_claw.png

15. Installieren Sie die benötigten Fähigkeiten. Im folgenden Beispiel wählen wir die Option „Skip for now“ (Leertaste zum Auswählen) und drücken dann die Eingabetaste.

    .. image:: /img/openclaw/install_skill_open_claw.png

16. Als Nächstes kommen Hooks; wir werden „command-logger“ und „session-memory“ auswählen.

    .. image:: /img/openclaw/hooks2_open_claw.png

17. Die Installation ist nun abgeschlossen. Sie können OpenClaw starten, indem Sie „Hatch in TUI“ auswählen und die Eingabetaste drücken.

   .. image:: /img/openclaw/hatch_open_claw.png

.. note:: 

   Sie können OpenClaw starten, indem Sie den folgenden Befehl eingeben:

    .. code-block:: bash

       openclaw tui

   Und Sie können die TUI-Schnittstelle durch zweimaliges Drücken von Strg+c verlassen.

------------------------------------------------------------------------

OpenClaw in die Lage versetzen, den PiDog zu steuern
-----------------------------------------------------------------

**Was ist PiDog Skill?**

PiDog Skill ist eine Erweiterung für OpenClaw, die es Ihnen ermöglicht, Ihren SunFounder PiDog V2 Roboterhund über natürliche Sprache zu steuern. Anstatt sich komplexe Befehlszeilenparameter merken zu müssen, können Sie OpenClaw einfach sagen, was PiDog tun soll – wie „lass den Hund sitzen“ oder „schalte die LED-Leuchten auf lila“ – und OpenClaw wird automatisch die entsprechenden Befehle ausführen.

Hier sind einige Dinge, die Sie mit PiDog Skill tun können:

* **Basisaktionen:** PiDog stehen, sitzen, liegen, mit dem Schwanz wedeln, bellen, vorwärts/rückwärts gehen oder links/rechts drehen lassen
* **Posen halten:** PiDog für längere Zeit in einer bestimmten Pose halten (wie z. B. Stehen)
* **LED-Lichtsteuerung:** Ändern der Augenfarben mit Effekten wie Atmen, Hören, Boom oder Dauerlicht
* **Farbanpassung:** Wählen Sie aus Rot, Grün, Blau, Gelb, Lila, Pink, Cyan, Weiß, Orange oder benutzerdefinierten Hex-Farben

----------------------------------------------------------------

Voraussetzungen
------------------------------

Bevor Sie PiDog Skill mit OpenClaw verwenden können, stellen Sie sicher, dass Sie Folgendes haben:

1.  **PiDog V2** korrekt zusammengebaut und mit Ihrem Raspberry Pi verbunden
2.  **OpenClaw** installiert und läuft
3.  Die folgenden Verzeichnisse existieren auf Ihrem System:

   - ``~/pidog``
   - ``~/robot-hat``
   - ``~/vilib``

Sie können die Installation überprüfen, indem Sie Folgendes ausführen:

.. code-block:: bash

   python3 -c "import pidog"

Wenn dieser Befehl fehlerfrei ausgeführt wird, können Sie fortfahren.

----------------------------------------------------------------

Installieren von PiDog Skill
------------------------------

Befolgen Sie diese Schritte, um PiDog Skill für OpenClaw zu installieren:

1.  **Erstellen Sie das Skills-Verzeichnis** (falls es nicht bereits existiert):

   .. code-block:: bash

      mkdir -p ~/.openclaw/workspace/skills/

2.  **Kopieren Sie die PiDog-Skill-Dateien** in das OpenClaw-Skills-Verzeichnis:

   .. code-block:: bash

      cp -r ~/pidog/pidog-control ~/.openclaw/workspace/skills/pidog-control/

   .. note:: Ersetzen Sie ``~/pidog-skill`` durch den tatsächlichen Pfad, in dem sich Ihre PiDog-Skill-Dateien befinden.

3.  **Überprüfen Sie die Installation**, indem Sie die Skill-Dateien auflisten:

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/pidog-control/scripts/

   Sie sollten ``pidog_ctl.py`` und ``pidog_rgb_ctl.py`` in der Ausgabe sehen.

----------------------------------------------------------------

Testen von PiDog Skill
------------------------------

Bevor Sie den Skill mit OpenClaw verwenden, wird empfohlen, die grundlegende Funktionalität direkt vom Terminal aus zu testen.

**Schritt 1: PiDog-Status prüfen**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py status

**Schritt 2: Führen Sie einen sicheren Test durch**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py safe-test

**Schritt 3: Testen Sie grundlegende Aktionen**

PiDog sitzen lassen:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action sit

PiDog stehen lassen und die Pose halten:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action stand --hold

PiDog bellen lassen:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action bark

**Schritt 4: Testen Sie die LED-Leuchten**

Testen Sie den Boom-Lichteffekt mit der Farbe Lila:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple

Testen Sie andere Lichteffekte:

.. code-block:: bash

   # Atem-Effekt mit roter Farbe
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light breath --color red

   # Hör-Effekt mit blauer Farbe
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light listen --color blue

   # Lichter ausschalten
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light off

----------------------------------------------------------------

Verwenden von PiDog Skill in OpenClaw
------------------------------------------------------

Sobald Sie bestätigt haben, dass PiDog Skill von der Befehlszeile aus funktioniert, können Sie es innerhalb von OpenClaw verwenden.

1.  **Starten Sie OpenClaw TUI**:

   .. code-block:: bash

      openclaw tui

2.  **Senden Sie Befehle in natürlicher Sprache**, um PiDog zu steuern. Hier sind einige Beispiele:

   * „Lass den Hund sitzen“
   * „Lass PiDog stehen und bleiben“
   * „Wedel mit dem Schwanz des Hundes“
   * „Lass den Hund bellen“
   * „Schalte die LED-Leuchten mit Boom-Effekt auf Lila“
   * „Setze die Augenlichter auf Atem-Effekt mit roter Farbe“
   * „Lass PiDog vorwärts gehen“

3.  **OpenClaw wird automatisch** Ihre Anfrage in den entsprechenden Befehl übersetzen und auf dem PiDog ausführen.

----------------------------------------------------------------

Verfügbare Aktionen und Befehle
-------------------------------------------------

Hier ist die vollständige Liste der unterstützten Aktionen für PiDog Skill:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Aktion
     - Beschreibung
   * - stand
     - PiDog aufstehen lassen
   * - sit
     - PiDog hinsetzen lassen
   * - lie
     - PiDog hinlegen lassen
   * - wag-tail
     - Mit dem Schwanz von PiDog wedeln
   * - bark
     - Bellgeräusch erzeugen
   * - forward
     - Vorwärts gehen
   * - backward
     - Rückwärts gehen

**Posen halten:**

Fügen Sie ``--hold`` zu einer beliebigen Aktion hinzu, um PiDog in dieser Pose zu halten. Zum Beispiel: „stand --hold“

**Lichteffekte:**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Effekt
     - Beschreibung
   * - off
     - Alle LED-Leuchten ausschalten
   * - breath
     - Sanfter Atem-/Pulseffekt
   * - listen
     - Reaktiver Hör-Modus
   * - boom
     - Dynamischer Burst-Effekt (am auffälligsten)
   * - solid
     - Konstantes Dauerlicht (verwenden Sie für bessere Wirkung „boom“)

**Unterstützte Farben:**

rot, grün, blau, gelb, lila, pink, cyan, weiß, orange oder Hex-Codes wie ``#FF5733``

----------------------------------------------------------------

Fehlerbehebung
------------------------------

OpenClaw-Probleme
^^^^^^^^^^^^^^^^^^^^^^^^

F: Während der Installation erhalte ich den Fehler ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. Was soll ich tun?

   Sie können dies vorerst ignorieren, könnten aber später auf Probleme stoßen. Bitte beziehen Sie sich dann jeweils darauf.

F: Wenn ich ``openclaw tui`` ausführe, erhalte ich den Fehler ``-bash: openclaw: command not found``. Was soll ich tun?

   Führen Sie den folgenden Befehl aus:

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   Sie sollten nun die TUI-Schnittstelle mit ``openclaw tui`` starten können.

F: In ``openclaw tui`` erhalte ich ``not connected to gateway — message not sent`` oder die Nachricht ``gateway disconnected: closed``.

   Dies liegt daran, dass Ihr OpenClaw Gateway-Dienst nicht gestartet ist. Öffnen Sie ein weiteres Terminal und führen Sie den folgenden Befehl aus, um das OpenClaw Gateway zu starten:

   .. code-block:: bash

      openclaw gateway

   Starten Sie dann ``openclaw tui`` neu, und Sie können es direkt verwenden.

F: Ich möchte den OpenClaw Gateway-Dienst so einrichten, dass er im Hintergrund läuft / automatisch beim Booten startet. Wie mache ich das?

   Normalerweise sollte Ihr OpenClaw Gateway-Dienst automatisch beim Booten starten. Wenn nicht, können Sie ihn manuell mit dem folgenden Befehl starten.

   1. Erstellen Sie das Verzeichnis ``~/.config/systemd/user``:

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user

   2. Erstellen Sie die Datei ``openclaw-gateway.service``:

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF

   3. Laden Sie dann die systemd-Konfiguration neu:

   .. code-block:: bash

      systemctl --user daemon-reload

   4. Starten Sie den Dienst:

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   An diesem Punkt starten Sie ``openclaw tui`` neu und können es direkt verwenden.

   5. Aktivieren Sie den automatischen Start beim Booten:

   .. code-block:: bash

      systemctl --user enable openclaw-gateway

F: Mein OpenClaw kann nicht auf dem System operieren. Was soll ich tun?

   Ein neu installiertes OpenClaw hat standardmäßig möglicherweise keine Berechtigung, auf Ihrem Raspberry Pi-System zu operieren; es kann nur chatten. Wir müssen die Berechtigungen manuell konfigurieren.

   1.  Öffnen Sie die OpenClaw-Konfigurationsdatei:

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  Suchen Sie die Option ``tools`` und ändern Sie ``profile`` und ``exec`` wie gezeigt.

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3.  Speichern und beenden.

   4.  Geben Sie den folgenden Befehl im Terminal ein, um das OpenClaw Gateway neu zu starten:

      .. code-block:: bash

         openclaw gateway restart

   Jetzt sollte OpenClaw Lese- und Schreibberechtigungen haben und auf Ihrem Raspberry Pi-System operieren können.

PiDog-Probleme
^^^^^^^^^^^^^^^^^^^^^^^^

F: PiDog reagiert nicht auf Befehle. Was soll ich tun?

   Stellen Sie zunächst sicher, dass PiDog ordnungsgemäß angeschlossen und eingeschaltet ist. Testen Sie dann den Basisbefehl:

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py status

   Wenn dies fehlschlägt, überprüfen Sie, ob die erforderlichen Verzeichnisse existieren:

      - ``~/pidog``
      - ``~/robot-hat``
      - ``~/vilib``

F: Der Test ``import pidog`` schlägt fehl.

   Dies bedeutet, dass die PiDog Python-Bibliothek nicht ordnungsgemäß installiert ist. Bitte lesen Sie die offizielle Installationsanleitung für PiDog V2, um die erforderlichen Bibliotheken zu installieren.

F: LED-Leuchten funktionieren nicht wie erwartet.

   Wenn das Dauerlicht nicht deutlich sichtbar ist, verwenden Sie stattdessen den ``boom``-Effekt – er liefert die auffälligsten Ergebnisse:

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple

F: OpenClaw erkennt den PiDog-Skill nicht.

   Erinnern Sie OpenClaw daran, die Skills zu synchronisieren, indem Sie in der TUI sagen: *„Bitte synchronisiere meine Skills“* oder starten Sie das OpenClaw Gateway neu:

   .. code-block:: bash

      openclaw gateway restart

F: Die Bell-Aktion klingt nicht richtig.

   Die Bell-Aktion verwendet standardmäßig den Sound ``single_bark_1``. Dies ist normales Verhalten für PiDog V2.