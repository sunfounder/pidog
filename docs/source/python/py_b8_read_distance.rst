Read Distance
=============

Through the Ultrasonic Module in its head, PiDog can detect obstacles ahead.

An ultrasonic module can detect objects between 2 and 400 cm away.

With the following function, you can read the distance as a floating point number.

.. code-block:: python

    Pidog.ultrasonic.read_distance()

**Here is an example of usage:**

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()
    while True:
        distance = my_dog.ultrasonic.read_distance()
        distance = round(distance,2)
        print(f"Distance: {distance} cm")
        time.sleep(0.5)    
