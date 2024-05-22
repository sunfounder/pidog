.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

5. Alle Aktionen stoppen
===========================

Nach den vorherigen Kapiteln können Sie feststellen, dass die Servo-Steuerung von PiDog in drei Threads unterteilt ist.
Dies ermöglicht es PiDog, Kopf und Körper gleichzeitig zu bewegen, sogar mit zwei Codezeilen.

**Hier sind einige Funktionen, die mit den drei Servo-Threads arbeiten:**

.. code-block:: python

    Pidog.wait_all_done()
    
Warten, bis alle Aktionen in den Puffern für Beinaktionen, Kopf und Schwanz ausgeführt wurden

.. code-block:: python

    Pidog.body_stop()
    
Stoppen Sie alle Aktionen von Beinen, Kopf und Schwanz

.. code-block:: python

    Pidog.stop_and_lie()
    
Stoppen Sie alle Aktionen von Beinen, Kopf und Schwanz und setzen Sie dann auf die "Liegen"-Pose zurück

.. code-block:: python

    Pidog.close()
    
Stoppen Sie alle Aktionen, setzen Sie auf die "Liegen"-Pose zurück und schließen Sie alle Threads, normalerweise beim Beenden eines Programms verwendet

**Hier sind einige häufige Anwendungen:**



.. code-block:: python
    :emphasize-lines: 10,36,45

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # Vorbereitung Liegestütz
        my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], speed=30)
        my_dog.head_move([[0, 0, 0]], pitch_comp=-10, speed=80) 
        my_dog.wait_all_done() # warten, bis alle Aktionen ausgeführt sind
        time.sleep(0.5)

        # Liegestütz 
        leg_pushup_action = [
            [90, -30, -90, 30, 80, 70, -80, -70],
            [45, 35, -45, -35, 80, 70, -80, -70],       
        ]
        head_pushup_action = [
            [0, 0, -30],
            [0, 0, 20],
        ]
        
        # Puffer mit Aktionen füllen
        for _ in range(50):
            my_dog.legs_move(leg_pushup_action, immediately=False, speed=50)
            my_dog.head_move(head_pushup_action, pitch_comp=-10, immediately=False, speed=50)
        
        # Pufferlänge anzeigen
        print(f"Länge des Beinpuffers (Start): {len(my_dog.legs_action_buffer)}")
        
        # 5 Sekunden halten & Pufferlänge anzeigen
        time.sleep(5)
        print(f"Länge des Beinpuffers (5s): {len(my_dog.legs_action_buffer)}")
        
        # Aktion stoppen & Pufferlänge anzeigen
        my_dog.stop_and_lie()
        print(f"Länge des Beinpuffers (Stopp): {len(my_dog.legs_action_buffer)}")

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mFEHLER: {e}\033[m")
    finally:
        print("Schließe ...")
        my_dog.close() # alle Servo-Threads schließen
