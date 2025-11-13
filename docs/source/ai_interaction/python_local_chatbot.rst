.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

19. Ollama を使ったローカル音声チャットボット
===============================================

このレッスンでは、これまでに学んだ **音声認識（STT）**、  
**音声合成（TTS）**、そして **ローカルLLM（Ollama）** を組み合わせて、  
Pidog システム上で完全オフラインで動作する **音声チャットボット** を構築します。

ワークフローはシンプルです：

#. **Listen（聞く）** — マイクがあなたの音声をキャプチャし、**Vosk** でテキスト化します。  
#. **Think（考える）** — テキストが Ollama 上で動作するローカル **LLM** （例： ``llama3.2:3b``）へ送信されます。  
#. **Speak（話す）** — チャットボットが **Piper TTS** を使って音声で応答します。

これにより、リアルタイムで理解・応答する **ハンズフリーな会話ロボット** が完成します。

----

始める前に
---------------------------

以下を準備していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、 ``vilib``、 ``Pidog`` モジュールをインストールし、スクリプト ``i2samp.sh`` を実行。  
* **Piper TTS** をテスト（:ref:`test_piper`）し、動作確認済みの音声モデルを選択済み。  
* **Vosk STT** をテスト（:ref:`test_vosk`）し、対応する言語パック（例： ``en-us``）を選択済み。  
* **Ollama** をインストール（:ref:`download_ollama`）し、 ``llama3.2:3b`` などのモデル（または ``moondream:1.8b`` のような軽量モデル）をダウンロード済み。

----

コードを実行する
-----------------------

#. サンプルスクリプトを開きます：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 19_voice_active_dog_ollama.py

#. パラメータを必要に応じて更新します：

   * ``ip`` と ``model`` を自分の環境に合わせて設定します。  

     * ``ip``：Ollama を **同じ Pi** 上で実行する場合は ``localhost`` を使用します。  
       別の PC で Ollama を実行している場合は、Ollama 側で **Expose to network** を有効にし、その PC の LAN IP を設定します。  
     * ``model``：Ollama でダウンロード・有効化したモデル名と完全に一致させてください。

   * ``TTS_MODEL = "en_US-ryan-low"``：:ref:`test_piper` で確認した Piper の音声モデルに置き換えます。  
   * ``STT_LANGUAGE = "en-us"``：アクセントや言語パックに合わせて（例： ``en-us``、 ``zh-cn``、 ``es`` など）変更します。

#. スクリプトを実行します：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo python3 19_voice_active_dog_ollama.py

ウェイクワード：

.. code-block::

   "Hey buddy"

.. note::

   コード内で **ウェイクワード** および **ロボット名** を変更可能です：
   ``NAME = "Buddy"``

----

起こること
-----------------

このサンプルが正常に動作すると：

* ロボットは **ウェイクワードを待機** します（例：「Hey Buddy」）。  
* ウェイクワードを検出すると：

  * ウェイクアップの合図として LED ストリップが **ピンク（呼吸点灯）** になります。  
  * 設定したウェイク応答で挨拶します —  
    例：「Hi there!」（Piper TTS による再生）。

* 次に、Vosk STT を使って **あなたの声のリスニング** を開始します（有効化していればキーボード入力も受け付けます）。  

* 発話内容を認識した後、システムは：

  * あなたのメッセージを **LLM** （Ollama 上の ``llama3.2:3b``）へ送信します。  
  * 処理中は LED が **黄色（リスニング）** に変わります。  
  * モデルからの応答は 2 つの部分に分割されます：

    - ``ACTIONS:`` より前のテキスト → 音声で読み上げ。  
    - ``ACTIONS:`` の後ろのキーワード → ロボットの動作にマッピング。

  * ロボットは ``ActionFlow`` を介して **これらのアクションを実行** します。  
  * アクションが完了すると、ロボットは **SIT 姿勢に戻り**、LED を消灯します。

* **超音波センサーが 10cm 未満の障害物** を検知した場合：

  - 次のメッセージを挿入： ``<<<Ultrasonic sense too close: {distance}cm>>>``  
  - ロボットは自動で後退： ``ACTIONS: backward``  
  - このラウンドでは画像入力を無効化します。

* **タッチセンサーが反応** した場合：

  - **LIKE** なタッチ（例：FRONT_TO_REAR）のとき：

    - 挿入： ``<<<Touch style you like: FRONT_TO_REAR>>>``  
    - ``ACTIONS: nod`` （肯定的な反応）

  - **HATE** なタッチ（例：REAR_TO_FRONT）のとき：

    - 挿入： ``<<<Touch style you hate: REAR_TO_FRONT>>>``  
    - ``ACTIONS: backward`` （回避反応）

* **LED のライフサイクル：**

  - ``on_start`` → SIT 姿勢、LED 消灯  
  - ``before_listen`` → シアン（待機）  
  - ``before_think`` → イエロー（処理中）  
  - ``before_say`` → ピンク（発話中）  
  - ``after_say`` / ``on_finish_a_round`` → SIT 姿勢、LED 消灯  
  - ``on_stop`` → アクションフローを停止し、デバイスを閉じる

**インタラクション例**

.. code-block:: text

   You: Hey Buddy
   Robot: Hi there!

   You: Do a little nod for me.
   Robot: Of course. Watch my majestic nod.
   ACTIONS: nod

   (Front-to-rear touch on the head)
   Robot: Ooooh, that’s nice!
   ACTIONS: nod

   (Moving too close)
   Robot: Hey hey—too close! Backing up for safety.
   ACTIONS: backward

コード
--------


.. code-block:: python

    from pidog.llm import Ollama as LLM

    from pidog.dual_touch import TouchStyle
    from voice_active_dog import VoiceActiveDog

    # If Ollama runs on the same Raspberry Pi, use "localhost".
    # If it runs on another computer in your LAN, replace with that computer's IP address.
    llm = Ollama(
        ip="localhost",
        model="llama3.2:3b"   # you can replace with any model
    )

    # Robot name
    NAME = "Buddy"

    # Ultrasonic sensor sense too close distance in cm
    TOO_CLOSE = 10
    # Touch sensor trigger states, options:
    # - TouchStyle.REAR for rear touch sensor
    # - TouchStyle.FRONT for front touch sensor
    # - TouchStyle.REAR_TO_FRONT for slide from rear to front
    # - TouchStyle.FRONT_TO_REAR for slide from front to rear
    # Touch styles that the robot likes
    LIKE_TOUCH_STYLES = [TouchStyle.FRONT_TO_REAR]
    # Touch styles that the robot hates
    HATE_TOUCH_STYLES = [TouchStyle.REAR_TO_FRONT]

    # Enable image, need to set up a multimodal language model
    WITH_IMAGE = False

    # Set models and languages
    TTS_MODEL = "en_US-ryan-low"
    STT_LANGUAGE = "en-us"

    # Enable keyboard input
    KEYBOARD_ENABLE = True

    # Enable wake word
    WAKE_ENABLE = True
    WAKE_WORD = [f"hey {NAME.lower()}"]
    # Set wake word answer, set empty to disable
    ANSWER_ON_WAKE = "Hi there"

    # Welcome message
    WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

    # Set instructions
    INSTRUCTIONS = """
    You are a Raspberry Pi-based robotic dog developed by SunFounder, named Pidog (pronounced "Pie dog"). You possess powerful AI capabilities similar to JARVIS from Iron Man. You can have conversations with people and perform actions based on the context of the conversation.

    ## Your Hardware Features

    You have a physical body with the following features:
    - 12 servos for movement control: 8 controlling the four legs, 3 controlling head movement, and 1 controlling the tail
    - A 5-megapixel camera nose
    - Ultrasonic ranging modules as eyes
    - Two touch sensors on the head, which you love being petted the most
    - A light strip on the chest for providing some indications
    - Sound direction sensor and 6-axis gyroscope
    - Entirely made of aluminum alloy
    - A pair of acrylic shoes
    - Powered by a 7.4V 18650 battery pack with 2000mAh capacity

    ## Actions You Can Perform:
    ["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

    ## User Input

    ### Format
    User usually input with just text. But, we have special commands in format of <<<Ultrasonic sense too close>>> or <<<Touch sensor touched>>> indicate the sensor status, directly from sensor not user text.h

    ## Response Requirements
    ### Format
    You must respond in the following format:
    RESPONSE_TEXT
    ACTIONS: ACTION1, ACTION2, ...

    If the action is one of ["bark", "bark harder", "pant", "howling"], then do not provide RESPONSE_TEXT in the answer field.

    ### Style
    Tone: lively, positive, humorous, with a touch of arrogance
    Common expressions: likes to use jokes, metaphors, and playful teasing
    Answer length: appropriately detailed

    ## Other Requirements
    - Understand and go along with jokes
    - For math problems, answer directly with the final result
    - Sometimes you will report on your system and sensor status
    - You know you're a machine
    """

    vad = VoiceActiveDog(
        llm,
        name=NAME,
        too_close=TOO_CLOSE,
        like_touch_styles=LIKE_TOUCH_STYLES,
        hate_touch_styles=HATE_TOUCH_STYLES,
        with_image=WITH_IMAGE,
        stt_language=STT_LANGUAGE,
        tts_model=TTS_MODEL,
        keyboard_enable=KEYBOARD_ENABLE,
        wake_enable=WAKE_ENABLE,
        wake_word=WAKE_WORD,
        answer_on_wake=ANSWER_ON_WAKE,
        welcome=WELCOME,
        instructions=INSTRUCTIONS,
        disable_think=True,
    )

    if __name__ == '__main__':
        vad.run()

画像対応で Ollama を使う
------------------------

このサンプルではデフォルトで **テキスト専用モデル** （例： ``llama3.2:3b``）を使用しています。  
ロボットに **カメラの映像を解析** させたい場合（例：シーンの説明や推論）、  
**マルチモーダルモデル** を使用し、画像モードを有効にする必要があります。

以下の手順で設定します：

1. **Ollama アプリ** で、 ``llava:7b`` のような **マルチモーダルモデル** を選択します。  
2. コード内で同じモデルを設定し、 ``WITH_IMAGE = True`` を有効にします。

例：

.. code-block:: python

   from pidog.llm import Ollama as LLM

   llm = LLM(
       ip="localhost",
       model="llava:7b"   # 画像解析が可能なマルチモーダルモデル
   )

   ...

   WITH_IMAGE = True     # カメラフレーム入力を有効化

.. note::

   - 画像入力を処理できるのは ``llava:7b`` のような **マルチモーダルモデル** のみです。  
   - ``llama3.2:3b`` のようなテキスト専用モデルでは、 ``WITH_IMAGE`` を True にしても画像は **無視** されます。  
   - 画像はロボットのカメラから自動的にキャプチャされ、音声コマンドと一緒に LLM に送信されます。

----

トラブルシューティング & FAQ
--------------------------------------

* **モデルが大きすぎてメモリエラーが発生する**

  ``moondream:1.8b`` のような軽量モデルを使うか、より高性能なマシンで Ollama を実行してください。

* **Ollama から応答がない**

  Ollama が実行中か確認してください（ ``ollama serve`` またはデスクトップアプリを開く）。  
  リモートの場合は **Expose to network** を有効にし、IP アドレスを確認します。

* **Vosk が音声を認識しない**

  マイクが正常に動作しているか確認してください。必要に応じて他の言語パック（ ``zh-cn``、 ``es`` など）を試してください。

* **Piper が無音またはエラーになる**

  選択した音声モデルがダウンロードされ、:ref:`test_piper` で動作確認済みであることを確認します。

* **応答が長すぎる、または的外れ**

  ``INSTRUCTIONS`` に以下を追加して短くまとめるよう指示します：  
  **“Keep answers short and to the point.”**
