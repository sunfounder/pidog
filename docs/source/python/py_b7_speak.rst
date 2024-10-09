.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con il supporto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato alle nuove presentazioni di prodotti e anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a giveaway e promozioni speciali durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

7. PiDog Parla
==========================

PiDog è in grado di emettere suoni, riproducendo in realtà file audio predefiniti.

Questi file audio sono salvati nel percorso ``pidog\sounds``, e puoi richiamarli utilizzando la seguente funzione:

.. code-block:: python

   Pidog.speak(name)

* ``name`` : Nome del file (senza suffisso), ad esempio ``"angry"``. ``Pidog`` fornisce i seguenti file audio predefiniti:

  * ``"angry"``
  * ``"confused_1"``
  * ``"confused_2"``
  * ``"confused_3"``
  * ``"growl_1"``
  * ``"growl_2"``
  * ``"howling"``
  * ``"pant"``
  * ``"single_bark_1"``
  * ``"single_bark_2"``
  * ``"snoring"``
  * ``"woohoo"``

**Esempio di utilizzo:**

.. code-block:: python

    # !/usr/bin/env python3
    ''' play sound effecfs
        Note that you need to run with "sudo"
    API:
        Pidog.speak(name, volume=100)
            play sound effecf in the file "../sounds"
            - name    str, file name of sound effect, no suffix required, eg: "angry"
            - volume  int, volume 0-100, default 100
    '''
    from pidog import Pidog
    import os
    import time

    # cambia la directory di lavoro
    abspath = os.path.abspath(os.path.dirname(__file__))
    os.chdir(abspath)

    my_dog = Pidog()

    print("\033[033mNote that you need to run with \"sudo\", otherwise there may be no sound.\033[m")

    # my_dog.speak("angry")
    # time.sleep(2)

    for name in os.listdir('../sounds'):
        name = name.split('.')[0] # rimuovi il suffisso
        print(name)
        my_dog.speak(name)
        # my_dog.speak(name, volume=50)
        time.sleep(3) # Nota: la durata di ogni effetto sonoro è diversa
    print("closing ...")
    my_dog.close()