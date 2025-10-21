.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

14. Voice Prompt Car with Espeak and Pico2Wave
=================================================

In this lesson, we'll use two built-in text-to-speech (TTS) engines on Raspberry Pi — **Espeak** and **Pico2Wave** — to make the Pidog talk.  

These two engines are both simple and run offline, but they sound quite different:

* **Espeak**: very lightweight and fast, but the voice is robotic. You can adjust speed, pitch, and volume.  
* **Pico2Wave**: produces a smoother and more natural voice than Espeak, but has fewer options to configure.  

You'll hear the difference in **voice quality** and **features**.  

----

Before You Start
----------------

Make sure you‘ve completed:

* :ref:`install_all_modules` — Install ``robot-hat``, ``vilib``, ``pidog`` modules, then run the script ``i2samp.sh``.

Testing Espeak
--------------------

Espeak is a lightweight TTS engine included in Raspberry Pi OS.  
Its voice sounds robotic, but it is highly configurable: you can adjust volume, pitch, speed, and more.  

**Steps to try it out**:

* Create a new file with the command:

  .. code-block:: bash
  
      cd ~/pidog/examples
      sudo nano test_tts_espeak.py

* Then copy the example code into it. Press ``Ctrl+X``, then ``Y``, and finally ``Enter`` to save and exit.

  .. code-block:: python
  
      from pidog.tts import Espeak

      tts = Espeak()
  
      # Optional voice tuning
      # tts.set_amp(100)   # 0 to 200
      # tts.set_speed(150) # 80 to 260
      # tts.set_gap(5)     # 0 to 200
      # tts.set_pitch(50)  # 0 to 99

      # Quick hello (sanity check)
      tts.say("Hello! I'm Espeak TTS.")
  
* Run the program with:

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* You should hear the Pidog say: “Hello! I'm Espeak TTS.”
* Uncomment the voice tuning lines in the code to experiment with how ``amp``, ``speed``, ``gap``, and ``pitch`` affect the sound.

----

Testing Pico2Wave
---------------------

Pico2Wave produces a more natural, human-like voice than Espeak.  
It's simpler to use but less flexible — you can only change the language, not the pitch or speed.

**Steps to try it out**:

* Create a new file with the command:

  .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_pico2wave.py

* Then copy the example code into it. Press ``Ctrl+X``, then ``Y``, and finally ``Enter`` to save and exit.

  .. code-block:: python
  
      from pidog.tts import Pico2Wave
  
      tts = Pico2Wave()
  
      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
      # Quick hello (sanity check)
      tts.say("Hello! I'm Pico2Wave TTS.")

* Run the program with:

  .. code-block::

    sudo python3 test_tts_pico2wave.py

* You should hear the Pidog say: “Hello! I'm Pico2Wave TTS.”
* Try switching the language (for example, ``es-ES`` for Spanish) and listen to the difference.  

----

Troubleshooting
-------------------

* **No sound when running Espeak or Pico2Wave**

  * Check that your speakers/headphones are connected and volume is not muted.  
  * Run a quick test in terminal:

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  If you hear nothing, the issue is with audio output, not your Python code.

* **Espeak voice sounds too fast or too robotic**

  * Try adjusting the parameters in your code:

    .. code-block:: python

       tts.set_speed(120)   # slower
       tts.set_pitch(60)    # different pitch

* **Permission denied when running code**

  * Try running with ``sudo``:

    .. code-block:: bash

       sudo python3 test_tts_espeak.py


Comparison: Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Feature
     - Espeak
     - Pico2Wave
   * - Voice quality
     - Robotic, synthetic
     - More natural, human-like
   * - Languages
     - Default English
     - Fewer, but common ones
   * - Adjustable
     - Yes (speed, pitch, etc.)
     - No (only language)
   * - Performance
     - Very fast, lightweight
     - Slightly slower, heavier

