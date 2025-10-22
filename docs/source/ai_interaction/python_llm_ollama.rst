.. note::

    Ciao! Benvenuto nella Community di appassionati di Raspberry Pi, Arduino e ESP32 di SunFounder su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e supera le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anticipo agli annunci dei nuovi prodotti e scopri in anteprima le novità.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

17. Conversazione Testuale con Ollama
=====================================

In questa lezione imparerai a utilizzare **Ollama**, uno strumento per eseguire localmente modelli linguistici e visivi di grandi dimensioni.  
Ti mostreremo come installare Ollama, scaricare un modello e collegare Pidog ad esso.

Prima di Iniziare
-----------------

Assicurati di aver completato:

* :ref:`install_all_modules` — Installa i moduli ``robot-hat``, ``vilib``, ``Pidog``, quindi esegui lo script ``i2samp.sh``.

.. _download_ollama:

1. Installa Ollama (LLM) e Scarica un Modello
---------------------------------------------

Puoi scegliere dove installare **Ollama**: 

* Sul tuo Raspberry Pi (esecuzione locale)  
* Oppure su un altro computer (Mac/Windows/Linux) nella **stessa rete locale**

**Modelli consigliati in base all’hardware**

Puoi scegliere qualsiasi modello disponibile su |link_ollama_hub|.  
I modelli sono disponibili in diverse dimensioni (3B, 7B, 13B, 70B...).  
I modelli più piccoli sono più veloci e richiedono meno memoria, mentre quelli più grandi offrono una qualità superiore ma necessitano di hardware più potente.

Consulta la tabella seguente per decidere quale dimensione di modello si adatta al tuo dispositivo:

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - Dimensione modello
     - RAM minima richiesta
     - Hardware consigliato
   * - ~3B parametri
     - 8GB (meglio 16GB)
     - Raspberry Pi 5 (16GB) o PC/Mac di fascia media
   * - ~7B parametri
     - 16GB+
     - Pi 5 (16GB, appena sufficiente) o PC/Mac di fascia media
   * - ~13B parametri
     - 32GB+
     - PC/Mac desktop con molta RAM
   * - 30B+ parametri
     - 64GB+
     - Workstation / Server / GPU consigliata
   * - 70B+ parametri
     - 128GB+
     - Server di fascia alta con più GPU

**Installazione su Raspberry Pi**

Se desideri eseguire Ollama direttamente sul tuo Raspberry Pi:

* Usa un **Raspberry Pi OS a 64 bit**  
* Fortemente consigliato: **Raspberry Pi 5 (16GB RAM)**

Esegui i seguenti comandi:

.. code-block:: bash

   # Installa Ollama
   curl -fsSL https://ollama.com/install.sh | sh

   # Scarica un modello leggero (ottimo per i test)
   ollama pull llama3.2:3b

   # Test veloce (digita 'hi' e premi Invio)
   ollama run llama3.2:3b

   # Avvia l’API (porta predefinita 11434)
   # Suggerimento: imposta OLLAMA_HOST=0.0.0.0 per consentire l’accesso dalla LAN
   OLLAMA_HOST=0.0.0.0 ollama serve

**Installazione su Mac / Windows / Linux (App Desktop)**

1. Scarica e installa Ollama da |link_ollama|  

   .. image:: img/llm_ollama_download.png

2. Apri l’app Ollama, vai su **Model Selector** e usa la barra di ricerca per trovare un modello. Ad esempio, digita ``llama3.2:3b`` (un modello piccolo e leggero per iniziare).  

   .. image:: img/llm_ollama_choose.png

3. Dopo il completamento del download, digita qualcosa di semplice come “Hi” nella finestra di chat. Ollama scaricherà automaticamente il modello al primo utilizzo.

   .. image:: img/llm_olama_llama_download.png

4. Vai su **Impostazioni** → abilita **Expose Ollama to the network**. Questo consente al tuo Raspberry Pi di connettersi tramite LAN.  

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   Se visualizzi un errore come:

   ``Error: model requires more system memory ...``

   Significa che il modello è troppo grande per la tua macchina.  
   Usa un **modello più piccolo** oppure passa a un computer con più RAM.

2. Testare Ollama
-----------------

Una volta installato Ollama e preparato il tuo modello, puoi testarlo rapidamente con un semplice ciclo di chat minimale.

**Passaggi**

#. Crea un nuovo file:

   .. code-block:: bash

      cd ~/pidog/examples
      nano test_llm_ollama.py

#. Incolla il seguente codice e salva (``Ctrl+X`` → ``Y`` → ``Invio``):

   .. code-block:: python

      from pidog.llm import Ollama

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      # Se Ollama gira sullo stesso Raspberry Pi, usa "localhost".
      # Se gira su un altro computer nella tua LAN, sostituisci con l’indirizzo IP di quel computer.
      llm = Ollama(
          ip="localhost",
          model="llama3.2:3b"   # puoi sostituirlo con qualsiasi modello
      )

      # Configurazione di base
      llm.set_max_messages(20)
      llm.set_instructions(INSTRUCTIONS)
      llm.set_welcome(WELCOME)

      print(WELCOME)

      while True:
          text = input(">>> ")
          if text.strip().lower() in {"exit", "quit"}:
              break

          # Risposta con output in streaming
          response = llm.prompt(text, stream=True)
          for token in response:
              if token:
                  print(token, end="", flush=True)
          print("")

#. Esegui il programma:

   .. code-block:: bash

      python3 test_llm_ollama.py

#. Ora puoi chattare con Pidog direttamente dal terminale.

   * Puoi scegliere **qualsiasi modello** disponibile su |link_ollama_hub|, ma i modelli più piccoli (es. ``moondream:1.8b``, ``phi3:mini``) sono consigliati se hai solo 8–16GB di RAM.  
   * Assicurati che il modello specificato nel codice corrisponda a quello che hai già scaricato con Ollama.  
   * Digita ``exit`` o ``quit`` per terminare il programma.  
   * Se non riesci a connetterti, assicurati che Ollama sia in esecuzione e che entrambi i dispositivi siano sulla stessa LAN se stai utilizzando un host remoto.

Risoluzione dei Problemi
------------------------

* **Ricevo un errore come: `model requires more system memory ...`.**

  * Ciò significa che il modello è troppo grande per il tuo dispositivo.  
  * Usa un modello più piccolo come ``moondream:1.8b`` o ``granite3.2-vision:2b``.  
  * Oppure utilizza una macchina con più RAM ed esponi Ollama alla rete.

* **Il codice non riesce a connettersi a Ollama (connessione rifiutata).** 

  Controlla quanto segue:
  
  * Assicurati che Ollama sia in esecuzione (``ollama serve`` o l’app desktop aperta).  
  * Se usi un computer remoto, abilita **Expose to network** nelle impostazioni di Ollama.  
  * Verifica che ``ip="..."`` nel tuo codice corrisponda all’indirizzo IP corretto della LAN.  
  * Controlla che entrambi i dispositivi siano sulla stessa rete locale.
