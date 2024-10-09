.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

10. Equilibrio
==================

Grazie al modulo IMU a 6 DOF di cui è dotato, PiDog ha un ottimo senso dell’equilibrio.

In questo esempio, puoi far camminare PiDog agevolmente su un tavolo e, anche se alzi un lato del tavolo, PiDog continuerà a muoversi con fluidità sulla lieve pendenza.

.. image:: img/py_10.gif

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 10_balance.py

Dopo l’avvio del programma, vedrai un layout di tastiera stampato nel terminale. 
Puoi controllare PiDog per farlo muovere agevolmente sulla rampa digitando i tasti 
indicati di seguito.

.. list-table:: 
    :widths: 25 25
    :header-rows: 1

    * - Tasti
      - Funzione
    * -  W
      -  Avanti 
    * -  E
      -  In Piedi 
    * -  A
      -  Gira a Sinistra 
    * -  S
      -  Indietro 
    * -  D
      -  Gira a Destra 
    * -  R
      -  Ogni pressione solleva leggermente il corpo; sono necessarie più pressioni per un sollevamento visibile.
    * -  F
      -  Ogni pressione abbassa il corpo un po'; sono necessarie più pressioni per una discesa evidente.
    
  
**Codice**


Trova il codice in |link_code_10_balance|.

