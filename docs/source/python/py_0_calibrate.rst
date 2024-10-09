.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e a tanti altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

2. Calibrazione del PiDog
=============================

**Introduzione**

Calibrare il tuo PiDog è un passaggio fondamentale per garantirne un funzionamento stabile ed efficiente. Questo processo aiuta a correggere eventuali squilibri o imprecisioni che potrebbero essere sorti durante l'assemblaggio o a causa di problemi strutturali. Segui attentamente questi passaggi per assicurarti che il PiDog cammini in modo stabile e si comporti come previsto.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/calibrate_before.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>


Se l'angolo di deviazione è troppo grande, è necessario tornare alla sezione :ref:`py_servo_adjust` per impostare l'angolo del servo a 0° e seguire le istruzioni per riassemblare il PiDog.


**Video di Calibrazione**

Per una guida completa, consulta il video dettagliato sulla calibrazione. Ti guiderà passo dopo passo attraverso il processo per calibrare accuratamente il tuo PiDog.

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/witCWeoHTdk?si=g8_RZDUkfjdwbLZu&amp;start=871&end=1160" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Passaggi**

I passaggi specifici sono i seguenti:

#. Posiziona il PiDog sulla base.

    .. image:: img/place-pidog.JPG

#. Naviga nella directory degli esempi di PiDog e avvia lo script ``0_calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 0_calibration.py
        
    All'avvio dello script, apparirà un'interfaccia utente nel tuo terminale.

    .. image:: img/CALI.slt.1.png

#. Qui devi selezionare il calibro di misurazione (60° o 90°). Se il kit include un calibro di 90°, seleziona la prima opzione; se invece è da 60°, seleziona la seconda opzione. Dopo aver scelto, entrerai nell'interfaccia seguente:

.. image:: img/CALI.slt.2.png



Calibro a 90°
------------------------------

#. Posiziona il **Calibro di Misurazione** (Acrilico C) come mostrato nell'immagine fornita. Nel terminale, premi ``1``, poi utilizza i tasti ``w`` e ``s`` per allineare i bordi come indicato.

    .. image:: img/CALI-1.2.png

#. Riposiziona il **Calibro di Misurazione** (Acrilico C) come illustrato nella prossima immagine. Premi ``2`` nel terminale, poi usa ``w`` e ``s`` per allineare i bordi come mostrato.

    .. image:: img/CALI-2.2.png

#. Ripeti il processo di calibrazione per i restanti servomotori (da 3 a 8). Assicurati che tutte e quattro le zampe del PiDog siano calibrate correttamente.



Calibro a 60°
------------------------------

#. Posiziona il **Calibro di Misurazione** (Acrilico C) come mostrato nell'immagine fornita. Colloca il lato lungo su una superficie piana. Nel terminale, premi ``1``, seguito dai tasti ``w`` e ``s`` per allineare i bordi come indicato nell'immagine.

    .. image:: img/CALI.60.1.JPG

#. Riposiziona il **Calibro di Misurazione** (Acrilico C) come illustrato nella prossima immagine. Premi ``2`` nel terminale, poi usa ``w`` e ``s`` per allineare i bordi come mostrato.

    .. image:: img/CALI.60.2.JPG

#. Ripeti il processo di calibrazione per i restanti servomotori (da 3 a 8). Assicurati che tutte e quattro le zampe del PiDog siano calibrate correttamente.

