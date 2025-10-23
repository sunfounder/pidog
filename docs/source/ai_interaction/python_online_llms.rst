.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_online_llm:

18. オンライン LLM への接続
================================

このレッスンでは、Pidog（または Raspberry Pi）をさまざまな **オンライン大規模言語モデル（LLM）** に接続する方法を学びます。  
各プロバイダーでは API キーが必要で、利用できるモデルも異なります。

ここでは次のことを説明します：

* API キーの安全な作成と保存方法  
* 自分に合ったモデルの選び方  
* サンプルコードを使ってモデルとチャットする方法

各プロバイダーごとに順を追って説明します。

----

始める前に
----------------

以下を完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、 ``vilib``、 ``pidog`` モジュールをインストールし、スクリプト ``i2samp.sh`` を実行。

OpenAI
----------

OpenAI は **GPT-4o** や **GPT-4.1** のような強力なモデルを提供しており、テキストと画像の両方に対応しています。

**API キーの取得と保存**

#. |link_openai_platform| にアクセスし、ログインします。**API keys** ページで **Create new secret key** をクリック。

   .. image:: img/llm_openai_create.png

#. Owner、Name、Project などの詳細を入力し、必要に応じて権限を設定したら **Create secret key** をクリック。

   .. image:: img/llm_openai_create_confirm.png

#. キーが作成されたらすぐにコピーします。再表示はできないため、紛失した場合は新しく発行する必要があります。

   .. image:: img/llm_openai_copy.png
 
#. プロジェクトフォルダ（例： ``/pidog/examples``）で ``secret.py`` というファイルを作成：

   .. code-block:: bash
   
       cd ~/pidog/examples
       sudo nano secret.py

#. 以下のようにキーを貼り付けます：

   .. code-block:: python

       # secret.py
       # 秘密情報をここに保存。このファイルを Git にコミットしないでください。
       OPENAI_API_KEY = "sk-xxx"

**課金の有効化とモデルの確認**

#. キーを使用する前に、OpenAI アカウントの **Billing** ページにアクセスし、支払い情報を追加して少額のクレジットをチャージします。

   .. image:: img/llm_openai_billing.png

#. 次に **Limits** ページで利用可能なモデルを確認し、コードで使用する正確なモデル ID をコピーします。

   .. image:: img/llm_openai_models.png

**サンプルコードでテスト**

#. サンプルコードを開きます：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 以下のコードに置き換え、 ``model="xxx"`` を希望のモデル（例： ``gpt-4o``）に変更します：

   .. code-block:: python

       from pidog.llm import OpenAI
       from secret import OPENAI_API_KEY
       
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
       
       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )

   保存して終了（ ``Ctrl+X`` → ``Y`` → ``Enter``）。

#. 最後にテストを実行します：


   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py
   

----

Gemini
------------------

Gemini は Google が提供する AI モデル群で、高速かつ汎用的なタスクに向いています。

**API キーの取得と保存**

#. |link_google_ai| にログインし、API Keys ページへ移動します。

   .. image:: img/llm_gemini_get.png

#. 右上の **Create API key** ボタンをクリックします。

   .. image:: img/llm_gemini_create.png

#. 既存のプロジェクトまたは新規プロジェクト用にキーを作成できます。

   .. image:: img/llm_gemini_choose.png

#. 生成された API キーをコピーします。

   .. image:: img/llm_gemini_copy.png

#. プロジェクトフォルダで以下を実行：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 以下のようにキーを貼り付けます：

   .. code-block:: python

        # secret.py
        # 秘密情報をここに保存。このファイルを Git にコミットしないでください。
       GEMINI_API_KEY = "AIxxx"

**利用可能なモデルの確認**

公式 |link_gemini_model| ページにアクセスすると、利用可能なモデルの一覧と、正確な API ID、各モデルの用途が表示されます。

   .. image:: img/llm_gemini_model.png

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 以下のコードに置き換え、 ``model="xxx"`` を希望するモデル（例：``gemini-2.5-flash``）に変更します：

   .. code-block:: python

       from pidog.llm import Gemini
       from secret import GEMINI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Gemini(
           api_key=GEMINI_API_KEY,
           model="gemini-2.5-flash",
       )

#. 保存して実行します：


   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Qwen
------------------

Qwen は Alibaba Cloud が提供する大規模言語モデルおよびマルチモーダルモデルのファミリーです。  
テキスト生成、推論、画像解析などのマルチモーダル理解をサポートしています。

**API キーの取得**

Qwen モデルを使用するには **API キー** が必要です。  
国際ユーザーは **DashScope International（Model Studio）** を使用します。  
中国本土のユーザーは **Bailian（百炼）** コンソールを使用できます。

* **国際ユーザー向け**

  #. Alibaba Cloud の公式 |link_qwen_inter| ページにアクセスします。  
  #. **Alibaba Cloud** アカウントでログインまたは新規登録します。  
  #. **Model Studio** に移動します（シンガポールまたは北京リージョンを選択）。  

     * ページ上部に “Activate Now” と表示された場合はクリックして有効化し、無料クレジットを受け取ります（シンガポールのみ）。  
     * 有効化は無料で、無料枠を超えた分のみ課金されます。  
     * 表示がない場合はすでに有効化済みです。

  #. **Key Management** ページへ進み、 **API Key** タブで **Create API Key** をクリックします。  
  #. 作成後、API キーをコピーして安全に保管します。

    .. image:: img/llm_qwen_api_key.png
        :width: 800

  .. note::
     香港、マカオ、台湾のユーザーも **International (Model Studio)** オプションを選択してください。

* **中国本土ユーザー向け**

  中国本土の場合は **Alibaba Cloud Bailian（百炼）** コンソールを使用します：

  #. |link_aliyun| （Bailian コンソール）にログインし、本人確認を完了します。  
  #. **Create API Key** を選択します。モデルサービスが有効化されていない場合は **Activate** をクリックし、利用規約に同意して無料枠を有効化します。その後、**Create API Key** ボタンが有効になります。

     .. image:: img/llm_qwen_aliyun_create.png

  #. **Create API Key** を再度クリックし、アカウントを確認後 **Confirm** をクリックします。

     .. image:: img/llm_qwen_aliyun_confirm.png

  #. 作成後、API キーをコピーします。

     .. image:: img/llm_qwen_aliyun_copy.png

**API キーの保存**

#. プロジェクトフォルダで以下を実行：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 以下のようにキーを貼り付けます：

   .. code-block:: python

        # secret.py
        # 秘密情報をここに保存。このファイルを Git にコミットしないでください。
        
        QWEN_API_KEY = "sk-xxx"

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 以下のコードに置き換え、 ``model="xxx"`` を希望するモデル（例： ``qwen-plus``）に変更します：

   .. code-block:: python

      from pidog.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )

#. 以下で実行します：


   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

Grok (xAI)
------------------
Grok は Elon Musk のチームによって開発された xAI の会話型 AI です。  
xAI API を通じて接続することができます。

**API キーの取得と保存**

#. |link_grok_ai| でアカウントを作成します。  
   先にクレジットをチャージしておく必要があります — チャージしないと API は動作しません。

#. API Keys ページにアクセスし、 **Create API key** をクリックします。

   .. image:: img/llm_grok_create.png

#. キーの名前を入力し、 **Create API key** をクリックします。

   .. image:: img/llm_grok_name.png

#. 生成されたキーをコピーし、安全に保管します。

   .. image:: img/llm_grok_copy.png

#. プロジェクトフォルダで以下を実行：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 以下のようにキーを貼り付けます：

   .. code-block:: python

        # secret.py
        # 秘密情報をここに保存。このファイルを Git にコミットしないでください。
        
        GROK_API_KEY = "xai-xxx"

**利用可能なモデルの確認**

xAI コンソールの Models ページにアクセスすると、利用可能なモデルとその API ID が表示されます。  
この ID をコード内で使用します。

   .. image:: img/llm_grok_model.png

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 以下のコードに置き換え、 ``model="xxx"`` を希望するモデル（例： ``grok-4-latest``）に変更します：

   .. code-block:: python

       from pidog.llm import Grok
       from secret import GROK_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. 以下で実行します：

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py
   
----

DeepSeek
------------------

DeepSeek は中国の LLM プロバイダーで、手頃な価格で高性能なモデルを提供しています。

**API キーの取得と保存**

#. |link_deepseek| にログインします。

#. 右上のメニューから **API Keys → Create API Key** を選択します。

   .. image:: img/llm_deepseek_create.png

#. 名前を入力し、 **Create** をクリックしてキーをコピーします。

   .. image:: img/llm_deepseek_copy.png

#. プロジェクトフォルダで以下を実行：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 以下のようにキーを追加します：

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**課金の有効化**

まずアカウントに少額（¥10 RMB など）をチャージしてください。

   .. image:: img/llm_deepseek_chognzhi.png

**利用可能なモデル**

（2025-09-12 時点）DeepSeek では以下のモデルが提供されています：

* ``deepseek-chat``  
* ``deepseek-reasoner``

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 以下のコードに置き換え、 ``model="xxx"`` を希望するモデル（例： ``deepseek-chat``）に変更します：

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

#. 以下で実行します：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Doubao
------------------
Doubao は ByteDance（バイトダンス）が提供する AI モデルプラットフォーム（Volcengine Ark）です。

**API キーの取得と保存**

#. |link_doubao| にログインします。

#. 左側のメニューから **API Key Management → Create API Key** を選択します。

   .. image:: img/llm_doubao_create.png

#. 名前を入力して **Create** をクリックします。

   .. image:: img/llm_doubao_name.png

#. **Show API Key** アイコンをクリックしてキーをコピーします。

   .. image:: img/llm_doubao_copy.png

#. プロジェクトフォルダで以下を実行：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. 以下のようにキーを追加します：

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**モデルの選択**

#. モデルマーケットにアクセスしてモデルを選択します。

   .. image:: img/llm_doubao_model_select.png

#. 例として **Doubao-seed-1.6** を選び、 **API 接入** をクリックします。

   .. image:: img/llm_doubao_model.png

#. API キーを選択し、 **Use API** をクリック。

   .. image:: img/llm_doubao_use_api.png

#. **Enable Model** をクリックします。

   .. image:: img/llm_doubao_kaitong.png

#. モデル ID にカーソルを合わせてコピーします。

   .. image:: img/llm_doubao_copy_id.png

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. 以下のコードに置き換え、 ``model="xxx"`` を希望するモデル（例： ``doubao-seed-1-6-250615``）に変更します：

   .. code-block:: python

       from pidog.llm import Doubao
       from secret import DOUBAO_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. 以下で実行します：


   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py


General
--------------

このプロジェクトは、複数の LLM プラットフォームへの接続を **統一インターフェース** を通じてサポートしています。  
以下のプラットフォームに標準対応しています：

* **OpenAI** （ChatGPT / GPT-4o、GPT-4、GPT-3.5）  
* **Gemini** （Google AI Studio / Vertex AI）  
* **Grok** （xAI）  
* **DeepSeek**  
* **Qwen（通义千问）**  
* **Doubao（豆包）**

さらに、**OpenAI API 形式と互換性のある他の LLM サービス** にも接続可能です。  
その場合は、各プラットフォームから **API Key** と適切な **base_url** を取得する必要があります。

**API キーの取得と保存**

#. 使用したいプラットフォームから **API Key** を取得します（詳細は各プラットフォームの公式コンソールを参照してください）。

#. プロジェクトフォルダで新しいファイルを作成します：

   .. code-block:: bash

      cd ~/pidog/examples
      nano secret.py

#. ``secret.py`` に以下のようにキーを追加します：

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   API Key は秘密情報です。 ``secret.py`` を公開リポジトリにアップロードしないでください。

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 18.online_llm_test.py

#. 以下のコード例を貼り付け、自分のプロバイダーに合った ``base_url`` と ``model`` を入力します：

   .. note::

      ``base_url`` について：  
      OpenAI API 形式および **互換性のある API** をサポートしています。  
      プロバイダーごとに ``base_url`` は異なるため、必ずドキュメントを確認してください。

   .. code-block:: python

      from pidog.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # 各プロバイダーの base_url を設定
          api_key=API_KEY,
          model="your-model-name-here",           # プロバイダーのモデル名を設定
      )

#. プログラムを実行します：


   .. code-block:: bash

      python3 18.online_llm_test.py



