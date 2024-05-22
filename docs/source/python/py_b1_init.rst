.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

1. PiDog-Initialisierung
============================

Die Funktionen von PiDog sind in der Klasse ``Pidog`` geschrieben, und der Prototyp dieser Klasse wird unten gezeigt.

.. code-block:: python

    Klasse: Pidog()

    __init__(leg_pins=DEFAULT_LEGS_PINS, 
            head_pins=DEFAULT_HEAD_PINS,
            tail_pin=DEFAULT_TAIL_PIN,
            leg_init_angles=None,
            head_init_angles=None,
            tail_init_angle=None)


PiDog muss auf eine der folgenden Arten instanziiert werden, wie unten gezeigt.

1. Folgend sind die einfachsten Schritte der Initialisierung.

.. code-block:: python

    # Pidog-Klasse importieren
    from pidog import Pidog

    # Instanziere einen Pidog
    my_dog = Pidog()

2. PiDog hat 12 Servos, die bei der Instanziierung initialisiert werden können.

.. code-block:: python

    # Pidog-Klasse importieren
    from pidog import Pidog

    # Instanziere einen Pidog mit benutzerdefinierten initialisierten Servowinkeln
    my_dog = Pidog(leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )

In der Klasse ``Pidog`` werden die Servos in drei Gruppen unterteilt.

* ``leg_init_angles``: In diesem Array bestimmen 8 Werte die Winkel von acht Servos, wobei die Servos (Pinnummern) die sie steuern, ``2, 3, 7, 8, 0, 1, 10, 11`` sind. Aus dem Faltblatt können Sie sehen, wo sich diese Servos befinden.

* ``head_init_angles``: Es gibt ein Array mit 3 Werten, Steuerungen für PiDog-Kopf Gieren, Rollen, Neigen Servos (``Nr. 4, 6, 5``) die auf Gieren, Rollen, Neigen oder Auslenkung des Körpers reagieren.

* ``tail_init_angle``: In diesem Array gibt es nur einen Wert, der sich der Steuerung des Schwanzservos widmet, das ist ``9``.


3. ``Pidog`` ermöglicht es Ihnen, die Seriennummer der Servos neu zu definieren, wenn Sie den Roboter instanziieren, falls Ihre Servoreihenfolge anders ist.

.. code-block:: python

    # Pidog-Klasse importieren
    from pidog import Pidog

    # Instanziere einen Pidog mit benutzerdefinierten initialisierten Pins & Servowinkeln
    my_dog = Pidog(leg_pins=[2, 3, 7, 8, 0, 1, 10, 11], 
                    head_pins=[4, 6, 5],
                    tail_pin=[9],
                    leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )
