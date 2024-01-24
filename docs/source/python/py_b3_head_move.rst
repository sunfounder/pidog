3. Kopfbewegungen
======================

Die Steuerung von PiDogs Kopfservo wird durch die folgenden Funktionen implementiert.

.. code-block:: python

    Pidog.head_move(target_yrps, roll_comp=0, pitch_comp=0, immediately=True, speed=50)

* ``target_angles``: Es ist ein zweidimensionales Array, das aus einem Array von 3 Servowinkeln (als Winkelgruppe bezeichnet) als Elemente besteht. Diese Winkelgruppen werden verwendet, um die Winkel der Kopfservos zu steuern. Wenn mehrere Winkelgruppen geschrieben werden, werden die nicht ausgeführten Winkelgruppen im Cache gespeichert.
* ``roll_comp``: Bietet Winkelkompensation auf der Rollachse.
* ``pitch_comp``: Bietet Winkelkompensation auf der Pitchachse.
* ``immediately``: Wenn diese Funktion aufgerufen wird, setzen Sie diesen Parameter auf ``True``, der Cache wird sofort geleert, um die neu geschriebene Winkelgruppe auszuführen; wenn der Parameter auf ``False`` gesetzt wird, wird die neu geschriebene Winkelgruppe zur Ausführungswarteschlange hinzugefügt.
* ``speed``: Die Geschwindigkeit, mit der die Winkelgruppe ausgeführt wird.

**PiDogs Kopfservo-Steuerung hat auch einige unterstützende Funktionen:**


.. code-block:: python

    Pidog.is_head_done()

Ob alle Kopfaktionen im Puffer ausgeführt werden sollen

.. code-block:: python

    Pidog.wait_head_done()

Warten, bis alle Kopfaktionen im Puffer ausgeführt wurden

.. code-block:: python

    Pidog.head_stop()

Alle Kopfaktionen des Beins im Puffer löschen, um die Kopfservos anzuhalten

**Hier sind einige häufige Anwendungsfälle:**

1. Fünfmal nicken.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(5):
        my_dog.head_move([[0, 0, 30],[0, 0, -30]], speed=80)
        my_dog.wait_head_done()
        time.sleep(0.5)

2. 10 Sekunden den Kopf schütteln.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.head_move([[30, 0, 0],[-30, 0, 0]], immediately=False, speed=30)

    # 10s halten
    time.sleep(10)

    my_dog.head_move([[0, 0, 0]], immediately=True, speed=80)

3. Ob sitzend oder halb stehend, PiDog hält seinen Kopf beim Kopfschütteln auf gleicher Höhe.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # Aktionsliste
    shake_head = [[30, 0, 0],[-30, 0, 0]]
    half_stand_leg = [[45, 10, -45, -10, 45, 10, -45, -10]]
    sit_leg = [[30, 60, -30, -60, 80, -45, -80, 45]]

    while True:
        # Kopf schütteln im Halbstand
        my_dog.legs_move(half_stand_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=0, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)

        # Kopf schütteln im Sitzen
        my_dog.legs_move(sit_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=-30, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)
