.. note::

    Ciao, benvenuto nella Community di appassionati di Raspberry Pi, Arduino e ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Modulo Ultrasonico
=============================

.. image:: img/ultrasonic_pic.png
    :width: 400
    :align: center

* **TRIG**: Ingresso Impulso di Attivazione
* **ECHO**: Uscita Impulso di Eco
* **GND**: Massa
* **VCC**: Alimentazione 5V

Questo è il sensore di distanza ultrasonico HC-SR04, che fornisce una misurazione senza contatto da 2 cm a 400 cm con una precisione fino a 3 mm. Il modulo include un trasmettitore ultrasonico, un ricevitore e un circuito di controllo.

È sufficiente collegare 4 pin: VCC (alimentazione), Trig (attivazione), Echo (ricezione) e GND (massa) per utilizzarlo facilmente nei tuoi progetti di misurazione.

**Caratteristiche**

* Tensione di Lavoro: DC5V
* Corrente di Lavoro: 16mA
* Frequenza di Lavoro: 40Hz
* Range Massimo: 500cm
* Range Minimo: 2cm
* Segnale di Ingresso Trigger: impulso TTL di 10µS
* Segnale di Uscita Eco: segnale di livello TTL proporzionale alla distanza
* Connettore: XH2.54-4P
* Dimensioni: 46x20,5x15 mm

**Principio di Funzionamento**

I principi di base sono i seguenti:

* Utilizzare un trigger IO per inviare un segnale di livello alto per almeno 10µS.
* Il modulo invia un impulso ultrasonico a 40 kHz per 8 cicli e rileva se viene ricevuto un segnale di ritorno.
* Echo emetterà un segnale di livello alto se un segnale di ritorno viene rilevato; la durata del livello alto è il tempo trascorso dall'emissione al ritorno del segnale.
* Distanza = (tempo di livello alto x velocità del suono (340 m/s)) / 2

    .. image:: img/ultrasonic_prin.jpg
        :width: 800

Formula: 

* us / 58 = distanza in centimetri
* us / 148 = distanza in pollici
* distanza = tempo di livello alto x velocità (340 m/s) / 2


**Note Applicative**

* Questo modulo non deve essere collegato durante l'accensione. Se necessario, collegare prima il GND del modulo, altrimenti il funzionamento del modulo potrebbe risultare compromesso.
* L'area dell'oggetto da misurare dovrebbe essere di almeno 0,5 metri quadrati e il più piatta possibile per evitare errori di misurazione.
