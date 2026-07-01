.. note::

    Ciao, benvenuto nella Community degli appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook!  
    Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti subito!

FAQ
==========

Q1: Quali versioni di PiDog sono disponibili?
------------------------------------------------------

PiDog è disponibile in due versioni: **Standard** e **V2**.

* **Versione Standard**: Compatibile con Raspberry Pi 3B+/4B/Zero 2W, **non compatibile** con Raspberry Pi 5.  
* **Versione V2**: Compatibile con Raspberry Pi 3/4/5 e Zero 2W. Presenta miglioramenti nel circuito del Robot HAT e nel driver dei servi, oltre a un migliore supporto di alimentazione per Pi 5.  
* **Alimentazione**: La V2 offre una gestione energetica potenziata per applicazioni ad alto consumo.

----

Q2: Come installo i moduli richiesti?
--------------------------------------------------

.. code-block:: bash

    # Robot HAT
    git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
    cd robot-hat && sudo python3 install.py

    # Vilib
    git clone https://github.com/sunfounder/vilib.git
    cd vilib && sudo python3 install.py

    # PiDog
    git clone https://github.com/sunfounder/pidog.git --depth 1
    cd pidog && sudo pip3 install . --break

Se non c’è audio:

.. code-block:: bash

    # I2S Audio
    cd ~/robot-hat
    sudo bash i2samp.sh

(Esegui più volte se necessario.)

----

Q3: Come eseguo la prima demo?
-------------------------------------

.. code-block:: bash

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

PiDog si sveglierà, si siederà e muoverà la coda.

----

Q4: Quali azioni e suoni integrati sono disponibili?
------------------------------------------------------

* Azioni: ``stand``, ``sit``, ``wag_tail``, ``trot``, ecc.  
* Suoni: ``bark``, ``howling``, ``pant``, ecc.

Esegui:

.. code-block:: bash

    sudo python3 2_function_demonstration.py

Poi inserisci numeri per attivare le azioni.

----

Q5: Come utilizza PiDog i sensori?
-------------------------------------

* **Ultrasuoni**: Evitamento ostacoli e pattugliamento.  
* **Tocco**: Tocco frontale = allerta; tocco posteriore = piacere.  
* **Direzione del suono**: Risponde alla direzione della sorgente sonora.

----

Q6: Quali funzioni AI supporta PiDog?
------------------------------------------------------

PiDog integra **TTS**, **STT** e **LLM**:

* **TTS**: Espeak, Pico2Wave, Piper, OpenAI.  
* **STT**: Vosk (offline).  
* **LLM**: Ollama (locale), OpenAI (online).

----

Q7: Devo calibrare i servo?
---------------------------------------------

Sì — **la calibrazione dei servo è necessaria sia per la versione Standard che per la V2** per garantire movimenti stabili ed evitare danni meccanici.

**Versione V2**  
Premi il **pulsante di azzeramento** sul Robot HAT per impostare automaticamente tutti i servo a 0°. Questo semplifica il processo di zeroing senza dover eseguire script.

**Versione Standard**  
Esegui lo script di zeroing **prima dell’installazione**:

.. code-block:: bash

   cd ~/pidog/examples
   sudo python3 servo_zeroing.py

Dopo l’installazione (per entrambe le versioni), controlla manualmente e regola con precisione gli angoli dei servo per allineare ogni arto con il righello di calibrazione.  
Questo evita instabilità, attriti o stress meccanici, garantendo movimenti fluidi e posture accurate.

----

Q8: Perché il mio PiDog cammina in modo instabile?
---------------------------------------------------

* Assicurati che tutti i servo siano stati installati a 0°.  
* Controlla che gli angoli dei servo corrispondano al righello di calibrazione (60°/90°).  
* Verifica che la batteria sia completamente carica.  
* Stringi bene tutte le viti dei servo.

----

Q9: Perché la fotocamera non funziona?
-----------------------------------------

* Assicurati che il cavo della fotocamera sia **inserito saldamente** nell’interfaccia CSI e che la linguetta di blocco nera sia fissata.  
* **Spegni** il Raspberry Pi prima di collegare o scollegare la fotocamera per evitare danni.  
* Testa la fotocamera con ``libcamera-hello`` o ``raspistill`` per verificare l’output dell’immagine.  
* Reinserisci il cavo se è allentato o installato in modo errato.

----

Q10: Perché l’altoparlante non funziona?
-----------------------------------------

* Assicurati che l’altoparlante del Robot HAT sia attivato. Se non hai ancora eseguito alcun codice di esempio PiDog, attivalo prima:

  .. code-block:: bash

     robot_hat enable_speaker

  È sufficiente farlo una volta per ogni avvio. Eseguire un qualsiasi esempio PiDog (che inizializza ``Pidog()``) lo fa automaticamente.

* Assicurati che il volume non sia disattivato e che il driver audio I2S sia installato.
* Se non si sente alcun suono, riconfigura I2S con:

.. code-block:: bash

    cd ~/robot-hat
    sudo bash i2samp.sh

* Riavvia il Raspberry Pi dopo aver eseguito lo script.

----

Q11: Perché il microfono non funziona?
-----------------------------------------

* Verifica se il sistema riconosce il microfono con:

.. code-block:: bash

    arecord -l

* Prova a registrare un file audio con:

.. code-block:: bash

    arecord -D plughw:1,0 -f cd test.wav

* Se non viene registrato nulla, seleziona il dispositivo di input corretto nelle impostazioni audio oppure usa ``alsamixer`` per regolare il volume di ingresso.  
* Assicurati che nessun altro processo stia occupando il dispositivo di input audio.

----

Q12: Perché il sensore di direzione del suono non funziona?
------------------------------------------------------------

* Assicurati che il sensore di direzione del suono sia collegato all’interfaccia SPI corretta.  
* Controlla che tutti i cavi siano collegati saldamente e non invertiti.  
* Verifica che l’alimentazione sia stabile e che il sensore non sia ostruito.  
* Riavvia il dispositivo e prova a eseguire nuovamente lo script di esempio.

----

Q13: Perché il sensore touch non risponde?
---------------------------------------------

* Assicurati che tutti i cavi del sensore touch siano ben collegati.  
* Ricorda: un segnale **LOW** indica che il sensore è stato toccato.  
* Testa il pin GPIO con ``gpio readall`` o con codice Python per verificare la rilevazione del segnale.  
* Controlla nuovamente il cablaggio e l’orientamento.

----

Q14: Perché la scheda LED non si accende o lampeggia in modo errato?
-----------------------------------------------------------------------

* Verifica che la scheda LED sia alimentata a **3,3 V** e collegata alla porta I2C.  
* Assicurati che **I2C sia abilitato** sul Raspberry Pi.  
* Esegui il seguente comando per controllare se la scheda viene rilevata:

.. code-block:: bash

    i2cdetect -y 1

* Se non compare alcun dispositivo, ricontrolla i collegamenti e riavvia il Pi.

----

Q15: Come viene alimentato PiDog?
-----------------------------------

* Utilizza un alimentatore Type-C da 5V 3A.  
* Luce rossa = in carica, spenta = completamente carica.  
* Può funzionare mentre è in carica.  
* Se l’indicatore non si accende, caricalo prima.

