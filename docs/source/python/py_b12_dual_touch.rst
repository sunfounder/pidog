.. note::

    Ciao, benvenuto nella Community SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

12. Accarezza la Testa del PiDog
======================================

Il modulo touch presente sulla testa di PiDog può rilevare come lo tocchi. Puoi utilizzare le seguenti funzioni per interagire con esso.

.. code-block:: python

   Pidog.dual_touch.read()

* Se tocchi il modulo da sinistra a destra (da davanti a dietro rispetto all'orientamento di PiDog), restituirà ``"LS"``.
* Se tocchi il modulo da destra a sinistra, restituirà ``"RS"``.
* Se tocchi il lato sinistro del modulo, restituirà ``"L"``.
* Se tocchi il lato destro del modulo, restituirà ``"R"``.
* Se il modulo non viene toccato, restituirà ``"N"``.

**Ecco un esempio di utilizzo:**

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()
    while True:
        touch_status = my_dog.dual_touch.read()
        print(f"touch_status: {touch_status}")
        time.sleep(0.5)

