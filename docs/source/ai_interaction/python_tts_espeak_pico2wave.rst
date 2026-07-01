.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

14. TTS mit Espeak und Pico2Wave
=================================================

In dieser Lektion verwenden wir zwei integrierte Text-to-Speech (TTS)-Engines auf dem Raspberry Pi — **Espeak** und **Pico2Wave** —, um Pidog sprechen zu lassen.

Beide Engines sind einfach und laufen offline, unterscheiden sich aber deutlich im Klang:

* **Espeak**: sehr leichtgewichtig und schnell, aber die Stimme klingt roboterhaft. Du kannst Geschwindigkeit, Tonhöhe und Lautstärke anpassen.  
* **Pico2Wave**: erzeugt eine weichere und natürlichere Stimme als Espeak, hat jedoch weniger Konfigurationsmöglichkeiten.

Du wirst den Unterschied in **Stimmqualität** und **Funktionsumfang** hören.

----

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere ``robot-hat``, ``vilib``, ``pidog`` und führe das Skript ``i2samp.sh`` aus.

Espeak testen
--------------------

Espeak ist eine leichtgewichtige TTS-Engine, die standardmäßig im Raspberry Pi OS enthalten ist.  
Ihre Stimme klingt roboterhaft, ist aber sehr gut konfigurierbar: Du kannst Lautstärke, Tonhöhe, Geschwindigkeit und mehr anpassen.

**Schritte zum Ausprobieren**:

* Erstelle eine neue Datei mit folgendem Befehl:

  .. code-block:: bash
  
      cd ~/pidog/examples
      sudo nano test_tts_espeak.py

* Kopiere dann den Beispielcode hinein. Drücke ``Ctrl+X``, dann ``Y`` und schließlich ``Enter``, um zu speichern und zu beenden.

  .. code-block:: python
  
      from pidog.tts import Espeak

      tts = Espeak()
  
      # Optionale Stimm-Anpassung
      # tts.set_amp(100)   # 0 bis 200
      # tts.set_speed(150) # 80 bis 260
      # tts.set_gap(5)     # 0 bis 200
      # tts.set_pitch(50)  # 0 bis 99

      # Schneller Test
      tts.say("Hello! I'm Espeak TTS.")
  
* Führe das Programm aus:

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* Du solltest hören, wie Pidog sagt: „Hello! I'm Espeak TTS.“  
* Entferne die Kommentarzeichen bei den Stimm-Anpassungszeilen im Code, um zu testen, wie ``amp``, ``speed``, ``gap`` und ``pitch`` den Klang verändern.

----

Pico2Wave testen
---------------------

Pico2Wave erzeugt eine natürlichere, menschlich klingende Stimme als Espeak.  
Es ist einfacher zu verwenden, bietet aber weniger Einstellungsmöglichkeiten — du kannst nur die Sprache ändern, nicht Tonhöhe oder Geschwindigkeit.

**Schritte zum Ausprobieren**:

* Erstelle eine neue Datei mit folgendem Befehl:

  .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_pico2wave.py

* Kopiere dann den Beispielcode hinein. Drücke ``Ctrl+X``, dann ``Y`` und schließlich ``Enter``, um zu speichern und zu beenden.

  .. code-block:: python
  
      from pidog.tts import Pico2Wave
  
      tts = Pico2Wave()
  
      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
      # Schneller Test
      tts.say("Hello! I'm Pico2Wave TTS.")

* Führe das Programm aus:

  .. code-block::

    sudo python3 test_tts_pico2wave.py

* Du solltest hören, wie Pidog sagt: „Hello! I'm Pico2Wave TTS.“  
* Probiere verschiedene Sprachen aus (z. B. ``es-ES`` für Spanisch) und höre dir die Unterschiede an.

----

Fehlerbehebung
-------------------

* **Kein Ton bei Espeak oder Pico2Wave**

  * Stelle sicher, dass der Robot HAT-Lautsprecher aktiviert ist. Wenn du noch keinen PiDog-Beispielcode ausgeführt hast, aktiviere ihn:

    .. code-block:: bash

       robot_hat enable_speaker

    Dies muss nur einmal pro Systemstart durchgeführt werden.

  * Überprüfe, ob Lautsprecher/Kopfhörer angeschlossen und nicht stummgeschaltet sind.
  * Führe einen kurzen Test im Terminal aus:

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  Wenn du nichts hörst, liegt das Problem an der Audioausgabe, nicht an deinem Python-Code.

* **Espeak-Stimme klingt zu schnell oder zu roboterhaft**

  * Versuche, die Parameter in deinem Code anzupassen:

    .. code-block:: python

       tts.set_speed(120)   # langsamer
       tts.set_pitch(60)    # andere Tonhöhe

* **„Permission denied“ beim Ausführen des Codes**

  * Versuche, den Code mit ``sudo`` auszuführen:

    .. code-block:: bash

       sudo python3 test_tts_espeak.py

Vergleich: Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Merkmal
     - Espeak
     - Pico2Wave
   * - Sprachqualität
     - Roboterhaft, synthetisch
     - Natürlicher, menschlicher Klang
   * - Sprachen
     - Standard: Englisch
     - Weniger, aber gebräuchliche Sprachen
   * - Einstellbar
     - Ja (Geschwindigkeit, Tonhöhe, usw.)
     - Nein (nur Sprache)
   * - Leistung
     - Sehr schnell, leichtgewichtig
     - Etwas langsamer, ressourcenintensiver

