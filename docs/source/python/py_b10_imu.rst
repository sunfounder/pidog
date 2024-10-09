.. note::

    Ciao, benvenuto nella Community SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

10. Lettura del Modulo IMU
==============================

Grazie al Modulo IMU a 6 DOF, PiDog può rilevare se è su una pendenza o se viene sollevato.

Il Modulo IMU a 6 DOF è dotato di un accelerometro a 3 assi e di un giroscopio a 3 assi, che permettono di misurare l'accelerazione e la velocità angolare lungo le tre direzioni.

.. note::

    Prima di utilizzare il modulo, assicurati che sia montato correttamente. L'etichetta sul modulo ti indicherà se è installato al contrario.

**Puoi leggere l'accelerazione utilizzando la seguente istruzione:**

.. code-block:: python

    ax, ay, az = Pidog.accData

Quando PiDog è posizionato in orizzontale, l'accelerazione sull'asse x (ossia ax) dovrebbe essere vicina all'accelerazione di gravità (1g), con un valore di -16384. I valori sugli assi y e z sono prossimi a 0.

**Utilizza il comando seguente per leggere la velocità angolare:**

.. code-block:: python

    gx, gy, gz = my_dog.gyroData

Nel caso in cui PiDog sia posizionato in orizzontale, tutti e tre i valori dovrebbero essere prossimi a 0.


**Ecco alcuni esempi su come utilizzare il Modulo a 6 DOF:**

1. Lettura in tempo reale dell'accelerazione e della velocità angolare.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    my_dog.do_action("pushup", step_count=10, speed=20)

    while True:
        ax, ay, az = my_dog.accData
        gx, gy, gz = my_dog.gyroData
        print(f"accData: {ax/16384:.2f} g ,{ay/16384:.2f} g, {az/16384:.2f} g       gyroData: {gx} °/s, {gy} °/s, {gz} °/s")
        time.sleep(0.2)
        if my_dog.is_legs_done():
            break

    my_dog.stop_and_lie()

    my_dog.close()

2. Calcolo dell'angolo di inclinazione del corpo di PiDog.

.. code-block:: python

    from pidog import Pidog
    import time
    import math

    my_dog = Pidog()

    while True:
        ax, ay, az = my_dog.accData
        body_pitch = math.atan2(ay,ax)/math.pi*180%360-180
        print(f"Body Degree: {body_pitch:.2f} °" )
        time.sleep(0.2)

    my_dog.close()

3. Mantenimento della testa livellata mentre PiDog è inclinato.

.. code-block:: python

    from pidog import Pidog
    import time
    import math

    my_dog = Pidog()

    while True:
        ax, ay, az = my_dog.accData
        body_pitch = math.atan2(ay,ax)/math.pi*180%360-180
        my_dog.head_move([[0, 0, 0]], pitch_comp=-body_pitch, speed=80)
        time.sleep(0.2)

    my_dog.close()