
.. _py_online_llm:

18. 连接在线大语言模型（LLM）
================================

在本课程中，你将学习如何将 PiDog（或 Raspberry Pi）连接到不同的 **在线大语言模型（LLM）**。  
每个服务商都需要 API Key，并提供多种模型可供选择。

我们将学习如何：

* 安全地创建并保存 API Key  
* 选择适合你需求的模型  
* 使用示例代码与这些模型对话

----

开始之前
----------------

请确保你已完成以下步骤：

* :ref:`install_all_modules` — 安装 ``robot-hat``、``vilib``、``pidog`` 模块，并运行 ``i2samp.sh`` 脚本。

OpenAI
----------

OpenAI 提供功能强大的模型，如 **GPT-4o** 和 **GPT-4.1**，它们支持文本与图像任务。

以下是设置步骤：

**获取并保存 API Key**

#. 前往 |link_openai_platform| 并登录。在 **API keys** 页面点击 **Create new secret key**。

   .. image:: img/llm_openai_create.png

#. 填写相关信息（Owner、Name、Project 及权限），然后点击 **Create secret key**。

   .. image:: img/llm_openai_create_confirm.png

#. 创建完成后，**立刻复制** API Key —— 你之后将无法再次查看它。如果丢失，需要重新生成。

   .. image:: img/llm_openai_copy.png

#. 在你的项目目录（例如 ``/pidog/examples``）下创建一个 ``secret.py`` 文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 将你的 API Key 粘贴进去，格式如下：

   .. code-block:: python

       # secret.py
       # 将密钥保存在此文件中，请勿提交到 Git
       OPENAI_API_KEY = "sk-xxx"

**启用付费功能并查看可用模型**

#. 使用前，前往 OpenAI 账户的 **Billing** 页面，添加支付方式并充值少量余额。

   .. image:: img/llm_openai_billing.png

#. 然后前往 **Limits** 页面查看你的账户可用的模型，并复制模型 ID 以便后续代码中使用。

   .. image:: img/llm_openai_models.png

**测试示例代码**

#. 打开示例代码：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 将内容替换为以下代码，并将 ``model="xxx"`` 替换为你想使用的模型（例如 ``gpt-4o``）：

   .. code-block:: python

       from pidog.llm import OpenAI
       from secret import OPENAI_API_KEY
       
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
       
       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )

   保存并退出（``Ctrl+X`` → ``Y`` → ``Enter``）。

#. 最后，运行测试：


   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py
   

----

Gemini
------------------

Gemini 是 Google 的一系列 AI 模型，响应速度快，适合通用型任务。

**获取并保存 API Key**

#. 登录 |link_google_ai|，进入 API Keys 页面。

   .. image:: img/llm_gemini_get.png

#. 点击右上角的 **Create API key** 按钮。

   .. image:: img/llm_gemini_create.png

#. 你可以为现有项目或新建项目生成 API Key。

   .. image:: img/llm_gemini_choose.png

#. 复制生成的 API Key。

   .. image:: img/llm_gemini_copy.png

#. 在项目目录中编辑密钥文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 粘贴你的密钥：

   .. code-block:: python

        # secret.py
        # 将密钥保存在此文件中，请勿提交到 Git
        GEMINI_API_KEY = "AIxxx"

**查看可用模型**

访问 |link_gemini_model| 官方页面，这里会列出可用的模型、对应的 API ID 以及适用的场景。

   .. image:: img/llm_gemini_model.png

**测试示例代码**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 将内容替换为以下代码，并将 ``model="xxx"`` 替换为所需模型（如 ``gemini-2.5-flash``）：

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

Qwen 是阿里云推出的一系列大语言与多模态模型，支持文本生成、推理和多模态理解（如图像分析）。

**获取 API Key**

调用 Qwen 模型需要一个 **API Key**。  
国际用户建议使用 **DashScope International（Model Studio）** 控制台；  
中国大陆用户可使用 **阿里云百炼（Bailian）** 控制台。

* **国际用户**

  #. 前往 |link_qwen_inter| （阿里云），登录或注册账号。  
  #. 进入 **Model Studio** （选择新加坡或北京地区）。  
     
     * 如果顶部出现 “Activate Now” 提示，点击激活 Model Studio 并领取免费额度（仅新加坡区域提供）。  
     * 激活免费，不会产生费用，只有用完免费额度后才会收费。  
     * 如果没有提示，表示服务已激活。
  
  #. 进入 **Key Management** 页面，在 **API Key** 标签下点击 **Create API Key**。  
  #. 创建完成后，复制并妥善保存你的 API Key。
  
  .. image:: img/llm_qwen_api_key.png
      :width: 800

  .. note::
     香港、澳门和台湾用户也请选择 **International（Model Studio）**。

* **中国大陆用户**

  如果你在中国大陆，可以使用 **阿里云百炼（Bailian）** 控制台：

  #. 登录 |link_aliyun| （百炼控制台）并完成实名认证。  
  #. 点击 **创建 API Key**，若提示未开通模型服务，点击 **开通**，同意协议并领取免费额度。  
     
     .. image:: img/llm_qwen_aliyun_create.png

  #. 再次点击 **创建 API Key**，检查账号后点击 **确认**。
  
     .. image:: img/llm_qwen_aliyun_confirm.png

  #. 创建完成后，复制 API Key。
  
     .. image:: img/llm_qwen_aliyun_copy.png

**保存 API Key**

#. 在你的项目目录中：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 将密钥粘贴进去：

   .. code-block:: python

        # secret.py
        # 将密钥保存在此文件中，请勿提交到 Git
        QWEN_API_KEY = "sk-xxx"

**测试示例代码**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 替换内容如下，并将 ``model="xxx"`` 改为你想要的模型（如 ``qwen-plus``）：

   .. code-block:: python

      from pidog.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )

#. 运行测试：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py


Grok (xAI)
------------------

Grok 是由 Elon Musk 团队开发的 xAI 对话式 AI，可以通过 xAI API 进行连接。

**获取并保存 API Key**

#. 前往 |link_grok_ai| 注册账号。请先充值一些额度，否则 API 无法使用。  
#. 进入 API Keys 页面，点击 **Create API key**。  

   .. image:: img/llm_grok_create.png

#. 输入密钥名称，然后点击 **Create API key**。  

   .. image:: img/llm_grok_name.png

#. 复制生成的密钥并妥善保存。  

   .. image:: img/llm_grok_copy.png

#. 在项目目录中：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 粘贴密钥：

   .. code-block:: python

        # secret.py
        # 将密钥保存在此文件中，请勿提交到 Git
        GROK_API_KEY = "xai-xxx"

**查看可用模型**

前往 xAI 控制台的模型页面，可以看到可用的模型及其精确的 API ID，将其用于代码中。

   .. image:: img/llm_grok_model.png

**测试示例代码**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 替换内容如下，并将 ``model="xxx"`` 改为你要使用的模型（如 ``grok-4-latest``）：

   .. code-block:: python

       from pidog.llm import Grok
       from secret import GROK_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. 运行测试：

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py
   
----

DeepSeek
------------------

DeepSeek 是一家中国的大模型提供商，提供高性价比且性能出色的模型。

**获取并保存 API Key**

#. 登录 |link_deepseek|。

#. 在右上角菜单中选择 **API Keys → Create API Key**。

   .. image:: img/llm_deepseek_create.png

#. 输入名称，点击 **Create**，然后复制密钥。

   .. image:: img/llm_deepseek_copy.png

#. 在项目目录中：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 添加你的密钥：

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**启用付费**

使用前需要先为账户充值。可以先充值少量金额（例如 10 元人民币）。

   .. image:: img/llm_deepseek_chognzhi.png

**可用模型**

截至 2025-09-12，DeepSeek 提供以下模型：

* ``deepseek-chat``  
* ``deepseek-reasoner``

**测试示例代码**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 将内容替换为以下代码，并将 ``model="xxx"`` 改为所需模型（如 ``deepseek-chat``）：

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

#. 运行测试：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py


Doubao
------------------

Doubao 是字节跳动旗下的 AI 模型平台（Volcengine Ark）。

**获取并保存 API Key**

#. 登录 |link_doubao|。

#. 在左侧菜单中找到 **API Key Management → Create API Key**。

   .. image:: img/llm_doubao_create.png

#. 输入名称并点击 **Create**。

   .. image:: img/llm_doubao_name.png

#. 点击 **Show API Key** 图标并复制密钥。

   .. image:: img/llm_doubao_copy.png

#. 在项目目录中：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 添加密钥：

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**选择模型**

#. 前往模型市场并选择一个模型。

   .. image:: img/llm_doubao_model_select.png

#. 例如，选择 **Doubao-seed-1.6**，点击 **API 接入**。

   .. image:: img/llm_doubao_model.png

#. 选择你的 API Key，点击 **Use API**。

   .. image:: img/llm_doubao_use_api.png

#. 点击 **Enable Model** 启用模型。

   .. image:: img/llm_doubao_kaitong.png

#. 鼠标悬停在模型 ID 上即可复制。

   .. image:: img/llm_doubao_copy_id.png

**测试示例代码**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 替换内容如下，并将 ``model="xxx"`` 改为你选择的模型（如 ``doubao-seed-1-6-250615``）：

   .. code-block:: python

       from pidog.llm import Doubao
       from secret import DOUBAO_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. 运行测试：


   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py


General
--------------

本项目通过统一的接口支持连接多个 LLM 平台。  
我们已内置支持以下模型服务：

* **OpenAI** （ChatGPT / GPT-4o, GPT-4, GPT-3.5）  
* **Gemini** （Google AI Studio / Vertex AI）  
* **Grok** （xAI）  
* **DeepSeek**  
* **Qwen（通义千问）**  
* **Doubao（豆包）**

此外，你还可以连接 **任何兼容 OpenAI API 格式的 LLM 服务**。  
对于这些平台，你需要手动获取对应的 **API Key** 和正确的 **base_url**。

**获取并保存 API Key**

#. 从你要使用的平台的官方控制台获取 **API Key**。  

#. 在项目文件夹中创建一个新文件：

   .. code-block:: bash

      cd ~/pidog/examples
      nano secret.py

#. 将你的 Key 添加到 ``secret.py`` 中：

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   请妥善保管 API Key，不要将 ``secret.py`` 上传到公共仓库。

**测试示例代码**

#. 打开测试文件：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 18.online_llm_test.py

#. 将 Python 文件内容替换为以下示例，并填写正确的 ``base_url`` 和 ``model``：

   .. note::

      关于 ``base_url``：  
      我们支持 OpenAI API 格式，也支持任何兼容 OpenAI API 的服务。  
      每个平台的 ``base_url`` 都不相同，请参考其官方文档。

   .. code-block:: python

      from pidog.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # 替换为你的平台 base_url
          api_key=API_KEY,
          model="your-model-name-here",           # 替换为你的模型名称
      )

#. 运行测试：

   .. code-block:: bash

      python3 18.online_llm_test.py



