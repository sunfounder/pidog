.. note::

   您好，欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者 Facebook 社区！与众多爱好者一起深入探索 Raspberry Pi、Arduino 和 ESP32。

   **为什么要加入？**

   - **专家支持**：获得来自我们社区和团队的售后问题及技术挑战方面的帮助。
   - **学习与分享**：交流技巧和教程，提升您的技能。
   - **独家预览**：抢先获取新产品公告和先睹为快的机会。
   - **特别折扣**：享受我们最新产品的独家折扣。
   - **节日促销与赠品**：参与赠品和节日促销活动。

   👉 准备好与我们一同探索和创造了吗？点击 [|link_sf_facebook|]，立即加入！

.. _py_online_llm:

18. 连接在线大语言模型（LLMs）
================================

在本课中，我们将学习如何将您的 PiDog（或 Raspberry Pi）连接到不同的 **在线大语言模型（LLMs）**。
每个提供商都提供一个 API 密钥，并提供不同的模型供您选择。

我们将介绍如何：

* 安全地创建和保存您的 API 密钥。
* 选择适合您需求的模型。
* 运行示例代码与模型进行对话。

让我们逐步了解每个提供商的设置方法。

----

开始之前
----------------

请确保您已完成：

* :ref:`install_all_modules` — 安装 ``robot-hat``、``vilib``、``pidog`` 模块，然后运行脚本 ``i2samp.sh``。


OpenAI
----------

OpenAI 提供强大的模型，如 **GPT-4o** 和 **GPT-4.1**，可用于文本和视觉任务。

设置方法如下：

**获取并保存您的 API 密钥**

#. 前往 |link_openai_platform| 并登录。在 **API keys** 页面，点击 **Create new secret key**。

   .. image:: img/llm_openai_create.png

#. 填写详细信息（Owner、Name、Project 以及权限，如果需要），然后点击 **Create secret key**。

   .. image:: img/llm_openai_create_confirm.png

#. 密钥创建后，请立即复制——您将无法再次查看。如果丢失，则需要重新生成一个新的。

   .. image:: img/llm_openai_copy.png

#. 在您的项目文件夹中（例如：``/pidog/examples``），创建一个名为 ``secret.py`` 的文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 将您的密钥粘贴到文件中，格式如下：

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**启用计费并查看模型**

#. 在使用密钥之前，请前往 OpenAI 账户的 **Billing** 页面，添加付款信息并充值少量额度。

   .. image:: img/llm_openai_billing.png

#. 然后前往 **Limits** 页面，查看您的账户可用的模型，并复制要在代码中使用的确切模型 ID。

   .. image:: img/llm_openai_models.png

**使用示例代码进行测试**

#. 打开示例代码：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 将内容替换为以下代码，并将 ``model="xxx"`` 更新为您想要的模型（例如 ``gpt-4o``）：

   .. code-block:: python

       from pidog.llm import OpenAI
       from secret import OPENAI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )

   保存并退出（``Ctrl+X``，然后 ``Y``，最后 ``Enter``）。

#. 最后，运行测试：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Gemini
------------------

Gemini 是 Google 的 AI 模型系列，速度快，非常适合通用任务。

**获取并保存您的 API 密钥**

#. 登录 |link_google_ai|，然后进入 API Keys 页面。

   .. image:: img/llm_gemini_get.png

#. 点击右上角的 **Create API key** 按钮。

   .. image:: img/llm_gemini_create.png

#. 您可以为现有项目或新项目创建密钥。

   .. image:: img/llm_gemini_choose.png

#. 复制生成的 API 密钥。

   .. image:: img/llm_gemini_copy.png

#. 在您的项目文件夹中：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 粘贴密钥：

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
       GEMINI_API_KEY = "AIxxx"

**查看可用模型**

前往官方 |link_gemini_model| 页面，您将在此看到模型列表、它们的确切 API ID，以及每个模型针对的用例。

   .. image:: img/llm_gemini_model.png

**使用示例代码进行测试**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 将内容替换为以下代码，并将 ``model="xxx"`` 更新为您想要的模型（例如 ``gemini-2.5-flash``）：

   .. code-block:: python

       from pidog.llm import Gemini
       from secret import GEMINI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Gemini(
           api_key=GEMINI_API_KEY,
           model="gemini-2.5-flash",
       )

#. 保存并运行：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Qwen
------------------

Qwen 是阿里云提供的系列大语言和多模态模型。
这些模型支持文本生成、推理和多模态理解（如图像分析）。

**获取 API 密钥**

要调用 Qwen 模型，您需要一个 **API 密钥**。
大多数国际用户应使用 **DashScope International（Model Studio）** 控制台。
中国大陆用户可以使用 **百炼（Bailian）** 控制台。

* **国际用户**

  #. 前往 |link_qwen_inter| 官方页面（阿里云国际站）。
  #. 登录或创建 **Alibaba Cloud** 账户。
  #. 导航至 **Model Studio**\ （选择新加坡或北京区域）。

      * 如果页面顶部出现 "Activate Now" 提示，请点击它以激活 Model Studio 并获得免费配额（仅限新加坡区域）。
      * 激活是免费的——只有在免费配额使用完毕后才会开始计费。
      * 如果没有出现激活提示，说明服务已处于激活状态。

  #. 进入 **Key Management** 页面。在 **API Key** 选项卡上，点击 **Create API Key**。
  #. 创建后，复制您的 API 密钥并妥善保管。

    .. image:: img/llm_qwen_api_key.png
        :width: 800

  .. note::
     香港、澳门和台湾的用户也应选择 **International（Model Studio）** 选项。

* **中国大陆用户**

  如果您在中国大陆，可以使用 **阿里云百炼（Bailian）** 控制台：

  #. 登录 |link_aliyun|\ （百炼控制台）并完成账户验证。
  #. 选择 **Create API Key**。如果提示模型服务未激活，请点击 **Activate**，同意条款并领取免费配额。激活后，**Create API Key** 按钮将会启用。

     .. image:: img/llm_qwen_aliyun_create.png

  #. 再次点击 **Create API Key**，检查您的账户，然后点击 **Confirm**。

     .. image:: img/llm_qwen_aliyun_confirm.png

  #. 创建完成后，复制您的 API 密钥。

     .. image:: img/llm_qwen_aliyun_copy.png

**保存您的 API 密钥**

#. 在您的项目文件夹中：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 将您的密钥粘贴为以下格式：

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.

        QWEN_API_KEY = "sk-xxx"

**使用示例代码进行测试**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 将内容替换为以下代码，并将 ``model="xxx"`` 更新为您想要的模型（例如 ``qwen-plus``）：

   .. code-block:: python

      from pidog.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )


#. 运行：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

Grok（xAI）
------------------
Grok 是 xAI 的对话式 AI，由 Elon Musk 的团队创建。您可以通过 xAI API 连接到它。

**获取并保存您的 API 密钥**

#. 在此处注册账户：|link_grok_ai|。请先向您的账户充值一些额度——否则 API 将无法使用。

#. 进入 API Keys 页面，点击 **Create API key**。

   .. image:: img/llm_grok_create.png

#. 为密钥输入一个名称，然后点击 **Create API key**。

   .. image:: img/llm_grok_name.png

#. 复制生成的密钥并妥善保管。

   .. image:: img/llm_grok_copy.png

#. 在您的项目文件夹中：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 将您的密钥粘贴为以下格式：

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.

        GROK_API_KEY = "xai-xxx"

**查看可用模型**

前往 xAI 控制台的 Models 页面。您可以在此看到您的团队可用的所有模型及其确切的 API ID——在代码中使用这些 ID。

   .. image:: img/llm_grok_model.png

**使用示例代码进行测试**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 将内容替换为以下代码，并将 ``model="xxx"`` 更新为您想要的模型（例如 ``grok-4-latest``）：

   .. code-block:: python

       from pidog.llm import Grok
       from secret import GROK_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. 运行：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

DeepSeek
------------------

DeepSeek 是一家中国的 LLM 提供商，提供经济实惠且功能强大的模型。

**获取并保存您的 API 密钥**

#. 登录 |link_deepseek|。

#. 在右上角菜单中，选择 **API Keys → Create API Key**。

   .. image:: img/llm_deepseek_create.png

#. 输入名称，点击 **Create**，然后复制密钥。

   .. image:: img/llm_deepseek_copy.png

#. 在您的项目文件夹中：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 添加您的密钥：

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**启用计费**

您需要先为账户充值。从小额开始（如 10 元人民币）。

   .. image:: img/llm_deepseek_chognzhi.png

**可用模型**

在撰写本文时（2025-09-12），DeepSeek 提供以下模型：

* ``deepseek-chat``
* ``deepseek-reasoner``

**使用示例代码进行测试**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 将内容替换为以下代码，并将 ``model="xxx"`` 更新为您想要的模型（例如 ``deepseek-chat``）：

   .. code-block:: python

       from pidog.llm import Deepseek
       from secret import DEEPSEEK_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Deepseek(
           api_key=DEEPSEEK_API_KEY,
           model="deepseek-chat",
           max_messages=20,
       )

#. 运行：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Doubao
------------------
Doubao 是字节跳动的 AI 模型平台（火山引擎方舟）。

**获取并保存您的 API 密钥**

#. 登录 |link_doubao|。

#. 在左侧菜单中，向下滚动到 **API Key Management → Create API Key**。

   .. image:: img/llm_doubao_create.png

#. 选择名称并点击 **Create**。

   .. image:: img/llm_doubao_name.png

#. 点击 **Show API Key** 图标并复制它。

   .. image:: img/llm_doubao_copy.png

#. 在您的项目文件夹中：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 添加您的密钥：

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**选择模型**

#. 前往模型市场挑选一个模型。

   .. image:: img/llm_doubao_model_select.png

#. 例如，选择 **Doubao-seed-1.6**，然后点击 **API 接入**。

   .. image:: img/llm_doubao_model.png

#. 选择您的 API 密钥，然后点击 **Use API**。

   .. image:: img/llm_doubao_use_api.png

#. 点击 **Enable Model**。

   .. image:: img/llm_doubao_kaitong.png

#. 将鼠标悬停在模型 ID 上以复制它。

   .. image:: img/llm_doubao_copy_id.png

**使用示例代码进行测试**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 将内容替换为以下代码，并将 ``model="xxx"`` 更新为您想要的模型（例如 ``doubao-seed-1-6-250615``）：

   .. code-block:: python

       from pidog.llm import Doubao
       from secret import DOUBAO_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. 运行：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py


通用平台
--------------

本项目支持通过统一接口连接到多个 LLM 平台。
我们内置了以下平台的支持：

* **OpenAI**\ （ChatGPT / GPT-4o、GPT-4、GPT-3.5）
* **Gemini**\ （Google AI Studio / Vertex AI）
* **Grok**\ （xAI）
* **DeepSeek**
* **Qwen（通义千问）**
* **Doubao（豆包）**

此外，您还可以连接到**任何兼容 OpenAI API 格式的其他 LLM 服务**。
对于这些平台，您需要手动获取 **API 密钥** 和正确的 **base_url**。

**获取并保存您的 API 密钥**

#. 从您要使用的平台获取 **API 密钥**。（详情请参阅各平台的官方控制台。）

#. 在您的项目文件夹中，创建一个新文件：

   .. code-block:: bash

      cd ~/pidog/examples
      nano secret.py

#. 将您的密钥添加到 ``secret.py`` 中：

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   请保管好您的 API 密钥。不要将 ``secret.py`` 上传到公共仓库。

**使用示例代码进行测试**

#. 打开测试文件：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 18.online_llm_test.py

#. 将一个 Python 文件的内容替换为以下示例，并填写您平台对应的 ``base_url`` 和 ``model``：

   .. note::

      关于 ``base_url``：
      我们支持 **OpenAI API 格式**，以及任何**\ 兼容**该格式的 API。
      每个提供商都有各自的 ``base_url``。请查阅其文档。

   .. code-block:: python

      from pidog.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # 填写您提供商的 base_url
          api_key=API_KEY,
          model="your-model-name-here",           # 从您的提供商处选择一个模型
      )


#. 运行程序：

   .. code-block:: bash

      python3 18.online_llm_test.py
