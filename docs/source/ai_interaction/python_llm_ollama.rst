.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

17. Ollama でテキストトーク
================================

このレッスンでは、ローカルで大規模言語モデル（LLM）およびビジョンモデルを実行できるツール **Ollama** の使い方を学びます。  
Ollama のインストール、モデルのダウンロード、そして Pidog との接続方法を紹介します。

始める前に
----------------

以下を完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、 ``vilib``、 ``Pidog`` モジュールをインストールし、スクリプト ``i2samp.sh`` を実行します。

.. _download_ollama:

1. Ollama（LLM）のインストールとモデルのダウンロード
-------------------------------------------------------------

**Ollama** は以下のいずれかの場所にインストールできます：

* Raspberry Pi 上（ローカル実行）  
* 同じローカルネットワーク内の別のコンピュータ（Mac / Windows / Linux）

**推奨モデルとハードウェアの目安**

|link_ollama_hub| にある任意のモデルを選択できます。  
モデルには 3B、7B、13B、70B... などさまざまなサイズがあり、小さいモデルは動作が速く少ないメモリで済みますが、大きいモデルはより高品質な応答を提供する代わりに、強力なハードウェアが必要です。

以下の表を参考に、デバイスに合ったモデルサイズを選んでください。

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - モデルサイズ
     - 最低必要RAM
     - 推奨ハードウェア
   * - 約3Bパラメータ
     - 8GB（16GB推奨）
     - Raspberry Pi 5（16GB）または中程度のPC/Mac
   * - 約7Bパラメータ
     - 16GB以上
     - Pi 5（16GB、ギリギリ動作）または中程度のPC/Mac
   * - 約13Bパラメータ
     - 32GB以上
     - 高メモリ搭載のデスクトップPC/Mac
   * - 30B+ パラメータ
     - 64GB以上
     - ワークステーション / サーバー / GPU推奨
   * - 70B+ パラメータ
     - 128GB以上
     - 複数GPUを搭載したハイエンドサーバー

**Raspberry Pi へのインストール**

Raspberry Pi に Ollama を直接インストールして実行する場合：

* **64-bit Raspberry Pi OS** を使用してください  
* 強く推奨： **Raspberry Pi 5（16GB RAM）**

以下のコマンドを実行します：

.. code-block:: bash

   # Ollama のインストール
   curl -fsSL https://ollama.com/install.sh | sh

   # 軽量モデルをダウンロード（テストに最適）
   ollama pull llama3.2:3b

   # クイックテスト（「hi」と入力してEnter）
   ollama run llama3.2:3b

   # APIを提供（デフォルトポート 11434）
   # LANからアクセス可能にするには OLLAMA_HOST=0.0.0.0 を設定
   OLLAMA_HOST=0.0.0.0 ollama serve

**Mac / Windows / Linux（デスクトップアプリ）へのインストール**

1. |link_ollama| から Ollama をダウンロードしてインストールします。  

   .. image:: img/llm_ollama_download.png

2. Ollama アプリを開き、**Model Selector** に移動し、検索バーに ``llama3.2:3b`` と入力します（最初に使うのに適した軽量モデルです）。

   .. image:: img/llm_ollama_choose.png

3. ダウンロードが完了したら、チャットウィンドウに「Hi」と入力します。初回使用時、自動的にモデルのダウンロードが開始されます。

   .. image:: img/llm_olama_llama_download.png

4. **Settings** → **Expose Ollama to the network** を有効にします。  
   これにより Raspberry Pi から LAN 経由で接続できます。

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   以下のようなエラーが表示された場合：

   ``Error: model requires more system memory ...``

   モデルがマシンのメモリに対して大きすぎます。  
   **より小さいモデル** を使用するか、より高性能なPCに切り替えてください。

2. Ollama のテスト
-------------------------------

Ollama のインストールとモデルの準備が完了したら、最小限のチャットループで素早くテストできます。

**手順**

#. 新しいファイルを作成します：

   .. code-block:: bash

      cd ~/pidog/examples
      nano test_llm_ollama.py

#. 以下のコードを貼り付けて保存します（ ``Ctrl+X`` → ``Y`` → ``Enter``）：

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

#. プログラムを実行します：

   .. code-block:: bash

      python3 test_llm_ollama.py

#. これで、ターミナルから直接 Pidog とチャットできます。

   * |link_ollama_hub| にある **任意のモデル** を選択できますが、8〜16GB RAM しかない場合は、 ``moondream:1.8b`` や ``phi3:mini`` のような小さいモデルを推奨します。  
   * コード内で指定するモデル名は、Ollama ですでにダウンロード済みのモデルと一致している必要があります。  
   * ``exit`` または ``quit`` と入力するとプログラムを終了できます。  
   * 接続できない場合は、Ollama が実行されていること、そしてリモートホストを使用している場合は両方のデバイスが同じ LAN 上にあることを確認してください。

トラブルシューティング
--------------------------------

* **「model requires more system memory ...」のようなエラーが表示される。**

  * モデルがデバイスに対して大きすぎることを意味します。  
  * ``moondream:1.8b`` や ``granite3.2-vision:2b`` のような小さいモデルを使用してください。  
  * または、より多くの RAM を搭載したマシンに切り替え、Ollama をネットワークに公開します。

* **コードが Ollama に接続できない（connection refused）。**

  以下を確認してください：
  
  * Ollama が実行されていること（``ollama serve`` またはデスクトップアプリが開いていること）。  
  * リモートコンピュータを使用している場合、Ollama の設定で **Expose to network** が有効になっていること。  
  * コード内の ``ip="..."`` が正しい LAN IP と一致していることを再確認。  
  * 両方のデバイスが同じローカルネットワーク上にあることを確認。
