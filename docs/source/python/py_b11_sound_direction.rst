
11. Schallerkennung in Richtung
===================================

Der PiDog verfügt über ein Soundrichtungssensor-Modul, das erkennt, aus welcher Richtung der Ton kommt, und wir können es durch Klatschen in seiner Nähe auslösen.

**Die Verwendung dieses Moduls ist so einfach wie das Aufrufen dieser Funktionen.**

.. code-block:: python

    Pidog.ears.isdetected()

Gibt ``True`` zurück, wenn ein Ton erkannt wird, andernfalls ``False``.

.. code-block:: python

    Pidog.ears.read()

Diese Funktion gibt die Richtung der Schallquelle zurück, im Bereich von 0 bis 359; wenn der Ton von vorne kommt, gibt es 0 zurück; wenn er von rechts kommt, gibt es 90 zurück.

**Ein Beispiel, wie man dieses Modul verwendet, sieht wie folgt aus:**

.. code-block:: python

    from pidog import Pidog

    my_dog = Pidog()

    while True:
        if my_dog.ears.isdetected():
            direction = my_dog.ears.read()
            print(f"Schallrichtung: {direction}")

