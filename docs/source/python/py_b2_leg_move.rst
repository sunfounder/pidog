.. _py_b2_leg_move:

2. Beinbewegungen
==========================

Die Beinbewegungen von PiDog werden durch die folgenden Funktionen implementiert.

.. code-block:: python

    Pidog.legs_move(target_angles, immediately=True, speed=50)

* ``target_angles``: Es ist ein zweidimensionales Array, das aus einem Array von 8 Servowinkeln (als Winkelgruppe bezeichnet) als Elemente besteht. Diese Winkelgruppen werden verwendet, um die Winkel der 8 Fußservos zu steuern. Wenn mehrere Winkelgruppen geschrieben werden, werden die nicht ausgeführten Winkelgruppen im Cache gespeichert.
* ``immediately`` : Wenn diese Funktion aufgerufen wird, setzen Sie diesen Parameter auf ``True``, der Cache wird sofort geleert, um die neu geschriebene Winkelgruppe auszuführen; wenn der Parameter auf ``False`` gesetzt wird, wird die neu geschriebene Winkelgruppe zur Ausführungswarteschlange hinzugefügt.
* ``speed`` : Die Geschwindigkeit, mit der die Winkelgruppe ausgeführt wird.

**Einige häufige Verwendungen sind unten aufgeführt:**

1.  Sofortige Aktion.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # halb stehen
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)   


2. Fügen Sie einige Winkelgruppen zur Ausführungswarteschlange hinzu.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # halb stehen
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # mehrere Aktionen
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70],
                        [90, -30, -90, 30, 80, 70, -80, -70],
                        [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   

3. Wiederholungen innerhalb von 10 Sekunden durchführen.


.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # halb stehen
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # Liegestütz-Vorbereitung
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], immediately=False, speed=20)

    # Liegestütz
    for _ in range(99):
        my_dog.legs_move([[90, -30, -90, 30, 80, 70, -80, -70],
                            [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   

    # 10s halten
    time.sleep(10)

    # stoppen und halb stehen
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], immediately=True, speed=50)  


**PiDogs Beinkontrolle hat auch die folgenden Funktionen, die zusammen verwendet werden können:**

.. code-block:: python

    Pidog.is_legs_done()

Diese Funktion wird verwendet, um zu bestimmen, ob die Winkelgruppe im Cache ausgeführt wurde. Wenn ja, gibt sie ``True`` zurück; andernfalls ``False``.

.. code-block:: python

    Pidog.wait_legs_done()

Pausiert das Programm, bis die Winkelgruppen im Cache ausgeführt wurden.

.. code-block:: python

    Pidog.legs_stop() 

Leert die Winkelgruppe im Cache.
