6. Vordefinierte Aktionen ausführen
========================================

Einige häufig verwendete Aktionen wurden bereits in PiDogs Bibliothek vorprogrammiert.
Sie können die folgende Funktion aufrufen, um PiDog diese Aktionen direkt ausführen zu lassen.

.. code-block:: python

    Pidog.do_action(action_name, step_count=1, speed=50)

* ``action_name``: Aktionsname, es können die folgenden Strings geschrieben werden.

    * ``"sit"``
    * ``"half_sit"``
    * ``"stand"``
    * ``"lie"``
    * ``"lie_with_hands_out"``
    * ``"forward"``
    * ``"backward"``
    * ``"turn_left"``
    * ``"turn_right"``
    * ``"trot"``
    * ``"stretch"``
    * ``"pushup"``
    * ``"doze_off"``
    * ``"nod_lethargy"``
    * ``"shake_head"``
    * ``"tilting_head_left"``
    * ``"tilting_head_right"``
    * ``"tilting_head"``
    * ``"head_bark"``
    * ``"head_up_down"``
    * ``"wag_tail"``

* ``step_count``: Wie oft diese Aktion ausgeführt werden soll.
* ``speed``: Wie schnell die Aktion ausgeführt werden soll.

**Hier ist ein Beispiel für die Nutzung:**

1. Zehn Liegestütze machen, dann auf dem Boden sitzen und süß wirken.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # Liegestütze
        my_dog.do_action("halb_sitzen", speed=60)
        my_dog.do_action("liegestütze", step_count=10, speed=60)
        my_dog.wait_all_done()
        
        # süß wirken
        my_dog.do_action("sitzen", speed=60)
        my_dog.do_action("schwanz_wedeln", step_count=100, speed=90)
        my_dog.do_action("kopf_neigen", step_count=5, speed=20)
        my_dog.wait_head_done()
        
        my_dog.stop_and_lie()

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mFEHLER: {e}\033[m")
    finally:
        print("Schließe ...")
        my_dog.close()    
