
17. 使用 Ollama 进行文本对话
================================

在本课程中，你将学习如何使用 **Ollama**，一个可以在本地运行大语言和视觉模型的工具。  
我们将向你展示如何安装 Ollama、下载模型，并将 PiDog 连接到它。

开始之前
----------------

请确保你已完成以下步骤：

* :ref:`install_all_modules` — 安装 ``robot-hat``、``vilib``、``pidog`` 模块，并运行脚本 ``i2samp.sh``。

.. _download_ollama:

1. 安装 Ollama（LLM）并下载模型
-------------------------------------------------

你可以选择在以下位置安装 **Ollama**：

* 在你的 Raspberry Pi 上（本地运行）  
* 或在 **同一局域网** 内的其他电脑（Mac/Windows/Linux）上

**根据硬件推荐模型**

你可以在 |link_ollama_hub| 上选择任何可用的模型。  
模型有不同的规模（3B、7B、13B、70B...）。  
较小的模型运行更快，对内存需求较低；较大的模型效果更好，但需要更强大的硬件。

请参考下表选择适合你的设备的模型大小：

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - 模型大小
     - 最低内存需求
     - 推荐硬件
   * - ~3B 参数
     - 8GB（16GB 更佳）
     - Raspberry Pi 5（16GB）或中端 PC/Mac
   * - ~7B 参数
     - 16GB+
     - Pi 5（16GB，勉强可用）或中端 PC/Mac
   * - ~13B 参数
     - 32GB+
     - 高内存 PC / Mac
   * - 30B+ 参数
     - 64GB+
     - 工作站 / 服务器 / GPU 推荐
   * - 70B+ 参数
     - 128GB+
     - 多 GPU 高端服务器

**在 Raspberry Pi 上安装**

如果你想直接在 Raspberry Pi 上运行 Ollama：

* 使用 **64 位 Raspberry Pi OS**  
* 强烈建议使用 **Raspberry Pi 5（16GB RAM）**

运行以下命令：

.. code-block:: bash

   # 安装 Ollama
   curl -fsSL https://ollama.com/install.sh | sh

   # 拉取轻量模型（适合测试）
   ollama pull llama3.2:3b

   # 运行快速测试（输入 hi 并回车）
   ollama run llama3.2:3b

   # 启动 API 服务（默认端口 11434）
   # 提示：设置 OLLAMA_HOST=0.0.0.0 以允许局域网访问
   OLLAMA_HOST=0.0.0.0 ollama serve

**在 Mac / Windows / Linux 上安装（桌面版）**

1. 从 |link_ollama| 下载并安装 Ollama。  

   .. image:: img/llm_ollama_download.png

2. 打开 Ollama 应用，进入 **Model Selector**，在搜索栏中输入模型名（例如 ``llama3.2:3b``）以下载轻量模型。  

   .. image:: img/llm_ollama_choose.png

3. 下载完成后，在聊天窗口中输入 “Hi”，Ollama 会在第一次使用时自动加载模型。

   .. image:: img/llm_olama_llama_download.png

4. 打开 **Settings（设置）** → 启用 **Expose Ollama to the network（对外开放 Ollama）**，这样 Raspberry Pi 就能通过局域网访问它。  

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   如果出现以下错误：

   ``Error: model requires more system memory ...``

   表示模型太大，超出了你的设备内存限制。  
   请使用更小的模型，或在内存更大的电脑上运行。

2. 测试 Ollama
--------------

当 Ollama 安装完成并准备好模型后，你可以通过一个最小化的聊天循环来快速测试它。

**步骤**

#. 创建一个新文件：

   .. code-block:: bash

      cd ~/pidog/examples
      nano test_llm_ollama.py

#. 将以下代码粘贴进去并保存（``Ctrl+X`` → ``Y`` → ``Enter``）：

   .. code-block:: python
 
      from pidog.llm import Ollama
 
      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"
 
      # If Ollama runs on the same Raspberry Pi, use "localhost".
      # If it runs on another computer in your LAN, replace with that computer's IP address.
      llm = Ollama(
          ip="localhost",
          model="llama3.2:3b"   # you can replace with any model
      )
 
      # Basic configuration
      llm.set_max_messages(20)
      llm.set_instructions(INSTRUCTIONS)
      llm.set_welcome(WELCOME)
 
      print(WELCOME)
 
      while True:
          text = input(">>> ")
          if text.strip().lower() in {"exit", "quit"}:
              break
 
          # Response with streaming output
          response = llm.prompt(text, stream=True)
          for token in response:
              if token:
                  print(token, end="", flush=True)
          print("")

#. 运行程序：

   .. code-block:: bash

      python3 test_llm_ollama.py

#. 现在你可以直接在终端中与 PiDog 进行对话。

   * 你可以选择 |link_ollama_hub| 上的 **任意模型**，但如果你的内存只有 8–16GB，建议使用较小的模型（例如 ``moondream:1.8b``、``phi3:mini``）。  
   * 确保代码中指定的模型名称与 Ollama 中已拉取的模型一致。  
   * 输入 ``exit`` 或 ``quit`` 以退出程序。  
   * 如果无法连接，请确认 Ollama 正在运行；如果使用远程主机，请确保两台设备在同一个局域网中。

故障排查
---------------

* **出现错误：`model requires more system memory ...`**

  * 表示模型太大，超出了你的设备内存限制。  
  * 使用较小的模型，如 ``moondream:1.8b`` 或 ``granite3.2-vision:2b``。  
  * 或者换用内存更大的电脑，并开启 Ollama 网络访问。

* **代码无法连接到 Ollama（连接被拒绝）**

  请检查以下事项：

  * 确保 Ollama 正在运行（使用 ``ollama serve`` 或已启动桌面应用）。  
  * 如果使用远程电脑，请在 Ollama 设置中启用 **Expose to network**。  
  * 确认代码中 ``ip="..."`` 的地址与局域网 IP 一致。  
  * 确保两台设备连接在同一个局域网内。
