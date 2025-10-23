.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

17. Textgespräche mit Ollama
============================

In dieser Lektion lernst du, wie du **Ollama** verwendest – ein Tool zum lokalen Ausführen großer Sprach- und Vision-Modelle.  
Wir zeigen dir, wie du Ollama installierst, ein Modell herunterlädst und Pidog damit verbindest.

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``Pidog`` und führe dann das Skript ``i2samp.sh`` aus.

.. _download_ollama:

1. Ollama (LLM) installieren und Modell herunterladen
-----------------------------------------------------

Du kannst entscheiden, wo du **Ollama** installieren möchtest:

* Auf deinem Raspberry Pi (lokale Ausführung)  
* Oder auf einem anderen Computer (Mac/Windows/Linux) im **gleichen lokalen Netzwerk**

**Empfohlene Modelle vs. Hardware**

Du kannst jedes Modell verwenden, das auf |link_ollama_hub| verfügbar ist.  
Modelle gibt es in verschiedenen Größen (3B, 7B, 13B, 70B ...).  
Kleinere Modelle laufen schneller und benötigen weniger Speicher, während größere Modelle bessere Qualität bieten, aber leistungsstärkere Hardware erfordern.

Sieh dir die Tabelle unten an, um zu entscheiden, welche Modellgröße zu deinem Gerät passt.

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - Modellgröße
     - Mindest-RAM erforderlich
     - Empfohlene Hardware
   * - ~3B Parameter
     - 8GB (16GB besser)
     - Raspberry Pi 5 (16GB) oder Mittelklasse-PC/Mac
   * - ~7B Parameter
     - 16GB+
     - Pi 5 (16GB, gerade ausreichend) oder Mittelklasse-PC/Mac
   * - ~13B Parameter
     - 32GB+
     - Desktop-PC / Mac mit viel RAM
   * - 30B+ Parameter
     - 64GB+
     - Workstation / Server / GPU empfohlen
   * - 70B+ Parameter
     - 128GB+
     - High-End-Server mit mehreren GPUs

**Installation auf Raspberry Pi**

Wenn du Ollama direkt auf deinem Raspberry Pi ausführen möchtest:

* Verwende ein **64-Bit Raspberry Pi OS**  
* Dringend empfohlen: **Raspberry Pi 5 (16GB RAM)**

Führe die folgenden Befehle aus:

.. code-block:: bash

   # Ollama installieren
   curl -fsSL https://ollama.com/install.sh | sh

   # Ein leichtgewichtiges Modell herunterladen (gut zum Testen)
   ollama pull llama3.2:3b

   # Kurzer Testlauf (Tippe 'hi' und drücke Enter)
   ollama run llama3.2:3b

   # API bereitstellen (Standardport 11434)
   # Tipp: setze OLLAMA_HOST=0.0.0.0, um Zugriff aus dem LAN zu erlauben
   OLLAMA_HOST=0.0.0.0 ollama serve

**Installation auf Mac / Windows / Linux (Desktop-App)**

1. Lade Ollama von |link_ollama| herunter und installiere es.

   .. image:: img/llm_ollama_download.png

2. Öffne die Ollama-App, gehe zum **Model Selector** und verwende die Suchleiste, um ein Modell zu finden. Gib zum Beispiel ``llama3.2:3b`` ein (ein kleines und leichtgewichtiges Modell zum Starten).

   .. image:: img/llm_ollama_choose.png

3. Nachdem der Download abgeschlossen ist, gib etwas Einfaches wie „Hi“ in das Chatfenster ein. Ollama lädt das Modell beim ersten Gebrauch automatisch herunter.

   .. image:: img/llm_olama_llama_download.png

4. Gehe zu **Settings** → aktiviere **Expose Ollama to the network**. Dadurch kann dein Raspberry Pi über das LAN eine Verbindung herstellen.

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   Wenn du eine Fehlermeldung wie

   ``Error: model requires more system memory ...``

   erhältst, ist das Modell zu groß für dein Gerät.  
   Verwende ein **kleineres Modell** oder wechsle zu einem Computer mit mehr RAM.

2. Ollama testen
----------------

Sobald Ollama installiert ist und dein Modell bereitsteht, kannst du es mit einer minimalen Chat-Schleife schnell testen.

**Schritte**

#. Erstelle eine neue Datei:

   .. code-block:: bash

      cd ~/pidog/examples
      nano test_llm_ollama.py

#. Füge den folgenden Code ein und speichere (``Ctrl+X`` → ``Y`` → ``Enter``):

   .. code-block:: python
 
      from pidog.llm import Ollama
 
      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"
 
      # If Ollama runs on the same Raspberry Pi, use "localhost".
      # If it runs on another computer in your LAN, replace with that computer's IP address.
      llm = Ollama(
          ip="localhost",
          model="llama3.2:3b"   # you can replace with any model
      )
 
      # Basic configuration
      llm.set_max_messages(20)
      llm.set_instructions(INSTRUCTIONS)
      llm.set_welcome(WELCOME)
 
      print(WELCOME)
 
      while True:
          text = input(">>> ")
          if text.strip().lower() in {"exit", "quit"}:
              break
 
          # Response with streaming output
          response = llm.prompt(text, stream=True)
          for token in response:
              if token:
                  print(token, end="", flush=True)
          print("")

#. Führe das Programm aus:

   .. code-block:: bash

      python3 test_llm_ollama.py

#. Jetzt kannst du direkt über das Terminal mit Pidog chatten.

   * Du kannst **jedes Modell** verwenden, das auf |link_ollama_hub| verfügbar ist, aber kleinere Modelle (z. B. ``moondream:1.8b``, ``phi3:mini``) werden empfohlen, wenn du nur 8–16 GB RAM hast.  
   * Achte darauf, dass das Modell, das du im Code angibst, mit dem Modell übereinstimmt, das du bereits in Ollama heruntergeladen hast.  
   * Tippe ``exit`` oder ``quit``, um das Programm zu beenden.  
   * Wenn keine Verbindung hergestellt werden kann, stelle sicher, dass Ollama läuft und beide Geräte sich im selben LAN befinden, wenn du einen Remote-Host verwendest.

Fehlerbehebung
--------------

* **Ich erhalte eine Fehlermeldung wie: `model requires more system memory ...`.**

  * Das bedeutet, dass das Modell zu groß für dein Gerät ist.  
  * Verwende ein kleineres Modell wie ``moondream:1.8b`` oder ``granite3.2-vision:2b``.  
  * Oder wechsle zu einem Rechner mit mehr RAM und aktiviere die Netzwerkfreigabe für Ollama.

* **Der Code kann keine Verbindung zu Ollama herstellen (connection refused).**

  Überprüfe Folgendes:
  
  * Stelle sicher, dass Ollama läuft (``ollama serve`` oder die Desktop-App ist geöffnet).  
  * Wenn du einen Remote-Computer nutzt, aktiviere **Expose to network** in den Ollama-Einstellungen.  
  * Überprüfe, ob die im Code angegebene ``ip="..."`` mit der richtigen LAN-IP übereinstimmt.  
  * Vergewissere dich, dass beide Geräte im selben lokalen Netzwerk sind.
