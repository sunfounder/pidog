.. note::

    Ciao! Benvenuto nella Community di appassionati di Raspberry Pi, Arduino e ESP32 di SunFounder su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e supera le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anticipo agli annunci dei nuovi prodotti e scopri in anteprima le novità.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_online_llm:

18. Connessione a LLM Online
============================

In questa lezione impareremo come connettere il tuo Pidog (o Raspberry Pi) a diversi **modelli linguistici di grandi dimensioni (LLM) online**.  
Ogni provider richiede una chiave API e offre diversi modelli tra cui scegliere.

Vedremo come:

* Creare e salvare in sicurezza le chiavi API.  
* Scegliere un modello adatto alle tue esigenze.  
* Eseguire il codice di esempio per chattare con i modelli.

Procediamo passo dopo passo per ogni provider.

----

Prima di Iniziare
-----------------

Assicurati di aver completato:

* :ref:`install_all_modules` — Installa i moduli ``robot-hat``, ``vilib``, ``pidog`` e poi esegui lo script ``i2samp.sh``.

OpenAI
------

OpenAI fornisce modelli potenti come **GPT-4o** e **GPT-4.1**, utilizzabili sia per testo che per visione.  

Ecco come configurarlo:

**Ottieni e Salva la tua Chiave API**

#. Vai su |link_openai_platform| e accedi. Nella pagina **API keys**, fai clic su **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Compila i dettagli (Owner, Nome, Progetto e autorizzazioni se necessarie), poi clicca su **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Una volta creata la chiave, copiala subito — non potrai più visualizzarla. Se la perdi, dovrai generarne una nuova.

   .. image:: img/llm_openai_copy.png

#. Nella cartella del tuo progetto (esempio: ``/pidog/examples``), crea un file chiamato ``secret.py``:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Incolla la chiave nel file come segue:

   .. code-block:: python

       # secret.py
       # Conserva qui le chiavi segrete. Non aggiungere mai questo file a Git.
       OPENAI_API_KEY = "sk-xxx"

**Abilita la fatturazione e controlla i modelli**

#. Prima di utilizzare la chiave, vai alla pagina **Billing** del tuo account OpenAI, aggiungi un metodo di pagamento e ricarica un piccolo importo di credito.

   .. image:: img/llm_openai_billing.png

#. Poi vai alla pagina **Limits** per controllare quali modelli sono disponibili per il tuo account e copia l’ID esatto del modello da usare nel codice.

   .. image:: img/llm_openai_models.png

**Test con codice di esempio**

#. Apri il file di esempio:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Sostituisci il contenuto con il codice seguente, aggiornando ``model="xxx"`` con il modello che vuoi utilizzare (per esempio, ``gpt-4o``):

   .. code-block:: python

       from pidog.llm import OpenAI
       from secret import OPENAI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )

   Salva ed esci (``Ctrl+X``, poi ``Y``, poi ``Invio``).

#. Infine, esegui il test:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py
   

----

Gemini
------------------

Gemini è la famiglia di modelli di intelligenza artificiale di Google.  
È veloce e ottimo per compiti generali.

**Ottieni e Salva la tua Chiave API**

#. Accedi a |link_google_ai|, quindi vai alla pagina **API Keys**.

   .. image:: img/llm_gemini_get.png

#. Clicca sul pulsante **Create API key** in alto a destra.

   .. image:: img/llm_gemini_create.png

#. Puoi creare una chiave per un progetto esistente oppure per uno nuovo.

   .. image:: img/llm_gemini_choose.png

#. Copia la chiave API generata.

   .. image:: img/llm_gemini_copy.png

#. Nella cartella del tuo progetto:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Incolla la chiave:

   .. code-block:: python

        # secret.py
        # Conserva qui le chiavi segrete. Non aggiungere mai questo file a Git.
        GEMINI_API_KEY = "AIxxx"

**Controlla i modelli disponibili**

Vai alla pagina ufficiale |link_gemini_model|, dove troverai l’elenco dei modelli, i rispettivi ID API esatti e per quali casi d’uso ciascuno è ottimizzato.

   .. image:: img/llm_gemini_model.png

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Sostituisci il contenuto con il codice seguente e aggiorna ``model="xxx"`` con il modello che vuoi usare (per esempio, ``gemini-2.5-flash``):

   .. code-block:: python

       from pidog.llm import Gemini
       from secret import GEMINI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Gemini(
           api_key=GEMINI_API_KEY,
           model="gemini-2.5-flash",
       )

#. Salva ed esegui:

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Qwen
------------------

Qwen è una famiglia di modelli linguistici e multimodali di grandi dimensioni fornita da Alibaba Cloud.  
Questi modelli supportano la generazione di testo, il ragionamento e la comprensione multimodale (come l’analisi delle immagini).

**Ottieni una Chiave API**

Per utilizzare i modelli Qwen, hai bisogno di una **Chiave API**.  
La maggior parte degli utenti internazionali dovrebbe utilizzare la console **DashScope International (Model Studio)**.  
Gli utenti della Cina continentale possono invece usare la console **Bailian (百炼)**.

* **Per Utenti Internazionali**

  #. Vai alla pagina ufficiale |link_qwen_inter| su **Alibaba Cloud**.  
  #. Accedi o crea un account **Alibaba Cloud**.  
  #. Vai su **Model Studio** (scegli la regione Singapore o Pechino).  

     * Se appare un messaggio “Activate Now” nella parte superiore della pagina, cliccalo per attivare Model Studio e ricevere la quota gratuita (solo Singapore).  
     * L’attivazione è gratuita — si paga solo dopo aver esaurito la quota gratuita.  
     * Se non compare alcun messaggio, significa che il servizio è già attivo.

  #. Vai alla pagina **Key Management**. Nella scheda **API Key**, clicca su **Create API Key**.  
  #. Dopo la creazione, copia la tua API Key e conservala in un luogo sicuro.

    .. image:: img/llm_qwen_api_key.png
        :width: 800

  .. note::
     Gli utenti di Hong Kong, Macao e Taiwan devono selezionare l’opzione **International (Model Studio)**.

* **Per Utenti della Cina Continentale**

  Se ti trovi nella Cina continentale, puoi usare la console **Alibaba Cloud Bailian (百炼)**:

  #. Accedi a |link_aliyun| (console Bailian) e completa la verifica dell’account.  
  #. Seleziona **Create API Key**. Se appare un messaggio che i servizi modello non sono attivati, clicca su **Activate**, accetta i termini e ottieni la quota gratuita. Dopo l’attivazione, il pulsante **Create API Key** sarà abilitato.

     .. image:: img/llm_qwen_aliyun_create.png

  #. Clicca nuovamente su **Create API Key**, verifica l’account e poi clicca su **Confirm**.

     .. image:: img/llm_qwen_aliyun_confirm.png

  #. Una volta creata, copia la tua Chiave API.

     .. image:: img/llm_qwen_aliyun_copy.png

**Salva la tua Chiave API**

#. Nella cartella del tuo progetto:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Incolla la chiave:

   .. code-block:: python

        # secret.py
        # Conserva qui le chiavi segrete. Non aggiungere mai questo file a Git.
        
        QWEN_API_KEY = "sk-xxx"

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Sostituisci il contenuto con il codice seguente e aggiorna ``model="xxx"`` con il modello che desideri (ad esempio, ``qwen-plus``):

   .. code-block:: python

      from pidog.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )

#. Esegui con:


   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

Grok (xAI)
------------------
Grok è l’AI conversazionale di xAI, creata dal team di Elon Musk. Puoi connetterti ad essa tramite l’API di xAI.

**Ottieni e Salva la tua Chiave API**

#. Registrati qui: |link_grok_ai|. Aggiungi prima del credito al tuo account — altrimenti l’API non funzionerà.

#. Vai alla pagina **API Keys** e clicca su **Create API key**.

   .. image:: img/llm_grok_create.png

#. Inserisci un nome per la chiave e clicca su **Create API key**.

   .. image:: img/llm_grok_name.png

#. Copia la chiave generata e conservala in un luogo sicuro.

   .. image:: img/llm_grok_copy.png

#. Nella cartella del tuo progetto:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Incolla la chiave:

   .. code-block:: python

        # secret.py
        # Conserva qui le chiavi segrete. Non aggiungere mai questo file a Git.
        
        GROK_API_KEY = "xai-xxx"

**Controlla i modelli disponibili**

Vai alla pagina **Models** nella console xAI. Qui puoi vedere tutti i modelli disponibili per il tuo team, insieme ai rispettivi ID API — utilizza questi ID nel tuo codice.

   .. image:: img/llm_grok_model.png

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Sostituisci il contenuto con il codice seguente e aggiorna ``model="xxx"`` con il modello che desideri (ad esempio, ``grok-4-latest``):

   .. code-block:: python

       from pidog.llm import Grok
       from secret import GROK_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. Esegui con:

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

DeepSeek
------------------

DeepSeek è un provider cinese di LLM che offre modelli potenti a costi contenuti.

**Ottieni e Salva la tua Chiave API**

#. Accedi a |link_deepseek|.

#. Nel menu in alto a destra, seleziona **API Keys → Create API Key**.

   .. image:: img/llm_deepseek_create.png

#. Inserisci un nome, clicca su **Create** e poi copia la chiave.

   .. image:: img/llm_deepseek_copy.png

#. Nella cartella del tuo progetto:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Aggiungi la chiave:

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**Abilita la fatturazione**

Dovrai ricaricare il tuo account prima dell’utilizzo. Inizia con un piccolo importo (ad esempio ¥10 RMB).

   .. image:: img/llm_deepseek_chognzhi.png

**Modelli disponibili**

Alla data (2025-09-12), DeepSeek offre:

* ``deepseek-chat``  
* ``deepseek-reasoner``

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Sostituisci il contenuto con il codice seguente e aggiorna ``model="xxx"`` con il modello desiderato (ad esempio, ``deepseek-chat``):

   .. code-block:: python

       from pidog.llm import Deepseek
       from secret import DEEPSEEK_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Deepseek(
           api_key=DEEPSEEK_API_KEY,
           model="deepseek-chat",
           max_messages=20,
       )

#. Esegui:


   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

Doubao
------------------
Doubao è la piattaforma di modelli AI di ByteDance (Volcengine Ark).

**Ottieni e Salva la tua Chiave API**

#. Accedi a |link_doubao|.

#. Nel menu a sinistra, scorri fino a **API Key Management → Create API Key**.

   .. image:: img/llm_doubao_create.png

#. Scegli un nome e clicca su **Create**.

   .. image:: img/llm_doubao_name.png

#. Clicca sull’icona **Show API Key** e copia la chiave.

   .. image:: img/llm_doubao_copy.png

#. Nella cartella del tuo progetto:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Aggiungi la chiave:

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**Scegli un modello**

#. Vai al marketplace dei modelli e seleziona un modello.

   .. image:: img/llm_doubao_model_select.png

#. Ad esempio, scegli **Doubao-seed-1.6**, quindi clicca su **API 接入**.

   .. image:: img/llm_doubao_model.png

#. Seleziona la tua chiave API e clicca su **Use API**.

   .. image:: img/llm_doubao_use_api.png

#. Clicca su **Enable Model**.

   .. image:: img/llm_doubao_kaitong.png

#. Passa con il mouse sopra l’ID del modello per copiarlo.

   .. image:: img/llm_doubao_copy_id.png

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Sostituisci il contenuto con il codice seguente e aggiorna ``model="xxx"`` con il modello che vuoi usare (ad esempio, ``doubao-seed-1-6-250615``):

   .. code-block:: python

       from pidog.llm import Doubao
       from secret import DOUBAO_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. Esegui con:

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Generale
--------------

Questo progetto supporta la connessione a più piattaforme LLM attraverso un’interfaccia unificata.  
Supporta nativamente:

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)  
* **Gemini** (Google AI Studio / Vertex AI)  
* **Grok** (xAI)  
* **DeepSeek**  
* **Qwen (通义千问)**  
* **Doubao (豆包)**

Inoltre, puoi connetterti a **qualsiasi altro servizio LLM compatibile con il formato API di OpenAI**.  
Per queste piattaforme, dovrai ottenere manualmente la tua **API Key** e il corretto **base_url**.

**Ottieni e Salva la tua Chiave API**

#. Ottieni una **API Key** dalla piattaforma che desideri utilizzare (consulta la console ufficiale di ciascun provider).

#. Nella cartella del tuo progetto, crea un nuovo file:

   .. code-block:: bash

      cd ~/pidog/examples
      nano secret.py

#. Aggiungi la chiave in ``secret.py``:

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   Mantieni privata la tua API Key. Non caricare mai ``secret.py`` in repository pubblici.

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 18.online_llm_test.py

#. Sostituisci il contenuto del file Python con l’esempio seguente, e compila i campi ``base_url`` e ``model`` con i dati corretti per il tuo provider:

   .. note::

      Riguardo ``base_url``:  
      Supportiamo il formato **OpenAI API** e qualsiasi API che sia **compatibile** con esso.  
      Ogni provider ha un proprio ``base_url`` — consulta la documentazione ufficiale.

   .. code-block:: python

      from pidog.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # inserisci il base_url del tuo provider
          api_key=API_KEY,
          model="your-model-name-here",           # scegli un modello dal tuo provider
      )

#. Esegui il programma:

   .. code-block:: bash

      python3 18.online_llm_test.py



