.. note::

    Ciao! Benvenuto nella Community di appassionati di Raspberry Pi, Arduino e ESP32 di SunFounder su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e supera le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anticipo agli annunci dei nuovi prodotti e scopri in anteprima le novità.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

14. TTS con Espeak e Pico2Wave
=================================================

In questa lezione utilizzeremo due motori di sintesi vocale (TTS) integrati in Raspberry Pi — **Espeak** e **Pico2Wave** — per far parlare il Pidog.  

Questi due motori sono semplici e funzionano completamente offline, ma hanno voci diverse:

* **Espeak**: molto leggero e veloce, ma con una voce robotica. Puoi regolare velocità, tono e volume.  
* **Pico2Wave**: produce una voce più fluida e naturale rispetto a Espeak, ma con meno opzioni di configurazione.  

Sentirai la differenza in termini di **qualità vocale** e **funzionalità**.  

----

Prima di iniziare
---------------------

Assicurati di aver completato:

* :ref:`install_all_modules` — Installa i moduli ``robot-hat``, ``vilib``, ``pidog`` e poi esegui lo script ``i2samp.sh``.

Testare Espeak
--------------------

Espeak è un motore TTS leggero incluso in Raspberry Pi OS.  
La sua voce è robotica, ma è altamente configurabile: puoi modificare volume, tono, velocità e altro.

**Passaggi per provarlo**:

* Crea un nuovo file con il comando:

  .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_espeak.py

* Copia il codice di esempio al suo interno. Premi ``Ctrl+X``, poi ``Y`` e infine ``Enter`` per salvare ed uscire.

  .. code-block:: python

      from pidog.tts import Espeak

      tts = Espeak()
  
      # Impostazioni opzionali della voce
      # tts.set_amp(100)   # 0 a 200
      # tts.set_speed(150) # 80 a 260
      # tts.set_gap(5)     # 0 a 200
      # tts.set_pitch(50)  # 0 a 99

      # Saluto veloce (verifica funzionamento)
      tts.say("Hello! I'm Espeak TTS.")
  
* Esegui il programma con:

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* Dovresti sentire il Pidog dire: “Hello! I'm Espeak TTS.”  
* Decommenta le righe di configurazione della voce nel codice per sperimentare come ``amp``, ``speed``, ``gap`` e ``pitch`` influenzano il suono.

----

Testare Pico2Wave
---------------------

Pico2Wave produce una voce più naturale e umana rispetto a Espeak.  
È più semplice da usare ma meno flessibile: puoi solo cambiare la lingua, non tono o velocità.

**Passaggi per provarlo**:

* Crea un nuovo file con il comando:

  .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_pico2wave.py

* Copia il codice di esempio al suo interno. Premi ``Ctrl+X``, poi ``Y`` e infine ``Enter`` per salvare ed uscire.

  .. code-block:: python
  
      from pidog.tts import Pico2Wave
  
      tts = Pico2Wave()
  
      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
      # Saluto veloce (verifica funzionamento)
      tts.say("Hello! I'm Pico2Wave TTS.")

* Esegui il programma con:

  .. code-block:: bash

    sudo python3 test_tts_pico2wave.py

* Dovresti sentire il Pidog dire: “Hello! I'm Pico2Wave TTS.”  
* Prova a cambiare lingua (ad esempio ``es-ES`` per spagnolo) e ascolta la differenza.

----

Risoluzione dei problemi
----------------------------

* **Nessun suono con Espeak o Pico2Wave**

  * Controlla che gli altoparlanti o le cuffie siano collegati e che il volume non sia disattivato.  
  * Esegui un test rapido nel terminale:

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  Se non senti nulla, il problema riguarda l’uscita audio e non il tuo codice Python.

* **La voce di Espeak è troppo veloce o troppo robotica**

  * Prova a regolare i parametri nel codice:

    .. code-block:: python

       tts.set_speed(120)   # più lento
       tts.set_pitch(60)    # tono diverso

* **Permesso negato durante l’esecuzione del codice**

  * Prova a eseguire con ``sudo``:

    .. code-block:: bash

       sudo python3 test_tts_espeak.py


Confronto: Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Funzionalità
     - Espeak
     - Pico2Wave
   * - Qualità vocale
     - Robotica, sintetica
     - Più naturale, simile a una voce umana
   * - Lingue
     - Inglese predefinito
     - Meno lingue, ma quelle principali
   * - Personalizzazione
     - Sì (velocità, tono, ecc.)
     - No (solo lingua)
   * - Prestazioni
     - Molto veloce e leggero
     - Leggermente più lento e pesante

