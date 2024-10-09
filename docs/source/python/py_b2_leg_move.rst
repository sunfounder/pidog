.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_b2_leg_move:

2. Movimento delle Zampe
============================

I movimenti delle zampe di PiDog sono implementati tramite le seguenti funzioni:

.. code-block:: python

    Pidog.legs_move(target_angles, immediately=True, speed=50)

* ``target_angles``: È un array bidimensionale composto da un array di 8 angoli dei servo (chiamato gruppo di angoli) come elementi. Questi gruppi di angoli saranno utilizzati per controllare i servomotori delle 8 zampe. Se vengono definiti più gruppi di angoli, i gruppi non ancora eseguiti verranno memorizzati nella cache.
* ``immediately`` : Se questo parametro è impostato su ``True``, la cache viene svuotata immediatamente per eseguire il nuovo gruppo di angoli; se impostato su ``False``, il nuovo gruppo di angoli viene aggiunto alla coda di esecuzione.
* ``speed`` : Velocità di esecuzione del gruppo di angoli.

**Di seguito sono riportati alcuni usi comuni:**

1. Eseguire un'azione immediatamente.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # mezzo squat
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)   

2. Aggiungere più gruppi di angoli alla coda di esecuzione.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # mezzo squat
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # azioni multiple
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70],
                      [90, -30, -90, 30, 80, 70, -80, -70],
                      [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   

3. Eseguire ripetizioni per 10 secondi.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # mezzo squat
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # preparazione per i push-up
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], immediately=False, speed=20)

    # push-up
    for _ in range(99):
        my_dog.legs_move([[90, -30, -90, 30, 80, 70, -80, -70],
                          [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   

    # mantenere la posizione per 10 secondi
    time.sleep(10)

    # fermare e ritornare in mezzo squat
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], immediately=True, speed=50)  

**Il controllo delle zampe di PiDog include anche le seguenti funzioni utilizzabili insieme:**

.. code-block:: python

    Pidog.is_legs_done()

Questa funzione viene utilizzata per determinare se il gruppo di angoli nella cache è stato eseguito. Se sì, restituisce ``True``; altrimenti restituisce ``False``.

.. code-block:: python

    Pidog.wait_legs_done()

Sospende il programma fino a quando i gruppi di angoli nella cache non sono stati eseguiti.

.. code-block:: python

    Pidog.legs_stop() 

Svuota il gruppo di angoli nella cache.
