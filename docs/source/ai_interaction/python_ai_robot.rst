.. note::

    Ciao! Benvenuto nella Community di appassionati di Raspberry Pi, Arduino e ESP32 di SunFounder su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e supera le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anticipo agli annunci dei nuovi prodotti e scopri in anteprima le novità.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ai_voice_assistant_robot:

20. Cane Assistente Vocale AI
=============================

Questa lezione trasforma il tuo Pidog in un **cane assistente vocale alimentato da IA** 🐶.  
Il robot può svegliarsi alla tua voce, capire ciò che dici, rispondere con personalità  
ed esprimere i suoi “sentimenti” attraverso movimenti, gesti ed effetti luminosi a LED.

Costruirai un **compagno robotico completamente interattivo** utilizzando:

* **LLM**: Large Language Model (ad es. OpenAI GPT o Doubao) per conversazioni naturali.  
* **STT**: Speech-to-Text per il riconoscimento vocale.  
* **TTS**: Text-to-Speech per risposte vocali espressive.  
* **Sensori + Azioni**: sensore a ultrasuoni, visione tramite fotocamera (opzionale), sensori tattili e movimenti espressivi integrati.

----

Prima di Iniziare
-----------------

Assicurati di aver completato:

* :ref:`install_all_modules` — Installa i moduli ``robot-hat``, ``vilib``, ``pidog`` e poi esegui lo script ``i2samp.sh``.  
* :ref:`test_piper` — Verifica le lingue supportate da **Piper TTS**.  
* :ref:`test_vosk` — Verifica le lingue supportate da **Vosk STT**.  
* :ref:`py_online_llm` — Questo passaggio è **molto importante**: ottieni la tua chiave API **OpenAI** o **Doubao**, o la chiave API per qualsiasi altro LLM supportato.

Dovresti già avere:

* Un **microfono** e un **altoparlante** funzionanti sul tuo Pidog.  
* Una **chiave API valida** salvata in ``secret.py``.  
* Una connessione di rete stabile (una **connessione cablata** è consigliata per una migliore stabilità).

----

Esegui l’Esempio
--------------------

Entrambe le versioni linguistiche si trovano nella stessa directory:

.. code-block:: bash

   cd ~/pidog/examples

**Versione inglese** (OpenAI GPT, istruzioni in inglese):

.. code-block:: bash

   sudo python3 20_voice_active_dog_gpt.py

* LLM: ``OpenAI GPT-4o-mini``  
* TTS: ``en_US-ryan-low`` (Piper)  
* STT: Vosk (``en-us``)

Parola di attivazione:

.. code-block::

   "Hey buddy"

---

**Versione cinese** (Doubao, istruzioni in cinese):

.. code-block:: bash

   sudo python3 20_voice_active_dog_doubao_cn.py

* LLM: ``Doubao-seed-1-6-250615``  
* TTS: ``zh_CN-huayan-x_low`` (Piper)  
* STT: Vosk (``cn``)

Parola di attivazione:

.. code-block::

   "你好 旺财"

.. note::

   Puoi modificare la **parola di attivazione** e il **nome del robot** nel codice:
   ``NAME = "Buddy"`` oppure ``NAME = "旺财"``  
   ``WAKE_WORD = ["hey buddy"]`` oppure ``WAKE_WORD = ["你好 旺财"]``

----

Cosa Accadrà
-------------

Quando esegui correttamente questo esempio:

* Il robot **attende la parola di attivazione** (ad es. “Hey Buddy”, “你好 旺财”).  
* Quando sente la parola di attivazione:

  * La striscia LED diventa **rosa (respiro)** come segnale di risveglio.  
  * Il robot ti saluta con la risposta di attivazione impostata —  
    ad es. “Ciao!” (tramite Piper TTS).

* Successivamente inizia ad **ascoltare la tua voce** tramite Vosk STT (o accetta l’input da tastiera se abilitato).  

* Dopo aver riconosciuto ciò che hai detto, il sistema:

  * Cattura un **frame della fotocamera** (perché ``WITH_IMAGE = True``) e invia il tuo messaggio + immagine al **LLM** (OpenAI ``gpt-4o-mini``).  
  * Il LED diventa **giallo (in ascolto / elaborazione)** mentre il modello pensa.  
  * La risposta del modello è divisa in due parti:

    - Testo prima di ``ACTIONS:`` → viene pronunciato ad alta voce.  
    - Parole chiave dopo ``ACTIONS:`` → mappate sui movimenti del robot.

  * Il robot **esegue queste azioni** tramite ``ActionFlow``.  
  * Al termine delle azioni, il robot **torna alla postura SEDUTO** e spegne i LED.

* Se il **sensore a ultrasuoni rileva un ostacolo** più vicino di 10 cm:

  - Viene iniettato un messaggio: ``<<<Ultrasonic sense too close: {distance}cm>>>``  
  - Il robot arretra automaticamente: ``ACTIONS: backward``  
  - **L’input immagine è disabilitato** per questo turno.

* Se il **sensore tattile viene attivato**:

  - Per un tocco di **gradimento** (ad es. FRONT_TO_REAR):

    - Inietta: ``<<<Touch style you like: FRONT_TO_REAR>>>``  
    - ``ACTIONS: nod`` (risposta positiva)

  - Per un tocco di **fastidio** (ad es. REAR_TO_FRONT):

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

Passare ad Altri LLM o TTS
----------------------------

Puoi passare facilmente ad altri LLM, TTS o lingue STT con poche modifiche:

* LLM supportati:

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Verifica le lingue supportate da **Piper TTS**.  
* :ref:`test_vosk` — Verifica le lingue supportate da **Vosk STT**.  

Per effettuare il cambio, modifica semplicemente la parte di inizializzazione nel codice:

.. code-block:: python

  from pidog.llm import OpenAI as LLM

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # Imposta modelli e lingue
  TTS_MODEL = "en_US-ryan-low"
  STT_LANGUAGE = "en-us"

----

Risoluzione dei Problemi
------------------------

* **Il robot non risponde alla parola di attivazione**  

  * Controlla che il microfono funzioni.  
  * Assicurati che ``WAKE_ENABLE = True``.  
  * Regola la parola di attivazione per adattarla alla tua pronuncia.

* **Nessun suono dall’altoparlante**

  * Assicurati che l’altoparlante del Robot HAT sia attivato. Se non hai ancora eseguito alcun codice di esempio PiDog, attivalo:

    .. code-block:: bash

       robot_hat enable_speaker

    È sufficiente farlo una volta per ogni avvio.

  * Verifica la configurazione del modello TTS.
  * Prova Piper o Espeak manualmente.
  * Controlla la connessione e il volume dell’altoparlante.

* **Errore nella chiave API o timeout** 
 
  * Controlla la tua chiave in ``secret.py``.  
  * Assicurati che la connessione di rete funzioni.  
  * Verifica che l’LLM sia supportato.

* **Il sensore a ultrasuoni si attiva inaspettatamente.**  

  * Controlla l’altezza e l’angolo d’installazione del sensore.  
  * Regola la soglia di distanza ``TOO_CLOSE`` nel codice.
