.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_wake_up:

1. Aufwecken
===============

Dies ist PiDogs erstes Projekt. Es wird Ihren PiDog aus einem tiefen Schlaf wecken.

.. image:: img/py_wakeup.gif


**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

Nachdem der Code ausgeführt wurde,
wird PiDog die folgenden Aktionen nacheinander durchführen:

Sich strecken, sich drehen, sitzen, mit dem Schwanz wedeln, hecheln.



**Code**

.. note::
    Sie können den unten stehenden Code **modifizieren/zurücksetzen/kopieren/ausführen/stoppen**. Bevor Sie das tun, müssen Sie jedoch zum Quellcode-Pfad wie ``pidog\examples`` gehen. Nachdem Sie den Code modifiziert haben, können Sie ihn direkt ausführen, um den Effekt zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import pant
    from preset_actions import body_twisting

    my_dog = Pidog(head_init_angles=[0, 0, -30])
    sleep(1)

    def wake_up():
        # stretch
        my_dog.rgb_strip.set_mode('listen', color='yellow', bps=0.6, brightness=0.8)
        my_dog.do_action('stretch', speed=50)
        my_dog.head_move([[0, 0, 30]]*2, immediately=True)
        my_dog.wait_all_done()
        sleep(0.2)
        body_twisting(my_dog)
        my_dog.wait_all_done()
        sleep(0.5)
        my_dog.head_move([[0, 0, -30]], immediately=True, speed=90)
        # sit and wag_tail
        my_dog.do_action('sit', speed=25)
        my_dog.wait_legs_done()
        my_dog.do_action('wag_tail', step_count=10, speed=100)
        my_dog.rgb_strip.set_mode('breath', color=[245, 10, 10], bps=2.5, brightness=0.8)
        pant(my_dog, pitch_comp=-30, volume=80)
        my_dog.wait_all_done()
        # hold
        my_dog.do_action('wag_tail', step_count=10, speed=30)
        my_dog.rgb_strip.set_mode('breath', 'pink', bps=0.5)
        while True:
            sleep(1)

    if __name__ == "__main__":
        try:
            wake_up()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()
