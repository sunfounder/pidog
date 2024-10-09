.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

11. Controlla PiDog con la Tastiera
===================================

In questo esempio, utilizzeremo la tastiera per controllare PiDog. È possibile premere i tasti nel terminale per farlo muovere.

.. list-table:: 
    :widths: 25 50 25 50 25 50
    :header-rows: 1

    * - Tasti
      - Funzione
      - Tasti
      - Funzione
      - Tasti
      - Funzione  
    * - 1
      - sonnecchia
      - q
      - abbaia più forte
      - a
      - gira a sinistra
    * - 2
      - flessioni
      - w
      - avanti
      - s
      - indietro
    * - 3
      - ulula
      - e
      - ansima
      - d
      - gira a destra
    * - 4
      - contorce il corpo
      - r
      - scodinzola
      - f
      - scuote la testa
    * - 5
      - si gratta
      - t
      - scuote la testa
      - g
      - dà il cinque
    * - u
      - rotazione testa
      - U
      - rotazione testa+
      - z
      - sdraiato
    * - i
      - inclinazione testa
      - I
      - inclinazione testa+
      - x
      - in piedi
    * - o
      - rotazione testa
      - O
      - rotazione testa+
      - c
      - seduto
    * - j
      - oscillazione testa
      - J
      - oscillazione testa+
      - v
      - si stira
    * - k
      - inclinazione testa
      - K
      - inclinazione testa+
      - m
      - reset testa
    * - l
      - oscillazione testa
      - L
      - oscillazione testa+
      - W
      - trotto

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 11_keyboard_control.py

Dopo l’avvio del programma, vedrai un layout di tastiera stampato nel terminale. Ora puoi controllare PiDog utilizzando la tastiera nel terminale.



**Codice**



Trova il codice in |link_code_11_keyboard_control|.

