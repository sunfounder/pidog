.. note::

    Ciao, benvenuto nella Community SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

11. Rilevamento della Direzione del Suono
==============================================

PiDog è dotato di un modulo sensore di direzione del suono, che rileva la provenienza dei suoni, e può essere attivato battendo le mani vicino a lui.

**Utilizzare questo modulo è semplice, basta chiamare le seguenti funzioni.**

.. code-block:: python

    Pidog.ears.isdetected()

Restituisce ``True`` se viene rilevato un suono, altrimenti ``False``.

.. code-block:: python

    Pidog.ears.read()

Questa funzione restituisce la direzione della sorgente sonora, con un intervallo da 0 a 359; se il suono proviene frontalmente, restituisce 0; se proviene dalla destra, restituisce 90.

**Ecco un esempio di come utilizzare questo modulo:**

.. code-block:: python

    from pidog import Pidog

    my_dog = Pidog()

    while True:
        if my_dog.ears.isdetected():
            direction = my_dog.ears.read()
            print(f"sound direction: {direction}")





