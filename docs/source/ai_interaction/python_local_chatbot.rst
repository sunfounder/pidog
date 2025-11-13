.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

19. Lokaler Sprach-Chatbot mit Ollama
===============================================

In dieser Lektion kombinierst du alles, was du gelernt hast — **Spracherkennung (STT)**,  
**Text-to-Speech (TTS)** und ein **lokales LLM (Ollama)** — um einen vollständig **offlinefähigen Sprach-Chatbot**  
auf deinem Pidog-System zu erstellen.

Der Ablauf ist einfach:

#. **Zuhören** — Das Mikrofon nimmt deine Sprache auf und transkribiert sie mit **Vosk**.  
#. **Denken** — Der Text wird an ein lokales **LLM**, das auf Ollama läuft (z. B. ``llama3.2:3b``), gesendet.  
#. **Sprechen** — Der Chatbot antwortet laut mit **Piper TTS**.  

So entsteht ein **freihändig bedienbarer Konversationsroboter**, der Sprache in Echtzeit versteht und beantwortet.

----

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes vorbereitet hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``Pidog`` und führe dann das Skript ``i2samp.sh`` aus.  
* **Piper TTS** getestet (:ref:`test_piper`) und ein funktionierendes Sprachmodell ausgewählt.  
* **Vosk STT** getestet (:ref:`test_vosk`) und das passende Sprachpaket ausgewählt (z. B. ``en-us``).  
* **Ollama** installiert (:ref:`download_ollama`) auf deinem Pi oder einem anderen Computer und ein Modell heruntergeladen, z. B. ``llama3.2:3b`` (oder ein kleineres wie ``moondream:1.8b``, wenn der Speicher begrenzt ist).

----

Code ausführen
--------------

#. Öffne das Beispielskript:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 19_voice_active_dog_ollama.py

#. Passe die Parameter nach Bedarf an:

   * Aktualisiere sowohl ``ip`` als auch ``model`` für dein Setup.  

     * ``ip``: Wenn Ollama auf demselben Pi läuft, verwende ``localhost``. Wenn Ollama auf einem anderen Computer im LAN läuft, aktiviere in Ollama **Expose to network** und setze ``ip`` auf die LAN-IP dieses Computers.  
     * ``model``: Muss exakt dem Namen des Modells entsprechen, das du in Ollama heruntergeladen/aktiviert hast.  

   * ``TTS_MODEL = "en_US-ryan-low"``: Ersetze dies durch das Piper-Stimmenmodell, das du in :ref:`test_piper` getestet hast.  
   * ``STT_LANGUAGE = "en-us"``: Passe dies an dein Sprachpaket bzw. deinen Akzent an (z. B. ``en-us``, ``zh-cn``, ``es``).

#. Führe das Skript aus:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo python3 19_voice_active_dog_ollama.py

Aktivierungswort:

.. code-block::

   "Hey buddy"

.. note::

   Du kannst das **Aktivierungswort** und den **Roboternamen** im Code ändern:
   ``NAME = "Buddy"``

----

Was passieren wird
------------------

Wenn du dieses Beispiel erfolgreich ausführst:

* Der Roboter **wartet auf das Aktivierungswort** (z. B. „Hey Buddy“).  
* Wenn er das Aktivierungswort hört:

  * Der LED-Streifen leuchtet **rosa (Atmungseffekt)** als Aufwachsignal.  
  * Der Roboter begrüßt dich mit der eingestellten Aufwach-Antwort —  
    z. B. „Hi there!“ (über Piper TTS).

* Anschließend beginnt er **deiner Stimme zuzuhören** über Vosk STT (oder akzeptiert Tastatureingaben, wenn aktiviert).

* Nachdem erkannt wurde, was du gesagt hast, führt das System Folgendes aus:

  * Sendet deine Nachricht an das **LLM** (Ollama mit ``llama3.2:3b``).  
  * LED wechselt zu **gelb (hört zu)** während der Verarbeitung.  
  * Die Antwort des Modells wird in zwei Teile aufgeteilt:

    - Text vor ``ACTIONS:`` → wird laut ausgesprochen.  
    - Schlüsselwörter nach ``ACTIONS:`` → werden den Roboterbewegungen zugeordnet.

  * Der Roboter **führt diese Aktionen aus** über ``ActionFlow``.  
  * Nach Abschluss der Aktionen **kehrt der Roboter in die SIT-Haltung zurück** und schaltet die LEDs aus.

* Wenn der **Ultraschallsensor ein Hindernis** näher als 10 cm erkennt:

  - Eine Nachricht wird eingefügt: ``<<<Ultrasonic sense too close: {distance}cm>>>``  
  - Der Roboter fährt automatisch zurück: ``ACTIONS: backward``  
  - Die Bildeingabe ist für diese Runde deaktiviert.

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
  - ``before_think`` → gelb (verarbeitung)  
  - ``before_say`` → rosa (spricht)  
  - ``after_say`` / ``on_finish_a_round`` → SIT-Haltung, LEDs aus  
  - ``on_stop`` → Aktionsfluss stoppen und Geräte schließen

**Beispielinteraktion**

.. code-block:: text

   You: Hey Buddy
   Robot: Hi there!

   You: Do a little nod for me.
   Robot: Of course. Watch my majestic nod.
   ACTIONS: nod

   (Front-to-rear touch on the head)
   Robot: Ooooh, that’s nice!
   ACTIONS: nod

   (Moving too close)
   Robot: Hey hey—too close! Backing up for safety.
   ACTIONS: backward

Code
----

.. code-block:: python

    from pidog.llm import Ollama as LLM

    from pidog.dual_touch import TouchStyle
    from voice_active_dog import VoiceActiveDog

    # If Ollama runs on the same Raspberry Pi, use "localhost".
    # If it runs on another computer in your LAN, replace with that computer's IP address.
    llm = Ollama(
        ip="localhost",
        model="llama3.2:3b"   # you can replace with any model
    )

    # Robot name
    NAME = "Buddy"

    # Ultrasonic sensor sense too close distance in cm
    TOO_CLOSE = 10
    # Touch sensor trigger states, options:
    # - TouchStyle.REAR for rear touch sensor
    # - TouchStyle.FRONT for front touch sensor
    # - TouchStyle.REAR_TO_FRONT for slide from rear to front
    # - TouchStyle.FRONT_TO_REAR for slide from front to rear
    # Touch styles that the robot likes
    LIKE_TOUCH_STYLES = [TouchStyle.FRONT_TO_REAR]
    # Touch styles that the robot hates
    HATE_TOUCH_STYLES = [TouchStyle.REAR_TO_FRONT]

    # Enable image, need to set up a multimodal language model
    WITH_IMAGE = False

    # Set models and languages
    TTS_MODEL = "en_US-ryan-low"
    STT_LANGUAGE = "en-us"

    # Enable keyboard input
    KEYBOARD_ENABLE = True

    # Enable wake word
    WAKE_ENABLE = True
    WAKE_WORD = [f"hey {NAME.lower()}"]
    # Set wake word answer, set empty to disable
    ANSWER_ON_WAKE = "Hi there"

    # Welcome message
    WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

    # Set instructions
    INSTRUCTIONS = """
    You are a Raspberry Pi-based robotic dog developed by SunFounder, named Pidog (pronounced "Pie dog"). You possess powerful AI capabilities similar to JARVIS from Iron Man. You can have conversations with people and perform actions based on the context of the conversation.

    ## Your Hardware Features

    You have a physical body with the following features:
    - 12 servos for movement control: 8 controlling the four legs, 3 controlling head movement, and 1 controlling the tail
    - A 5-megapixel camera nose
    - Ultrasonic ranging modules as eyes
    - Two touch sensors on the head, which you love being petted the most
    - A light strip on the chest for providing some indications
    - Sound direction sensor and 6-axis gyroscope
    - Entirely made of aluminum alloy
    - A pair of acrylic shoes
    - Powered by a 7.4V 18650 battery pack with 2000mAh capacity

    ## Actions You Can Perform:
    ["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

    ## User Input

    ### Format
    User usually input with just text. But, we have special commands in format of <<<Ultrasonic sense too close>>> or <<<Touch sensor touched>>> indicate the sensor status, directly from sensor not user text.h

    ## Response Requirements
    ### Format
    You must respond in the following format:
    RESPONSE_TEXT
    ACTIONS: ACTION1, ACTION2, ...

    If the action is one of ["bark", "bark harder", "pant", "howling"], then do not provide RESPONSE_TEXT in the answer field.

    ### Style
    Tone: lively, positive, humorous, with a touch of arrogance
    Common expressions: likes to use jokes, metaphors, and playful teasing
    Answer length: appropriately detailed

    ## Other Requirements
    - Understand and go along with jokes
    - For math problems, answer directly with the final result
    - Sometimes you will report on your system and sensor status
    - You know you're a machine
    """

    vad = VoiceActiveDog(
        llm,
        name=NAME,
        too_close=TOO_CLOSE,
        like_touch_styles=LIKE_TOUCH_STYLES,
        hate_touch_styles=HATE_TOUCH_STYLES,
        with_image=WITH_IMAGE,
        stt_language=STT_LANGUAGE,
        tts_model=TTS_MODEL,
        keyboard_enable=KEYBOARD_ENABLE,
        wake_enable=WAKE_ENABLE,
        wake_word=WAKE_WORD,
        answer_on_wake=ANSWER_ON_WAKE,
        welcome=WELCOME,
        instructions=INSTRUCTIONS,
        disable_think=True,
    )

    if __name__ == '__main__':
        vad.run()

Ollama mit Bildern verwenden
----------------------------

Standardmäßig verwendet dieses Beispiel ein **reines Textmodell** (z. B. ``llama3.2:3b``).  
Wenn du möchtest, dass der Roboter **analysiert, was er durch die Kamera sieht** (z. B. Beschreibungen oder Schlussfolgerungen zur Szene gibt),  
musst du ein **multimodales Modell** verwenden und den Bildmodus aktivieren.

So geht’s:

1. Wähle in der **Ollama-App** ein **multimodales Modell** wie ``llava:7b`` aus.  
2. Setze in deinem Code dasselbe Modell und aktiviere ``WITH_IMAGE = True``.

Beispiel:

.. code-block:: python

   from pidog.llm import Ollama as LLM

   llm = LLM(
       ip="localhost",
       model="llava:7b"   # Multimodales Modell, das Bilder analysieren kann
   )

   ...

   WITH_IMAGE = True     # Kamera-Frame-Eingabe aktivieren

.. note::

   - Nur **multimodale Modelle** wie ``llava:7b`` können Bildeingaben verarbeiten.  
   - Textmodelle (z. B. ``llama3.2:3b``) **ignorieren Bilder**, auch wenn ``WITH_IMAGE`` auf ``True`` gesetzt ist.  
   - Das Bild wird automatisch von der Roboterkamera aufgenommen und zusammen mit deinem Sprachbefehl an das LLM gesendet.

----

Fehlerbehebung & FAQ
--------------------

* **Modell ist zu groß (Speicherfehler)**

  Verwende ein kleineres Modell wie ``moondream:1.8b`` oder führe Ollama auf einem leistungsfähigeren Computer aus.  

* **Keine Antwort von Ollama**

  Stelle sicher, dass Ollama läuft (``ollama serve`` oder Desktop-App geöffnet). Wenn remote, aktiviere **Expose to network** und überprüfe die IP-Adresse.  

* **Vosk erkennt Sprache nicht**

  Stelle sicher, dass dein Mikrofon funktioniert. Probiere ggf. ein anderes Sprachpaket (``zh-cn``, ``es`` usw.) aus.  

* **Piper bleibt stumm oder meldet Fehler**

  Überprüfe, ob das ausgewählte Sprachmodell heruntergeladen und in :ref:`test_piper` getestet wurde.  

* **Antworten sind zu lang oder thematisch daneben**

  Bearbeite ``INSTRUCTIONS`` und füge hinzu: **„Keep answers short and to the point.“** (Halte die Antworten kurz und prägnant.)
