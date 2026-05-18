.. _pidog_skill:

.. start_using_pidog

21. Utilizzare OpenClaw per controllare PiDog
========================================


**Che cos'è OpenClaw?**

Pensalo come una versione potenziata di ChatGPT. Mentre i chatbot tradizionali possono solo parlare (generare testo), OpenClaw può eseguire azioni. Comprende le tue istruzioni in linguaggio naturale e può effettivamente eseguire operazioni sul tuo computer, come eseguire comandi, gestire file e chiamare vari strumenti.

Ecco alcuni scenari applicativi fantastici:

* **Assistente personale a tutto tondo:** lascialo aiutarti a gestire la tua agenda, impostare promemoria e monitorare le attività. Devi solo digli qualcosa in un'app di chat (come Telegram, WhatsApp) e lui ricorderà ed eseguirà.
* **Colla per l'automazione:** può fungere da legante per i tuoi vari servizi. Ad esempio, può monitorare un sito web per variazioni di prezzo. Quando rileva una riduzione, può attivare automaticamente un flusso di lavoro n8n per inviarti una notifica via email.
* **Assistente di sviluppo dedicato:** ti aiuta a gestire server, eseguire script e controllare log. Puoi dire semplicemente: "Controlla il carico di sistema per me" e lui può connettersi in SSH al tuo server, eseguire il comando e restituire i risultati.
* **Compagno hardware:** questo è un caso d'uso molto interessante. Puoi far controllare l'hardware collegato a un Raspberry Pi da OpenClaw. Ad esempio, uno sviluppatore lo ha usato per controllare un aspirapolvere robot con un braccio meccanico, oppure per analizzare i dati di un simulatore di guida e mostrarli su uno schermo LED. Il team ufficiale di Raspberry Pi lo ha persino usato per costruire una cabina fotografica automatica per un matrimonio, semplicemente tramite conversazione, senza scrivere una riga di codice!


.. important::

   Il Raspberry Pi Zero 2W ha solo 512 MB di RAM, mentre OpenClaw richiede almeno 1 GB. Pertanto non può funzionare correttamente. Si consiglia un Raspberry Pi 4/5 o superiore.

Quick Start OpenClaw
------------------------------

Se vuoi sperimentare il potere di OpenClaw il più rapidamente possibile, usa questo metodo. Installerà automaticamente e avvierà una procedura guidata di configurazione interattiva.

1.  Apri il terminale sul tuo Raspberry Pi ed esegui direttamente il comando seguente. Questo comando scarica lo script di installazione dal sito ufficiale ed esegue:

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash
   
    .. note:: Poiché le nuove versioni vengono aggiornate rapidamente, è normale se i passaggi di installazione differiscono leggermente.

2.  Lo script scaricherà e installerà OpenClaw automaticamente.

    .. image:: /img/openclaw/install_open_claw.png


3.  Successivamente vedrai un prompt di sicurezza che ti chiederà se ti fidi di OpenClaw. Una volta sicuro che sia affidabile, usa i tasti freccia per selezionare "Yes" e premi Invio.

    .. image:: /img/openclaw/security_open_claw.png


4.  Seleziona Quick Start e poi premi Invio.

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  Seleziona il tuo Model, quindi premi Invio. In questo esempio useremo OpenAI.

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  Seleziona OpenAI API Key.

    .. image:: /img/openclaw/api_key_open_claw.png

7.  Incolla la chiave API ora.

    .. image:: /img/openclaw/paste_api_key_open_claw.png

.. |link_openai_platform| raw:: html

    <a href="https://platform.openai.com/settings/organization/api-keys" target="_blank">OpenAI Platform</a>

8.  Vai a |link_openai_platform| e accedi. Nella pagina **API keys**, clicca su **Create new secret key**.

    .. image:: /img/openclaw/llm_openai_create.png

9.  Compila i dettagli (Owner, Name, Project e autorizzazioni se necessarie), poi clicca su **Create secret key**.

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. Una volta creata la chiave, copiala subito — non potrai più visualizzarla. Se la perdi, dovrai generarne una nuova.

    .. image:: /img/openclaw/llm_openai_copy.png

11. Incolla la chiave nella configurazione di OpenClaw.

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. Seleziona il Model che desideri utilizzare. In questo esempio useremo **Keep current**.

    .. image:: /img/openclaw/model_config_open_claw.png

13. Successivamente viene la selezione del canale. I canali si riferiscono ai servizi di comunicazione supportati da OpenClaw, come Telegram, WhatsApp, Discord e altro. Usa il tasto freccia verso il basso per selezionare l'opzione "Skip for now", poi premi Invio.

    .. image:: /img/openclaw/channel_open_claw.png

14. Ora ti verrà chiesto di configurare immediatamente le skill. Seleziona "Yes" e premi Invio.

    .. image:: /img/openclaw/config_skill_open_claw.png

15. Installa le skill che ti servono. Nell'esempio seguente selezioniamo l'opzione "Skip for now" (premi la barra spaziatrice per selezionare), quindi premi Invio.

    .. image:: /img/openclaw/install_skill_open_claw.png


16. Successivamente ci sono i Hooks; selezioneremo "command-logger" e "session-memory".

    .. image:: /img/openclaw/hooks2_open_claw.png


17. L'installazione è ora completa. Puoi avviare OpenClaw selezionando "Hatch in TUI" e premendo Invio.

   .. image:: /img/openclaw/hatch_open_claw.png


.. note:: 
   
   Puoi avviare OpenClaw inserendo il comando seguente:

    .. code-block:: bash

       openclaw tui

   E puoi premere ctrl+c due volte per uscire dall'interfaccia tui.

------------------------------------------------------------------------

Far funzionare OpenClaw con PiDog
----------------------------------------------

**Che cos'è PiDog Skill?**

PiDog Skill è un'estensione per OpenClaw che ti permette di controllare il tuo robot PiDog V2 SunFounder tramite linguaggio naturale. Invece di dover ricordare parametri complessi da riga di comando, puoi semplicemente dire a OpenClaw cosa vuoi che faccia PiDog — ad esempio "fai sedere il cane" o "accendi le luci LED di viola" — e OpenClaw eseguirà automaticamente i comandi appropriati.

Ecco alcune cose che puoi fare con PiDog Skill:

* **Azioni di base:** fai stare in piedi, seduto, sdraiato, far agitare la coda, abbaiare, camminare avanti/indietro o girare a sinistra/destra.
* **Mantenere una posa:** mantieni PiDog in una posizione specifica (come stare in piedi) per periodi prolungati.
* **Controllo delle luci LED:** cambia il colore degli occhi con effetti come respiro, ascolto, boom o luce fissa.
* **Personalizzazione del colore:** scegli tra rosso, verde, blu, giallo, viola, rosa, ciano, bianco, arancione o colori esadecimali personalizzati.

----------------------------------------------------------------

Prerequisiti
------------------------------

Prima di poter utilizzare PiDog Skill con OpenClaw, assicurati di avere:

1. **PiDog V2** correttamente assemblato e collegato al tuo Raspberry Pi
2. **OpenClaw** installato e in esecuzione
3. Le seguenti directory presenti nel sistema:

   - ``~/pidog``
   - ``~/robot-hat``
   - ``~/vilib``

Puoi verificare l'installazione eseguendo:

.. code-block:: bash

   python3 -c "import pidog"

Se questo comando viene eseguito senza errori, sei pronto per procedere.

----------------------------------------------------------------

Installazione di PiDog Skill
------------------------------

Segui questi passaggi per installare PiDog Skill per OpenClaw:

1. **Crea la cartella skills** (se non esiste già):

   .. code-block:: bash

      mkdir -p ~/.openclaw/workspace/skills/

2. **Copia i file della skill PiDog** nella directory delle skill di OpenClaw:

   .. code-block:: bash

      cp -r ~/pidog/pidog-control ~/.openclaw/workspace/skills/pidog-control/

   .. note:: Sostituisci ``~/pidog-skill`` con il percorso reale dove si trovano i file della skill PiDog.

3. **Verifica l'installazione** controllando i file della skill:

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/pidog-control/scripts/

   Dovresti vedere ``pidog_ctl.py`` e ``pidog_rgb_ctl.py`` nell'output.

----------------------------------------------------------------

Test di PiDog Skill
------------------------------

Prima di utilizzare la skill con OpenClaw, è consigliabile testare la funzionalità di base direttamente dal terminale.

**Passo 1: Controlla lo stato di PiDog**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py status

**Passo 2: Esegui un test sicuro**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py safe-test

**Passo 3: Prova le azioni di base**

Fai sedere PiDog:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action sit

Fai alzare PiDog e mantieni la posa:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action stand --hold

Fai abbaiare PiDog:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action bark

**Passo 4: Verifica le luci LED**

Prova l'effetto boom con colore viola:

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple

Prova altri effetti luminosi:

.. code-block:: bash

   # Effetto respiro con colore rosso
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light breath --color red

   # Effetto ascolto con colore blu
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light listen --color blue

   # Spegni le luci
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light off

----------------------------------------------------------------

Utilizzare PiDog Skill in OpenClaw
------------------------------

Una volta verificato che PiDog Skill funziona dalla riga di comando, puoi iniziare a usarlo all'interno di OpenClaw.

1. **Avvia l'interfaccia OpenClaw TUI**:

   .. code-block:: bash

      openclaw tui
