.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de Raspberry Pi, Arduino y ESP32 de SunFounder en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirte?**

    - **Soporte de Expertos**: Resuelve problemas postventa y supera desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y Compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede de forma anticipada a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!

5. Detener Todas las Acciones
===================================

Después de los capítulos anteriores, habrás notado que el control de los servos de PiDog se divide en tres hilos.
Esto permite que la cabeza y el cuerpo de PiDog se muevan simultáneamente, incluso con solo dos líneas de código.

**Aquí hay algunas funciones que gestionan estos tres hilos de servos:**


.. code-block:: python

    Pidog.wait_all_done()

Espera a que se ejecuten todas las acciones en los búferes de las patas, la cabeza y la cola.

.. code-block:: python

    Pidog.body_stop()

Detiene todas las acciones de las patas, la cabeza y la cola.

.. code-block:: python

    Pidog.stop_and_lie()

Detiene todas las acciones de las patas, la cabeza y la cola, y luego resetea a la pose de "acostado".

.. code-block:: python

    Pidog.close()

Detiene todas las acciones, restablece a la pose de "acostado" y cierra todos los hilos, generalmente usado al salir de un programa.


**A continuación, se presentan algunos casos de uso comunes:**

.. code-block:: python
    :emphasize-lines: 10,36,45

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # preparar para flexiones
        my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], speed=30)
        my_dog.head_move([[0, 0, 0]], pitch_comp=-10, speed=80) 
        my_dog.wait_all_done()  # esperar a que todas las acciones se completen
        time.sleep(0.5)

        # flexiones 
        leg_pushup_action = [
            [90, -30, -90, 30, 80, 70, -80, -70],
            [45, 35, -45, -35, 80, 70, -80, -70],       
        ]
        head_pushup_action = [
            [0, 0, -30],
            [0, 0, 20],
        ]
        
        # llenar los búferes de acción
        for _ in range(50):
            my_dog.legs_move(leg_pushup_action, immediately=False, speed=50)
            my_dog.head_move(head_pushup_action, pitch_comp=-10, immediately=False, speed=50)
        
        # mostrar longitud del búfer
        print(f"legs buffer length (start): {len(my_dog.legs_action_buffer)}")
        
        # mantener durante 5 segundos y mostrar longitud del búfer
        time.sleep(5)
        print(f"legs buffer length (5s): {len(my_dog.legs_action_buffer)}")
        
        # detener acciones y mostrar longitud del búfer
        my_dog.stop_and_lie()
        print(f"legs buffer length (stop): {len(my_dog.legs_action_buffer)}")

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        print("closing ...")
        my_dog.close()  # cerrar todos los hilos de servos
