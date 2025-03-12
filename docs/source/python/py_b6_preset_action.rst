.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a tanti altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con il supporto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue abilità.
    - **Anteprime Esclusive**: Ottieni accesso anticipato alle nuove presentazioni di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a giveaway e promozioni speciali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

6. Esegui Azioni Predefinite
================================

Alcune azioni comunemente utilizzate sono già state pre-scritte nella libreria di PiDog.
Puoi richiamare la funzione seguente per far eseguire queste azioni direttamente a PiDog.

.. code-block:: python

    Pidog.do_action(action_name, step_count=1, speed=50)

* ``action_name`` : Nome dell'azione, con le seguenti stringhe disponibili.

    * ``"sit"``
    * ``"half_sit"``
    * ``"stand"``
    * ``"lie"``
    * ``"lie_with_hands_out"``
    * ``"forward"``
    * ``"backward"``
    * ``"turn_left"``
    * ``"turn_right"``
    * ``"trot"``
    * ``"stretch"``
    * ``"push_up"``
    * ``"doze_off"``
    * ``"nod_lethargy"``
    * ``"shake_head"``
    * ``"tilting_head_left"``
    * ``"tilting_head_right"``
    * ``"tilting_head"``
    * ``"head_bark"``
    * ``"head_up_down"``
    * ``"wag_tail"``

* ``step_count`` : Numero di volte in cui eseguire questa azione.
* ``speed`` : Velocità con cui eseguire l'azione.

**Ecco un esempio di utilizzo:**

1. Esegui dieci flessioni, poi siediti a terra e fai il carino.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # flessioni
        my_dog.do_action("half_sit", speed=60)
        my_dog.do_action("push_up", step_count=10, speed=60)
        my_dog.wait_all_done()
        
        # fare il carino
        my_dog.do_action("sit", speed=60)
        my_dog.do_action("wag_tail", step_count=100,speed=90)
        my_dog.do_action("tilting_head", step_count=5, speed=20)
        my_dog.wait_head_done()
        
        my_dog.stop_and_lie()

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        print("closing ...")
        my_dog.close()    
