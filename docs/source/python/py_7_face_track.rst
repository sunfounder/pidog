.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

7. Gesichtsverfolgung
========================

PiDog wird ruhig an Ort und Stelle sitzen. Sie klatschen Beifall, es sieht in Ihre Richtung, und wenn es Sie sieht, sagt es Hallo.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/face_track.mp4" type="video/mp4">
      Ihr Browser unterstützt das Video-Tag nicht.
   </video>

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 7_face_track.py

Nachdem Sie diesen Code ausgeführt haben, startet PiDog die Kamera und aktiviert die Gesichtserkennungsfunktion.
Sie können in Ihrem Browser ``http://+ PiDogs IP +/mjpg`` besuchen (wie meine ``http://192.168.18.138:9000/mjpg``), um das Bild der Kamera zu sehen.

Dann setzt sich PiDog hin und aktiviert das Soundrichtungssensor-Modul, um die Richtung Ihres Klatschens zu erkennen.
Wenn PiDog Klatschen (oder andere Geräusche) hört, dreht es seinen Kopf in Richtung der Schallquelle und versucht, Sie zu finden.

Wenn es Sie sieht (die Gesichtserkennung findet ein Objekt), wedelt es mit dem Schwanz und gibt ein Bellen von sich.

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

    def face_track():
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=True, web=True)
        Vilib.human_detect_switch(True)
        sleep(0.2)
        print('start')
        yaw = 0
        roll = 0
        pitch = 0
        flag = False
        direction = 0

        my_dog.do_action('sit', speed=50)
        my_dog.head_move([[yaw, 0, pitch]], pitch_comp=-40, immediately=True, speed=80)
        my_dog.wait_all_done()
        sleep(0.5)
        # Cleanup sound detection by servos moving
        if my_dog.ears.isdetected():    
            direction = my_dog.ears.read()

        while True:
            if flag == False:
                my_dog.rgb_strip.set_mode('breath', 'pink', bps=1)
            # If heard somthing, turn to face it
            if my_dog.ears.isdetected():
                flag = False
                direction = my_dog.ears.read()
                pitch = 0
                if direction > 0 and direction < 160:
                    yaw = -direction
                    if yaw < -80:
                        yaw = -80
                elif direction > 200 and direction < 360:
                    yaw = 360 - direction
                    if yaw > 80:
                        yaw = 80
                my_dog.head_move([[yaw, 0, pitch]], pitch_comp=-40, immediately=True, speed=80)
                my_dog.wait_head_done()
                sleep(0.05)

            ex = Vilib.detect_obj_parameter['human_x'] - 320
            ey = Vilib.detect_obj_parameter['human_y'] - 240
            people = Vilib.detect_obj_parameter['human_n']

            # If see someone, bark at him/her
            if people > 0 and flag == False:
                flag = True
                my_dog.do_action('wag_tail', step_count=2, speed=100)
                bark(my_dog, [yaw, 0, 0], pitch_comp=-40, volume=80)
                if my_dog.ears.isdetected():
                    direction = my_dog.ears.read()

            if ex > 15 and yaw > -80:
                yaw -= 0.5 * int(ex/30.0+0.5)

            elif ex < -15 and yaw < 80:
                yaw += 0.5 * int(-ex/30.0+0.5)

            if ey > 25:
                pitch -= 1*int(ey/50+0.5)
                if pitch < - 30:
                    pitch = -30
            elif ey < -25:
                pitch += 1*int(-ey/50+0.5)
                if pitch > 30:
                    pitch = 30

            print('direction: %s |number: %s | ex, ey: %s, %s | yrp: %s, %s, %s '
                % (direction, people, ex, ey, round(yaw, 2), round(roll, 2), round(pitch, 2)),
                end='\r',
                flush=True,
                )
            my_dog.head_move([[yaw, 0, pitch]], pitch_comp=-40, immediately=True, speed=100)
            sleep(0.05)


    if __name__ == "__main__":
        try:
            face_track()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            Vilib.camera_close()
            my_dog.close()
