.. note::

    Ciao, benvenuto nella Community SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con il supporto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni l'accesso anticipato alle nuove presentazioni di prodotti e anteprime.
    - **Sconti Esclusivi**: Approfitta di offerte speciali sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a giveaway e promozioni speciali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

8. Lettura della Distanza
=============================

Attraverso il Modulo Ultrasonico integrato nella sua testa, PiDog può rilevare gli ostacoli di fronte a sé.

Un modulo ultrasonico è in grado di rilevare oggetti tra 2 e 400 cm di distanza.

Con la seguente funzione, puoi leggere la distanza come un valore in virgola mobile:

.. code-block:: python

    Pidog.ultrasonic.read_distance()

**Ecco un esempio di utilizzo:**

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()
    while True:
        distance = my_dog.ultrasonic.read_distance()
        distance = round(distance,2)
        print(f"Distance: {distance} cm")
        time.sleep(0.5)
