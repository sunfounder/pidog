.. note::

    Ciao! Benvenuto nella Community di appassionati di Raspberry Pi, Arduino e ESP32 di SunFounder su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e supera le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anticipo agli annunci dei nuovi prodotti e scopri in anteprima le novità.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

15. TTS con Piper e OpenAI
========================================================

Nella lezione precedente abbiamo provato due motori TTS integrati in Raspberry Pi (**Espeak** e **Pico2Wave**).  
Ora esploriamo due opzioni molto più potenti: **Piper** (offline, basato su reti neurali) e **OpenAI TTS** (online, basato su cloud).

* **Piper**: un motore TTS locale che funziona offline su Raspberry Pi.  
* **OpenAI TTS**: un servizio online che fornisce voci molto naturali e simili a quelle umane.

Prima di iniziare
----------------------

Assicurati di aver completato:

* :ref:`install_all_modules` — Installa i moduli ``robot-hat``, ``vilib``, ``pidog`` e poi esegui lo script ``i2samp.sh``.

.. _test_piper:

Testare Piper
------------------

**Passaggi per provarlo**:

#. Crea un nuovo file:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_piper.py

#. Copia il codice di esempio qui sotto nel file. Premi ``Ctrl+X``, poi ``Y`` e infine ``Enter`` per salvare ed uscire.

   .. code-block:: python

       from pidog.tts import Piper

       tts = Piper()

       # Elenca le lingue supportate
       print(tts.available_countrys())

       # Elenca i modelli per l'inglese (en_us)
       print(tts.available_models('en_us'))

       # Imposta un modello vocale (download automatico se non presente)
       tts.set_model("en_US-amy-low")

       # Pronuncia un messaggio
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()``: mostra le lingue supportate.  
   * ``available_models()``: elenca i modelli disponibili per una lingua.  
   * ``set_model()``: imposta il modello vocale (lo scarica automaticamente se mancante).  
   * ``say()``: converte il testo in voce e lo riproduce.

#. Esegui il programma:

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. La prima volta che lo esegui, il modello vocale selezionato verrà scaricato automaticamente.

   * Dovresti sentire il Pidog dire: ``Hello! I'm Piper TTS.``  
   * Puoi cambiare modello linguistico chiamando ``set_model()`` con un nome diverso.


Testare OpenAI TTS
-------------------------------

**Ottieni e salva la tua Chiave API**

#. Vai a |link_openai_platform| ed effettua il login. Nella pagina **API keys**, clicca su **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Compila i dettagli (Owner, Name, Project e permessi se necessario), poi clicca su **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Una volta creata la chiave, copiala subito — non sarà più visibile. Se la perdi, dovrai generarne una nuova.

   .. image:: img/llm_openai_copy.png

#. Nella cartella del tuo progetto (per esempio: ``/pidog/examples``), crea un file chiamato ``secret.py``:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Incolla la chiave nel file:

   .. code-block:: python

       # secret.py
       # Conserva qui le chiavi segrete. Non aggiungere mai questo file a Git.
       OPENAI_API_KEY = "sk-xxx"

**Scrivi ed esegui un programma di test**

#. Crea un nuovo file:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano test_tts_openai.py

#. Copia il codice di esempio qui sotto. Premi ``Ctrl+X``, poi ``Y`` e infine ``Enter`` per salvare ed uscire.

   .. code-block:: python

      from pidog.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # oppure usa la versione try/except mostrata sopra

      # Inizializza OpenAI TTS
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # modello TTS a bassa latenza
      tts.set_voice('alloy')            # scegli una voce

      # Saluto veloce (verifica funzionamento)
      tts.say("Hello! I'm OpenAI TTS.")

#. Esegui il programma:

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. Dovresti sentire il Pidog dire:
  

   ``Hello! I'm OpenAI TTS.``

----

Risoluzione dei problemi
--------------------------------

* **No module named 'secret'**

  Questo significa che ``secret.py`` non si trova nella stessa cartella del tuo file Python.  
  Sposta ``secret.py`` nella stessa directory in cui esegui lo script, ad esempio:

  .. code-block:: bash

     ls ~/pidog/examples
     # Assicurati di vedere sia: secret.py che il tuo file .py

* **OpenAI: Invalid API key / 401**

  * Controlla di aver incollato la chiave completa (inizia con ``sk-``) e che non ci siano spazi o ritorni a capo extra.  
  * Assicurati che il codice la importi correttamente:

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Conferma che la tua Raspberry Pi abbia accesso a Internet (prova con ``ping api.openai.com``).

* **OpenAI: Quota exceeded / billing error**

  * Potresti dover aggiungere un metodo di pagamento o aumentare la quota nel pannello OpenAI.  
  * Riprova dopo aver risolto il problema di account/fatturazione.

* **Piper: tts.say() viene eseguito ma non si sente nulla**

  * Assicurati che un modello vocale sia effettivamente presente:

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * Controlla che il nome del modello nel codice sia scritto correttamente:

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Verifica il dispositivo di uscita audio/volume sulla tua Raspberry Pi (``alsamixer``) e che gli altoparlanti siano collegati e accesi.

* **Errori ALSA / dispositivi audio (es. “Audio device busy” o “No such file or directory”)**

  * Chiudi altri programmi che stanno usando l’audio.  
  * Riavvia la Raspberry Pi se il dispositivo rimane occupato.  
  * Seleziona il dispositivo corretto nelle impostazioni audio di Raspberry Pi OS (HDMI o jack cuffie).

* **Permission denied durante l’esecuzione di Python**

  * Prova ad eseguire con ``sudo`` se l’ambiente lo richiede:

    .. code-block:: bash

       sudo python3 test_tts_piper.py



Confronto tra motori TTS
-------------------------

.. list-table:: Confronto funzionalità: Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - Voce
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - Dove gira
     - Integrato su Raspberry Pi (offline)
     - Integrato su Raspberry Pi (offline)
     - Raspberry Pi / PC (offline, richiede modello)
     - Cloud (online, richiede API key)
   * - Qualità vocale
     - Robotica
     - Più naturale di Espeak
     - Naturale (neural TTS)
     - Molto naturale / simile a voce umana
   * - Controlli
     - Velocità, tono, volume
     - Controlli limitati
     - Scelta tra diverse voci/modelli
     - Scelta di modelli e voci
   * - Lingue
     - Molte (qualità variabile)
     - Set limitato
     - Molte lingue e voci disponibili
     - Migliore in inglese (altre lingue variano)
   * - Latenza / velocità
     - Molto veloce
     - Veloce
     - Tempo reale su Pi 4/5 con modelli “low”
     - Dipende dalla rete (solitamente bassa)
   * - Configurazione
     - Minima
     - Minima
     - Download dei modelli ``.onnx`` + ``.onnx.json``
     - Creazione API key, installazione client
   * - Migliore per
     - Test rapidi, prompt semplici
     - Voce offline leggermente migliore
     - Progetti locali con buona qualità
     - Massima qualità, opzioni vocali avanzate
