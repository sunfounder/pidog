.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!


10. IMU-Lesen
================

Durch das 6-DOF-IMU-Modul kann PiDog feststellen, ob es sich auf einer Steigung befindet oder angehoben wird.

Das 6-DOF-IMU-Modul ist mit einem 3-Achsen-Beschleunigungssensor und einem 3-Achsen-Gyroskop ausgestattet, was die Messung von Beschleunigung und Winkelgeschwindigkeit in drei Richtungen ermöglicht.

.. note::

    Bevor Sie das Modul verwenden, stellen Sie sicher, dass es korrekt zusammengebaut ist. Das Etikett auf dem Modul gibt Ihnen Auskunft darüber, ob es umgekehrt ist.

**Sie können die Beschleunigung wie folgt auslesen:**

.. code-block:: python

   ax, ay, az = Pidog.accData

Wenn der PiDog horizontal platziert ist, sollte die Beschleunigung auf der x-Achse (d.h. ax) nahe der Erdbeschleunigung (1g) liegen, mit einem Wert von -16384. Die Werte auf der y-Achse und z-Achse sollten nahe bei 0 liegen.

**Verwenden Sie die folgende Methode, um die Winkelgeschwindigkeit auszulesen:**

.. code-block:: python

   gx, gy, gz = my_dog.gyroData

Im Fall, dass der PiDog horizontal platziert ist, sollten alle drei Werte nahe bei 0 liegen.

**Hier sind einige Beispiele dafür, wie das 6-DOF-Modul verwendet wird:**

1. Echtzeit-Beschleunigung und Winkelgeschwindigkeit auslesen

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    my_dog.do_action("Liegestütze", Schrittanzahl=10, Geschwindigkeit=20)

    while True:
        ax, ay, az = my_dog.accData
        gx, gy, gz = my_dog.gyroData
        print(f"accData: {ax/16384:.2f} g ,{ay/16384:.2f} g, {az/16384:.2f} g       gyroData: {gx} °/s, {gy} °/s, {gz} °/s")
        time.sleep(0.2)
        if my_dog.is_legs_done():
            break

    my_dog.stop_and_lie()

    my_dog.close()

2. Neigungswinkel des PiDog-Körpers berechnen

.. code-block:: python

    from pidog import Pidog
    import time
    import math

    my_dog = Pidog()

    while True:
        ax, ay, az = my_dog.accData
        Körperneigung = math.atan2(ay, ax) / math.pi * 180 % 360 - 180
        print(f"Körpergrad: {Körperneigung:.2f} °" )
        time.sleep(0.2)

    my_dog.close()

3. Während des Neigens hält PiDog seine Augen horizontal

.. code-block:: python

    from pidog import Pidog
    import time
    import math

    my_dog = Pidog()

    while True:
        ax, ay, az = my_dog.accData
        Körperneigung = math.atan2(ay, ax) / math.pi * 180 % 360 - 180
        my_dog.head_move([[0, 0, 0]], Pitch-Kompensation=-Körperneigung, Geschwindigkeit=80)
        time.sleep(0.2)

    my_dog.close()
