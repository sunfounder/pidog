.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

7. PiDog Speak
==========================

PiDog can make sound, it is actually playing a piece of audio.

These audios are saved under ``pidog\sounds`` path, you can call the following function to play them.

.. code-block:: python

   Pidog.speak(name)

* ``name`` : Filename (without suffix), such as ``"angry"``. ``Pidog`` provides the following audio.

  * ``"angry"``
  * ``"confused_1"``
  * ``"confused_2"``
  * ``"confused_3"``
  * ``"growl_1"``
  * ``"growl_2"``
  * ``"howling"``
  * ``"pant"``
  * ``"single_bark_1"``
  * ``"single_bark_2"``
  * ``"snoring"``
  * ``"woohoo"``

**Here is an example of usage:**

.. code-block:: python

    # !/usr/bin/env python3
    ''' play sound effecfs
        Note that you need to run with "sudo"
    API:
        Pidog.speak(name, volume=100)
            play sound effecf in the file "../sounds"
            - name    str, file name of sound effect, no suffix required, eg: "angry"
            - volume  int, volume 0-100, default 100
    '''
    from pidog import Pidog
    import os
    import time

    # change working directory
    abspath = os.path.abspath(os.path.dirname(__file__))
    # print(abspath)
    os.chdir(abspath)

    my_dog = Pidog()

    print("\033[033mNote that you need to run with \"sudo\", otherwise there may be no sound.\033[m")

    # my_dog.speak("angry")
    # time.sleep(2)

    for name in os.listdir('../sounds'):
        name = name.split('.')[0] # remove suffix
        print(name)
        my_dog.speak(name)
        # my_dog.speak(name, volume=50)
        time.sleep(3) # Note that the duration of each sound effect is different
    print("closing ...")
    my_dog.close()