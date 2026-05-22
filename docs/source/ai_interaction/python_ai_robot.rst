.. note::

   您好，欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者 Facebook 社区！与众多爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32。

   **为什么要加入？**

   - **专家支持**：借助我们的社区和团队，解决售后问题和技术难题。
   - **学习与分享**：交流技巧和教程，提升您的技能。
   - **独家预览**：抢先获取新产品公告和先睹为快的机会。
   - **特别折扣**：享受我们最新产品的专属优惠。
   - **节日促销与赠品活动**：参与赠品和节日促销活动。

   👉 准备好和我们一起探索和创造了吗？点击 [|link_sf_facebook|]，立即加入吧！

.. _ai_voice_assistant_robot:

20. AI 语音助手狗
===========================

本节课将您的 Pidog 化身为一只 **AI 驱动的语音助手狗** 🐶。
这款机器人可以通过语音唤醒，理解您说的话，用富有个性的方式回应，
并通过动作、姿态和 LED 灯光效果表达它的"情绪"。

您将构建一个**完全交互式的机器人伙伴**，使用以下技术：

* **LLM**：大语言模型（如 OpenAI GPT 或 豆包），用于自然对话。
* **STT**：语音转文字，用于语音识别。
* **TTS**：文字转语音，用于富有表现力的语音回复。
* **传感器 + 动作**：超声波传感、摄像头视觉（可选）、触摸传感器以及内置的表情动作。

----

准备工作
----------------

请确保您已完成以下步骤：

* :ref:`install_all_modules` — 安装 ``robot-hat``、``vilib``、``pidog`` 模块，然后运行脚本 ``i2samp.sh``。
* :ref:`test_piper` — 查看 **Piper TTS** 支持的语言。
* :ref:`test_vosk` — 查看 **Vosk STT** 支持的语言。
* :ref:`py_online_llm` — 这一步**非常重要**：获取您的 **OpenAI** 或 **\ 豆包** API 密钥，或其他受支持的 LLM 的 API 密钥。

您应该已经具备以下条件：

* Pidog 上正常工作的**麦克风**\ 和**扬声器**。
* 在 ``secret.py`` 中保存的**有效 API 密钥**。
* 稳定的网络连接（建议使用**有线连接**\ 以获得更好的稳定性）。

----

运行示例
---------------

两个语言版本放在同一目录下：

.. code-block:: bash

   cd ~/pidog/examples

**英文版**\ （OpenAI GPT，英文指令）：

.. code-block:: bash

   sudo python3 20_voice_active_dog_gpt.py

* LLM：``OpenAI GPT-4o-mini``
* TTS：``en_US-ryan-low``\ （Piper）
* STT：Vosk（``en-us``）

唤醒词：

.. code-block::

   "Hey buddy"

---

**中文版**\ （豆包，中文指令）：

.. code-block:: bash

   sudo python3 20_voice_active_dog_doubao_cn.py

* LLM：``Doubao-seed-1-6-250615``
* TTS：``zh_CN-huayan-x_low``\ （Piper）
* STT：Vosk（``cn``）

唤醒词：

.. code-block::

   "你好 旺财"

.. note::

   您可以在代码中修改**唤醒词**\ 和**机器人名称**：
   ``NAME = "Buddy"`` 或 ``NAME = "旺财"``
   ``WAKE_WORD = ["hey buddy"]`` 或 ``WAKE_WORD = ["你好 旺财"]``

----

运行效果
-----------------

成功运行此示例后：

* 机器人**等待唤醒词**\ （例如 "Hey Buddy"、"你好 旺财"）。
* 当听到唤醒词时：

  * LED 灯带变为**粉色（呼吸效果）**，作为唤醒提示。
  * 机器人用设定的唤醒回应问候您 —
    例如 "Hi there!"（通过 Piper TTS）。

* 然后开始**通过 Vosk STT 聆听您的语音**\ （如果启用，也接受键盘输入）。

* 识别到您说的话后，系统：

  * 拍摄一帧**摄像头画面**\ （因为 ``WITH_IMAGE = True``），将您的消息和图像发送给 **LLM**\ （OpenAI ``gpt-4o-mini``）。
  * LED 变为**黄色（聆听/处理中）**，等待模型思考。
  * 模型回复分为两部分：

    - ``ACTIONS:`` 之前的文字 → 语音朗读出来。
    - ``ACTIONS:`` 之后的关键词 → 映射为机器人动作。

  * 机器人通过 ``ActionFlow`` **执行这些动作**。
  * 动作完成后，机器人**回到坐姿**\ 并关闭 LED。

* 如果**超声波传感器检测到障碍物**\ 小于 10 厘米：

  - 注入消息：``<<<Ultrasonic sense too close: {distance}cm>>>``
  - 机器人自动后退：``ACTIONS: backward``
  - 本轮**禁用图像输入**。

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

   You: What do you see in front of you?
   Robot: I can see a notebook and a blue mug on the table.
   ACTIONS: think

   You: Do a little nod for me.
   Robot: Of course. Watch my majestic nod.
   ACTIONS: nod

   (Front-to-rear touch on the head)
   Robot: Ooooh, that's nice!
   ACTIONS: nod

   (Moving too close)
   Robot: Hey hey—too close! Backing up for safety.
   ACTIONS: backward


----

切换到其他 LLM 或 TTS
------------------------------

您只需少量修改即可轻松切换到其他 LLM、TTS 或 STT 语言：

* 支持的 LLM：

  * OpenAI
  * 豆包
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — 查看 **Piper TTS** 支持的语言。
* :ref:`test_vosk` — 查看 **Vosk STT** 支持的语言。

要切换，只需修改代码中的初始化部分：

.. code-block:: python

  from pidog.llm import OpenAI as LLM

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # 设置模型和语言
  TTS_MODEL = "en_US-ryan-low"
  STT_LANGUAGE = "en-us"

----

故障排除
---------------

* **机器人对唤醒词没有反应**

  * 检查麦克风是否正常工作。
  * 确保 ``WAKE_ENABLE = True``。
  * 调整唤醒词以匹配您的发音。

* **扬声器没有声音**

  * 验证 TTS 模型设置。
  * 手动测试 Piper 或 Espeak。
  * 检查扬声器连接和音量。

* **API 密钥错误或超时**

  * 检查 ``secret.py`` 中的密钥。
  * 确保网络连接正常。
  * 确认 LLM 受支持。

* **超声波传感器不断意外触发。**

  * 检查传感器安装高度和角度。
  * 在代码中调整 ``TOO_CLOSE`` 距离阈值。
