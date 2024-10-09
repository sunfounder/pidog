.. note::

    Ciao, benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto del nostro team e della community.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e a preview speciali.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

3. Alimentazione per Raspberry Pi (Importante)
=================================================

Ricarica
----------

Collega il cavo della batteria. Successivamente, inserisci il cavo USB-C per caricare la batteria.
Dovrai utilizzare un caricabatterie personale; consigliamo un caricatore da 5V 3A, oppure puoi usare il caricabatterie del tuo smartphone.

.. image:: img/BTR_IMG_1096.png

.. note::
    Collega una fonte di alimentazione esterna Type-C alla porta Type-C del robot hat; la ricarica della batteria inizierà immediatamente e si accenderà una spia rossa.\
    Quando la batteria sarà completamente carica, la spia rossa si spegnerà automaticamente.


Accensione
------------

Accendi l'interruttore. La spia di alimentazione e l'indicatore di livello della batteria si accenderanno.

.. image:: img/BTR_IMG_1097.png

Aspetta qualche secondo e sentirai un leggero beep, indicando che il Raspberry Pi è stato avviato con successo.

.. note::
    Se entrambe le spie di livello della batteria sono spente, è necessario caricare la batteria.
    Quando hai bisogno di sessioni prolungate di programmazione o debugging, puoi mantenere il Raspberry Pi operativo inserendo il cavo USB-C per caricare contemporaneamente la batteria.

Batteria 18650
------------------

.. image:: img/5pin_battery.jpg

* VCC: Terminale positivo della batteria. Sono presenti due set di VCC e GND per aumentare la corrente e ridurre la resistenza.
* Centrale: Per bilanciare la tensione tra le due celle e proteggere la batteria.
* GND: Terminale negativo della batteria.

Questo è un pacco batteria personalizzato realizzato da SunFounder, composto da due batterie 18650 con una capacità di 2000mAh. Il connettore è XH2.54 5P, che può essere caricato direttamente una volta collegato alla scheda di espansione.

**Caratteristiche**

* Ricarica della batteria: 5V/2A
* Uscita della batteria: 5V/5A
* Capacità della batteria: 3.7V 2000mAh x 2
* Durata della batteria: 90 minuti
* Tempo di ricarica della batteria: 130 minuti
* Connettore: XH2.54 5P
