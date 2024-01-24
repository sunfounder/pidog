8. Entfernung lesen
======================

Durch das Ultraschallmodul in seinem Kopf kann PiDog Hindernisse vor ihm erkennen.

Ein Ultraschallmodul kann Objekte zwischen 2 und 400 cm Entfernung erkennen.

Mit der folgenden Funktion können Sie die Entfernung als Fließkommazahl lesen.

.. code-block:: python

    Pidog.ultrasonic.read_distance()

**Hier ist ein Beispiel für die Nutzung:**

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()
    while True:
        distance = my_dog.ultrasonic.read_distance()
        distance = round(distance, 2)
        print(f"Entfernung: {distance} cm")
        time.sleep(0.5)    
