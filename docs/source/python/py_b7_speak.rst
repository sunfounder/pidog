PiDog Speak
==========================

PiDog can make sound, it is actually playing a piece of audio.

These audios are saved under ``pidog\sounds`` path, you can call the following function to play them.

.. code-block:: python

   Pidog.speak(name)

* ``name`` : Filename (without suffix), such as ``"angry"``. PiDog provides the following audio.

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

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        my_dog.do_action("sit", speed=60)
        my_dog.wait_all_done()
        time.sleep(0.5)

        my_dog.do_action("wag_tail", step_count=100,speed=20)
        my_dog.do_action("tilting_head", step_count=2, speed=20)
        my_dog.speak('confused_3')
        my_dog.wait_head_done()

        my_dog.stop_and_lie()

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        print("closing ...")
        my_dog.close()        