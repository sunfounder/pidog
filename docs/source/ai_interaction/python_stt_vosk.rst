.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

16. STT mit Vosk (Offline)
==============================================

Vosk ist eine leichtgewichtige Speech-to-Text (STT) Engine, die viele Sprachen unterstützt und vollständig **offline** auf dem Raspberry Pi läuft.  
Du benötigst nur einmalig Internetzugang, um ein Sprachmodell herunterzuladen. Danach funktioniert alles **ohne Netzwerkverbindung**.

In dieser Lektion werden wir:

* Das Mikrofon auf dem Raspberry Pi überprüfen.  
* Vosk mit einem ausgewählten Sprachmodell installieren und testen.

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``pidog`` und führe dann das Skript ``i2samp.sh`` aus.

1. Mikrofon überprüfen
----------------------

Bevor du die Spracherkennung verwendest, solltest du sicherstellen, dass dein USB-Mikrofon korrekt funktioniert.

#. Liste die verfügbaren Aufnahmegeräte auf:

   .. code-block:: bash

      arecord -l

   Achte auf eine Zeile wie ``card 1: ... device 0``.

#. Nimm eine kurze Probe auf (ersetze ``1,0`` durch die gefundenen Zahlen):

   .. code-block:: bash

      arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

   * Beispiel: Wenn dein Gerät ``card 2, device 0`` ist, verwende:

   .. code-block:: bash

      arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

#. Spiele die Aufnahme ab, um sie zu überprüfen:

   .. important::

      Der Robot HAT-Lautsprecher muss aktiviert werden, bevor Audio abgespielt werden kann. Wenn du noch keinen PiDog-Beispielcode ausgeführt hast, aktiviere ihn zuerst:

      .. code-block:: bash

         robot_hat enable_speaker

      Dies muss nur einmal pro Systemstart durchgeführt werden. Das Ausführen eines beliebigen PiDog-Beispiels (das ``Pidog()`` initialisiert) erledigt dies automatisch.

   .. code-block:: bash

      aplay test.wav

#. Passe bei Bedarf die Mikrofonlautstärke an:

   .. code-block:: bash

      alsamixer

   * Drücke **F6**, um dein USB-Mikrofon auszuwählen.  
   * Suche den **Mic**- oder **Capture**-Kanal.  
   * Stelle sicher, dass das Mikrofon nicht stummgeschaltet ist (**[MM]** bedeutet stumm; drücke ``M``, um es zu aktivieren → es sollte **[OO]** anzeigen).  
   * Verwende die Pfeiltasten ↑ / ↓, um die Aufnahme-Lautstärke zu ändern.


.. _test_vosk:

2. Vosk testen
--------------------------

**Schritte zum Ausprobieren**:

#. Erstelle eine neue Datei:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_stt_vosk.py

#. Kopiere den Beispielcode hinein. Drücke ``Ctrl+X``, dann ``Y`` und ``Enter``, um zu speichern und zu beenden.

   .. code-block:: python

      from pidog.stt import Vosk

      vosk = Vosk(language="en-us")

      print(vosk.available_languages)

      while True:
          print("Say something")
          result = vosk.listen(stream=False)
          print(result)

#. Führe das Programm aus:

   .. code-block:: bash

      sudo python3 test_stt_vosk.py

#. Beim ersten Start mit einer neuen Sprache lädt Vosk das **Sprachmodell automatisch herunter** (standardmäßig die **kleine Version**).  
   Gleichzeitig wird die Liste der unterstützten Sprachen ausgegeben. Du wirst Folgendes sehen:

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   Das bedeutet:

   * Die Modelldatei (``vosk-model-small-en-us-0.15``) wurde heruntergeladen.  
   * Die Liste der unterstützten Sprachen wurde angezeigt.  
   * Das System hört nun zu — sprich in das Pidog-Mikrofon, und der erkannte Text wird im Terminal angezeigt.

   **Tipps**:

   * Halte das Mikrofon etwa 15–30 cm entfernt.  
   * Wähle ein Modell, das zu deiner Sprache und deinem Akzent passt.

**Streaming-Modus (optional)**

Du kannst die Sprache auch kontinuierlich streamen, um Teilergebnisse während des Sprechens zu sehen:

.. code-block:: python

   from pidog.stt import Vosk

   vosk = Vosk(language="en-us")

   while True:
       print("Say something")
       for result in vosk.listen(stream=True):
           if result["done"]:
               print(f"final:   {result['final']}")
           else:
               print(f"partial: {result['partial']}", end="\r", flush=True)

Fehlerbehebung
-----------------

* **No such file or directory (beim Ausführen von `arecord`)**

  Möglicherweise hast du die falsche Karten-/Gerätenummer verwendet.  
  Führe aus:

  .. code-block:: bash

     arecord -l

  und ersetze ``1,0`` durch die Nummern, die für dein USB-Mikrofon angezeigt werden.

* **Aufgenommene Datei hat keinen Ton**

  Öffne den Mixer und überprüfe die Mikrofonlautstärke:

  .. code-block:: bash

     alsamixer

  * Drücke **F6**, um dein USB-Mikrofon auszuwählen.  
  * Stelle sicher, dass **Mic/Capture** nicht stummgeschaltet ist (**[OO]** statt **[MM]**).  
  * Erhöhe die Lautstärke mit ↑.

* **Vosk erkennt keine Sprache**

  * Achte darauf, dass der **Sprachcode** zu deinem Modell passt (z. B. ``en-us`` für Englisch, ``zh-cn`` für Chinesisch).  
  * Halte das Mikrofon 15–30 cm entfernt und vermeide Hintergrundgeräusche.  
  * Sprich deutlich und langsam.

* **Hohe Latenz / langsame Erkennung**

  * Der automatische Download nutzt standardmäßig ein **kleines Modell** (schneller, aber weniger genau).  
  * Wenn es trotzdem langsam ist, schließe andere Programme, um CPU-Ressourcen freizugeben.
