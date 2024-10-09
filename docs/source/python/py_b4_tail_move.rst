.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati come te.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotto e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti riservati sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

4. Movimento della Coda
============================

Di seguito sono riportate le funzioni che controllano il movimento della coda di PiDog. Questo metodo è simile a :ref:`py_b2_leg_move`.

.. code-block:: python

    Pidog.tail_move(target_angles, immediately=True, speed=50)

* ``target_angles`` : È un array bidimensionale composto da un array di 1 angolo del servo (definito gruppo di angoli) come elemento. Questi gruppi di angoli verranno utilizzati per controllare il movimento della coda. Se vengono definiti più gruppi di angoli, quelli non eseguiti verranno memorizzati nella cache.
* ``immediately`` : Quando si chiama la funzione, impostare questo parametro su ``True``, la cache verrà svuotata immediatamente per eseguire il nuovo gruppo di angoli; se impostato su ``False``, il nuovo gruppo di angoli viene aggiunto alla coda di esecuzione.
* ``speed`` : Velocità di esecuzione del gruppo di angoli.

**Il controllo del servo della coda di PiDog dispone anche di alcune funzioni di supporto:**

.. code-block:: python

    Pidog.is_tail_done()

Verifica se tutte le azioni della coda presenti nel buffer sono state eseguite.

.. code-block:: python

    Pidog.wait_tail_done()

Attende che tutte le azioni della coda nel buffer siano state completate.

.. code-block:: python

    Pidog.tail_stop()

Elimina tutte le azioni della coda nel buffer, fermando così il servomotore della coda.


**Ecco alcuni casi d'uso comuni:**

1. Scuotere la coda per 10 secondi.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.tail_move([[30],[-30]], immediately=False, speed=30)

    # mantenere per 10s
    time.sleep(10)

    my_dog.tail_stop()