.. note::

   您好，欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者 Facebook 社区！与众多爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32。

   **为什么要加入？**

   - **专家支持**：借助我们的社区和团队，解决售后问题和技术难题。
   - **学习与分享**：交流技巧和教程，提升您的技能。
   - **独家预览**：抢先获取新产品公告和先睹为快的机会。
   - **特别折扣**：享受我们最新产品的专属优惠。
   - **节日促销与赠品活动**：参与赠品和节日促销活动。

   👉 准备好和我们一起探索和创造了吗？点击 [|link_sf_facebook|]，立即加入吧！

17. 使用 Ollama 进行文字对话
=================================

在本课中，您将学习如何使用 **Ollama**——一个用于本地运行大语言和视觉模型的工具。
我们将向您展示如何安装 Ollama、下载模型，并将 Pidog 连接到它。

准备工作
----------------

请确保您已完成以下步骤：

* :ref:`install_all_modules` — 安装 ``robot-hat``、``vilib``、``Pidog`` 模块，然后运行脚本 ``i2samp.sh``。

.. _download_ollama:

1. 安装 Ollama（LLM）并下载模型
-------------------------------------------------

您可以选择在哪里安装 **Ollama**：

* 在您的 Raspberry Pi 上（本地运行）
* 或者在**同一本地网络**\ 中的另一台电脑（Mac/Windows/Linux）上

**推荐模型与硬件对照**

您可以选择 |link_ollama_hub| 上提供的任何模型。
模型有不同的大小（3B、7B、13B、70B...）。
较小的模型运行更快，所需内存更少，而较大的模型提供更好的质量，但需要强大的硬件。

请查看下表，决定哪种模型大小适合您的设备。

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - 模型大小
     - 最低内存要求
     - 推荐硬件
   * - ~3B 参数
     - 8GB（16GB 更佳）
     - Raspberry Pi 5（16GB）或中端 PC/Mac
   * - ~7B 参数
     - 16GB+
     - Pi 5（16GB，勉强可用）或中端 PC/Mac
   * - ~13B 参数
     - 32GB+
     - 大内存台式 PC / Mac
   * - 30B+ 参数
     - 64GB+
     - 工作站 / 服务器 / 推荐使用 GPU
   * - 70B+ 参数
     - 128GB+
     - 配备多 GPU 的高端服务器

**在 Raspberry Pi 上安装**

如果您想在 Raspberry Pi 上直接运行 Ollama：

* 使用 **64 位 Raspberry Pi OS**
* 强烈建议：**Raspberry Pi 5（16GB RAM）**

运行以下命令：

.. code-block:: bash

   # 安装 Ollama
   curl -fsSL https://ollama.com/install.sh | sh

   # 拉取轻量模型（适合测试）
   ollama pull llama3.2:3b

   # 快速运行测试（输入 'hi' 并按回车）
   ollama run llama3.2:3b

   # 启动 API 服务（默认端口 11434）
   # 提示：设置 OLLAMA_HOST=0.0.0.0 以允许局域网访问
   OLLAMA_HOST=0.0.0.0 ollama serve

**在 Mac / Windows / Linux 上安装（桌面应用）**

1. 从 |link_ollama| 下载并安装 Ollama

   .. image:: img/llm_ollama_download.png

2. 打开 Ollama 应用，进入**模型选择器**，使用搜索栏查找模型。例如，输入 ``llama3.2:3b``\ （这是一个小巧轻量的入门模型）。

   .. image:: img/llm_ollama_choose.png

3. 下载完成后，在聊天窗口中输入一些简单内容，如"Hi"，Ollama 会在首次使用时自动开始下载。

   .. image:: img/llm_olama_llama_download.png

4. 进入**设置** → 启用**\ 向网络公开 Ollama**。这允许您的 Raspberry Pi 通过局域网连接到它。

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   如果您看到如下错误：

   ``Error: model requires more system memory ...``

   说明该模型对您的机器来说过大。
   请使用**较小的模型**\ 或切换到内存更大的电脑。

2. 测试 Ollama
--------------

安装好 Ollama 且模型就绪后，您可以通过一个简单的聊天循环快速测试它。

**步骤**

#. 创建一个新文件：

   .. code-block:: bash

      cd ~/pidog/examples
      nano test_llm_ollama.py

#. 粘贴以下代码并保存（``Ctrl+X`` → ``Y`` → ``Enter``）：

   .. code-block:: python

      from pidog.llm import Ollama

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      # 如果 Ollama 运行在同一个 Raspberry Pi 上，请使用 "localhost"。
      # 如果运行在局域网中的另一台电脑上，请替换为该电脑的 IP 地址。
      llm = Ollama(
          ip="localhost",
          model="llama3.2:3b"   # 您可以替换为任何模型
      )

      # 基本配置
      llm.set_max_messages(20)
      llm.set_instructions(INSTRUCTIONS)
      llm.set_welcome(WELCOME)

      print(WELCOME)

      while True:
          text = input(">>> ")
          if text.strip().lower() in {"exit", "quit"}:
              break

          # 流式输出响应
          response = llm.prompt(text, stream=True)
          for token in response:
              if token:
                  print(token, end="", flush=True)
          print("")

#. 运行程序：

   .. code-block:: bash

      python3 test_llm_ollama.py

#. 现在您可以直接在终端中与 Pidog 聊天了。

   * 您可以选择 |link_ollama_hub| 上的**任何模型**，但如果您只有 8–16GB 内存，建议使用较小的模型（例如 ``moondream:1.8b``、``phi3:mini``）。
   * 确保代码中指定的模型与您在 Ollama 中已拉取的模型一致。
   * 输入 ``exit`` 或 ``quit`` 可停止程序。
   * 如果无法连接，请确保 Ollama 正在运行，并且如果使用远程主机，两台设备需在同一局域网内。


故障排除
---------------


* **出现类似 `model requires more system memory ...` 的错误。**

  * 这意味着该模型对您的设备来说过大。
  * 使用较小的模型，如 ``moondream:1.8b`` 或 ``granite3.2-vision:2b``。
  * 或者切换到内存更大的机器，并向网络公开 Ollama。

* **代码无法连接到 Ollama（连接被拒绝）。**

  请检查以下内容：

  * 确保 Ollama 正在运行（``ollama serve`` 或桌面应用已打开）。
  * 如果使用远程电脑，请在 Ollama 设置中启用**向网络公开**。
  * 再次确认代码中的 ``ip="..."`` 是正确的局域网 IP。
  * 确认两台设备在同一个本地网络中。
