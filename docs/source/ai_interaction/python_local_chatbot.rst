.. note::

    Ciao! Benvenuto nella Community di appassionati di Raspberry Pi, Arduino e ESP32 di SunFounder su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e supera le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anticipo agli annunci dei nuovi prodotti e scopri in anteprima le novità.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

19. Chatbot Vocale Locale con Ollama
=====================================

In questa lezione combinerai tutto ciò che hai imparato — **riconoscimento vocale (STT)**,  
**sintesi vocale (TTS)** e un **LLM locale (Ollama)** — per creare un **chatbot vocale completamente offline**  
che gira sul tuo sistema Pidog.

Il flusso di lavoro è semplice:

#. **Ascolta** — Il microfono cattura la tua voce e la trascrive con **Vosk**.  
#. **Pensa** — Il testo viene inviato a un **LLM locale** in esecuzione su Ollama (es. ``llama3.2:3b``).  
#. **Parla** — Il chatbot risponde ad alta voce utilizzando **Piper TTS**.  

Questo crea un **robot conversazionale a mani libere** capace di comprendere e rispondere in tempo reale.

----

Prima di Iniziare
-----------------

Assicurati di aver preparato quanto segue:

* :ref:`install_all_modules` — Installa i moduli ``robot-hat``, ``vilib``, ``Pidog`` e poi esegui lo script ``i2samp.sh``.  
* Testa **Piper TTS** (:ref:`test_piper`) e scegli un modello vocale funzionante.  
* Testa **Vosk STT** (:ref:`test_vosk`) e scegli il pacchetto lingua corretto (es. ``en-us``).  
* Installa **Ollama** (:ref:`download_ollama`) sul tuo Pi o su un altro computer e scarica un modello come ``llama3.2:3b`` (o uno più leggero come ``moondream:1.8b`` se la memoria è limitata).

----

Esegui il Codice
----------------

#. Apri lo script di esempio:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 19_voice_active_dog_ollama.py

#. Aggiorna i parametri secondo le tue esigenze:

   * Aggiorna ``ip`` e ``model`` in base alla tua configurazione.

     * ``ip``: Se Ollama è in esecuzione sullo **stesso Pi**, usa ``localhost``. Se Ollama è su un altro computer della LAN, abilita **Expose to network** in Ollama e imposta ``ip`` sull’indirizzo IP LAN di quel computer.  
     * ``model``: Deve corrispondere esattamente al nome del modello che hai scaricato/attivato in Ollama.  

   * ``TTS_MODEL = "en_US-ryan-low"``: Sostituisci con il modello vocale Piper che hai verificato in :ref:`test_piper`.  
   * ``STT_LANGUAGE = "en-us"``: Cambia in base al pacchetto lingua/adattamento per il tuo accento (es. ``en-us``, ``zh-cn``, ``es``).  

#. Esegui lo script:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo python3 19_voice_active_dog_ollama.py

Parola di attivazione:

.. code-block::

   "Hey buddy"

.. note::

   Puoi modificare la **parola di attivazione** e il **nome del robot** nel codice:
   ``NAME = "Buddy"``


----

Cosa Accadrà
-------------

Quando esegui correttamente questo esempio:

* Il robot **attende la parola di attivazione** (ad es. “Hey Buddy”).  
* Quando sente la parola di attivazione:

  * La striscia LED diventa **rosa (respiro)** come segnale di risveglio.  
  * Il robot ti saluta con la risposta di attivazione impostata —  
    ad es. “Ciao!” (tramite Piper TTS).

* Successivamente inizia ad **ascoltare la tua voce** tramite Vosk STT (o accetta l’input da tastiera se abilitato).  

* Dopo aver riconosciuto ciò che hai detto, il sistema:

  * Invia il tuo messaggio al **LLM** (Ollama con ``llama3.2:3b``).  
  * Il LED diventa **giallo (in ascolto)** durante l’elaborazione.  
  * La risposta del modello è divisa in due parti:

    - Testo prima di ``ACTIONS:`` → viene pronunciato ad alta voce.  
    - Parole chiave dopo ``ACTIONS:`` → mappate sui movimenti del robot.

  * Il robot **esegue queste azioni** tramite ``ActionFlow``.  
  * Al termine delle azioni, il robot **torna alla postura SEDUTO** e spegne i LED.

* Se il **sensore a ultrasuoni rileva un ostacolo** più vicino di 10 cm:

  - Viene iniettato un messaggio: ``<<<Ultrasonic sense too close: {distance}cm>>>``  
  - Il robot arretra automaticamente: ``ACTIONS: backward``  
  - L’input immagine è disabilitato per questo turno.

* Se il **sensore tattile viene attivato**:

  - Per un tocco di **gradimento** (es. FRONT_TO_REAR):

    - Inietta: ``<<<Touch style you like: FRONT_TO_REAR>>>``  
    - ``ACTIONS: nod`` (risposta positiva)

  - Per un tocco di **fastidio** (es. REAR_TO_FRONT):

    - Inietta: ``<<<Touch style you hate: REAR_TO_FRONT>>>``  
    - ``ACTIONS: backward`` (reazione di evitamento)

* **Ciclo di vita dei LED:**  

  - ``on_start`` → postura SEDUTO, LED spenti  
  - ``before_listen`` → ciano (pronto)  
  - ``before_think`` → giallo (elaborazione)  
  - ``before_say`` → rosa (parla)  
  - ``after_say`` / ``on_finish_a_round`` → postura SEDUTO, LED spenti  
  - ``on_stop`` → interrompe il flusso di azioni e chiude i dispositivi

**Esempio di interazione**

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

Codice
----------


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

Utilizzo di Ollama con Immagini
-------------------------------

Per impostazione predefinita, questo esempio utilizza un modello **solo testo** (es. ``llama3.2:3b``).  
Se vuoi che il robot **analizzi ciò che vede attraverso la fotocamera** (es. descrivere o ragionare sulla scena),  
devi usare un **modello multimodale** e abilitare la modalità immagine.

Per farlo:

1. Nell’app **Ollama**, seleziona un **modello multimodale** come ``llava:7b``.  
2. Nel tuo codice, imposta lo stesso modello e abilita ``WITH_IMAGE = True``.

Esempio:

.. code-block:: python

   from pidog.llm import Ollama as LLM

   llm = LLM(
       ip="localhost",
       model="llava:7b"   # modello multimodale che può analizzare immagini
   )

   ...

   WITH_IMAGE = True     # abilita l’input dalla fotocamera

.. note::

   - Solo i **modelli multimodali** come ``llava:7b`` possono elaborare input visivi.  
   - I modelli solo testo (es. ``llama3.2:3b``) **ignoreranno le immagini** anche se ``WITH_IMAGE`` è impostato su ``True``.  
   - L’immagine viene catturata automaticamente dalla fotocamera del robot e inviata al LLM insieme al comando vocale.

----

Risoluzione dei Problemi & FAQ
------------------------------

* **Il modello è troppo grande (errore di memoria)**

  Usa un modello più piccolo come ``moondream:1.8b`` oppure esegui Ollama su un computer più potente.

* **Nessuna risposta da Ollama**

  Assicurati che Ollama sia in esecuzione (``ollama serve`` o app desktop aperta).  
  Se remoto, abilita **Expose to network** e controlla l’indirizzo IP.

* **Vosk non riconosce la voce**

  Verifica che il microfono funzioni. Prova un altro pacchetto lingua (``zh-cn``, ``es`` ecc.) se necessario.

* **Piper silenzioso o con errori**

  Conferma che il modello vocale scelto sia stato scaricato e testato in :ref:`test_piper`.

* **Risposte troppo lunghe o fuori tema**

  Modifica ``INSTRUCTIONS`` aggiungendo: **“Mantieni le risposte brevi e concise.”**
