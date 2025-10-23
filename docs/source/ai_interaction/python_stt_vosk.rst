.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

16. Vosk を使った STT（オフライン）
==============================================

Vosk は、軽量な音声認識（STT）エンジンで、多くの言語をサポートし、Raspberry Pi 上で完全に **オフライン** で動作します。  
最初に一度だけ言語モデルをダウンロードすれば、その後はネット接続なしで利用可能です。

このレッスンでは以下を行います：

* Raspberry Pi 上のマイクの動作確認  
* 選択した言語モデルで Vosk をインストール＆テスト

----

始める前に
----------------

以下を完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、 ``vilib``、 ``pidog`` モジュールをインストールし、スクリプト ``i2samp.sh`` を実行します。

1. マイクの確認
--------------------------

音声認識を使う前に、USB マイクが正しく動作しているか確認します。

#. 使用可能な録音デバイスを一覧表示：

   .. code-block:: bash

      arecord -l

   ``card 1: ... device 0`` のような行を探します。

#. 短い音声を録音（ ``1,0`` は取得したカード番号とデバイス番号に置き換え）：

   .. code-block:: bash

      arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

   例：デバイスが ``card 2, device 0`` の場合：

   .. code-block:: bash

      arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

#. 再生して録音を確認：

   .. code-block:: bash

      aplay test.wav

#. マイクの音量調整：

   .. code-block:: bash

      alsamixer

   * **F6** を押して USB マイクを選択  
   * **Mic** または **Capture** チャンネルを探す  
   * ミュート状態でないことを確認（ **[MM]** はミュート、 ``M`` キーで解除 → **[OO]** にする）  
   * ↑ / ↓ で録音音量を調整

----

.. _test_vosk:

2. Vosk のテスト
--------------------------

**手順**：

#. 新しいファイルを作成：

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_stt_vosk.py

#. 以下のコードをコピー＆貼り付けし、 ``Ctrl+X`` → ``Y`` → ``Enter`` で保存します。

   .. code-block:: python

      from pidog.stt import Vosk

      vosk = Vosk(language="en-us")

      print(vosk.available_languages)

      while True:
          print("Say something")
          result = vosk.listen(stream=False)
          print(result)

#. プログラムを実行：

   .. code-block:: bash

      sudo python3 test_stt_vosk.py

#. 初回実行時、新しい言語を使用する場合は Vosk が自動的に **言語モデルをダウンロード** します（デフォルトでは small バージョン）。  
   その後、対応言語の一覧が表示されます：

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

これが表示されれば：

* モデルファイル（ ``vosk-model-small-en-us-0.15``）がダウンロード完了  
* 対応言語の一覧が表示される  
* システムが音声認識を待機中 — マイクに話しかけると認識結果がターミナルに表示されます

**ヒント**：

* マイクは 15〜30 cm 程度離すと良いです。  
* 使用する言語と発音に合ったモデルを選びましょう。

**ストリーミングモード（オプション）**

音声を話しながらリアルタイムで部分的な認識結果を確認することも可能です：

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

トラブルシューティング
----------------------------------

* **`arecord` 実行時に「No such file or directory」と表示される**

  カード／デバイス番号が間違っている可能性があります。  
  以下を実行し：

  .. code-block:: bash

     arecord -l

  USB マイクに対応する番号に ``1,0`` を置き換えてください。

* **録音ファイルに音が入っていない**

  ミキサーを開いてマイク音量を確認します：

  .. code-block:: bash

     alsamixer

  * **F6** を押して USB マイクを選択  
  * **Mic / Capture** がミュートではないことを確認（**[OO]** になっている必要があります。**[MM]** の場合は ``M`` で解除）  
  * ↑ で音量を上げます

* **Vosk が音声を認識しない**

  * 言語コードがモデルと一致しているか確認（例：英語は ``en-us``、中国語は ``zh-cn``）  
  * マイクとの距離を 15〜30cm に保ち、周囲の雑音を減らします  
  * はっきり、ゆっくりと話します

* **認識が遅い／反応が悪い**

  * デフォルトでは **small モデル** を自動ダウンロードします（高速ですが精度は低め）  
  * それでも遅い場合は、他のプログラムを終了して CPU を確保してください
