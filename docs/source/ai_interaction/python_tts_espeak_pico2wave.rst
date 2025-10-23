.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

14. Espeak と Pico2Wave を使った TTS
=================================================

このレッスンでは、Raspberry Pi に組み込まれている 2 つのテキスト読み上げ（TTS）エンジン  
**Espeak** と **Pico2Wave** を使って、Pidog にしゃべらせてみます。

これら 2 つのエンジンはどちらもシンプルでオフラインで動作しますが、音声の特徴は異なります：

* **Espeak**：非常に軽量で高速。音はロボットっぽいですが、速度・ピッチ・音量などを調整可能。  
* **Pico2Wave**：Espeak よりも自然な音声を生成。ただし設定項目は少なめ。

**音質** と **機能** の違いを実際に聞いて体験してみましょう。

----

始める前に
----------------

以下を完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、 ``vilib``、 ``pidog`` モジュールをインストールし、スクリプト ``i2samp.sh`` を実行します。

Espeak のテスト
--------------------

Espeak は Raspberry Pi OS に標準で含まれる軽量な TTS エンジンです。  
声はロボットっぽいものの、音量・ピッチ・速度などを柔軟に調整できます。

**手順**：

* 新しいファイルを作成します：

  .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_espeak.py

* 以下のコードをコピー＆貼り付けし、 ``Ctrl+X`` → ``Y`` → ``Enter`` で保存します。

  .. code-block:: python

      from pidog.tts import Espeak

      tts = Espeak()

      # オプションで音声調整
      # tts.set_amp(100)   # 0 ～ 200
      # tts.set_speed(150) # 80 ～ 260
      # tts.set_gap(5)     # 0 ～ 200
      # tts.set_pitch(50)  # 0 ～ 99

      # 確認のための簡単な読み上げ
      tts.say("Hello! I'm Espeak TTS.")

* 以下のコマンドで実行します：

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* Pidog が “Hello! I'm Espeak TTS.” と話すのが聞こえるはずです。  
* コード内のコメントアウトを外すことで ``amp``、 ``speed``、 ``gap``、 ``pitch`` を調整し、音の違いを試せます。

----

Pico2Wave のテスト
---------------------

Pico2Wave は Espeak よりも自然で人間らしい音声を生成します。  
使い方はシンプルですが、ピッチやスピードは変更できず、 **言語のみ** 変更可能です。

**手順**：

* 新しいファイルを作成します：

  .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_pico2wave.py

* 以下のコードをコピー＆貼り付けし、 ``Ctrl+X`` → ``Y`` → ``Enter`` で保存します。

  .. code-block:: python
  
      from pidog.tts import Pico2Wave
  
      tts = Pico2Wave()
  
      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
      # 確認のための簡単な読み上げ
      tts.say("Hello! I'm Pico2Wave TTS.")

* 以下のコマンドで実行します：

  .. code-block:: bash

    sudo python3 test_tts_pico2wave.py

* Pidog が “Hello! I'm Pico2Wave TTS.” と話すのが聞こえるはずです。  
* 言語を ``es-ES`` （スペイン語）などに切り替えて、声の違いを確認してみましょう。

----

トラブルシューティング
---------------------------

* **Espeak や Pico2Wave を実行しても音が出ない**

  * スピーカー／ヘッドホンの接続と、音量がミュートになっていないかを確認します。  
  * 端末で簡単なテストを実行します：

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  それでも聞こえない場合、問題は Python コードではなく **音声出力** 側にあります。

* **Espeak の声が速すぎる／ロボットっぽい**

  * コード内のパラメータを調整してみてください：

    .. code-block:: python

       tts.set_speed(120)   # ゆっくりにする
       tts.set_pitch(60)    # ピッチを調整

* **コード実行時に Permission denied が出る**

  * ``sudo`` を付けて実行してみてください：

    .. code-block:: bash

       sudo python3 test_tts_espeak.py


比較：Espeak と Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - 機能
     - Espeak
     - Pico2Wave
   * - 音質
     - ロボット的・合成的
     - より自然で人間らしい
   * - 対応言語
     - 既定は英語
     - 少なめだが主要言語をカバー
   * - 調整可能項目
     - あり（速度・ピッチ など）
     - なし（言語のみ）
   * - パフォーマンス
     - 非常に高速・軽量
     - やや遅く・やや重い


