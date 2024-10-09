.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a tanti altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con il supporto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue abilità.
    - **Anteprime Esclusive**: Ottieni accesso anticipato alle nuove presentazioni di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a giveaway e promozioni speciali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

5. Arresto di Tutte le Azioni
================================

Dopo i capitoli precedenti, avrai notato che il controllo dei servo di PiDog è suddiviso in tre thread distinti.
Questo consente alla testa e al corpo di PiDog di muoversi simultaneamente, anche con due linee di codice separate.

**Di seguito sono elencate alcune funzioni che operano sui tre thread dei servo:**

.. code-block:: python

    Pidog.wait_all_done()
    
Attende che tutte le azioni presenti nei buffer delle gambe, della testa e della coda siano completate.

.. code-block:: python

    Pidog.body_stop()
    
Ferma tutte le azioni di gambe, testa e coda.

.. code-block:: python

    Pidog.stop_and_lie()
    
Ferma tutte le azioni di gambe, testa e coda e ripristina la posizione in "lie".

.. code-block:: python

    Pidog.close()
    
Ferma tutte le azioni, ripristina la posizione in "lie" e chiude tutti i thread. Di solito viene usato per terminare un programma.


**Ecco alcuni esempi di utilizzo comune:**


.. code-block:: python
    :emphasize-lines: 10,36,45

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # preparazione push-up
        my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], speed=30)
        my_dog.head_move([[0, 0, 0]], pitch_comp=-10, speed=80) 
        my_dog.wait_all_done() # attende che tutte le azioni siano completate
        time.sleep(0.5)

        # push-up 
        leg_pushup_action = [
            [90, -30, -90, 30, 80, 70, -80, -70],
            [45, 35, -45, -35, 80, 70, -80, -70],       
        ]
        head_pushup_action = [
            [0, 0, -30],
            [0, 0, 20],
        ]
        
        # riempi i buffer delle azioni
        for _ in range(50):
            my_dog.legs_move(leg_pushup_action, immediately=False, speed=50)
            my_dog.head_move(head_pushup_action, pitch_comp=-10, immediately=False, speed=50)
        
        # mostra la lunghezza del buffer
        print(f"legs buffer length (start): {len(my_dog.legs_action_buffer)}")
        
        # mantieni per 5 secondi e mostra la lunghezza del buffer
        time.sleep(5)
        print(f"legs buffer length (5s): {len(my_dog.legs_action_buffer)}")
        
        # ferma le azioni e mostra la lunghezza del buffer
        my_dog.stop_and_lie()
        print(f"legs buffer length (stop): {len(my_dog.legs_action_buffer)}")

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        print("closing ...")
        my_dog.close() # chiude tutti i thread dei servo
