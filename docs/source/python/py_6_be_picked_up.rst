.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

6. Hochgehoben werden
==============================

Versuchen Sie, Ihren PiDog vom Boden zu heben, PiDog wird sich fühlen, als könnte es fliegen, und es wird in einer Superman-Pose jubeln.

.. image:: img/py_6.gif

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 6_be_picked_up.py

Nachdem das Programm gestartet wurde, berechnet das 6-DOF-IMU-Modul ständig die Beschleunigung in vertikaler Richtung.
Wenn PiDog in einem Zustand der Schwerelosigkeit berechnet wird, nimmt PiDog eine Superman-Pose ein und jubelt.
Andernfalls wird angenommen, dass PiDog auf flachem Boden steht und eine Stehpose einnimmt.

**Code**

.. note::
    Sie können den unten stehenden Code **modifizieren/zurücksetzen/kopieren/ausführen/stoppen**. Bevor Sie das tun, müssen Sie jedoch zum Quellcode-Pfad wie ``pidog\examples`` gehen. Nachdem Sie den Code modifiziert haben, können Sie ihn direkt ausführen, um den Effekt zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep

    my_dog = Pidog()
    sleep(0.1)


    def fly():
        my_dog.rgb_strip.set_mode('boom', color='red', bps=3)
        my_dog.legs.servo_move([45, -45, 90, -80, 90, 90, -90, -90], speed=60)
        my_dog.do_action('wag_tail', step_count=10, speed=100)
        my_dog.speak('woohoo', volume=80)
        my_dog.wait_legs_done()
        sleep(1)

    def stand():
        my_dog.rgb_strip.set_mode('breath', color='green', bps=1)
        my_dog.do_action('stand', speed=60)
        my_dog.wait_legs_done()
        sleep(1)

    def be_picked_up():
        isUp = False
        upflag = False
        downflag = False

        stand()

        while True:
            ax = my_dog.accData[0]
            print('ax: %s, is up: %s' % (ax, isUp))

            # gravity : 1G = -16384
            if ax < -18000: # if down, acceleration is in the same direction as gravity, ax < -1G
                my_dog.body_stop()
                if upflag == False:
                    upflag = True
                if downflag == True:
                    isUp = False
                    downflag = False
                    stand()

            if ax > -13000: # if up, acceleration is the opposite of gravity, ax will > -1G
                my_dog.body_stop()
                if upflag == True:
                    isUp = True
                    upflag = False
                    fly()
                if downflag == False:
                    downflag = True

            sleep(0.02)


    if __name__ == "__main__":
        try:
            be_picked_up()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()