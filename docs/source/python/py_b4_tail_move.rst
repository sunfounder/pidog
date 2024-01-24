4. Schwanzbewegungen
=============================

Folgend sind die Funktionen, die PiDogs Schwanz steuern. Diese Funktion ähnelt :ref:`py_b2_leg_move`.

.. code-block:: python

    Pidog.tail_move(target_angles, immediately=True, speed=50)

* ``target_angles``: Es ist ein zweidimensionales Array, das aus einem Array von 1 Servowinkel (als Winkelgruppe bezeichnet) als Elemente besteht. Diese Winkelgruppen werden verwendet, um die Winkel des Schwanzservos zu steuern. Wenn mehrere Winkelgruppen geschrieben werden, werden die nicht ausgeführten Winkelgruppen im Cache gespeichert.
* ``immediately``: Wenn diese Funktion aufgerufen wird, setzen Sie diesen Parameter auf ``True``, der Cache wird sofort geleert, um die neu geschriebene Winkelgruppe auszuführen; wenn der Parameter auf ``False`` gesetzt wird, wird die neu geschriebene Winkelgruppe zur Ausführungswarteschlange hinzugefügt.
* ``speed``: Die Geschwindigkeit, mit der die Winkelgruppe ausgeführt wird.

**PiDogs Schwanzservo-Steuerung hat auch einige unterstützende Funktionen:**

.. code-block:: python

    Pidog.is_tail_done()

ob alle Schwanzaktionen im Puffer ausgeführt werden sollen

.. code-block:: python

    Pidog.wait_tail_done()

warten, bis alle Schwanzaktionen im Puffer ausgeführt wurden

.. code-block:: python

    Pidog.tail_stop()

alle Schwanzaktionen des Beins im Puffer löschen, um den Schwanzservo anzuhalten

**Hier sind einige häufige Anwendungsfälle:**

1. Schwanz wedeln für 10 Sekunden.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.tail_move([[30],[-30]], immediately=False, speed=30)

    # 10s halten
    time.sleep(10)

    my_dog.tail_stop()
