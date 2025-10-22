
16. 使用 Vosk 进行 STT（离线语音识别）
==============================================

Vosk 是一个轻量级的语音转文字（STT）引擎，支持多种语言，并且可以在 Raspberry Pi 上完全 **离线** 运行。  
你只需联网一次下载语言模型，之后即可在无网络环境下使用。

在本课程中，我们将：

* 检查 Raspberry Pi 上的麦克风是否可用。  
* 安装并测试 Vosk 及所选语言模型。

在开始之前
----------------

请确保你已经完成以下步骤：

* :ref:`install_all_modules` — 安装 ``robot-hat``、``vilib``、``pidog`` 模块，并运行 ``i2samp.sh`` 脚本。

1. 检查麦克风
--------------------------

在使用语音识别前，请确保 USB 麦克风工作正常。

#. 列出可用录音设备：

   .. code-block:: bash

      arecord -l

   查找类似 ``card 1: ... device 0`` 的行。

#. 录制一段测试音频（将 ``1,0`` 替换为你的设备编号）：

   .. code-block:: bash

      arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

   * 例如：如果设备为 ``card 2, device 0``，使用：

   .. code-block:: bash

      arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

#. 播放测试录音：

   .. code-block:: bash

      aplay test.wav

#. 如有需要，调整麦克风音量：

   .. code-block:: bash

      alsamixer

   * 按 **F6** 选择你的 USB 麦克风。  
   * 找到 **Mic** 或 **Capture** 通道。  
   * 确保未静音（**[MM]** 表示静音，按 ``M`` 取消静音 → 应显示 **[OO]**）。  
   * 使用 ↑ / ↓ 键调整音量。

.. _test_vosk:

2. 测试 Vosk
--------------------------

**测试步骤**：

#. 创建一个新文件：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_stt_vosk.py

#. 粘贴以下代码并保存（``Ctrl+X`` → ``Y`` → ``Enter``）：

   .. code-block:: python

      from pidog.stt import Vosk

      vosk = Vosk(language="en-us")

      print(vosk.available_languages)

      while True:
          print("Say something")
          result = vosk.listen(stream=False)
          print(result)

#. 运行程序：

   .. code-block:: bash

      sudo python3 test_stt_vosk.py

#. 第一次运行新语言时，Vosk 会自动下载语言模型（默认下载 **small** 版本），并打印支持的语言列表。你将看到类似输出：

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   这意味着：

   * 语言模型（``vosk-model-small-en-us-0.15``）已下载完成。  
   * 系统已打印支持语言列表。  
   * 系统正在监听，请对着 Pidog 麦克风说话，识别的文字将出现在终端中。

   **提示**：

   * 将麦克风保持在 15–30 cm 距离。  
   * 选择与你的语言和口音匹配的模型。

**可选：流式识别模式**

你也可以开启流式识别，在讲话过程中看到实时识别结果。

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

故障排查
-----------------

* **运行 `arecord` 时提示 No such file or directory（找不到文件）**

  可能是你使用了错误的声卡或设备编号。  
  运行：

  .. code-block:: bash

     arecord -l

  然后将 ``1,0`` 替换为你的 USB 麦克风对应的编号。

* **录音文件没有声音**

  打开混音器检查麦克风音量：

  .. code-block:: bash

     alsamixer

  * 按 **F6** 选择你的 USB 麦克风。  
  * 确保 **Mic/Capture** 没有被静音（应为 **[OO]** 而不是 **[MM]**）。  
  * 使用 ↑ 键提高录音音量。

* **Vosk 无法识别语音**

  * 确保使用的 **语言代码** 与模型匹配（例如英文用 ``en-us``，中文用 ``zh-cn``）。  
  * 保持麦克风距离 15–30 cm，避免环境噪音。  
  * 清晰、适中语速地说话。

* **识别延迟高 / 速度慢**

  * 默认下载的是 **small 版本** 模型（速度更快但精度较低）。  
  * 如果仍然很慢，请关闭其他程序，释放 CPU 资源。
