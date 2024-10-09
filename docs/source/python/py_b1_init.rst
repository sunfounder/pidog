.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

1. Inizializzazione di PiDog
===============================

Le funzionalità di PiDog sono implementate nella classe ``Pidog``, il cui prototipo è mostrato qui di seguito.

.. code-block:: python

    Class: Pidog()

    __init__(leg_pins=DEFAULT_LEGS_PINS, 
            head_pins=DEFAULT_HEAD_PINS,
            tail_pin=DEFAULT_TAIL_PIN,
            leg_init_angles=None,
            head_init_angles=None,
            tail_init_angle=None)


PiDog deve essere istanziato in uno dei seguenti modi, come illustrato di seguito.

1. Ecco i passaggi più semplici per inizializzare PiDog.

.. code-block:: python

    # Importa la classe Pidog
    from pidog import Pidog

    # Istanzia un oggetto Pidog
    my_dog = Pidog()

2. PiDog è dotato di 12 servomotori, i cui angoli possono essere inizializzati durante l'istanza.

.. code-block:: python

    # Importa la classe Pidog
    from pidog import Pidog

    # Istanzia un oggetto Pidog con angoli di servo personalizzati
    my_dog = Pidog(leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )

Nella classe ``Pidog``, i servomotori sono suddivisi in tre gruppi.

* ``leg_init_angles``: In questo array, 8 valori definiscono gli angoli di otto servomotori, associati ai pin ``2, 3, 7, 8, 0, 1, 10, 11``. Dal diagramma, è possibile vedere la loro posizione esatta sul robot.

* ``head_init_angles``: Un array con 3 valori che controlla i servomotori della testa di PiDog per yaw, roll e pitch (``n. 4, 6, 5``), che reagiscono ai movimenti di rotazione, inclinazione o deflessione del corpo.

* ``tail_init_angle``: In questo array è presente un solo valore, dedicato al controllo del servomotore della coda (``n. 9``).

3. La classe ``Pidog`` permette di ridefinire i numeri seriali dei servomotori durante l'istanza, se l'ordine dei tuoi servo è diverso da quello predefinito.

.. code-block:: python

    # Importa la classe Pidog
    from pidog import Pidog

    # Istanzia un oggetto Pidog con pin personalizzati e angoli dei servomotori definiti
    my_dog = Pidog(leg_pins=[2, 3, 7, 8, 0, 1, 10, 11], 
                    head_pins=[4, 6, 5],
                    tail_pin=[9],
                    leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )