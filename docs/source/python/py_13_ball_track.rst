.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_ball_track:

13. Inseguimento della Palla
=====================================

PiDog resterà seduto tranquillamente al suo posto.
Se metti una palla rossa davanti a lui, si alzerà e inizierà a inseguirla.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/bull_track.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 13_ball_track.py

Dopo aver eseguito questo codice, PiDog avvierà la videocamera.
Puoi visitare ``http://+ PiDog's IP +/mjpg`` (nel mio caso è ``http://192.168.18.138:9000/mjpg``) nel tuo browser per visualizzare l'immagine della videocamera.

**Codice**

.. note::
    Puoi **Modificare/Reimpostare/Copiare/Eseguire/Interrompere** il codice qui sotto. Ma prima devi posizionarti nel percorso del codice sorgente, come ``pidog\examples``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere il risultato.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from vilib import Vilib
    from preset_actions import bark

    my_dog = Pidog()

    sleep(0.1)

    STEP = 0.5

    def delay(time):
        my_dog.wait_legs_done()
        my_dog.wait_head_done()
        sleep(time)

    def ball_track():
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=True, web=True)
        Vilib.color_detect_switch(True)
        sleep(0.2)
        print('start')
        yaw = 0
        roll = 0
        pitch = 0
        flag = False
        direction = 0

        my_dog.do_action('stand', speed=50)
        my_dog.head_move([[yaw, 0, pitch]], immediately=True, speed=80)
        delay(0.5)

        while True:

            ball_x = Vilib.detect_obj_parameter['color_x'] - 320
            ball_y = Vilib.detect_obj_parameter['color_y'] - 240
            width = Vilib.detect_obj_parameter['color_w']

            if ball_x > 15 and yaw > -80:
                yaw -= STEP

            elif ball_x < -15 and yaw < 80:
                yaw += STEP

            if ball_y > 25:
                pitch -= STEP
                if pitch < - 40:
                    pitch = -40
            elif ball_y < -25:
                pitch += STEP
                if pitch > 20:
                    pitch = 20

            print(f"yaw: {yaw}, pitch: {pitch}, width: {width}")

            my_dog.head_move([[yaw, 0, pitch]], immediately=True, speed=100)
            if width == 0:
                pitch = 0
                yaw = 0
            elif width < 300:
                if my_dog.is_legs_done():
                    if yaw < -30:
                        print("turn right")
                        my_dog.do_action('turn_right', speed=98)
                    elif yaw > 30:
                        print("turn left")
                        my_dog.do_action('turn_left', speed=98)
                    else:
                        my_dog.do_action('forward', speed=98)
            sleep(0.02)


    if __name__ == "__main__":
        try:
            ball_track()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            Vilib.camera_close()
            my_dog.close()
