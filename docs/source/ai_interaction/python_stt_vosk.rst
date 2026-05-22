.. note::

   您好，欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者 Facebook 社区！与众多爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32。

   **为什么要加入？**

   - **专家支持**：借助我们的社区和团队，解决售后问题和技术难题。
   - **学习与分享**：交流技巧和教程，提升您的技能。
   - **独家预览**：抢先获取新产品公告和先睹为快的机会。
   - **特别折扣**：享受我们最新产品的专属优惠。
   - **节日促销与赠品活动**：参与赠品和节日促销活动。

   👉 准备好和我们一起探索和创造了吗？点击 [|link_sf_facebook|]，立即加入吧！

16. 使用 Vosk 进行离线语音识别
==============================================

Vosk 是一个轻量级的语音转文字（STT）引擎，支持多种语言，可在 Raspberry Pi 上完全**离线**\ 运行。
您只需联网一次下载语言模型。之后，所有功能无需网络连接即可使用。

在本课中，我们将：

* 检查 Raspberry Pi 上的麦克风。
* 安装并使用所选语言模型测试 Vosk。

准备工作
----------------

请确保您已完成以下步骤：

* :ref:`install_all_modules` — 安装 ``robot-hat``、``vilib``、``pidog`` 模块，然后运行脚本 ``i2samp.sh``。

1. 检查您的麦克风
--------------------------

在使用语音识别之前，请确保您的 USB 麦克风正常工作。

#. 列出可用的录音设备：

   .. code-block:: bash

      arecord -l

   查找类似 ``card 1: ... device 0`` 的行。

#. 录制一段短样本（将 ``1,0`` 替换为您找到的编号）：

   .. code-block:: bash

      arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

   * 示例：如果您的设备是 ``card 2, device 0``，请使用：

   .. code-block:: bash

      arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

#. 播放以确认录音效果：

   .. code-block:: bash

      aplay test.wav

#. 如有需要，调节麦克风音量：

   .. code-block:: bash

      alsamixer

   * 按 **F6** 选择您的 USB 麦克风。
   * 找到 **Mic** 或 **Capture** 通道。
   * 确保没有静音（**[MM]** 表示静音，按 ``M`` 取消静音 → 应显示 **[OO]**）。
   * 使用 ↑ / ↓ 方向键改变录音音量。


.. _test_vosk:

2. 测试 Vosk
--------------------------

**尝试步骤如下**：

#. 创建一个新文件：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_stt_vosk.py

#. 将示例代码复制到文件中。按 ``Ctrl+X``，然后按 ``Y``，再按 ``Enter`` 保存并退出。

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

#. 首次使用新语言运行此代码时，Vosk 将**自动下载语言模型**\ （默认会下载**\ 小型**版本）。
   同时，它还会打印出支持的语言列表。然后您将看到：

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   这意味着：

   * 模型文件（``vosk-model-small-en-us-0.15``）已下载完成。
   * 支持的语言列表已打印出来。
   * 系统正在聆听 — 对着 Pidog 的麦克风说话，识别的文字将显示在终端中。

   **提示**：

   * 保持麦克风距离约 15–30 厘米。
   * 选择与您的语言和口音匹配的模型。

**流式模式（可选）**

您也可以连续流式传输语音，在说话时实时查看部分识别结果：

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

故障排除
-----------------

* **运行 `arecord` 时提示没有此类文件或目录**

  您可能使用了错误的声卡/设备编号。
  运行：

  .. code-block:: bash

     arecord -l

  并将 ``1,0`` 替换为您的 USB 麦克风显示的编号。

* **录制的文件没有声音**

  打开混音器检查麦克风音量：

  .. code-block:: bash

     alsamixer

  * 按 **F6** 选择您的 USB 麦克风。
  * 确保 **Mic/Capture** 没有静音（**[OO]** 而非 **[MM]**）。
  * 使用 ↑ 键提高音量。

* **Vosk 无法识别语音**

  * 确保**语言代码**\ 与您的模型匹配（例如英文用 ``en-us``，中文用 ``zh-cn``）。
  * 保持麦克风距离 15–30 厘米，并避免背景噪音。
  * 清晰且缓慢地说话。

* **高延迟 / 识别速度慢**

  * 默认自动下载的是**小型模型**\ （速度更快，但准确度较低）。
  * 如果仍然很慢，请关闭其他程序以释放 CPU。
