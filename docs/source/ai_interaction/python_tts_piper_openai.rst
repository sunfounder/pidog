
15. 使用 Piper 和 OpenAI 进行 TTS
========================================================

在上一课中，我们体验了 Raspberry Pi 上的两种内置 TTS 引擎（**Espeak** 和 **Pico2Wave**）。  
接下来，我们将探索两种更强大的 TTS 方案：**Piper** （离线）与 **OpenAI TTS** （在线）。

* **Piper**：本地运行的神经网络 TTS 引擎，可离线工作。  
* **OpenAI TTS**：在线服务，语音自然、接近人类音色。  

----

在开始之前
----------------

请确保你已完成：

* :ref:`install_all_modules` — 安装 ``robot-hat``、``vilib``、``pidog`` 模块，并运行 ``i2samp.sh`` 脚本。

.. _test_piper:

测试 Piper
------------------

**测试步骤**：

#. 创建一个新文件：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_piper.py

#. 将以下代码粘贴进去，并按 ``Ctrl+X`` → ``Y`` → ``Enter`` 保存退出。

   .. code-block:: python

       from pidog.tts import Piper

       tts = Piper()

       # 列出支持的语言
       print(tts.available_countrys())

       # 列出英语（en_us）的可用模型
       print(tts.available_models('en_us'))

       # 设置语音模型（如果本地没有，会自动下载）
       tts.set_model("en_US-amy-low")

       # 播放语音
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()``：列出支持的语言  
   * ``available_models()``：列出该语言的可用语音模型  
   * ``set_model()``：设置语音模型（如缺失会自动下载）  
   * ``say()``：将文本转换为语音并播放

#. 运行程序：

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. 第一次运行时会自动下载语音模型。  

   * 然后你将听到 Pidog 说： ``Hello! I'm Piper TTS.``  
   * 你可以通过 ``set_model()`` 切换其他语音模型。


测试 OpenAI TTS
-------------------------------

**获取并保存 API Key**

#. 前往 |link_openai_platform| 并登录，在 **API keys** 页面点击 **Create new secret key**。

   .. image:: img/llm_openai_create.png

#. 填写相关信息并点击 **Create secret key**。

   .. image:: img/llm_openai_create_confirm.png

#. 复制密钥（此后将无法再次查看），如果丢失需要重新生成。

   .. image:: img/llm_openai_copy.png

#. 在项目文件夹中（例如 ``/pidog/examples``）创建 ``secret.py``：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 将密钥写入文件：

   .. code-block:: python

       # secret.py
       # 存储私密信息，请勿上传到公共仓库
       OPENAI_API_KEY = "sk-xxx"

**编写并运行测试程序**

#. 创建一个新文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano test_tts_openai.py

#. 粘贴以下代码并保存退出：

   .. code-block:: python

      from pidog.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # 也可使用 try/except 方式

      # 初始化 OpenAI TTS
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # 低延迟 TTS 模型
      tts.set_voice('alloy')            # 选择语音

      # 简单测试
      tts.say("Hello! I'm OpenAI TTS.")

#. 运行程序：

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. 你将听到 Pidog 说：

   ``Hello! I'm OpenAI TTS.``


----

故障排查
-------------------

* **No module named 'secret'**

  说明 ``secret.py`` 不在与 Python 代码相同的目录下。  
  请将 ``secret.py`` 移动到你运行脚本的同一目录，例如：

  .. code-block:: bash

     ls ~/pidog/examples
     # 确认能看到：secret.py 和 你的 .py 文件

* **OpenAI: Invalid API key / 401**

  * 确保复制的是完整的 API Key（以 ``sk-`` 开头），且没有多余空格或换行。  
  * 确保代码正确导入：

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * 确认树莓派的网络连通性（例如 ``ping api.openai.com``）。

* **OpenAI: Quota exceeded / billing error**

  * 你可能需要在 OpenAI 控制台添加付款方式或增加额度。  
  * 解决后再尝试运行。

* **Piper: tts.say() 正常执行但没有声音**

  * 确认语音模型是否存在：

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * 检查代码中的模型名称是否完全一致：

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * 使用 ``alsamixer`` 检查音量和输出设备，并确认扬声器已连接且供电。

* **ALSA / 声卡相关报错（如 “Audio device busy” 或 “No such file or directory”）**

  * 关闭占用音频设备的其他程序。  
  * 若设备持续被占用，重启树莓派。  
  * 在 Raspberry Pi OS 音频设置中选择正确的输出设备（HDMI 或耳机插孔）。

* **运行 Python 时提示权限不足**

  * 某些音频输出环境需要使用 ``sudo``：

    .. code-block:: bash

       sudo python3 test_tts_piper.py


TTS 引擎对比
-------------------------

.. list-table:: Espeak、Pico2Wave、Piper、OpenAI TTS 功能对比
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - 项目
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - 运行方式
     - 树莓派内置（离线）
     - 树莓派内置（离线）
     - 树莓派 / PC（离线，需下载模型）
     - 云端（在线，需要 API Key）
   * - 语音质量
     - 机械音
     - 比 Espeak 更自然
     - 神经网络语音，自然度高
     - 近似真人语音
   * - 控制能力
     - 可调语速、音高、音量
     - 控制较少
     - 可选多种声音/模型
     - 可选模型和声音
   * - 语言支持
     - 多语言（质量不一）
     - 语言较少
     - 多语种语音模型
     - 英语最佳（其他视可用性而定）
   * - 延迟 / 速度
     - 非常快
     - 快
     - 在 Pi 4/5 上使用“low”模型可实时
     - 依赖网络（一般延迟较低）
   * - 部署
     - 简单
     - 简单
     - 下载 ``.onnx`` + ``.onnx.json`` 模型
     - 申请 API Key，安装客户端
   * - 适用场景
     - 快速测试、简单语音播报
     - 稍好一点的离线语音
     - 本地项目、高质量 TTS
     - 最高质量、语音选择丰富
