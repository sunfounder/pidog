.. note::

    Ciao, benvenuto nella Community SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e agli altri membri della community.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per perfezionare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima alle nuove presentazioni di prodotto e alle anticipazioni.
    - **Sconti Esclusivi**: Approfitta di sconti speciali sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a giveaway e promozioni speciali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

9. Striscia RGB di PiDog
============================

PiDog è dotato di una striscia RGB sul petto, che utilizza per esprimere diverse emozioni.

È possibile controllarla utilizzando la seguente funzione:

.. code-block:: python

    Pidog.rgb_strip.set_mode(style='breath', color='white', bps=1, brightness=1):

* ``style`` : Modalità di visualizzazione della striscia RGB. Ecco i valori disponibili:

  * ``breath``
  * ``boom``
  * ``bark``

* ``color`` : Colore della striscia RGB. Puoi inserire valori RGB a 16 bit, come ``#a10a0a``, o scegliere uno dei seguenti nomi di colore:

  * ``"white"``
  * ``"black"``
  * ``"white"``
  * ``"red"``
  * ``"yellow"``
  * ``"green"``
  * ``"blue"``
  * ``"cyan"``
  * ``"magenta"``
  * ``"pink"``

* ``brightness`` : Livello di luminosità della striscia RGB. Puoi inserire un valore in virgola mobile da 0 a 1, come ad esempio ``0.5``.

* ``bps`` : Float, velocità di animazione della visualizzazione; più piccolo è il valore, più rapido sarà il cambiamento.

Utilizza la seguente istruzione per disabilitare la striscia RGB:

.. code-block:: python

    Pidog.rgb_strip.close()

Ecco alcuni esempi di utilizzo:

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    while True:
        # style="breath", color="pink"
        my_dog.rgb_strip.set_mode(style="breath", color='pink')
        time.sleep(3)

        # style="bark", color="#a10a0a"
        my_dog.rgb_strip.set_mode(style="bark", color="#a10a0a")
        time.sleep(3)

        # style="boom", color="#a10a0a", brightness=0.5, bps=2.5
        my_dog.rgb_strip.set_mode(style="boom", color="#a10a0a", bps=2.5, brightness=0.5)
        time.sleep(3)

        # close
        my_dog.rgb_strip.close()
        time.sleep(2)

