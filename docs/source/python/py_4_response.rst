.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

4. Reaktion
================

In diesem Projekt wird PiDog auf interessante Weise mit Ihnen interagieren.

Wenn Sie von vorne nach PiDogs Kopf greifen und ihn festhalten, wird es wachsam bellen.

.. image:: img/py_4-2.gif
    :width: 430

Aber wenn Sie von hinten her nach seinem Kopf greifen und ihn streicheln, wird es das sehr genießen.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/touch_head.mp4" type="video/mp4">
      Ihr Browser unterstützt das Video-Tag nicht.
   </video>

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 4_response.py

Nachdem Sie dieses Beispiel ausgeführt haben, wird PiDogs Ultraschallmodul erkennen, ob sich ein Hindernis voraus befindet.
Wenn es Ihre Hand erkennt, leuchtet das Atemlicht rot auf, PiDog macht einen Schritt zurück und bellt.

Gleichzeitig wird auch der Berührungssensor arbeiten. Wenn der Berührungssensor gestreichelt wird (nicht nur berührt), 
wird PiDog mit dem Kopf schütteln, mit dem Schwanz wedeln und ein zufriedenes Aussehen zeigen.

**Code**

.. note::
    Sie können den unten stehenden Code **modifizieren/zurücksetzen/kopieren/ausführen/stoppen**. Bevor Sie das tun, müssen Sie jedoch zum Quellcode-Pfad wie ``pidog\examples`` gehen. Nachdem Sie den Code modifiziert haben, können Sie ihn direkt ausführen, um den Effekt zu sehen.

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
            # alert
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
            # relax
            if my_dog.dual_touch.read() != 'N':
                if len(my_dog.head_action_buffer) < 2:
                    head_nod(1)
                    my_dog.do_action('wag_tail', step_count=10, speed=80)
                    my_dog.rgb_strip.set_mode('listen', color="#8A2BE2", bps=0.35, brightness=0.8)
            # calm
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
