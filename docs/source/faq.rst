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

PiDog è disponibile in due versioni: **V1** e **V2**.

* **Versione V1**: Compatibile con Raspberry Pi 3B+/4B/Zero 2W, **non compatibile** con Raspberry Pi 5.
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

Se non c'è audio:

.. code-block:: bash

    # I2S Audio
    cd ~/robot-hat
    sudo bash i2samp.sh

(Esegui più volte se necessario.)

----

Q3: Why do I get a "piper-tts" error during installation?
----------------------------------------------------------

.. important::

   If you see this error during ``pip3 install``:

   .. code-block:: text

       ERROR: Could not find a version that satisfies the requirement piper-tts==1.3.0
       ERROR: No matching distribution found for piper-tts==1.3.0

   It means you are using a **32-bit** Raspberry Pi OS. The ``piper-tts`` package only provides pre-built wheels for **64-bit** systems. Reinstall the OS using the **64-bit** version of Raspberry Pi OS and the installation will succeed.

----

Q4: Come eseguo la prima demo?
-------------------------------------

.. code-block:: bash

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

PiDog si sveglierà, si siederà e muoverà la coda.

----

Q5: Quali azioni e suoni integrati sono disponibili?
------------------------------------------------------

* Azioni: ``stand``, ``sit``, ``wag_tail``, ``trot``, ecc.
* Suoni: ``bark``, ``howling``, ``pant``, ecc.

Esegui:

.. code-block:: bash

    sudo python3 2_function_demonstration.py

Poi inserisci numeri per attivare le azioni.

----

Q6: Come utilizza PiDog i sensori?
-------------------------------------

* **Ultrasuoni**: Evitamento ostacoli e pattugliamento.
* **Tocco**: Tocco frontale = allerta; tocco posteriore = piacere.
* **Direzione del suono**: Risponde alla direzione della sorgente sonora.

----

Q7: Quali funzioni AI supporta PiDog?
------------------------------------------------------

PiDog integra **TTS**, **STT** e **LLM**:

* **TTS**: Espeak, Pico2Wave, Piper, OpenAI.
* **STT**: Vosk (offline).
* **LLM**: Ollama (locale), OpenAI (online).

----

Q8: Devo calibrare i servo?
---------------------------------------------

Sì — **la calibrazione dei servo è necessaria sia per la versione V1 che per la V2** per garantire movimenti stabili ed evitare danni meccanici.

**Versione V2**

The Robot HAT on the V2 version has a **zeroing button**. Press it to automatically set all servos to 0° — no script needed.

If your PiDog V2's legs are in the wrong position after assembly (for example, servos appear at strange angles or the robot cannot stand properly), you can use the zero button to fix this:

#. Power on the PiDog.
#. Press the **zero button** on the Robot HAT — all servos will forcibly return to 0°.
#. Reassemble the legs in the correct orientation following the assembly instructions.

For a step-by-step demonstration, watch the video below:

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zmN_mGxTKuU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Versione V1**

The V1 version uses a script to zero the servos. Run the following command — it will set all servos to 0°:

.. code-block:: bash

   cd ~/pidog/examples
   sudo python3 servo_zeroing.py

This should be done **before installation** to ensure each servo starts from the correct zero position. If your PiDog V1's legs are in the wrong position after assembly, re-run this script to reset all servos to 0°, then reassemble the legs correctly.


----

Q9: Perché il mio PiDog cammina in modo instabile?
---------------------------------------------------

* Assicurati che tutti i servo siano stati installati a 0°.
* Controlla che gli angoli dei servo corrispondano al righello di calibrazione (60°/90°).
* Verifica che la batteria sia completamente carica.
* Stringi bene tutte le viti dei servo.

----

Q10: Servo zeroing works, but calibration example doesn't move any servo?
--------------------------------------------------------------------------

If pressing the zeroing button moves all servos to 0° normally, but the calibration script cannot control any servo, the problem is likely a hardware connection issue between the Raspberry Pi and the Robot HAT.

.. note::

   The zeroing button is only available on **PiDog V2** (which uses Robot HAT V5). PiDog V1 does not have this feature and must use the ``servo_zeroing.py`` script instead.

**Why this happens**

* Servo zeroing is handled **directly by the Robot HAT** — it works independently without the Raspberry Pi.
* Running calibration or any servo control from code requires the Raspberry Pi to communicate with the Robot HAT through the **GPIO header pins**.

**How to diagnose**

This is often caused by poor soldering on either side of the GPIO connection:

* The **Raspberry Pi's 40-pin GPIO header** (especially on Zero 2W, where the header must be soldered on by the user).
* The **Robot HAT's female header pins**.

Take clear, well-lit photos of both sets of pins and send them to SunFounder support at service@sunfounder.com. The team will help identify whether resoldering is needed.

----

Q11: Perché la fotocamera non funziona?
-----------------------------------------

* Assicurati che il cavo della fotocamera sia **inserito saldamente** nell'interfaccia CSI e che la linguetta di blocco nera sia fissata.
* **Spegni** il Raspberry Pi prima di collegare o scollegare la fotocamera per evitare danni.
* Testa la fotocamera con ``libcamera-hello`` o ``raspistill`` per verificare l'output dell'immagine.
* Reinserisci il cavo se è allentato o installato in modo errato.

----

Q12: Perché l'altoparlante non funziona?
-----------------------------------------

* Assicurati che l'altoparlante del Robot HAT sia attivato. Se non hai ancora eseguito alcun codice di esempio PiDog, attivalo prima:

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

Q13: Perché il microfono non funziona?
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

Q14: Perché il sensore di direzione del suono non funziona?
------------------------------------------------------------

* Assicurati che il sensore di direzione del suono sia collegato all'interfaccia SPI corretta.
* Controlla che tutti i cavi siano collegati saldamente e non invertiti.
* Verifica che l'alimentazione sia stabile e che il sensore non sia ostruito.
* Riavvia il dispositivo e prova a eseguire nuovamente lo script di esempio.

----

Q15: Perché il sensore touch non risponde?
---------------------------------------------

* Assicurati che tutti i cavi del sensore touch siano ben collegati.
* Ricorda: un segnale **LOW** indica che il sensore è stato toccato.
* Testa il pin GPIO con ``gpio readall`` o con codice Python per verificare la rilevazione del segnale.
* Controlla nuovamente il cablaggio e l'orientamento.

----

Q16: Why is the ultrasonic sensor not working?
-----------------------------------------------

#. Run the ultrasonic test to check the reading:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 ultrasonic_test.py

   If the reading shows **-1**, the sensor is not functioning correctly.

#. Verify the wiring:

   * **White wire** → GPIO **17**
   * **Yellow wire** → GPIO **4**

#. If the wiring is correct and the reading is still -1, contact SunFounder support at service@sunfounder.com for further assistance.

----

Q17: Perché la scheda LED non si accende o lampeggia in modo errato?
-----------------------------------------------------------------------

* Verifica che la scheda LED sia alimentata a **3,3 V** e collegata alla porta I2C.
* Assicurati che **I2C sia abilitato** sul Raspberry Pi.
* Esegui il seguente comando per controllare se la scheda viene rilevata:

.. code-block:: bash

    i2cdetect -y 1

* Se non compare alcun dispositivo, ricontrolla i collegamenti e riavvia il Pi.

----

Q18: Why are the 6-DOF IMU and 11-channel RGB board not working?
-----------------------------------------------------------------

If both the 6-DOF IMU and the 11-channel RGB LED board are not responding, the issue is likely with the shared I2C connection:

#. First, check whether the devices are detected on the I2C bus:

   .. code-block:: bash

       sudo i2cdetect -y 1

   The expected addresses are:

   * **0x36** — 6-DOF IMU
   * **0x74** — 11-channel RGB LED board

   If one or both addresses are missing, the corresponding device is not properly connected.

#. Try connecting the 6-DOF IMU to a different port and test again.
#. Connect the 6-DOF IMU directly to the Robot HAT's I2C port, then run the test:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 imu_test.py

#. If the IMU works when connected directly, the problem is with the 11-channel RGB board's pass-through port.
#. To confirm, connect the 11-channel RGB board directly to the I2C port and test:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 rgb_strip_test.py

----

Q19: Come viene alimentato PiDog?
-----------------------------------

* Utilizza un alimentatore Type-C da 5V 3A.
* Luce rossa = in carica, spenta = completamente carica.
* Può funzionare mentre è in carica.
* Se l'indicatore non si accende, caricalo prima.

----
