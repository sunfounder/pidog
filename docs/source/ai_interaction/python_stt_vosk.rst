.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

16. STT with Vosk (Offline)
==============================================

Vosk is a lightweight speech-to-text (STT) engine that supports many languages and runs fully **offline** on Raspberry Pi.  
You only need internet access once to download a language model. After that, everything works without a network connection.  

In this lesson, we will install Vosk and test it with a language model of your choice.

Before You Start
----------------

Make sure you've completed:

* :ref:`install_all_modules` — Install ``robot-hat``, ``vilib``, ``pidog`` modules, then run the script ``i2samp.sh``.

.. _test_vosk:

1. Test Vosk
--------------------------

**Steps to try it out**:

#. Create a new file:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_stt_vosk.py

#. Copy the example code into it. Press ``Ctrl+X``, then ``Y``, and ``Enter`` to save and exit.

   .. code-block:: python

      from pidog.stt import Vosk

      vosk = Vosk(language="en-us")

      print(vosk.available_languages)

      while True:
          print("Say something")
          result = vosk.listen(stream=False)
          print(result)

#. Run the program:

   .. code-block:: bash

      sudo python3 test_stt_vosk.py

#. The first time you run this code with a new language, Vosk will **automatically download the language model** (by default it will download the **small** version).  
   At the same time, it will also print out the list of supported languages. Then you will see:

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   This means:

   * The model file (``vosk-model-small-en-us-0.15``) has been downloaded.  
   * The list of supported languages has been printed.  
   * The system is now listening — say something into the Pidog microphone, and the recognized text will appear in the terminal.

   **Tips**:

   * Keep the microphone about 15–30 cm away.  
   * Pick a model that matches your language and accent.  

**Streaming Mode (optional)**

You can also stream speech continuously to see partial results as you speak:

.. code-block:: python

   from pidog.stt import Vosk

   vosk = Vosk(language="en-us")

   while True:
       print("Say something")
       for result in vosk.listen(stream=True):
           if result["done"]:
               print(f"final:   {result['final']}")
           else:
               print(f"partial: {result['partial']}", end="\r", flush=True)

Troubleshooting
-----------------

* **The microphone records nothing, or arecord fails with "No such file or directory"**

  The card/device number is probably wrong, or the input is muted. First list the recording devices:

  .. code-block:: bash

     arecord -l

  Look for your USB microphone and note its numbers, then record a test sample, replacing ``1,0`` with the numbers you found:

  .. code-block:: bash

     arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

  If the recording is still silent, open the mixer:

  .. code-block:: bash

     alsamixer

  Press **F6** to select your USB microphone, unmute **Mic** / **Capture** (**[OO]** instead of **[MM]**), and raise the level with ↑ / ↓.

* **Vosk does not recognize speech**

  * Make sure the **language code** matches your model (e.g. ``en-us`` for English, ``zh-cn`` for Chinese).  
  * Keep the microphone 15–30 cm away and avoid background noise.  
  * Speak clearly and slowly.

* **High latency / slow recognition**

  * The default auto-download is a **small model** (faster, but less accurate).  
  * If it’s still slow, close other programs to free CPU.  
