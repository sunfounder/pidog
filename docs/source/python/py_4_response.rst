.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

4. Risposta
==============

In questo progetto, PiDog interagirà con te in modo divertente.

Se allunghi la mano e tocchi la testa di PiDog dal davanti, abbaiarà in modo vigile.


.. image:: img/py_4-2.gif
    :width: 430


Ma se lo accarezzi da dietro, apprezzerà molto la tua attenzione.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/touch_head.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 4_response.py

Dopo aver avviato questo esempio, il modulo ultrasonico di PiDog rileverà se c'è un ostacolo di fronte.
Se rileva la tua mano, la luce respiratoria diventerà rossa, farà un passo indietro e abbaiarà.

Allo stesso tempo, il sensore tattile entrerà in funzione. Se accarezzi il sensore (non solo toccandolo), 
PiDog scuoterà la testa, scodinzolerà e mostrerà un'espressione di piacere.




**Codice**

.. note::
    Puoi **Modificare/Resettare/Copiare/Eseguire/Interrompere** il codice riportato qui sotto. Ma prima, devi accedere al percorso del codice sorgente come ``pidog\examples``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere l'effetto.

.. raw:: html

    <run></run>

.. code-block:: python


    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from math import sin
    from preset_actions import bark_action

    my_dog = Pidog()
    sleep(0.1)

    def lean_forward():
        my_dog.speak('angry', volume=80)
        bark_action(my_dog)
        sleep(0.2)
        bark_action(my_dog)
        sleep(0.8)
        bark_action(my_dog)

    def head_nod(step):
        y = 0
        r = 0
        p = 30
        angs = []
        for i in range(20):
            r = round(10*sin(i*0.314), 2)
            p = round(20*sin(i*0.314) + 10, 2)
            angs.append([y, r, p])

        my_dog.head_move(angs*step, immediately=False, speed=80)

    def alert():
        my_dog.do_action('stand', step_count=1, speed=90)
        my_dog.rgb_strip.set_mode('breath', color='pink', bps=1, brightness=0.8)
        while True:
            print(
                f'distance.value: {round(my_dog.ultrasonic.read_distance(), 2)} cm, touch {my_dog.dual_touch.read()}')
            # allerta
            if my_dog.ultrasonic.read_distance() < 15 and my_dog.ultrasonic.read_distance() > 1:
                my_dog.head_move([[0, 0, 0]], immediately=True, speed=90)
                my_dog.tail_move([[0]], immediately=True, speed=90)
                my_dog.rgb_strip.set_mode('bark', color='red', bps=2, brightness=0.8)
                my_dog.do_action('backward', step_count=1, speed=98)
                my_dog.wait_all_done()
                lean_forward()
                while len(my_dog.legs_action_buffer) > 0:
                    sleep(0.1)
                my_dog.do_action('stand', step_count=1, speed=90)
                sleep(0.5)
            # rilassato
            if my_dog.dual_touch.read() != 'N':
                if len(my_dog.head_action_buffer) < 2:
                    head_nod(1)
                    my_dog.do_action('wag_tail', step_count=10, speed=80)
                    my_dog.rgb_strip.set_mode('listen', color="#8A2BE2", bps=0.35, brightness=0.8)
            # calma
            else:
                my_dog.rgb_strip.set_mode('breath', color='pink', bps=1, brightness=0.8)
                my_dog.tail_stop()
            sleep(0.2)

    if __name__ == "__main__":
        try:
            alert()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()
