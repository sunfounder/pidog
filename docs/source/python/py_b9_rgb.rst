9. PiDog RGB Strip
========================

There is an RGB Strip on PiDog's chest, which PiDog can use to express emotions.

You can call the following function to control it.

.. code-block:: python

    Pidog.rgb_strip.set_mode(style='breath', color='white', bps=1, brightness=1):

* ``style`` : The lighting display mode of RGB Strip, the following are its available values.

  * ``breath``
  * ``boom``
  * ``bark``

* ``color`` : The lights of the RGB Strip show the colors. You can enter 16-bit RGB values, such as ``#a10a0a``, or the following color names.

  * ``"white"``
  * ``"black"``
  * ``"white"``
  * ``"red"``
  * ``"yellow"``
  * ``"green"``
  * ``"blue"``
  * ``"cyan"``
  * ``"magenta"``
  * ``"pink"``

* ``brightness`` : RGB Strip lights display brightness, you can enter a floating-point value from 0 to 1, such as ``0.5``.

* ``delay`` : Float, display animation speed, the smaller the value, the faster the change.

Use the following statement to disable RGB Striping.

.. code-block:: python

    Pidog.rgb_strip.close()


Here are examples of their use:

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    while True:
        # style="breath", color="pink"
        my_dog.rgb_strip.set_mode(style="breath", color='pink')
        time.sleep(3)

        # style:"boom", color="#a10a0a"
        my_dog.rgb_strip.set_mode(style="bark", color="#a10a0a")
        time.sleep(3)

        # style:"boom", color="#a10a0a", brightness=0.5, bps=2.5
        my_dog.rgb_strip.set_mode(style="boom", color="#a10a0a", bps=2.5, brightness=0.5)
        time.sleep(3)

        # close
        my_dog.rgb_strip.close()
        time.sleep(2)

