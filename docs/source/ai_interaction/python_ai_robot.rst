.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ai_voice_assistant_robot:

20. AI音声アシスタントドッグ
===============================

このレッスンでは、Pidogを **AI搭載の音声アシスタントドッグ** に変身させます。  
ロボットはあなたの声で起動し、話しかけた内容を理解し、  
個性のある声で応答し、動き・ジェスチャー・LEDの光で「感情」を表現できます。

以下を活用して、 **完全にインタラクティブなロボットコンパニオン** を作成します：

* **LLM**：大規模言語モデル（例：OpenAI GPTまたはDoubao）による自然な会話。  
* **STT**：音声認識（Speech-to-Text）。  
* **TTS**：音声合成（Text-to-Speech）による表情豊かな音声応答。  
* **センサー＋アクション**：超音波センサー、カメラ（オプション）、タッチセンサー、内蔵の表現豊かな動き。

----

始める前に
----------------

以下を完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat`` 、 ``vilib`` 、 ``pidog`` モジュールをインストールし、スクリプト ``i2samp.sh`` を実行します。  
* :ref:`test_piper` — **Piper TTS** の対応言語を確認。  
* :ref:`test_vosk` — **Vosk STT** の対応言語を確認。  
* :ref:`py_online_llm` — **とても重要**： **OpenAI** または **Doubao** など、対応するLLMのAPIキーを取得します。

事前に用意しておくもの：

* Pidogに接続された動作する **マイク** と **スピーカー**。  
* ``secret.py`` に保存された有効な **APIキー** 。  
* 安定したネットワーク接続（ **有線接続** を推奨します）。

----

サンプルを実行する
------------------------------

両方の言語バージョンは同じディレクトリに配置されています：

.. code-block:: bash

   cd ~/pidog/examples

**英語版** （OpenAI GPT、英語の手順）：

.. code-block:: bash

   sudo python3 20_voice_active_dog_gpt.py

* LLM: ``OpenAI GPT-4o-mini``  
* TTS: ``en_US-ryan-low`` (Piper)  
* STT: Vosk (``en-us``)

起動ワード：

.. code-block::

   "Hey buddy"

---

**中国語版** （Doubao、中国語の手順）：

.. code-block:: bash

   sudo python3 20_voice_active_dog_doubao_cn.py

* LLM: ``Doubao-seed-1-6-250615``  
* TTS: ``zh_CN-huayan-x_low`` (Piper)  
* STT: Vosk (``cn``)

起動ワード：

.. code-block::

   "你好 旺财"

.. note::

   コード内で **起動ワード** と **ロボット名** を変更できます：
   ``NAME = "Buddy"`` または ``NAME = "旺财"``  
   ``WAKE_WORD = ["hey buddy"]`` または ``WAKE_WORD = ["你好 旺财"]``

----

何が起こるか
-----------------

このサンプルを正しく実行すると、以下のように動作します：

* ロボットは **ウェイクワードを待機** します（例：「Hey Buddy」「你好 旺财」）。

* ウェイクワードを検知すると：

  * LED ストリップが **ピンク（呼吸エフェクト）** に点灯し、起動合図を示します。  
  * ロボットが設定されたウェイク応答を発話します —  
    例：「Hi there!」（Piper TTS による）

* その後、Vosk STT を使って **あなたの音声を認識** します（キーボード入力が有効な場合は入力も可能）。

* 音声を認識したあと、システムは次を実行します：

  * ``WITH_IMAGE = True`` のため **カメラフレームをキャプチャ** し、あなたのメッセージと画像を **LLM** （OpenAI ``gpt-4o-mini``）に送信します。  
  * モデルが考えている間、LED は **イエロー（処理中）** に変わります。  
  * モデルの応答は2つの部分に分かれます：

    - ``ACTIONS:`` より前 → 音声で出力されます。  
    - ``ACTIONS:`` より後 → ロボットの動作キーワードにマッピングされます。

  * ロボットは ``ActionFlow`` を使って **アクションを実行** します。  
  * 動作完了後、ロボットは **SIT 姿勢に戻り**、LED は消灯します。

* **超音波センサーが 10 cm 未満の障害物を検知** した場合：

  - メッセージを注入: ``<<<Ultrasonic sense too close: {distance}cm>>>``  
  - ロボットが自動で後退: ``ACTIONS: backward``  
  - このラウンドでは **画像入力が無効** になります。

* **タッチセンサーが反応** した場合：

  - **LIKE** タッチ（例：FRONT_TO_REAR）のとき：

    - 注入: ``<<<好きなタッチスタイル: FRONT_TO_REAR>>>``  
    - ``ACTIONS: nod`` （肯定的な反応）

  - **HATE** タッチ（例：REAR_TO_FRONT）のとき：

    - 注入: ``<<<嫌いなタッチスタイル: REAR_TO_FRONT>>>``  
    - ``ACTIONS: backward`` （回避反応）

* **LED のライフサイクル:**

  - ``on_start`` → SIT 姿勢、LED 消灯  
  - ``before_listen`` → シアン（待機状態）  
  - ``before_think`` → イエロー（処理中）  
  - ``before_say`` → ピンク（発話中）  
  - ``after_say`` / ``on_finish_a_round`` → SIT 姿勢、LED 消灯  
  - ``on_stop`` → アクションフローを停止し、デバイスを閉じる

**インタラクション例**


.. code-block:: text

   You: Hey Buddy
   Robot: Hi there!

   You: What do you see in front of you?
   Robot: I can see a notebook and a blue mug on the table.
   ACTIONS: think

   You: Do a little nod for me.
   Robot: Of course. Watch my majestic nod.
   ACTIONS: nod

   (Front-to-rear touch on the head)
   Robot: Ooooh, that’s nice!
   ACTIONS: nod

   (Moving too close)
   Robot: Hey hey—too close! Backing up for safety.
   ACTIONS: backward


----

他の LLM または TTS への切り替え
--------------------------------------------

少しコードを編集するだけで、他の LLM、TTS、または STT 言語に簡単に切り替えることができます：

* サポートされている LLM：

  * OpenAI  
  * Doubao  
  * Deepseek  
  * Gemini  
  * Qwen  
  * Grok

* :ref:`test_piper` — **Piper TTS** の対応言語を確認。  
* :ref:`test_vosk` — **Vosk STT** の対応言語を確認。

切り替えるには、コードの初期化部分を以下のように変更します：

.. code-block:: python

  from pidog.llm import OpenAI as LLM

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # モデルと言語を設定
  TTS_MODEL = "en_US-ryan-low"
  STT_LANGUAGE = "en-us"

----

トラブルシューティング
--------------------------

* **ロボットがウェイクワードに反応しない場合**  

  * マイクが動作しているか確認。  
  * ``WAKE_ENABLE = True`` になっているか確認。  
  * ウェイクワードをあなたの発音に合わせて調整。

* **スピーカーから音が出ない場合**  

  * TTS モデルの設定を確認。  
  * Piper または Espeak を手動でテスト。  
  * スピーカーの接続と音量を確認。

* **API キーのエラーまたはタイムアウト**  

  * ``secret.py`` のキーを確認。  
  * ネットワーク接続を確認。  
  * LLM がサポートされていることを確認。

* **超音波センサーが予期せず反応し続ける場合**  

  * センサーの取り付け高さと角度を確認。  
  * コード内の ``TOO_CLOSE`` 距離閾値を調整。
