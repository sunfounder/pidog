.. note::

   你好，欢迎加入 SunFounder 的 Raspberry Pi & Arduino & ESP32 爱好者 Facebook 社区！与众多爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32。

   **为什么要加入？**

   - **专家支持**：借助我们的社区和团队，解决售后问题和技术难题。
   - **学习与分享**：交流技巧和教程，提升你的技能。
   - **独家预览**：抢先获取新产品发布和预告信息。
   - **特别折扣**：享受我们最新产品的独家折扣。
   - **节日促销与抽奖**：参与抽奖和假日促销活动。

   👉 准备好和我们一起探索和创造了吗？点击 [|link_sf_facebook|]，立即加入！

15. 使用 Piper 和 OpenAI 进行 TTS
========================================================

在上一课中，我们在 Raspberry Pi 上尝试了两种内置 TTS 引擎（**Espeak** 和 **Pico2Wave**）。现在让我们探索另外两种更强大的选择：**Piper**\ （离线、基于神经网络）和 **OpenAI TTS**\ （在线、基于云）。

* **Piper**：本地 TTS 引擎，在 Raspberry Pi 上离线运行。
* **OpenAI TTS**：在线服务，提供非常自然、类似人声的语音。

开始之前
----------------

请确保已完成以下步骤：

* :ref:`install_all_modules` — 安装 ``robot-hat``、``vilib``、``pidog`` 模块，然后运行脚本 ``i2samp.sh``。

.. _test_piper:

测试 Piper
------------------

**尝试步骤如下**：

#. 创建一个新文件：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_piper.py

#. 将下面的示例代码复制到文件中。按 ``Ctrl+X``，然后按 ``Y``，最后按 ``Enter`` 保存并退出。

   .. code-block:: python

       from pidog.tts import Piper

       tts = Piper()

       # List supported languages
       print(tts.available_countrys())

       # List models for English (en_us)
       print(tts.available_models('en_us'))

       # Set a voice model (auto-download if not already present)
       tts.set_model("en_US-amy-low")

       # Say something
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()``：打印支持的语言。
   * ``available_models()``：列出该语言可用的模型。
   * ``set_model()``：设置语音模型（如果缺少会自动下载）。
   * ``say()``：将文本转换为语音并播放。

#. 运行程序：

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. 首次运行时，所选语音模型会自动下载。

   * 然后你应该能听到 Pidog 说：``Hello! I'm Piper TTS.``

   * 你可以通过调用 ``set_model()`` 并传入不同的名称来切换其他语言模型。


测试 OpenAI TTS
-------------------------------

**获取并保存你的 API 密钥**

#. 访问 |link_openai_platform| 并登录。在 **API keys** 页面，单击 **Create new secret key**。

   .. image:: img/llm_openai_create.png

#. 填写相关信息（Owner、Name、Project 及权限，如果需要），然后单击 **Create secret key**。

   .. image:: img/llm_openai_create_confirm.png

#. 密钥创建后，请立即复制——你将无法再次查看。如果丢失，则必须生成一个新的密钥。

   .. image:: img/llm_openai_copy.png

#. 在你的项目文件夹中（例如：``/pidog/examples``），创建一个名为 ``secret.py`` 的文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 将密钥粘贴到文件中，如下所示：

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**编写并运行测试程序**

#. 创建一个新文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano test_tts_openai.py

#. 将下面的示例代码复制到文件中。按 ``Ctrl+X``，然后按 ``Y``，最后按 ``Enter`` 保存并退出。

   .. code-block:: python

      from pidog.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # or use the try/except version shown above

      # Initialize OpenAI TTS
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # low-latency TTS model
      tts.set_voice('alloy')            # pick a voice

      # Quick hello (sanity check)
      tts.say("Hello! I'm OpenAI TTS.")

#. 运行程序：

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. 你应该能听到 Pidog 说：

   ``Hello! I'm OpenAI TTS.``

----

故障排查
-------------------

* **No module named 'secret'**

  这意味着 ``secret.py`` 不在你的 Python 文件所在的同一文件夹中。
  将 ``secret.py`` 移动到运行脚本的同一目录下，例如：

  .. code-block:: bash

     ls ~/pidog/examples
     # Make sure you see both: secret.py and your .py file

* **OpenAI: Invalid API key / 401**

  * 检查你是否粘贴了完整的密钥（以 ``sk-`` 开头），且没有多余的空格或换行。
  * 确保你的代码正确导入了它：

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * 确认你的 Pi 可以访问网络（尝试 ``ping api.openai.com``）。

* **OpenAI: Quota exceeded / billing error**

  * 你可能需要在 OpenAI 仪表板中添加计费信息或增加配额。
  * 在解决账户/计费问题后重试。

* **Piper: tts.say() 运行但无声音**

  * 确保语音模型确实存在：

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * 确认代码中的模型名称完全匹配：

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * 检查 Pi 上的音频输出设备/音量（``alsamixer``），并确保扬声器已连接且通电。

* **ALSA / 音频设备错误（例如 "Audio device busy" 或 "No such file or directory"）**

  * 关闭其他使用音频的程序。
  * 如果设备一直忙碌，重启 Pi。
  * 对于 HDMI 与耳机插孔输出，请在 Raspberry Pi OS 的音频设置中选择正确的设备。

* **运行 Python 时权限被拒绝**

  * 如果你的环境需要，请尝试使用 ``sudo``：

    .. code-block:: bash

       sudo python3 test_tts_piper.py



TTS 引擎对比
-------------------------

.. list-table:: 功能对比：Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - 项目
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - 运行平台
     - Raspberry Pi 内置（离线）
     - Raspberry Pi 内置（离线）
     - Raspberry Pi / PC（离线，需要模型）
     - 云端（在线，需要 API 密钥）
   * - 语音质量
     - 机器人感强
     - 比 Espeak 更自然
     - 自然（神经 TTS）
     - 非常自然/接近人声
   * - 可调参数
     - 速度、音调、音量
     - 有限的调节选项
     - 选择不同的语音/模型
     - 选择模型和音色
   * - 语言支持
     - 多语言（质量参差不齐）
     - 有限的语言集
     - 提供多种语音/语言
     - 英语效果最佳（其他语言视可用性而定）
   * - 延迟/速度
     - 非常快
     - 快
     - 在 Pi 4/5 上使用 "low" 模型可实时
     - 依赖网络（通常延迟较低）
   * - 设置步骤
     - 极少
     - 极少
     - 下载 ``.onnx`` + ``.onnx.json`` 模型
     - 创建 API 密钥，安装客户端
   * - 最佳用途
     - 快速测试、基本提示
     - 稍好的离线语音
     - 质量更好的本地项目
     - 最高质量、丰富的语音选项
