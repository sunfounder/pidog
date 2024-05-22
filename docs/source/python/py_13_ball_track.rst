.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_ball_track:

13. Ballverfolgung
======================

PiDog wird ruhig an Ort und Stelle sitzen.
Wenn Sie einen roten Ball vor ihm platzieren, wird es aufstehen und dann dem Ball nachjagen.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/bull_track.mp4" type="video/mp4">
      Ihr Browser unterstützt das Video-Tag nicht.
   </video>

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 13_ball_track.py

Nachdem Sie diesen Code ausgeführt haben, startet PiDog die Kamera.
Sie können in Ihrem Browser ``http://+ PiDogs IP +/mjpg`` besuchen (wie meine ``http://192.168.18.138:9000/mjpg``), um das Bild der Kamera zu sehen.

**Code**

.. note::
    Sie können den unten stehenden Code **modifizieren/zurücksetzen/kopieren/ausführen/stoppen**. Bevor Sie das tun, müssen Sie jedoch zum Quellcode-Pfad wie ``pidog\examples`` gehen. Nachdem Sie den Code modifiziert haben, können Sie ihn direkt ausführen, um den Effekt zu sehen.

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
