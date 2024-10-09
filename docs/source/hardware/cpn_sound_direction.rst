.. note::

    Ciao! Benvenuto nella Community di appassionati di Raspberry Pi, Arduino e ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Sensore di Direzione del Suono
===================================

.. image:: img/cpn_sound.png
   :width: 400
   :align: center

Questo è un modulo di riconoscimento della direzione del suono, dotato di 3 microfoni 
in grado di rilevare le fonti sonore da tutte le direzioni. È equipaggiato con un 
TR16F064B, utilizzato per elaborare i segnali acustici e calcolare la direzione della 
sorgente sonora. L'unità minima di riconoscimento di questo modulo è di 20 gradi, con 
un intervallo di dati compreso tra 0 e 360°.

Processo di trasmissione dei dati: il controller principale alza il pin BUSY e il 
TR16F064B inizia a monitorare la direzione. Quando il modulo 064B rileva la direzione, 
abbassa il pin BUSY. Quando il controller principale rileva che il pin BUSY è basso, 
invia dati arbitrari a 16 bit al 064B (seguendo la trasmissione MSB) e riceve i dati a 
16 bit, che rappresentano la direzione del suono elaborata dal modulo 064B. Una volta 
completato, il controller principale riporta il pin BUSY ad alto per iniziare nuovamente 
la rilevazione della direzione.


**Specifiche Tecniche**

* Alimentazione: 3,3V
* Comunicazione: SPI
* Connettore: PH2.0 a 7 pin
* Intervallo di riconoscimento della direzione del suono: 360°
* Precisione del riconoscimento angolare: ~10°

**Pin Out**

* GND - Ingresso di massa
* VCC - Ingresso di alimentazione a 3,3V
* MOSI - SPI MOSI
* MISO - SPI MISO
* SCLK - Clock SPI
* CS - Selezione chip SPI
* BUSY - Rilevazione stato di busy
