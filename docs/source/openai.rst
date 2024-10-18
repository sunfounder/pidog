
Interazione AI con GPT-4O
================================================

Nei progetti precedenti, abbiamo utilizzato la programmazione per dirigere PiDog in compiti predeterminati, il che potrebbe sembrare un po' monotono. Questo progetto introduce un entusiasmante passo avanti verso un'interazione dinamica. Attenzione a non cercare di ingannare il nostro cane robotico: ora è dotato di una comprensione ben superiore rispetto a prima!

Questa iniziativa illustra tutti i passaggi tecnici necessari per integrare GPT-4O nel tuo sistema, inclusa la configurazione degli ambienti virtuali necessari, l'installazione delle librerie fondamentali e la configurazione delle chiavi API e degli ID degli assistenti.

.. note::

   Questo progetto richiede l'uso di |link_openai_platform|, e l'accesso a OpenAI è a pagamento. Inoltre, l'API di OpenAI è fatturata separatamente rispetto a ChatGPT, con il proprio piano tariffario disponibile su https://openai.com/api/pricing/.

   Pertanto, è necessario decidere se proseguire con questo progetto oppure assicurarsi di avere i fondi necessari per l'API di OpenAI.

Che tu abbia un microfono per comunicare direttamente o preferisca digitare in una finestra di comando, le risposte di PiDog alimentate da GPT-4O ti sorprenderanno!

Iniziamo questo progetto e sblocchiamo un nuovo livello di interazione con PiDog!


.. raw:: html

   <video controls style = "max-width:90%">
     <source src="_static/video/chatgpt4o.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>


1. Installazione dei pacchetti e delle dipendenze necessarie
--------------------------------------------------------------
.. note::

   È necessario installare prima i moduli necessari per PiCar-X. Per ulteriori dettagli, fare riferimento a: :ref:`install_all_modules`.
   

In questa sezione, creeremo e attiveremo un ambiente virtuale, installando al suo interno i pacchetti e le dipendenze necessarie. Questo garantisce che i pacchetti installati non interferiscano con il resto del sistema, mantenendo l'isolamento delle dipendenze del progetto e prevenendo conflitti con altri progetti o pacchetti di sistema.

#. Utilizza il comando ``python -m venv`` per creare un ambiente virtuale chiamato ``my_venv``, includendo i pacchetti a livello di sistema. L'opzione ``--system-site-packages`` consente all'ambiente virtuale di accedere ai pacchetti installati a livello di sistema, utile quando sono necessarie librerie a livello di sistema.

   .. code-block:: shell

      python -m venv --system-site-packages my_venv

#. Passa alla directory ``my_venv`` e attiva l'ambiente virtuale utilizzando il comando ``source bin/activate``. Il prompt del comando cambierà per indicare che l'ambiente virtuale è attivo.

   .. code-block:: shell

      cd my_venv
      source bin/activate

#. Ora, installa i pacchetti Python necessari all'interno dell'ambiente virtuale attivato. Questi pacchetti saranno isolati all'interno dell'ambiente virtuale e non influenzeranno gli altri pacchetti di sistema.

   .. code-block:: shell

      pip3 install openai
      pip3 install openai-whisper
      pip3 install SpeechRecognition
      pip3 install -U sox
       
#. Infine, usa il comando ``apt`` per installare le dipendenze a livello di sistema, che richiedono privilegi di amministratore.

   .. code-block:: shell

      sudo apt install python3-pyaudio
      sudo apt install sox


2. Ottenere la Chiave API e l'ID dell'Assistente
----------------------------------------------------

**Ottieni la Chiave API**

#. Visita |link_openai_platform| e clicca sul pulsante **Create new secret key** in alto a destra.

   .. image:: img/apt_create_api_key.png
      :width: 700
      :align: center

#. Seleziona il Proprietario, Nome, Progetto e i permessi necessari, quindi clicca su **Create secret key**.

   .. image:: img/apt_create_api_key2.png
      :width: 700
      :align: center

#. Una volta generata, salva questa chiave segreta in un luogo sicuro e facilmente accessibile. Per motivi di sicurezza, non potrai visualizzarla nuovamente tramite il tuo account OpenAI. Se perdi questa chiave segreta, dovrai generarne una nuova.

   .. image:: img/apt_create_api_key_copy.png
      :width: 700
      :align: center

**Ottieni l'ID dell'Assistente**

#. Successivamente, clicca su **Assistants**, poi clicca su **Create**, assicurandoti di essere nella pagina del **Dashboard**.

   .. image:: img/apt_create_assistant.png
      :width: 700
      :align: center

#. Sposta il cursore qui per copiare l'**ID dell'assistente**, quindi incollalo in una casella di testo o altrove. Questo è l'identificatore univoco per questo assistente.

   .. image:: img/apt_create_assistant_id.png
      :width: 700
      :align: center

#. Assegna un nome casuale, quindi copia il contenuto seguente nel campo **Instructions** per descrivere il tuo assistente.

   .. image:: img/apt_create_assistant_instructions.png
      :width: 700
      :align: center

   .. code-block::

      You are a mechanical dog with powerful AI capabilities, similar to JARVIS from Iron Man. Your name is Pidog. You can have conversations with people and perform actions based on the context of the conversation.

      ## actions you can do:
      ["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag_tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

      ## Response Format:
      {"actions": ["wag_tail"], "answer": "Hello, I am Pidog."}

      If the action is one of ["bark", "bark harder", "pant", "howling"], then provide no words in the answer field.

      ## Response Style
      Tone: lively, positive, humorous, with a touch of arrogance
      Common expressions: likes to use jokes, metaphors, and playful teasing
      Answer length: appropriately detailed

      ## Other
      a. Understand and go along with jokes.
      b. For math problems, answer directly with the final.
      c. Sometimes you will report on your system and sensor status.
      d. You know you're a machine.

#. PiDog è dotato di un modulo fotocamera che puoi attivare per catturare immagini e caricarle su GPT utilizzando il nostro codice di esempio. Pertanto, ti consigliamo di scegliere GPT-4O, che possiede capacità di analisi delle immagini. Naturalmente, puoi anche optare per gpt-3.5-turbo o altri modelli.

   .. image:: img/apt_create_assistant_model.png
      :width: 700
      :align: center

#. Ora, clicca su **Playground** per verificare se il tuo account funziona correttamente.

   .. image:: img/apt_playground.png

#. Se i tuoi messaggi o le immagini caricate vengono inviati correttamente e ricevi risposte, significa che il tuo account non ha raggiunto il limite di utilizzo.

   .. image:: img/apt_playground_40.png
      :width: 700
      :align: center

#. Se incontri un messaggio di errore dopo aver inserito informazioni, potresti aver raggiunto il limite di utilizzo. Controlla il tuo pannello di utilizzo o le impostazioni di fatturazione.

   .. image:: img/apt_playground_40mini_3.5.png
      :width: 700
      :align: center

3. Inserimento della Chiave API e dell'ID dell'Assistente
-----------------------------------------------------------------

#. Utilizza il comando seguente per aprire il file ``keys.py``.

   .. code-block:: shell

      nano ~/pidog/gpt_examples/keys.py

#. Inserisci la Chiave API e l'ID dell'Assistente che hai appena copiato.

   .. code-block:: python

      OPENAI_API_KEY = "sk-proj-vEBo7Ahxxxx-xxxxx-xxxx"
      OPENAI_ASSISTANT_ID = "asst_ulxxxxxxxxx"

#. Premi ``Ctrl + X``, ``Y``, e poi ``Enter`` per salvare il file e uscire.

4. Esecuzione dell'Esempio
----------------------------------
Comunicazione Testuale
^^^^^^^^^^^^^^^^^^^^^^^^^^

Se il tuo PiDog non è dotato di un microfono, puoi utilizzare l'input da tastiera per interagire con lui eseguendo i comandi seguenti.

#. Ora, esegui i comandi seguenti utilizzando sudo, poiché l'altoparlante di PiDog non funzionerà senza permessi di amministratore. Il processo potrebbe richiedere del tempo per completarsi.

   .. code-block:: shell

      cd ~/pidog/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_dog.py --keyboard

#. Una volta eseguiti correttamente i comandi, vedrai l'output seguente, che indica che tutti i componenti di PiDog sono pronti.

   .. code-block:: shell

      vilib 0.3.8 launching ...
      picamera2 0.3.19
      config_file: /home/pi2/.config/pidog/pidog.conf
      robot_hat init ... done
      imu_sh3001 init ... done
      rgb_strip init ... done
      dual_touch init ... done
      sound_direction init ... done
      sound_effect init ... done
      ultrasonic init ... done

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      input:

#. Ti verrà fornito anche un link per visualizzare il feed della fotocamera di PiDog sul tuo browser: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Ora puoi digitare i tuoi comandi nella finestra del terminale e premere Enter per inviarli. Le risposte di PiDog potrebbero sorprenderti.

   .. note::
      
      PiDog deve ricevere il tuo input, inviarlo a GPT per l'elaborazione, ricevere la risposta e riprodurla tramite sintesi vocale. Questo processo richiede un po' di tempo, quindi ti invitiamo a essere paziente.

   .. image:: img/apt_keyboard_input.png
      :width: 700
      :align: center

#. Se stai utilizzando il modello GPT-4O, puoi anche fare domande basate su ciò che PiDog vede.

Comunicazione Vocale
^^^^^^^^^^^^^^^^^^^^^^^^^^

Se il tuo PiDog è dotato di un microfono, o se desideri acquistarne uno cliccando su |link_microphone|, puoi interagire con PiDog utilizzando comandi vocali.

#. Prima di tutto, verifica che il Raspberry Pi abbia rilevato il microfono.

   .. code-block:: shell

      arecord -l

   If successful, you will receive the following information, indicating that your microphone has been detected.

   .. code-block:: 

      **** List of CAPTURE Hardware Devices ****
      card 3: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

#. Esegui il comando seguente, poi parla con PiDog o emetti qualche suono. Il microfono registrerà i suoni nel file ``op.wav``. Premi ``Ctrl + C`` per interrompere la registrazione.

   .. code-block:: shell

      rec op.wav

#. Infine, usa il comando seguente per riprodurre il suono registrato e confermare che il microfono funzioni correttamente.

   .. code-block:: shell

      sudo play op.wav

#. Ora, esegui i comandi seguenti utilizzando sudo, poiché l'altoparlante di PiDog non funzionerà senza permessi di amministratore. Il processo potrebbe richiedere del tempo per completarsi.

   .. code-block:: shell

      cd ~/pidog/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_dog.py

#. Una volta eseguiti correttamente i comandi, vedrai l'output seguente, che indica che tutti i componenti di PiDog sono pronti.

   .. code-block:: shell
      
      vilib 0.3.8 launching ...
      picamera2 0.3.19
      config_file: /home/pi2/.config/pidog/pidog.conf
      robot_hat init ... done
      imu_sh3001 init ... done
      rgb_strip init ... done
      dual_touch init ... done
      sound_direction init ... done
      sound_effect init ... done
      ultrasonic init ... done

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      listening ...

#. Ti verrà fornito anche un link per visualizzare il feed della fotocamera di PiDog sul tuo browser: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Ora puoi parlare con PiDog, e le sue risposte potrebbero sorprenderti.

   .. note::
      
      PiDog deve ricevere il tuo input, convertirlo in testo, inviarlo a GPT per l'elaborazione, ricevere la risposta e riprodurla tramite sintesi vocale. Questo processo richiede un po' di tempo, quindi ti invitiamo a essere paziente.

   .. image:: img/apt_speech_input.png
      :width: 700
      :align: center

#. Se stai utilizzando il modello GPT-4O, puoi anche fare domande basate su ciò che PiDog vede.

.. raw:: html

   <video controls style = "max-width:90%">
     <source src="_static/video/chatgpt4o.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>

5. Modifica dei parametri [opzionale]
-------------------------------------------
Nel file ``gpt_dog.py``, individuare le seguenti righe. È possibile modificare questi parametri per configurare la lingua STT, il guadagno del volume TTS e il ruolo della voce.

* **STT (Speech to Text)** si riferisce al processo in cui il microfono di PiCar-X cattura il parlato e lo converte in testo da inviare a GPT. È possibile specificare la lingua per migliorare la precisione e la latenza in questa conversione.
* **TTS (Text to Speech)** è il processo di conversione delle risposte di testo di GPT in parlato, che viene riprodotto attraverso l'altoparlante di PiCar-X. È possibile regolare il guadagno del volume e selezionare un ruolo di voce per l'output TTS.

.. code-block:: python

   # openai assistant init
   # =================================================================
   openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'picrawler')
   # LANGUAGE = ['zh', 'en'] # configurare il codice della lingua STT, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
   LANGUAGE = []
   VOLUME_DB = 3 # guadagno del volume TTS, preferibilmente inferiore a 5db
   # selezionare il ruolo della voce TTS, potrebbe essere "alloy, echo, fable, onyx, nova e shimmer"
   # https://platform.openai.com/docs/guides/text-to-speech/supported-languages
   TTS_VOICE = 'nova'

* Variabile ``LANGUAGE``:

  * Migliora l'accuratezza e il tempo di risposta dello Speech-to-Text (STT).
  * ``LANGUAGE = []`` significa supportare tutte le lingue, ma questo potrebbe ridurre l'accuratezza dell'STT e aumentare la latenza.
  * Si consiglia di impostare la/le lingua/e specifica/e utilizzando i codici linguistici di |link_iso_language_code| per migliorare le prestazioni.
  
* Variabile ``VOLUME_DB``:

  * Controlla il guadagno applicato all'output Text-to-Speech (TTS).
  * Aumentare il valore aumenterà il volume, ma è meglio mantenere il valore inferiore a 5dB per evitare distorsioni audio.

* Variabile ``TTS_VOICE``:

  * Seleziona il ruolo della voce per l'output Text-to-Speech (TTS).
  * Opzioni disponibili: ``alloy, echo, fable, onyx, nova, shimmer``.
  * È possibile sperimentare con diverse voci di |link_voice_options| per trovarne una che si adatti al tono e al pubblico desiderato. Le voci disponibili sono attualmente ottimizzate per l'inglese.

