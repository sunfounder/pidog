.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

8. Liegestütze
=================

PiDog ist ein sportbegeisterter Roboter, der mit Ihnen Liegestütze machen wird.

.. image:: img/py_8.gif

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 8_pushup.py

Nachdem das Programm gestartet wurde, wird PiDog eine Plank-Position einnehmen und dann durch Liegestütze und Bellen zyklisch gehen.

**Code**

.. note::
    Sie können den unten stehenden Code **modifizieren/zurücksetzen/kopieren/ausführen/stoppen**. Bevor Sie das tun, müssen Sie jedoch zum Quellcode-Pfad wie ``pidog\examples`` gehen. Nachdem Sie den Code modifiziert haben, können Sie ihn direkt ausführen, um den Effekt zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import push_up, bark

    my_dog = Pidog()

    sleep(0.5)


    def main():
        my_dog.legs_move([[45, -25, -45, 25, 80, 70, -80, -70]], speed=50)
        my_dog.head_move([[0, 0, -20]], speed=90)
        my_dog.wait_all_done()
        sleep(0.5)
        bark(my_dog, [0, 0, -20])
        sleep(0.1)
        bark(my_dog, [0, 0, -20])

        sleep(1)
        my_dog.rgb_strip.set_mode("speak", color="blue", bps=2)
        while True:
            push_up(my_dog, speed=92)
            bark(my_dog, [0, 0, -40])
            sleep(0.4)


    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()