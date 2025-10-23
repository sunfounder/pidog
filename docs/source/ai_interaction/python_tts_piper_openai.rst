.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

15. Piper と OpenAI を使った TTS
========================================================

前回のレッスンでは、Raspberry Pi に標準搭載されている 2 つの TTS エンジン（ **Espeak** と **Pico2Wave**）を試しました。  
今回は、より強力な 2 つの音声合成エンジンを使います：

* **Piper**：Raspberry Pi 上で動作するオフラインのニューラルネットワーク型 TTS。  
* **OpenAI TTS**：オンラインの高品質音声合成サービスで、非常に自然な音声を生成します。

----

始める前に
----------------

以下を完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、 ``vilib``、 ``pidog`` モジュールをインストールし、スクリプト ``i2samp.sh`` を実行します。

.. _test_piper:

Piper のテスト
------------------

**手順**：

#. 新しいファイルを作成：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_piper.py

#. 以下のコードを貼り付け、 ``Ctrl+X`` → ``Y`` → ``Enter`` で保存します。

   .. code-block:: python

       from pidog.tts import Piper

       tts = Piper()

       # サポートされている言語の一覧を表示
       print(tts.available_countrys())

       # 英語 (en_us) のモデル一覧を表示
       print(tts.available_models('en_us'))

       # 音声モデルを設定（未ダウンロードの場合は自動で取得）
       tts.set_model("en_US-amy-low")

       # テスト音声
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()``：利用可能な言語を表示  
   * ``available_models()``：指定した言語のモデルを一覧表示  
   * ``set_model()``：音声モデルを設定（未取得なら自動ダウンロード）  
   * ``say()``：テキストを音声に変換して再生

#. 以下のコマンドで実行：

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. 初回実行時、選択した音声モデルが自動的にダウンロードされます。

   * Pidog が ``Hello! I'm Piper TTS.`` と話すのが聞こえるはずです。  
   * ``set_model()`` に他のモデル名を指定すれば、別の言語や声にも切り替えられます。


OpenAI TTS をテストする
-------------------------------

**API キーを取得して保存する**

#. |link_openai_platform| にアクセスしてログインします。 **API keys** ページで **Create new secret key** をクリックします。

   .. image:: img/llm_openai_create.png

#. 詳細（Owner、Name、Project、必要に応じて permissions）を入力し、 **Create secret key** をクリックします。

   .. image:: img/llm_openai_create_confirm.png

#. キーが作成されたら、すぐにコピーしてください — 再表示はできません。失くした場合は、新しいキーを生成する必要があります。

   .. image:: img/llm_openai_copy.png

#. プロジェクトフォルダ（例: ``/pidog/examples``）に ``secret.py`` というファイルを作成します:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. ファイルに以下のようにキーを貼り付けます:

   .. code-block:: python

       # secret.py
       # シークレット情報をここに保存します。このファイルを Git にコミットしないでください。
       OPENAI_API_KEY = "sk-xxx"

**テストプログラムを作成して実行する**

#. 新しいファイルを作成します:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano test_tts_openai.py

#. 下記のサンプルコードをファイルにコピーします。 ``Ctrl+X`` 、次に ``Y`` 、最後に ``Enter`` を押して保存して終了します。

   .. code-block:: python

      from pidog.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # または上記の try/except バージョンを使用

      # OpenAI TTS を初期化
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # 低遅延 TTS モデル
      tts.set_voice('alloy')            # 音声を選択

      # クイックテスト（動作確認）
      tts.say("Hello! I'm OpenAI TTS.")

#. プログラムを実行します:

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. Pidog から次の音声が聞こえるはずです：  

   ``Hello! I'm OpenAI TTS.``

----

トラブルシューティング
--------------------------------------

* **'secret' というモジュールが見つかりません（No module named 'secret'）**

  これは ``secret.py`` が Python ファイルと同じフォルダにないことを意味します。  
  ``secret.py`` をスクリプトを実行しているディレクトリに移動してください。例:

  .. code-block:: bash

     ls ~/pidog/examples
     # secret.py と .py ファイルの両方が表示されることを確認します

* **OpenAI: 無効な API キー / 401**

  * キー全体（ ``sk-`` で始まる）を正しく貼り付け、余分なスペースや改行がないことを確認してください。
  * コードで正しくインポートしていることを確認します:

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Pi 上でネットワークアクセスを確認します（ ``ping api.openai.com`` を試してください）。

* **OpenAI: クォータ超過 / 請求エラー（Quota exceeded / billing error）**

  * OpenAI ダッシュボードで請求情報を追加するか、クォータを増やす必要がある場合があります。
  * アカウントまたは請求の問題を解決した後、再試行してください。

* **Piper: tts.say() は動作するが音声が出ない**

  * 音声モデルが実際に存在することを確認します:

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * コード内のモデル名が正確に一致していることを確認します:

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Pi のオーディオ出力デバイスと音量（ ``alsamixer``）を確認し、スピーカーが接続・電源オンになっていることを確認してください。

* **ALSA / サウンドデバイスのエラー（例: 「Audio device busy」 または 「No such file or directory」）**

  * 他のプログラムでオーディオが使用されていないことを確認してください。
  * デバイスがビジー状態のままなら、Pi を再起動してください。
  * HDMI とヘッドフォンジャックの出力を切り替える場合は、Raspberry Pi OS のオーディオ設定で正しいデバイスを選択してください。

* **Python 実行時に「Permission denied」と表示される**

  * 環境によっては ``sudo`` が必要な場合があります:

    .. code-block:: bash

       sudo python3 test_tts_piper.py

TTS エンジンの比較
-------------------------

.. list-table:: 機能比較: Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - 項目
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - 実行環境
     - Raspberry Pi に標準搭載（オフライン）
     - Raspberry Pi に標準搭載（オフライン）
     - Raspberry Pi / PC（オフライン、モデルが必要）
     - クラウド（オンライン、APIキーが必要）
   * - 音声品質
     - ロボット的
     - Espeak より自然
     - 自然（ニューラルTTS）
     - 非常に自然 / 人間らしい
   * - コントロール
     - 速度、ピッチ、音量
     - 制御は限定的
     - 音声/モデルを選択可能
     - モデルと音声を選択可能
   * - 対応言語
     - 多言語（品質は言語により異なる）
     - 限定的な言語セット
     - 多数の音声/言語が利用可能
     - 英語が最も高品質（その他は提供状況による）
   * - レイテンシ / 速度
     - 非常に高速
     - 高速
     - Pi 4/5 上で “low” モデルを使えばリアルタイム
     - ネットワーク依存（通常は低遅延）
   * - セットアップ
     - 最小限
     - 最小限
     - ``.onnx`` と ``.onnx.json`` モデルをダウンロード
     - APIキー作成、クライアントインストール
   * - 最適な用途
     - 簡単なテスト、基本的なプロンプト
     - ちょっと良いオフライン音声
     - より高品質なローカルプロジェクト
     - 最高品質、豊富な音声オプション

