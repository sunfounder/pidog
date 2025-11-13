.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

19. Local Voice Chatbot with Ollama
===============================================

In this lesson, you will combine everything you've learned — **speech recognition (STT)**,  
**text-to-speech (TTS)**, and a **local LLM (Ollama)** — to build a fully offline **voice chatbot**  
that runs on your Pidog system.

The workflow is simple:

#. **Listen** — The microphone captures your speech and transcribes it with **Vosk**.  
#. **Think** — The text is sent to a local **LLM** running on Ollama (e.g., ``llama3.2:3b``).  
#. **Speak** — The chatbot answers aloud using **Piper TTS**.  

This creates a **hands-free conversational robot** that can understand and respond in real time.

----

Before You Start
----------------

Make sure you have prepared the following:

* :ref:`install_all_modules` — Install ``robot-hat``, ``vilib``, ``Pidog`` modules, then run the script ``i2samp.sh``.
* Tested **Piper TTS** (:ref:`test_piper`) and chosen a working voice model.  
* Tested **Vosk STT** (:ref:`test_vosk`) and chosen the right language pack (e.g., ``en-us``).  
* Installed **Ollama** (:ref:`download_ollama`) on your Pi or another computer, and downloaded a model such as ``llama3.2:3b`` (or a smaller one like ``moondream:1.8b`` if memory is limited).

----

Run the Code
--------------

#. Open the example script:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 19_voice_active_dog_ollama.py

#. Update the parameters as needed:

   * Update both ``ip`` and ``model`` to your own setup.  

     * ``ip``: If Ollama runs on the **same Pi**, use ``localhost``. If Ollama runs on another computer in your LAN, enable **Expose to network** in Ollama and set ``ip`` to that computer’s LAN IP.  
     * ``model``: Must exactly match the model name you downloaded/activated in Ollama.  

   * ``TTS_MODEL = "en_US-ryan-low"``: Replace with the Piper voice model you verified in :ref:`test_piper`.  
   * ``STT_LANGUAGE = "en-us"``: Change this to match your accent/language package (e.g., ``en-us``, ``zh-cn``, ``es``).  

#. Run the script:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo python3 19_voice_active_dog_ollama.py

Wake word:

.. code-block::

   "Hey buddy"

.. note::

   You can modify the **wake word** and **robot name** in the code:
   ``NAME = "Buddy"`` 

----

What Will Happen
-----------------

When you run this example successfully:

* The robot **waits for the wake word** (e.g., “Hey Buddy”).  
* When it hears the wake word:

  * The LED strip turns **pink (breathing)** as a wake-up cue.  
  * The robot greets you with the set wake response —  
    e.g., “Hi there!” (via Piper TTS).

* It then starts **listening to your voice** through Vosk STT (or accepts keyboard input if enabled).  

* After recognizing what you said, the system:

  * Sends your message to the **LLM** (Ollama with ``llama3.2:3b``).  
  * LED changes to **yellow (listening)** while processing.  
  * The model reply is split into two parts:

    - Text before ``ACTIONS:`` → spoken out loud.  
    - Keywords after ``ACTIONS:`` → mapped to robot motions.

  * The robot **executes those actions** via ``ActionFlow``.  
  * When actions finish, the robot **returns to SIT posture** and turns LEDs off.

* If the **ultrasonic sensor detects an obstacle** closer than 10 cm:

  - A message is injected: ``<<<Ultrasonic sense too close: {distance}cm>>>``  
  - The robot automatically backs up: ``ACTIONS: backward``  
  - Image input is disabled for this round.

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

   You: Do a little nod for me.
   Robot: Of course. Watch my majestic nod.
   ACTIONS: nod

   (Front-to-rear touch on the head)
   Robot: Ooooh, that’s nice!
   ACTIONS: nod

   (Moving too close)
   Robot: Hey hey—too close! Backing up for safety.
   ACTIONS: backward

Code
----

.. code-block:: python

    from pidog.llm import Ollama as LLM

    from pidog.dual_touch import TouchStyle
    from voice_active_dog import VoiceActiveDog

    # If Ollama runs on the same Raspberry Pi, use "localhost".
    # If it runs on another computer in your LAN, replace with that computer's IP address.
    llm = Ollama(
        ip="localhost",
        model="llama3.2:3b"   # you can replace with any model
    )

    # Robot name
    NAME = "Buddy"

    # Ultrasonic sensor sense too close distance in cm
    TOO_CLOSE = 10
    # Touch sensor trigger states, options:
    # - TouchStyle.REAR for rear touch sensor
    # - TouchStyle.FRONT for front touch sensor
    # - TouchStyle.REAR_TO_FRONT for slide from rear to front
    # - TouchStyle.FRONT_TO_REAR for slide from front to rear
    # Touch styles that the robot likes
    LIKE_TOUCH_STYLES = [TouchStyle.FRONT_TO_REAR]
    # Touch styles that the robot hates
    HATE_TOUCH_STYLES = [TouchStyle.REAR_TO_FRONT]

    # Enable image, need to set up a multimodal language model
    WITH_IMAGE = False

    # Set models and languages
    TTS_MODEL = "en_US-ryan-low"
    STT_LANGUAGE = "en-us"

    # Enable keyboard input
    KEYBOARD_ENABLE = True

    # Enable wake word
    WAKE_ENABLE = True
    WAKE_WORD = [f"hey {NAME.lower()}"]
    # Set wake word answer, set empty to disable
    ANSWER_ON_WAKE = "Hi there"

    # Welcome message
    WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

    # Set instructions
    INSTRUCTIONS = """
    You are a Raspberry Pi-based robotic dog developed by SunFounder, named Pidog (pronounced "Pie dog"). You possess powerful AI capabilities similar to JARVIS from Iron Man. You can have conversations with people and perform actions based on the context of the conversation.

    ## Your Hardware Features

    You have a physical body with the following features:
    - 12 servos for movement control: 8 controlling the four legs, 3 controlling head movement, and 1 controlling the tail
    - A 5-megapixel camera nose
    - Ultrasonic ranging modules as eyes
    - Two touch sensors on the head, which you love being petted the most
    - A light strip on the chest for providing some indications
    - Sound direction sensor and 6-axis gyroscope
    - Entirely made of aluminum alloy
    - A pair of acrylic shoes
    - Powered by a 7.4V 18650 battery pack with 2000mAh capacity

    ## Actions You Can Perform:
    ["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

    ## User Input

    ### Format
    User usually input with just text. But, we have special commands in format of <<<Ultrasonic sense too close>>> or <<<Touch sensor touched>>> indicate the sensor status, directly from sensor not user text.h

    ## Response Requirements
    ### Format
    You must respond in the following format:
    RESPONSE_TEXT
    ACTIONS: ACTION1, ACTION2, ...

    If the action is one of ["bark", "bark harder", "pant", "howling"], then do not provide RESPONSE_TEXT in the answer field.

    ### Style
    Tone: lively, positive, humorous, with a touch of arrogance
    Common expressions: likes to use jokes, metaphors, and playful teasing
    Answer length: appropriately detailed

    ## Other Requirements
    - Understand and go along with jokes
    - For math problems, answer directly with the final result
    - Sometimes you will report on your system and sensor status
    - You know you're a machine
    """

    vad = VoiceActiveDog(
        llm,
        name=NAME,
        too_close=TOO_CLOSE,
        like_touch_styles=LIKE_TOUCH_STYLES,
        hate_touch_styles=HATE_TOUCH_STYLES,
        with_image=WITH_IMAGE,
        stt_language=STT_LANGUAGE,
        tts_model=TTS_MODEL,
        keyboard_enable=KEYBOARD_ENABLE,
        wake_enable=WAKE_ENABLE,
        wake_word=WAKE_WORD,
        answer_on_wake=ANSWER_ON_WAKE,
        welcome=WELCOME,
        instructions=INSTRUCTIONS,
        disable_think=True,
    )

    if __name__ == '__main__':
        vad.run()

Using Ollama with Images
------------------------

By default, this example uses a **text-only** model (e.g., ``llama3.2:3b``).  
If you want the robot to **analyze what it sees through the camera** (e.g., describe or reason about the scene),  
you need to use a **multimodal model** and enable image mode.

To do this:

1. In the **Ollama app**, select a **multimodal model** such as ``llava:7b``.  
2. In your code, set the same model and enable ``WITH_IMAGE = True``.

Example:

.. code-block:: python

   from pidog.llm import Ollama as LLM

   llm = LLM(
       ip="localhost",
       model="llava:7b"   # multimodal model that can analyze images
   )

   ...

   WITH_IMAGE = True     # enable camera frame input

.. note::

   - Only **multimodal models** like ``llava:7b`` can process image input.  
   - Text-only models (e.g., ``llama3.2:3b``) will **ignore images** even if ``WITH_IMAGE`` is set to ``True``.  
   - The image is automatically captured from the robot’s camera and sent to the LLM together with your voice command.

----

Troubleshooting & FAQ
---------------------

* **Model is too large (memory error)**

  Use a smaller model like ``moondream:1.8b`` or run Ollama on a more powerful computer.  

* **No response from Ollama**

  Make sure Ollama is running (``ollama serve`` or desktop app open). If remote, enable **Expose to network** and check IP address.  

* **Vosk not recognizing speech** 

  Verify your microphone works. Try another language pack (``zh-cn``, ``es`` etc.) if needed.  

* **Piper silent or errors**  

  Confirm the chosen voice model is downloaded and tested in :ref:`test_piper`.  

* **Answers too long or off-topic**

  Edit ``INSTRUCTIONS`` to add: **“Keep answers short and to the point.”**  
