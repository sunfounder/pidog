.. note::

   您好，欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者 Facebook 社区！与众多爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32。

   **为什么要加入？**

   - **专家支持**：借助我们的社区和团队，解决售后问题和技术难题。
   - **学习与分享**：交流技巧和教程，提升您的技能。
   - **独家预览**：抢先获取新产品公告和先睹为快的机会。
   - **特别折扣**：享受我们最新产品的专属优惠。
   - **节日促销与赠品活动**：参与赠品和节日促销活动。

   👉 准备好和我们一起探索和创造了吗？点击 [|link_sf_facebook|]，立即加入吧！

19. 使用 Ollama 的本地语音聊天机器人
===============================================

在本课中，您将结合之前学到的所有知识——**语音识别（STT）**、**\ 文字转语音（TTS）**和**\ 本地 LLM（Ollama）**——构建一个完全离线的**\ 语音聊天机器人**，在您的 Pidog 系统上运行。

工作流程很简单：

#. **聆听** — 麦克风捕捉您的语音，并通过 **Vosk** 转录为文字。
#. **思考** — 将文字发送到 Ollama 上运行的本地 **LLM**\ （例如 ``llama3.2:3b``）。
#. **说话** — 聊天机器人通过 **Piper TTS** 语音回答。

这创建了一个**免提的对话机器人**，能够实时理解和回应。

----

准备工作
----------------

请确保您已准备好以下内容：

* :ref:`install_all_modules` — 安装 ``robot-hat``、``vilib``、``Pidog`` 模块，然后运行脚本 ``i2samp.sh``。
* 已测试 **Piper TTS**\ （:ref:`test_piper`）并选择了可用的语音模型。
* 已测试 **Vosk STT**\ （:ref:`test_vosk`）并选择了正确的语言包（例如 ``en-us``）。
* 已在您的 Pi 或其他电脑上安装 **Ollama**\ （:ref:`download_ollama`），并下载了诸如 ``llama3.2:3b`` 的模型（如果内存有限，可使用 ``moondream:1.8b`` 等更小的模型）。

----

运行代码
--------------

#. 打开示例脚本：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 19_voice_active_dog_ollama.py

#. 根据需要更新参数：

   * 将 ``ip`` 和 ``model`` 更新为您的实际配置。

     * ``ip``：如果 Ollama 运行在**同一台 Pi** 上，使用 ``localhost``。如果 Ollama 运行在局域网中的另一台电脑上，请在 Ollama 中启用**\ 向网络公开**，并将 ``ip`` 设置为该电脑的局域网 IP。
     * ``model``：必须与您在 Ollama 中下载/激活的模型名称完全一致。

   * ``TTS_MODEL = "en_US-ryan-low"``：替换为您在 :ref:`test_piper` 中验证过的 Piper 语音模型。
   * ``STT_LANGUAGE = "en-us"``：根据您的口音/语言包更改此设置（例如 ``en-us``、``zh-cn``、``es``）。

#. 运行脚本：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo python3 19_voice_active_dog_ollama.py

唤醒词：

.. code-block::

   "Hey buddy"

.. note::

   您可以在代码中修改**唤醒词**\ 和**机器人名称**：
   ``NAME = "Buddy"``

----

运行效果
-----------------

成功运行此示例后：

* 机器人**等待唤醒词**\ （例如 "Hey Buddy"）。
* 当听到唤醒词时：

  * LED 灯带变为**粉色（呼吸效果）**，作为唤醒提示。
  * 机器人用设定的唤醒回应问候您 —
    例如 "Hi there!"（通过 Piper TTS）。

* 然后开始**通过 Vosk STT 聆听您的语音**\ （如果启用，也接受键盘输入）。

* 识别到您说的话后，系统：

  * 将您的消息发送给 **LLM**\ （Ollama 配合 ``llama3.2:3b``）。
  * LED 变为**黄色（聆听中）**，等待处理。
  * 模型回复分为两部分：

    - ``ACTIONS:`` 之前的文字 → 语音朗读出来。
    - ``ACTIONS:`` 之后的关键词 → 映射为机器人动作。

  * 机器人通过 ``ActionFlow`` **执行这些动作**。
  * 动作完成后，机器人**回到坐姿**\ 并关闭 LED。

* 如果**超声波传感器检测到障碍物**\ 小于 10 厘米：

  - 注入消息：``<<<Ultrasonic sense too close: {distance}cm>>>``
  - 机器人自动后退：``ACTIONS: backward``
  - 本轮禁用图像输入。

* 如果**触摸传感器被触发**：

  - 对于**喜欢**\ 的触摸方式（例如 FRONT_TO_REAR）：

    - 注入：``<<<Touch style you like: FRONT_TO_REAR>>>``
    - ``ACTIONS: nod``\ （积极回应）

  - 对于**讨厌**\ 的触摸方式（例如 REAR_TO_FRONT）：

    - 注入：``<<<Touch style you hate: REAR_TO_FRONT>>>``
    - ``ACTIONS: backward``\ （回避反应）

* **LED 生命周期：**

  - ``on_start`` → 坐姿，LED 关闭
  - ``before_listen`` → 青色（就绪）
  - ``before_think`` → 黄色（处理中）
  - ``before_say`` → 粉色（说话中）
  - ``after_say`` / ``on_finish_a_round`` → 坐姿，LED 关闭
  - ``on_stop`` → 停止动作流并关闭设备

**交互示例**

.. code-block:: text

   You: Hey Buddy
   Robot: Hi there!

   You: Do a little nod for me.
   Robot: Of course. Watch my majestic nod.
   ACTIONS: nod

   (Front-to-rear touch on the head)
   Robot: Ooooh, that's nice!
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

    # 如果 Ollama 运行在同一个 Raspberry Pi 上，请使用 "localhost"。
    # 如果运行在局域网中的另一台电脑上，请替换为该电脑的 IP 地址。
    llm = Ollama(
        ip="localhost",
        model="llama3.2:3b"   # 您可以替换为任何模型
    )

    # 机器人名称
    NAME = "Buddy"

    # 超声波传感器检测过近距离（厘米）
    TOO_CLOSE = 10
    # 触摸传感器触发状态，选项：
    # - TouchStyle.REAR 后部触摸传感器
    # - TouchStyle.FRONT 前部触摸传感器
    # - TouchStyle.REAR_TO_FRONT 从后向前滑动
    # - TouchStyle.FRONT_TO_REAR 从前向后滑动
    # 机器人喜欢的触摸方式
    LIKE_TOUCH_STYLES = [TouchStyle.FRONT_TO_REAR]
    # 机器人讨厌的触摸方式
    HATE_TOUCH_STYLES = [TouchStyle.REAR_TO_FRONT]

    # 启用图像，需要设置多模态语言模型
    WITH_IMAGE = False

    # 设置模型和语言
    TTS_MODEL = "en_US-ryan-low"
    STT_LANGUAGE = "en-us"

    # 启用键盘输入
    KEYBOARD_ENABLE = True

    # 启用唤醒词
    WAKE_ENABLE = True
    WAKE_WORD = [f"hey {NAME.lower()}"]
    # 设置唤醒回应，设为空以禁用
    ANSWER_ON_WAKE = "Hi there"

    # 欢迎消息
    WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

    # 设置指令
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
    User usually input with just text. But, we have special commands in format of <<<Ultrasonic sense too close>>> or <<<Touch sensor touched>>> indicate the sensor status, directly from sensor not user text.

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

将 Ollama 与图像配合使用
------------------------

默认情况下，此示例使用**纯文本**\ 模型（例如 ``llama3.2:3b``）。
如果您希望机器人**分析通过摄像头看到的内容**\ （例如描述或推理场景），
您需要使用**多模态模型**\ 并启用图像模式。

具体操作如下：

1. 在 **Ollama 应用**\ 中，选择一个**多模态模型**，例如 ``llava:7b``。
2. 在代码中设置相同的模型，并启用 ``WITH_IMAGE = True``。

示例：

.. code-block:: python

   from pidog.llm import Ollama as LLM

   llm = LLM(
       ip="localhost",
       model="llava:7b"   # 可以分析图像的多模态模型
   )

   ...

   WITH_IMAGE = True     # 启用摄像头画面输入

.. note::

   - 只有**多模态模型**\ （如 ``llava:7b``）才能处理图像输入。
   - 纯文本模型（例如 ``llama3.2:3b``）即使将 ``WITH_IMAGE`` 设置为 ``True``，也会**忽略图像**。
   - 图像会自动从机器人的摄像头捕获，并与您的语音指令一起发送给 LLM。

----

故障排除与常见问题
---------------------

* **模型过大（内存错误）**

  使用较小的模型，如 ``moondream:1.8b``，或在更强大的电脑上运行 Ollama。

* **Ollama 无响应**

  确保 Ollama 正在运行（``ollama serve`` 或桌面应用已打开）。如果使用远程，启用**向网络公开**\ 并检查 IP 地址。

* **Vosk 无法识别语音**

  验证麦克风正常工作。如有需要，尝试其他语言包（``zh-cn``、``es`` 等）。

* **Piper 无声音或报错**

  确认所选语音模型已下载并在 :ref:`test_piper` 中测试通过。

* **回答过长或偏离主题**

  编辑 ``INSTRUCTIONS``，添加：**"保持回答简短且切题。"**
