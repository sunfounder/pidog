.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Sumérgete más a fondo en Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de Expertos**: Resuelve problemas postventa y supera desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y Compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede de forma anticipada a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Aprovecha descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

6. Realizar Acciones Predefinidas
=================================

Algunas de las acciones más utilizadas ya han sido preescritas en la biblioteca de PiDog.
Puedes usar la siguiente función para hacer que PiDog realice estas acciones directamente.

.. code-block:: python

    Pidog.do_action(action_name, step_count=1, speed=50)

* ``action_name`` : Nombre de la acción. Se pueden utilizar las siguientes cadenas:

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
    * ``"push_up"``
    * ``"doze_off"``
    * ``"nod_lethargy"``
    * ``"shake_head"``
    * ``"tilting_head_left"``
    * ``"tilting_head_right"``
    * ``"tilting_head"``
    * ``"head_bark"``
    * ``"head_up_down"``
    * ``"wag_tail"``

* ``step_count`` : Número de veces que se repetirá la acción.
* ``speed`` : Velocidad a la que se ejecutará la acción.

**Aquí tienes un ejemplo de uso:**

1. Realizar diez flexiones, luego sentarse en el suelo y hacer una pose adorable.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # flexiones
        my_dog.do_action("half_sit", speed=60)
        my_dog.do_action("push_up", step_count=10, speed=60)
        my_dog.wait_all_done()
        
        # pose adorable
        my_dog.do_action("sit", speed=60)
        my_dog.do_action("wag_tail", step_count=100,speed=90)
        my_dog.do_action("tilting_head", step_count=5, speed=20)
        my_dog.wait_head_done()
        
        my_dog.stop_and_lie()

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        print("closing ...")
        my_dog.close()
