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
===========================

Q1: Riguardo all'errore "pinctrl: not found".
-------------------------------------------------------------------

Se incontri l'errore seguente:

.. code-block::

    pinctrl: not found

Significa che hai installato il sistema Bullseye. Si consiglia di installare il sistema **Bookworm** al suo posto.

Q2: Informazioni sul caricabatterie
-------------------------------------------------------------------

Per caricare la batteria, collega semplicemente un alimentatore Type-C da 5V/2A alla porta di alimentazione del Robot Hat. Non è necessario accendere l'interruttore di alimentazione del Robot Hat durante la ricarica.
Puoi anche utilizzare il dispositivo mentre la batteria è in carica.

.. image:: img/robot_hat_pic.png
    :align: center
    :width: 500

Durante la ricarica, l'energia in ingresso viene amplificata dal chip di ricarica per caricare la batteria e contemporaneamente alimentare il convertitore DC-DC per uso esterno, con una potenza di ricarica di circa 10W.
Se il consumo di energia esterna rimane elevato per un periodo prolungato, la batteria potrebbe integrare l'alimentazione, in modo simile all'uso di un telefono mentre è in carica. Tuttavia, fai attenzione alla capacità della batteria per evitare che si esaurisca completamente durante l'uso e la ricarica simultanei.
