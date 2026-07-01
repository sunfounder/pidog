.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

15. TTS mit Piper und OpenAI
========================================================

In der vorherigen Lektion haben wir zwei integrierte TTS-Engines auf dem Raspberry Pi ausprobiert (**Espeak** und **Pico2Wave**).  
Jetzt sehen wir uns zwei leistungsstärkere Optionen an: **Piper** (offline, auf neuronalen Netzen basierend) und **OpenAI TTS** (online, cloudbasiert).

* **Piper**: Eine lokale TTS-Engine, die offline auf dem Raspberry Pi läuft.  
* **OpenAI TTS**: Ein Online-Dienst, der sehr natürliche, menschlich klingende Stimmen erzeugt.

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere ``robot-hat``, ``vilib``, ``pidog`` und führe das Skript ``i2samp.sh`` aus.

.. _test_piper:

Piper testen
------------------

**Schritte zum Ausprobieren**:

#. Erstelle eine neue Datei:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_piper.py

#. Kopiere den folgenden Beispielcode in die Datei. Drücke ``Ctrl+X``, dann ``Y`` und schließlich ``Enter``, um zu speichern und zu beenden.

   .. code-block:: python

       from pidog.tts import Piper

       tts = Piper()

       # Unterstützte Sprachen auflisten
       print(tts.available_countrys())

       # Modelle für Englisch (en_us) auflisten
       print(tts.available_models('en_us'))

       # Sprachmodell festlegen (wird automatisch heruntergeladen, falls nicht vorhanden)
       tts.set_model("en_US-amy-low")

       # Text ausgeben
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()``: listet die unterstützten Sprachen auf.  
   * ``available_models()``: listet die verfügbaren Modelle für die gewählte Sprache auf.  
   * ``set_model()``: legt das Sprachmodell fest (wird automatisch heruntergeladen, falls es fehlt).  
   * ``say()``: wandelt Text in Sprache um und spielt ihn ab.

#. Führe das Programm aus:

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. Beim ersten Ausführen wird das gewählte Sprachmodell automatisch heruntergeladen. 

   * Danach solltest du hören, wie Pidog sagt: ``Hello! I'm Piper TTS.``

   * Du kannst das Sprachmodell ändern, indem du ``set_model()`` mit einem anderen Namen aufrufst.


OpenAI TTS testen
-------------------------------

**API-Schlüssel abrufen und speichern**

#. Gehe zu |link_openai_platform| und melde dich an. Klicke auf der Seite **API keys** auf **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Fülle die Details aus (Owner, Name, Projekt und ggf. Berechtigungen) und klicke auf **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Sobald der Schlüssel erstellt ist, **kopiere ihn sofort** — du kannst ihn später nicht mehr einsehen. Wenn du ihn verlierst, musst du einen neuen Schlüssel generieren.

   .. image:: img/llm_openai_copy.png

#. Erstelle in deinem Projektordner (z. B. ``/pidog/examples``) eine Datei namens ``secret.py``:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Füge deinen Schlüssel in die Datei ein:

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**Testprogramm schreiben und ausführen**

#. Erstelle eine neue Datei:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano test_tts_openai.py

#. Kopiere den folgenden Beispielcode in die Datei. Drücke ``Ctrl+X``, dann ``Y`` und schließlich ``Enter``, um zu speichern und zu beenden.

   .. code-block:: python

      from pidog.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # or use the try/except version shown above

      # Initialize OpenAI TTS
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # low-latency TTS model
      tts.set_voice('alloy')            # pick a voice

      # Quick hello (sanity check)
      tts.say("Hello! I'm OpenAI TTS.")

#. Führe das Programm aus:

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. Du solltest hören, wie Pidog sagt:  

   ``Hello! I'm OpenAI TTS.``

----

Fehlerbehebung
-------------------

* **No module named 'secret'**

  Das bedeutet, dass ``secret.py`` nicht im selben Ordner wie deine Python-Datei liegt.  
  Verschiebe ``secret.py`` in das Verzeichnis, aus dem du das Skript startest, z. B.:

  .. code-block:: bash

     ls ~/pidog/examples
     # Stelle sicher, dass secret.py und deine .py-Datei dort liegen

* **OpenAI: Invalid API key / 401**

  * Überprüfe, ob du den vollständigen Schlüssel eingefügt hast (beginnt mit ``sk-``) und keine Leerzeichen oder Zeilenumbrüche enthalten sind.  
  * Stelle sicher, dass dein Code den Schlüssel korrekt importiert:

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Überprüfe die Netzwerkverbindung deines Raspberry Pi (z. B. ``ping api.openai.com``).

* **OpenAI: Quota exceeded / Abrechnungsfehler**

  * Du musst möglicherweise ein Zahlungsmittel hinterlegen oder dein Nutzungslimit im OpenAI-Dashboard erhöhen.  
  * Versuche es erneut, nachdem du das Konto-/Abrechnungsproblem behoben hast.

* **Piper: tts.say() läuft, aber kein Ton**

  * Überprüfe, ob tatsächlich ein Sprachmodell vorhanden ist:

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * Stelle sicher, dass der Modellname im Code exakt übereinstimmt:

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Stelle sicher, dass der Robot HAT-Lautsprecher aktiviert ist. Wenn du noch keinen PiDog-Beispielcode ausgeführt hast, aktiviere ihn:

    .. code-block:: bash

       robot_hat enable_speaker

    Dies muss nur einmal pro Systemstart durchgeführt werden.

  * Überprüfe das Audioausgabegerät / die Lautstärke auf deinem Raspberry Pi (``alsamixer``) und ob Lautsprecher angeschlossen und eingeschaltet sind.

* **ALSA- / Audiogeräte-Fehler (z. B. „Audio device busy“ oder „No such file or directory“)**
  
  * Schließe andere Programme, die Audio verwenden.  
  * Starte den Raspberry Pi neu, wenn das Gerät weiterhin belegt ist.  
  * Wähle in den Raspberry-Pi-Audioeinstellungen das richtige Ausgabegerät (HDMI vs. Kopfhöreranschluss).

* **Permission denied beim Ausführen von Python**

  * Führe das Skript bei Bedarf mit ``sudo`` aus:

    .. code-block:: bash

       sudo python3 test_tts_piper.py



Vergleich der TTS-Engines
-------------------------

.. list-table:: Funktionsvergleich: Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - Merkmal
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - Läuft auf
     - Integriert auf Raspberry Pi (offline)
     - Integriert auf Raspberry Pi (offline)
     - Raspberry Pi / PC (offline, benötigt Modell)
     - Cloud (online, benötigt API-Schlüssel)
   * - Stimmqualität
     - Roboterhaft
     - Natürlicher als Espeak
     - Natürlich (neuronales TTS)
     - Sehr natürlich / menschlich
   * - Steuerung
     - Geschwindigkeit, Tonhöhe, Lautstärke
     - Eingeschränkte Steuerung
     - Auswahl verschiedener Stimmen/Modelle
     - Auswahl von Modellen und Stimmen
   * - Sprachen
     - Viele (Qualität variiert)
     - Eingeschränkte Auswahl
     - Viele Stimmen/Sprachen verfügbar
     - Am besten in Englisch (andere je nach Verfügbarkeit)
   * - Latenz / Geschwindigkeit
     - Sehr schnell
     - Schnell
     - Echtzeitfähig auf Pi 4/5 mit „low“-Modellen
     - Netzwerkabhängig (meist geringe Latenz)
   * - Einrichtung
     - Minimal
     - Minimal
     - Download von ``.onnx`` + ``.onnx.json`` Modellen
     - API-Schlüssel erstellen, Client installieren
   * - Am besten geeignet für
     - Schnelle Tests, einfache Sprachansagen
     - Etwas bessere Offline-Stimme
     - Lokale Projekte mit besserer Qualität
     - Höchste Qualität, umfangreiche Stimmoptionen
