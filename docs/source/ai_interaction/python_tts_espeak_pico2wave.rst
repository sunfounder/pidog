.. note::

   您好，欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者 Facebook 社区！与众多爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32。

   **为什么要加入？**

   - **专家支持**：获得来自我们社区和团队的售后问题及技术挑战方面的帮助。
   - **学习与分享**：交流技巧和教程，提升您的技能。
   - **独家预览**：抢先获取新产品公告和先睹为快的机会。
   - **特别折扣**：享受我们最新产品的独家折扣。
   - **节日促销与赠品**：参与赠品和节日促销活动。

   👉 准备好与我们一同探索和创造了吗？点击 [|link_sf_facebook|]，立即加入！

14. 使用 Espeak 和 Pico2Wave 进行 TTS 语音合成
=================================================

在本课中，我们将使用 Raspberry Pi 上两个内置的文本转语音（TTS）引擎——**Espeak** 和 **Pico2Wave**——来让 PiDog 开口说话。

这两个引擎都简单易用且可离线运行，但它们的音质差别很大：

* **Espeak**：非常轻量且快速，但声音带有机器人音。您可以调节语速、音调和音量。
* **Pico2Wave**：与 Espeak 相比，能产生更平滑、更自然的语音，但可配置选项较少。

您将亲耳听到它们在**音质**\ 和**功能**\ 上的区别。

----

开始之前
----------------

请确保您已完成：

* :ref:`install_all_modules` — 安装 ``robot-hat``、``vilib``、``pidog`` 模块，然后运行脚本 ``i2samp.sh``。

测试 Espeak
--------------------

Espeak 是 Raspberry Pi OS 自带的一个轻量级 TTS 引擎。
它的声音听起来带有机器人音，但可配置性很高：您可以调节音量、音调、语速等。

**测试步骤**：

* 使用以下命令创建一个新文件：

  .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_espeak.py

* 然后将示例代码复制进去。按 ``Ctrl+X``，然后 ``Y``，最后 ``Enter`` 保存并退出。

  .. code-block:: python

      from pidog.tts import Espeak

      tts = Espeak()

      # Optional voice tuning
      # tts.set_amp(100)   # 0 to 200
      # tts.set_speed(150) # 80 to 260
      # tts.set_gap(5)     # 0 to 200
      # tts.set_pitch(50)  # 0 to 99

      # Quick hello (sanity check)
      tts.say("Hello! I'm Espeak TTS.")

* 运行程序：

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* 您应该能听到 PiDog 说："Hello! I'm Espeak TTS."
* 取消代码中语音调节行的注释，尝试调整 ``amp``、``speed``、``gap`` 和 ``pitch`` 参数，听听声音的变化。

----

测试 Pico2Wave
---------------------

Pico2Wave 能产生比 Espeak 更自然、更像人声的语音。
它使用起来更简单，但灵活性较低——您只能更改语言，无法调节音调或语速。

**测试步骤**：

* 使用以下命令创建一个新文件：

  .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_pico2wave.py

* 然后将示例代码复制进去。按 ``Ctrl+X``，然后 ``Y``，最后 ``Enter`` 保存并退出。

  .. code-block:: python

      from pidog.tts import Pico2Wave

      tts = Pico2Wave()

      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT

      # Quick hello (sanity check)
      tts.say("Hello! I'm Pico2Wave TTS.")

* 运行程序：

  .. code-block::

    sudo python3 test_tts_pico2wave.py

* 您应该能听到 PiDog 说："Hello! I'm Pico2Wave TTS."
* 尝试切换语言（例如使用 ``es-ES`` 表示西班牙语），听听不同语言之间的区别。

----

故障排除
-------------------

* **运行 Espeak 或 Pico2Wave 时没有声音**

  * 检查扬声器/耳机是否连接好，音量是否未静音。
  * 在终端中快速测试：

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  如果听不到声音，则问题出在音频输出上，而非您的 Python 代码。

* **Espeak 声音太快或太机器人化**

  * 尝试调整代码中的参数：

    .. code-block:: python

       tts.set_speed(120)   # 更慢
       tts.set_pitch(60)    # 不同音调

* **运行代码时权限被拒绝**

  * 尝试使用 ``sudo`` 运行：

    .. code-block:: bash

       sudo python3 test_tts_espeak.py


对比：Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - 特性
     - Espeak
     - Pico2Wave
   * - 语音质量
     - 机器人音，合成音
     - 更自然，类人音
   * - 语言支持
     - 默认为英语
     - 较少，但覆盖常用语言
   * - 可调节性
     - 是（语速、音调等）
     - 否（仅可调语言）
   * - 性能
     - 非常快，轻量
     - 略慢，较重
