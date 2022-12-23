Sound Direction Detect
======================

The PiDog has a Sound Direction Sensor Module that detects where sound is coming from, and we can trigger it by clapping near it.

**Using this module is as simple as calling these functions.**

.. code-block:: python

    Pidog.ears.isdetected()

Returns ``True`` if sound is detected, ``False`` otherwise.

.. code-block:: python

    Pidog.ears.read()

This function returns the direction of the sound source, with a range of 0 to 359; if the sound comes from the front, it returns 0; if it comes from the right, it returns 90.

**An example of how to use this module is as follows:**

.. code-block:: python

    from pidog import Pidog

    my_dog = Pidog()

    while True:
        if my_dog.ears.isdetected():
            direction = my_dog.ears.read()
            print(f"sound direction: {direction}")





