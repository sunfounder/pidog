
12. Streicheln Sie den Kopf des PiDog
=================================================

Der Touch-Schalter am Kopf des PiDog kann erkennen, wie Sie ihn berühren. Sie können die folgenden Funktionen aufrufen, um ihn zu verwenden.

.. code-block:: python

   Pidog.dual_touch.read()

* Berühren Sie das Modul von links nach rechts (von vorne nach hinten für die Ausrichtung des PiDog), es wird ``"LS"`` zurückgeben.
* Berühren Sie das Modul von rechts nach links, es wird ``"RS"`` zurückgeben.
* Berühren Sie das Modul, wenn die linke Seite des Moduls berührt wird, wird es ``"L"`` zurückgeben.
* Wenn die rechte Seite des Moduls berührt wird, wird es ``"R"`` zurückgeben.
* Wenn das Modul nicht berührt wird, wird es ``"N"`` zurückgeben.

**Hier ist ein Beispiel für seine Verwendung:**

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()
    while True:
        touch_status = my_dog.dual_touch.read()
        print(f"Berührungsstatus: {touch_status}")
        time.sleep(0.5)


