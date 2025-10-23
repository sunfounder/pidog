.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ai_voice_assistant_robot:

20. KI-Sprachassistent-Hund
===========================

In dieser Lektion verwandelst du deinen Pidog in einen **KI-gestützten Sprachassistenten-Hund** 🐶.  
Der Roboter kann auf deine Stimme reagieren, verstehen, was du sagst, mit Persönlichkeit antworten  
und seine „Gefühle“ durch Bewegungen, Gesten und LED-Lichteffekte ausdrücken.

Du wirst einen **voll interaktiven Robotergefährten** bauen mit:

* **LLM**: Large Language Model (z. B. OpenAI GPT oder Doubao) für natürliche Konversation.  
* **STT**: Speech-to-Text für Spracherkennung.  
* **TTS**: Text-to-Speech für ausdrucksstarke Sprachausgabe.  
* **Sensoren + Aktionen**: Ultraschallsensorik, Kamerasicht (optional), Berührungssensoren und eingebaute ausdrucksstarke Bewegungen.

----

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``pidog`` und führe dann das Skript ``i2samp.sh`` aus.
* :ref:`test_piper` — Überprüfe die unterstützten Sprachen von **Piper TTS**.  
* :ref:`test_vosk` — Überprüfe die unterstützten Sprachen von **Vosk STT**.  
* :ref:`py_online_llm` — Dieser Schritt ist **sehr wichtig**: Besorge dir deinen **OpenAI**- oder **Doubao**-API-Schlüssel oder den API-Schlüssel eines anderen unterstützten LLM.

Du solltest bereits haben:

* Ein funktionierendes **Mikrofon** und **Lautsprecher** an deinem Pidog.  
* Einen **gültigen API-Schlüssel**, der in ``secret.py`` gespeichert ist.  
* Eine stabile Netzwerkverbindung (eine **Kabelverbindung** wird für bessere Stabilität empfohlen).

----

Beispiel ausführen
------------------

Beide Sprachversionen befinden sich im selben Verzeichnis:

.. code-block:: bash

   cd ~/pidog/examples

**Englische Version** (OpenAI GPT, Anweisungen auf Englisch):

.. code-block:: bash

   sudo python3 20_voice_active_dog_gpt.py

* LLM: ``OpenAI GPT-4o-mini``  
* TTS: ``en_US-ryan-low`` (Piper)  
* STT: Vosk (``en-us``)

Aktivierungswort:

.. code-block::

   "Hey buddy"

---

**Chinesische Version** (Doubao, Anweisungen auf Chinesisch):

.. code-block:: bash

   sudo python3 20_voice_active_dog_doubao_cn.py

* LLM: ``Doubao-seed-1-6-250615``  
* TTS: ``zh_CN-huayan-x_low`` (Piper)  
* STT: Vosk (``cn``)

Aktivierungswort:

.. code-block::

   "你好 旺财"

.. note::

   Du kannst das **Aktivierungswort** und den **Roboternamen** im Code ändern:
   ``NAME = "Buddy"`` oder ``NAME = "旺财"``  
   ``WAKE_WORD = ["hey buddy"]`` oder ``WAKE_WORD = ["你好 旺财"]``

----

Was passieren wird
------------------

Wenn du dieses Beispiel erfolgreich ausführst:

* Der Roboter **wartet auf das Aktivierungswort** (z. B. „Hey Buddy“, „你好 旺财“).  
* Wenn er das Aktivierungswort hört:

  * Der LED-Streifen leuchtet **rosa (Atmungseffekt)** als Aufwachsignal.  
  * Der Roboter begrüßt dich mit der eingestellten Aufwach-Antwort —  
    z. B. „Hi there!“ (über Piper TTS).

* Anschließend beginnt er **deiner Stimme zuzuhören** über Vosk STT (oder akzeptiert Tastatureingaben, wenn aktiviert).

* Nachdem erkannt wurde, was du gesagt hast, führt das System Folgendes aus:

  * Nimmt ein **Kamerabild** auf (weil ``WITH_IMAGE = True``) und sendet deine Nachricht + Bild an das **LLM** (OpenAI ``gpt-4o-mini``).  
  * LED wechselt zu **gelb (hört/verarbeitet)**, während das Modell denkt.  
  * Die Antwort des Modells wird in zwei Teile aufgeteilt:

    - Text vor ``ACTIONS:`` → wird laut ausgesprochen.  
    - Schlüsselwörter nach ``ACTIONS:`` → werden den Roboterbewegungen zugeordnet.

  * Der Roboter **führt diese Aktionen aus** über ``ActionFlow``.  
  * Nach Abschluss der Aktionen **kehrt der Roboter in die SIT-Haltung zurück** und schaltet die LEDs aus.

* Wenn der **Ultraschallsensor ein Hindernis** näher als 10 cm erkennt:

  - Eine Nachricht wird eingefügt: ``<<<Ultrasonic sense too close: {distance}cm>>>``  
  - Der Roboter fährt automatisch zurück: ``ACTIONS: backward``  
  - **Bildeingabe ist** für diese Runde **deaktiviert**.

* Wenn der **Berührungssensor ausgelöst wird**:

  - Bei einer **LIKE**-Berührung (z. B. FRONT_TO_REAR):

    - Einfügen: ``<<<Touch style you like: FRONT_TO_REAR>>>``  
    - ``ACTIONS: nod`` (positive Reaktion)

  - Bei einer **HATE**-Berührung (z. B. REAR_TO_FRONT):

    - Einfügen: ``<<<Touch style you hate: REAR_TO_FRONT>>>``  
    - ``ACTIONS: backward`` (Abwehrreaktion)

* **LED-Lebenszyklus:**

  - ``on_start`` → SIT-Haltung, LEDs aus  
  - ``before_listen`` → cyan (bereit)  
  - ``before_think`` → gelb (verarbeiten)  
  - ``before_say`` → rosa (spricht)  
  - ``after_say`` / ``on_finish_a_round`` → SIT-Haltung, LEDs aus  
  - ``on_stop`` → Aktionsfluss stoppen und Geräte schließen

**Beispielinteraktion**

.. code-block:: text

   You: Hey Buddy
   Robot: Hi there!

   You: What do you see in front of you?
   Robot: I can see a notebook and a blue mug on the table.
   ACTIONS: think

   You: Do a little nod for me.
   Robot: Of course. Watch my majestic nod.
   ACTIONS: nod

   (Front-to-rear touch on the head)
   Robot: Ooooh, that’s nice!
   ACTIONS: nod

   (Moving too close)
   Robot: Hey hey—too close! Backing up for safety.
   ACTIONS: backward


----

Wechsel zu anderen LLMs oder TTS
-----------------------------------

Du kannst ganz einfach auf andere LLMs, TTS- oder STT-Sprachen umschalten — mit nur wenigen Codeänderungen:

* Unterstützte LLMs:

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Überprüfe die unterstützten Sprachen von **Piper TTS**.  
* :ref:`test_vosk` — Überprüfe die unterstützten Sprachen von **Vosk STT**.  

Um umzuschalten, ändere einfach den Initialisierungsteil im Code:

.. code-block:: python

  from pidog.llm import OpenAI as LLM

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # Modelle und Sprachen festlegen
  TTS_MODEL = "en_US-ryan-low"
  STT_LANGUAGE = "en-us"

----

Fehlerbehebung
--------------

* **Der Roboter reagiert nicht auf das Aktivierungswort**

  * Überprüfe, ob das Mikrofon funktioniert.  
  * Stelle sicher, dass ``WAKE_ENABLE = True`` ist.  
  * Passe das Aktivierungswort an deine Aussprache an.

* **Kein Ton aus dem Lautsprecher**
 
  * Überprüfe die TTS-Modellkonfiguration.  
  * Teste Piper oder Espeak manuell.  
  * Überprüfe Lautsprecheranschluss und Lautstärke.

* **API-Key-Fehler oder Zeitüberschreitung** 
 
  * Überprüfe deinen Schlüssel in ``secret.py``.  
  * Stelle sicher, dass eine Netzwerkverbindung besteht.  
  * Bestätige, dass das LLM unterstützt wird.

* **Ultraschallsensor wird ständig unerwartet ausgelöst.**  

  * Überprüfe Montagehöhe und Winkel des Sensors.  
  * Passe den ``TOO_CLOSE``-Distanzschwellenwert im Code an.
