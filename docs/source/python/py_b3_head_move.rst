.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

3. Movimento della Testa
============================

Il movimento del servo della testa di PiDog è controllato tramite le seguenti funzioni:

.. code-block:: python

    Pidog.head_move(target_yrps, roll_comp=0, pitch_comp=0, immediately=True, speed=50)

* ``target_angles``: È un array bidimensionale composto da un array di 3 angoli dei servo (definiti gruppo di angoli) come elementi. Questi gruppi di angoli verranno utilizzati per controllare i servo della testa. Se vengono definiti più gruppi di angoli, quelli non eseguiti verranno memorizzati nella cache.
* ``roll_comp``: Fornisce una compensazione angolare sull'asse del rollio.
* ``pitch_comp``: Fornisce una compensazione angolare sull'asse dell'inclinazione.
* ``immediately``: Se impostato su ``True``, la cache viene svuotata immediatamente per eseguire il nuovo gruppo di angoli; se impostato su ``False``, il nuovo gruppo di angoli viene aggiunto alla coda di esecuzione.
* ``speed``: Velocità di esecuzione del gruppo di angoli.

**Il controllo del servo della testa di PiDog dispone anche di alcune funzioni di supporto:**

.. code-block:: python

    Pidog.is_head_done()

Verifica se tutte le azioni della testa presenti nel buffer sono state eseguite.

.. code-block:: python

    Pidog.wait_head_done()

Attende che tutte le azioni della testa nel buffer siano state completate.

.. code-block:: python

    Pidog.head_stop()

Elimina tutte le azioni della testa nel buffer, fermando così i servomotori della testa.


**Ecco alcuni casi d'uso comuni:**

1. Esegui un cenno del capo cinque volte.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(5):
        my_dog.head_move([[0, 0, 30], [0, 0, -30]], speed=80)
        my_dog.wait_head_done()
        time.sleep(0.5)

2. Scuoti la testa per 10 secondi.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.head_move([[30, 0, 0], [-30, 0, 0]], immediately=False, speed=30)

    # mantenere per 10s
    time.sleep(10)

    my_dog.head_move([[0, 0, 0]], immediately=True, speed=80)

3. PiDog mantiene la testa orizzontale anche durante il movimento, sia che stia seduto sia che stia in semi-squat.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # lista delle azioni
    shake_head = [[30, 0, 0], [-30, 0, 0]]
    half_stand_leg = [[45, 10, -45, -10, 45, 10, -45, -10]]
    sit_leg = [[30, 60, -30, -60, 80, -45, -80, 45]]

    while True:
        # scuotere la testa in posizione di semi-squat
        my_dog.legs_move(half_stand_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=0, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)

        # scuotere la testa in posizione seduta
        my_dog.legs_move(sit_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=-30, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)
