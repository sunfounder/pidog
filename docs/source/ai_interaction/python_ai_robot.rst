
.. _ai_voice_assistant_robot:

20. AI 语音助手狗
===========================

本课程将把你的 PiDog 打造成一只 **AI 驱动的语音助手狗** 🐶。  
它可以通过你的语音唤醒，理解你说的话，用有个性的方式回应，  
并通过动作、姿态和 LED 灯光效果来表达它的“情绪”。

你将打造一个 **完全可交互的机器人伙伴**，使用以下技术：

* **LLM**：大语言模型（如 OpenAI GPT 或 豆包）实现自然对话。  
* **STT**：语音转文本，实现语音识别。  
* **TTS**：文本转语音，实现富有表现力的语音回复。  
* **传感器 + 动作**：超声波传感器、摄像头（可选）、触摸传感器以及内置动作表达。

----

开始之前
----------------

请确保你已完成以下步骤：

* :ref:`install_all_modules` — 安装 ``robot-hat``、 ``vilib``、 ``pidog`` 模块，并运行 ``i2samp.sh``。  
* :ref:`test_piper` — 检查 **Piper TTS** 支持的语言。  
* :ref:`test_vosk` — 检查 **Vosk STT** 支持的语言。  
* :ref:`py_online_llm` —  **非常重要** ：获取你的 **OpenAI**、 **豆包** 或其他支持的 LLM API Key。

你需要准备好：

* PiDog 上已连接并正常工作的 **麦克风** 和 **扬声器**；  
* 一个保存在 ``secret.py`` 文件中的 **有效 API Key**；  
* 稳定的网络连接（推荐使用 **有线网络** 以获得更好的稳定性）。

----

运行示例
---------------

中英文示例文件放在同一目录中：

.. code-block:: bash

   cd ~/pidog/examples

**英文版本** （使用 OpenAI GPT，英文交互）：

.. code-block:: bash

   sudo python3 20_voice_active_dog_gpt.py

* LLM： ``OpenAI GPT-4o-mini``  
* TTS： ``en_US-ryan-low`` （Piper）  
* STT： Vosk（ ``en-us``）

唤醒词：

.. code-block::

   "Hey buddy"

---

**中文版本** （使用豆包，中文交互）：

.. code-block:: bash

   sudo python3 20_voice_active_dog_doubao_cn.py

* LLM： ``Doubao-seed-1-6-250615``  
* TTS： ``zh_CN-huayan-x_low`` （Piper）  
* STT：Vosk（ ``cn`` ）

唤醒词：

.. code-block::

   "你好 旺财"

.. note::

   你可以在代码中修改 **唤醒词** 和 **机器人名字**：
   ``NAME = "Buddy"`` 或 ``NAME = "旺财"``  
   ``WAKE_WORD = ["hey buddy"]`` 或 ``WAKE_WORD = ["你好 旺财"]``

----

会发生什么
-----------------

当你成功运行这个示例后：

* 机器人会 **等待唤醒词** （例如：“Hey Buddy” 或 “你好 旺财”）。  
* 当听到唤醒词时：

  * LED 灯带会变为 **粉色（呼吸效果）**，作为唤醒提示。  
  * 机器人会用预设的唤醒语回应你 —  
    例如 “Hi there!”（通过 Piper TTS）。

* 随后，它会通过 Vosk STT **开始监听你的语音** （也可启用键盘输入模式）。  

* 当识别到你说的话后，系统将：

  * 捕获一帧 **摄像头图像** （因为 ``WITH_IMAGE = True``），并将你的语音内容 + 图像一并发送给 **LLM** （OpenAI ``gpt-4o-mini``）。  
  * LED 灯会变为 **黄色** （表示正在聆听/处理）。  
  * LLM 的回复会被分为两部分：

    - ``ACTIONS:`` 之前的文本 → 语音播报  
    - ``ACTIONS:`` 之后的关键词 → 映射为机器人动作

  * 机器人会通过 ``ActionFlow`` **执行这些动作**。  
  * 当动作完成后，机器人会 **回到坐姿（SIT）** 并关闭 LED 灯。

* 如果 **超声波传感器检测到距离小于 10 cm 的障碍物**：

  - 系统会注入提示信息： ``<<<Ultrasonic sense too close: {distance}cm>>>``  
  - 机器人自动执行后退动作： ``ACTIONS: backward``  
  - 本轮将 **不使用图像输入**。

* 如果 **触摸传感器被触发**：

  - 对于 **LIKE 类型触摸** （如 FRONT_TO_REAR）：

    - 注入： ``<<<Touch style you like: FRONT_TO_REAR>>>``  
    - ``ACTIONS: nod`` （积极反馈）

  - 对于 **HATE 类型触摸** （如 REAR_TO_FRONT）：

    - 注入： ``<<<Touch style you hate: REAR_TO_FRONT>>>``  
    - ``ACTIONS: backward`` （回避反应）

* **LED 生命周期**：

  - ``on_start`` → 坐姿，LED 关闭  
  - ``before_listen`` → 青色（准备状态）  
  - ``before_think`` → 黄色（处理中）  
  - ``before_say`` → 粉色（语音播放）  
  - ``after_say`` / ``on_finish_a_round`` → 坐姿，LED 关闭  
  - ``on_stop`` → 停止动作流程并关闭设备

**示例对话**

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

切换其他 LLM 或 TTS
------------------------------

你可以通过简单修改几行代码，轻松切换不同的 LLM、TTS 或 STT 语言：

* 支持的 LLM：

  * OpenAI
  * 豆包（Doubao）
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — 检查 **Piper TTS** 支持的语言。  
* :ref:`test_vosk` — 检查 **Vosk STT** 支持的语言。  

要切换，只需修改代码初始化部分，例如：

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

故障排查
---------------

* **机器人对唤醒词没有反应**  

  * 检查麦克风是否工作正常。  
  * 确保 ``WAKE_ENABLE = True``。  
  * 调整唤醒词以匹配你的发音。

* **扬声器没有声音**
 
  * 检查 TTS 模型配置是否正确。  
  * 手动测试 Piper 或 Espeak。  
  * 检查扬声器连接和音量。

* **API Key 报错或超时** 
 
  * 检查 ``secret.py`` 中的密钥是否正确。  
  * 确保网络连接正常。  
  * 确认使用的 LLM 是受支持的。

* **超声波传感器频繁误触发**  

  * 检查传感器的安装高度和角度。  
  * 在代码中调整 ``TOO_CLOSE`` 距离阈值。
