.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ai_voice_assistant_car:

20. AI Voice Assistant Dog
===========================

This lesson transforms your Pidog into an **AI-powered voice assistant dog** 🐶.  
The robot can wake up to your voice, understand what you say, talk back with personality,  
and express its “feelings” through movements, gestures, and LED lighting effects.

You'll build a **fully interactive robotic companion** using:

* **LLM**: Large Language Model (e.g., OpenAI GPT or Doubao) for natural conversation.  
* **STT**: Speech-to-Text for voice recognition.  
* **TTS**: Text-to-Speech for expressive voice replies.  
* **Sensors + Actions**: Ultrasonic sensing, camera vision (optional), touch sensors, and built-in expressive movements.

----

Before You Start
----------------

Make sure you‘ve completed:

* :ref:`install_all_modules` — Install ``robot-hat``, ``vilib``, ``pidog`` modules, then run the script ``i2samp.sh``.
* :ref:`test_piper` — Check the supported languages of **Piper TTS**.  
* :ref:`test_vosk` — Check the supported languages of **Vosk STT**.  
* :ref:`py_online_llm` — This step is **very important**: obtain your **OpenAI** or **Doubao** API key, or the API key for any other supported LLM.

You should already have:

* A working **microphone** and **speaker** on your Pidog.  
* A **valid API key** stored in ``secret.py``.  
* A stable network connection (a **wired connection** is recommended for better stability).

----

Run the Example
---------------

Both language versions are placed in the same directory:

.. code-block:: bash

   cd ~/pidog/examples

**English version** (OpenAI GPT, instructions in English):

.. code-block:: bash

   sudo python3 20_voice_active_dog_gpt.py

* LLM: ``OpenAI GPT-4o-mini``  
* TTS: ``en_US-ryan-low`` (Piper)  
* STT: Vosk (``en-us``)

Wake word:

.. code-block::

   "Hey buddy"

---

**Chinese version** (Doubao, instructions in Chinese):

.. code-block:: bash

   sudo python3 20_voice_active_dog_doubao_cn.py

* LLM: ``Doubao-seed-1-6-250615``  
* TTS: ``zh_CN-huayan-x_low`` (Piper)  
* STT: Vosk (``cn``)

Wake word:

.. code-block::

   "你好 旺财"

.. note::

   You can modify the **wake word** and **robot name** in the code:
   ``NAME = "Buddy"`` or ``NAME = "旺财"``  
   ``WAKE_WORD = ["hey buddy"]`` or ``WAKE_WORD = ["你好 旺财"]``

----

What Will Happen
-----------------

When you run this example successfully:

* The robot **waits for the wake word** (e.g., “Hey Buddy”，“你好 旺财”).  
* When it hears the wake word:

  * The LED strip turns **pink (breathing)** as a wake-up cue.  
  * The robot greets you with the set wake response —  
    e.g., “Hi there!” (via Piper TTS).

* It then starts **listening to your voice** through Vosk STT (or accepts keyboard input if enabled).  

* After recognizing what you said, the system:

  * Captures a **camera frame** (because ``WITH_IMAGE = True``) and sends your message + image to the **LLM** (OpenAI ``gpt-4o-mini``).  
  * LED changes to **yellow (listening/processing)** while the model thinks.  
  * The model reply is split into two parts:

    - Text before ``ACTIONS:`` → spoken out loud.  
    - Keywords after ``ACTIONS:`` → mapped to robot motions.

  * The robot **executes those actions** via ``ActionFlow``.  
  * When actions finish, the robot **returns to SIT posture** and turns LEDs off.

* If the **ultrasonic sensor detects an obstacle** closer than 10 cm:

  - A message is injected: ``<<<Ultrasonic sense too close: {distance}cm>>>``  
  - The robot automatically backs up: ``ACTIONS: backward``  
  - **Image input is disabled** for this round.

* If the **touch sensor is triggered**:

  - For a **LIKE** touch (e.g., FRONT_TO_REAR):

    - Inject: ``<<<Touch style you like: FRONT_TO_REAR>>>``  
    - ``ACTIONS: nod`` (positive response)

  - For a **HATE** touch (e.g., REAR_TO_FRONT):

    - Inject: ``<<<Touch style you hate: REAR_TO_FRONT>>>``  
    - ``ACTIONS: backward`` (avoidance reaction)

* **LED lifecycle:**

  - ``on_start`` → SIT posture, LEDs off  
  - ``before_listen`` → cyan (ready)  
  - ``before_think`` → yellow (processing)  
  - ``before_say`` → pink (speaking)  
  - ``after_say`` / ``on_finish_a_round`` → SIT posture, LEDs off  
  - ``on_stop`` → stop action flow and close devices

**Example interaction**

.. code-block:: text

   You: Hey Buddy
   Robot: Hi there!

   You: What do you see in front of you?
   Robot: I can see a notebook and a blue mug on the table.
   ACTIONS: think

   You: Do a little nod for me.
   Robot: Of course. Watch my majestic nod.
   ACTIONS: nod

   (Front-to-rear touch on the head)
   Robot: Ooooh, that’s nice!
   ACTIONS: nod

   (Moving too close)
   Robot: Hey hey—too close! Backing up for safety.
   ACTIONS: backward


----

Switching to Other LLMs or TTS
------------------------------

You can easily switch to other LLMs, TTS, or STT languages with just a few edits:

* Supported LLMs:

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Check the supported languages of **Piper TTS**.  
* :ref:`test_vosk` — Check the supported languages of **Vosk STT**.  

To switch, simply modify the initialization part in the code:

.. code-block:: python

  from pidog.llm import OpenAI as LLM

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # Set models and languages
  TTS_MODEL = "en_US-ryan-low"
  STT_LANGUAGE = "en-us"

----

Troubleshooting
---------------

* **The robot doesn’t respond to wake word**  

  * Check if the microphone works.  
  * Ensure ``WAKE_ENABLE = True``.  
  * Adjust wake word to match your pronunciation.

* **No sound from the speaker**
 
  * Verify TTS model setup.  
  * Test Piper or Espeak manually.  
  * Check speaker connection and volume.

* **API Key error or timeout** 
 
  * Check your key in ``secret.py``.  
  * Ensure network connection.  
  * Confirm the LLM is supported.

* **Ultrasonic sensor keeps triggering unexpectedly.**  

  * Check sensor installation height and angle.  
  * Adjust the ``TOO_CLOSE`` distance threshold in code.
