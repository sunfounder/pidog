
19. 使用 Ollama 构建本地语音聊天机器人
===============================================

在本课程中，你将把之前学到的所有知识结合起来——  
包括 **语音识别（STT）**、**文本转语音（TTS）** 和 **本地大模型（Ollama）**，  
在 PiDog 系统上构建一个完全离线运行的 **语音聊天机器人** 🤖🐶。

工作流程非常简单：

#. **Listen（聆听）** — 麦克风采集你的语音，并通过 **Vosk** 将其转录为文本。  
#. **Think（思考）** — 文本被发送到本地运行的 **Ollama LLM** （例如 ``llama3.2:3b``）。  
#. **Speak（回应）** — 聊天机器人通过 **Piper TTS** 进行语音回复。  

这样就实现了一个 **全程免手动操作** 的实时语音交互机器人。

----

开始之前
----------------

请确保你已完成以下准备：

* :ref:`install_all_modules` — 安装 ``robot-hat``、``vilib``、``pidog`` 模块，并运行 ``i2samp.sh`` 脚本。  
* 测试 **Piper TTS** （:ref:`test_piper`）并选择一个可用的语音模型。  
* 测试 **Vosk STT** （:ref:`test_vosk`）并选择合适的语言包（如 ``en-us``）。  
* 在 Pi 或其他电脑上安装 **Ollama** （:ref:`download_ollama`），并下载一个模型（如 ``llama3.2:3b``，或较小的 ``moondream:1.8b`` 以适配内存）。

----

运行示例代码
--------------

#. 打开示例脚本：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 19_voice_active_dog_ollama.py

#. 根据实际情况修改参数：

   * 修改 ``ip`` 和 ``model``：

     * ``ip``：如果 Ollama 运行在 **同一台 Pi** 上，使用 ``localhost``。  
       如果运行在局域网的另一台电脑上，请在 Ollama 中启用 **Expose to network** 并设置该电脑的局域网 IP。  
     * ``model``：必须与 Ollama 中下载/激活的模型名称完全一致。

   * ``TTS_MODEL = "en_US-ryan-low"``：替换为你在 :ref:`test_piper` 中确认可用的 Piper 语音模型。  
   * ``STT_LANGUAGE = "en-us"``：根据你的语言包修改（如 ``en-us``、``zh-cn``、``es`` 等）。

#. 运行脚本：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo python3 19_voice_active_dog_ollama_with_image.py

唤醒词：

.. code-block::

   "Hey buddy"

.. note::

   你可以在代码中修改 **唤醒词** 和 **机器人名字**：
   ``NAME = "Buddy"``

----

运行效果
-----------------

当你成功运行该示例后：

* 机器人会 **等待唤醒词** （例如：“Hey Buddy”）。  
* 当听到唤醒词时：

  * LED 灯带会变为 **粉色（呼吸效果）**，作为唤醒提示。  
  * 机器人会用预设的唤醒语回应你 —  
    例如 “Hi there!”（通过 Piper TTS）。

* 随后，它会通过 Vosk STT **开始监听你的语音** （也可以启用键盘输入）。  

* 当识别到你的话语后，系统会：

  * 将内容发送到 **LLM** （Ollama 上运行的 ``llama3.2:3b`` 模型）。  
  * LED 变为 **黄色**，表示正在处理。  
  * 模型的回复会被分为两部分：

    - ``ACTIONS:`` 之前的文本 → 语音播报  
    - ``ACTIONS:`` 之后的关键词 → 对应机器人动作

  * 机器人会通过 ``ActionFlow`` **执行对应动作**。  
  * 当动作完成后，机器人会 **回到坐姿（SIT）** 并关闭 LED 灯。

* 如果 **超声波传感器检测到小于 10 cm 的障碍物**：

  - 系统会注入提示信息： ``<<<Ultrasonic sense too close: {distance}cm>>>``  
  - 机器人会自动后退： ``ACTIONS: backward``  
  - 本轮不启用图像输入。

* 如果 **触摸传感器被触发**：

  - 对于 **LIKE 类型触摸** （如 FRONT_TO_REAR）：

    - 注入： ``<<<Touch style you like: FRONT_TO_REAR>>>``  
    - ``ACTIONS: nod`` （积极反馈）

  - 对于 **HATE 类型触摸** （如 REAR_TO_FRONT）：

    - 注入： ``<<<Touch style you hate: REAR_TO_FRONT>>>``  
    - ``ACTIONS: backward`` （回避动作）

* **LED 生命周期**：

  - ``on_start`` → 坐姿，LED 关闭  
  - ``before_listen`` → 青色（准备）  
  - ``before_think`` → 黄色（处理中）  
  - ``before_say`` → 粉色（说话中）  
  - ``after_say`` / ``on_finish_a_round`` → 坐姿，LED 关闭  
  - ``on_stop`` → 停止动作流程并关闭设备

**示例交互**

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

代码
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

使用 Ollama 分析图像
------------------------

默认情况下，此示例使用的是 **纯文本模型** （例如 ``llama3.2:3b``）。  
如果你希望机器人能通过摄像头 **分析和描述所看到的内容** （如识别物体、理解场景），  
就需要使用 **多模态模型** 并开启图像模式。

操作步骤：

1. 在 **Ollama 应用** 中，选择一个 **多模态模型**，例如 ``llava:7b``。  
2. 在代码中设置相同的模型，并启用 ``WITH_IMAGE = True``。

示例代码：

.. code-block:: python

   from pidog.llm import Ollama as LLM

   llm = LLM(
       ip="localhost",
       model="llava:7b"   # 多模态模型，可分析图像
   )

   ...

   WITH_IMAGE = True     # 启用摄像头图像输入

.. note::

   - 只有像 ``llava:7b`` 这样的 **多模态模型** 才能处理图像输入。  
   - 文本模型（如 ``llama3.2:3b``）即使设置了 ``WITH_IMAGE = True``，也会 **忽略图像**。  
   - 图像会由 PiDog 的摄像头自动捕获，并与语音命令一同发送给 LLM。

----

故障排查与常见问题
---------------------

* **模型过大（内存不足）**

  请使用较小的模型（如 ``moondream:1.8b``）或在性能更强的电脑上运行 Ollama。

* **Ollama 无响应**

  确保 Ollama 已启动（``ollama serve`` 或桌面版已打开）。  
  如果使用远程主机，请启用 **Expose to network** 并检查 IP 地址。

* **Vosk 无法识别语音**

  检查麦克风是否工作正常，必要时更换语言包（如 ``zh-cn``、``es`` 等）。

* **Piper 没有声音或报错**

  确认你选择的语音模型已下载，并在 :ref:`test_piper` 中成功测试。

* **回答过长或跑题**

  修改 ``INSTRUCTIONS``，添加一条提示：**“Keep answers short and to the point.”（保持回答简洁明了）**。
