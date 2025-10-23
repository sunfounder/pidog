.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e a tanti altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

2. Calibrazione di PiDog
=============================

**Introduzione**

La calibrazione del tuo PiDog è un passaggio fondamentale per garantirne il funzionamento stabile ed efficiente. Questo processo aiuta a correggere eventuali squilibri o imprecisioni causate da errori di assemblaggio o strutturali. Segui attentamente i passaggi indicati di seguito per assicurarti che PiDog cammini in modo fluido e funzioni come previsto.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/calibrate_before.mp4" type="video/mp4">
      Il tuo browser non supporta il tag video.
   </video>

Se l’angolo di deviazione è troppo grande, torna a :ref:`py_servo_adjust`, imposta l’angolo del servo a 0°, quindi riassembla PiDog seguendo le istruzioni.

**Video di calibrazione**

Per una guida dettagliata, consulta il video completo di calibrazione. Questo video mostra passo dopo passo, in modo visivo, come calibrare correttamente il tuo PiDog.

.. note::

   Il kit PiDog include un righello di calibrazione da 90° o da 60°. Nel video viene utilizzato quello da 90°, ma il processo con quello da 60° è molto simile. Puoi anche fare riferimento alla guida illustrata qui sotto.
    
    .. image:: img/cali_ruler.png
         :width: 400
         :align: center

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/witCWeoHTdk?si=g8_RZDUkfjdwbLZu&amp;start=871&end=1160" title="Lettore video YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Passaggi**

Procedi come segue:

#. Posiziona PiDog su una piattaforma piana.

   .. image:: img/place-pidog.JPG

#. Accedi alla directory degli esempi di PiDog ed esegui lo script ``0_calibration.py``.

   .. raw:: html

        <run></run>

   .. code-block::

        cd ~/pidog/examples
        sudo python3 0_calibration.py

#. Dopo l’esecuzione dello script, nel terminale apparirà un’interfaccia interattiva. Seleziona il tipo di righello di calibrazione che possiedi:  
   scegli l’opzione 1 per 90°, oppure l’opzione 2 per 60°.

    .. image:: img/CALI.slt.1.png

#. Dopo aver fatto la tua scelta, apparirà la seguente interfaccia di calibrazione:

    .. image:: img/CALI.slt.2.png

**Se utilizzi il righello di calibrazione da 60°**

#. Posiziona il **righello di calibrazione (lastra acrilica a C)** come mostrato, con il lato lungo appoggiato sulla superficie orizzontale. Premi ``1`` nel terminale e usa i tasti ``w`` e ``s`` per allineare i bordi.

    .. image:: img/CALI.60.1.JPG

#. Riposiziona il **righello di calibrazione** come mostrato nella figura seguente. Premi ``2`` nel terminale e utilizza nuovamente ``w`` e ``s`` per effettuare una regolazione fine.

    .. image:: img/CALI.60.2.JPG

#. Ripeti la procedura di calibrazione per i servocomandi dal 3 all’8 per assicurarti che tutte e quattro le gambe di PiDog siano correttamente calibrate.

**Se utilizzi il righello di calibrazione da 90°**

#. Posiziona il **righello di calibrazione (lastra acrilica a C)** come illustrato. Premi ``1`` nel terminale, quindi usa ``w`` e ``s`` per allineare i bordi all’immagine di riferimento.

    .. image:: img/CALI-1.2.png

#. Riposiziona il **righello di calibrazione (lastra acrilica a C)** come mostrato. Premi ``2`` nel terminale e regola nuovamente con ``w`` e ``s``.

    .. image:: img/CALI-2.2.png

#. Ripeti la procedura di calibrazione per i servocomandi dal 3 all’8 per assicurarti che tutte e quattro le gambe di PiDog siano correttamente calibrate.

**Completamento della calibrazione**

- Una volta calibrati tutti i servocomandi, esegui nuovamente i codici di esempio per camminata o postura di PiDog per verificare che i movimenti siano fluidi.  
- Se noti deviazioni, rientra nel programma di calibrazione per effettuare ulteriori regolazioni.  
- Si consiglia vivamente di completare questa procedura subito dopo il primo assemblaggio per garantire la stabilità operativa.

.. tip::

   Per evitare di dover ripetere la calibrazione, puoi registrare gli angoli dei servocomandi o esportare il file di configurazione una volta completata la calibrazione. Questo ti permetterà di ripristinare rapidamente le impostazioni in futuro.
