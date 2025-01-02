AIとのインタラクション：GPT-4Oの活用
=====================================================

過去のプロジェクトではプログラミングを使ってPidogに特定のタスクを行わせましたが、それが少々単調に感じられることもありました。このプロジェクトでは、ダイナミックなエンゲージメントに向けてのスリリングな飛躍を紹介します。機械の犬を出し抜こうとするのは注意が必要です—今ではこれまで以上に多くのことを理解できるように装備されています！

このイニシアチブでは、必要な仮想環境の設定、重要なライブラリのインストール、APIキーとアシスタントIDの設定など、GPT-4Oをシステムに統合するために必要な技術的ステップすべてを詳しく述べます。

.. note::

   このプロジェクトでは |link_openai_platform| の使用が必要で、OpenAIへの支払いが必要です。さらに、OpenAI APIはChatGPTとは別に課金され、専用の価格設定がhttps://openai.com/api/pricing/で確認できます。

   そのため、このプロジェクトを続けるか、OpenAI APIに資金を供給したかどうかを決定する必要があります。

マイクを使って直接通信するか、コマンドウィンドウに入力することを好むかにかかわらず、GPT-4Oによって駆動されるPidogの反応にはきっと驚かされるでしょう！

このプロジェクトに飛び込んで、Pidogとの新しいレベルのインタラクションを解き放ちましょう！

.. raw:: html

   <video controls style = "max-width:90%">
     <source src="_static/video/chatgpt4o.mp4" type="video/mp4">
     お使いのブラウザはビデオタグをサポートしていません。
   </video>

1. 必要なパッケージと依存関係のインストール
--------------------------------------------------------------

.. note::

   まず、PiCar-X用の必要なモジュールをインストールする必要があります。詳細については、:ref:`install_all_modules` を参照してください。
   

このセクションでは、仮想環境を作成してアクティブにし、必要なパッケージと依存関係をインストールします。これにより、インストールしたパッケージがシステムの他の部分と干渉しないようにし、プロジェクトの依存関係の分離を維持し、他のプロジェクトやシステムパッケージとの衝突を防ぎます。

#. ``python -m venv`` コマンドを使用して ``my_venv`` という名前の仮想環境を作成します。システムレベルのパッケージを含めます。 ``--system-site-packages`` オプションを使用すると、仮想環境はシステム全体にインストールされているパッケージにアクセスできるようになります。これは、システムレベルのライブラリが必要な場合に便利です。

   .. code-block:: shell

      python -m venv --system-site-packages my_venv

#. ``my_venv`` ディレクトリに移動し、 ``source bin/activate`` コマンドを使用して仮想環境をアクティブにします。コマンドプロンプトが変更されて、仮想環境がアクティブであることを示します。

   .. code-block:: shell

      cd my_venv
      source bin/activate

#. その後、アクティブ化された仮想環境内で必要なPythonパッケージをインストールします。これらのパッケージは仮想環境に隔離され、他のシステムパッケージに影響を与えません。

   .. code-block:: shell

      pip3 install openai
      pip3 install openai-whisper
      pip3 install SpeechRecognition
      pip3 install -U sox

#. 最後に、管理者権限を要するシステムレベルの依存関係をインストールするために ``apt`` コマンドを使用します。

   .. code-block:: shell

      sudo apt install python3-pyaudio
      sudo apt install sox

2. APIキーとアシスタントIDの取得
-----------------------------------------

**APIキーの取得**

#. |link_openai_platform| にアクセスし、右上の角にある **新しいシークレットキーを作成** ボタンをクリックします。

   .. image:: img/apt_create_api_key.png
      :width: 700
      :align: center

#. 必要に応じてオーナー、名前、プロジェクト、および権限を選択し、次に **シークレットキーを作成** をクリックします。

   .. image:: img/apt_create_api_key2.png
      :width: 700
      :align: center

#. 生成されたら、このシークレットキーを安全でアクセス可能な場所に保存します。セキュリティ上の理由から、OpenAIアカウントを通じて再びこのシークレットキーを表示することはできません。このシークレットキーを失った場合は、新しいものを生成する必要があります。

   .. image:: img/apt_create_api_key_copy.png
      :width: 700
      :align: center

**アシスタントIDの取得**

#. 次に、 **アシスタント** をクリックし、 **作成** をクリックして、 **ダッシュボード** ページにいることを確認します。

   .. image:: img/apt_create_assistant.png
      :width: 700
      :align: center

#. ここにカーソルを移動して **アシスタントID** をコピーし、テキストボックスまたは他の場所に貼り付けます。これがこのアシスタントの一意の識別子です。

   .. image:: img/apt_create_assistant_id.png
      :width: 700
      :align: center

#. ランダムに名前を設定し、次に **指示** ボックスに次の内容をコピーして、あなたのアシスタントを説明します。

   .. image:: img/apt_create_assistant_instructions.png
      :width: 700
      :align: center

   .. code-block::

      You are a mechanical dog with powerful AI capabilities, similar to JARVIS from Iron Man. Your name is Pidog. You can have conversations with people and perform actions based on the context of the conversation.

      ## actions you can do:
      ["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag_tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

      ## Response Format:
      {"actions": ["wag_tail"], "answer": "Hello, I am Pidog."}

      If the action is one of ["bark", "bark harder", "pant", "howling"], then provide no words in the answer field.

      ## Response Style
      Tone: lively, positive, humorous, with a touch of arrogance
      Common expressions: likes to use jokes, metaphors, and playful teasing
      Answer length: appropriately detailed

      ## Other
      a. Understand and go along with jokes.
      b. For math problems, answer directly with the final.
      c. Sometimes you will report on your system and sensor status.
      d. You know you're a machine.

#. Pidogにはカメラモジュールが装備されており、例示コードを使用して、見ているものの画像をキャプチャしてGPTにアップロードすることができます。そのため、画像解析機能を持つGPT-4Oの選択を推奨します。もちろん、gpt-3.5-turboや他のモデルを選ぶことも可能です。

   .. image:: img/apt_create_assistant_model.png
      :width: 700
      :align: center

#. 今すぐ **Playground** をクリックして、アカウントが正常に機能しているか確認してください。

   .. image:: img/apt_playground.png

#. メッセージやアップロードした画像が正常に送信され、返信があれば、アカウントが使用限度に達していないことを意味します。

   .. image:: img/apt_playground_40.png
      :width: 700
      :align: center

#. 情報を入力した後にエラーメッセージが表示された場合、使用限度に達している可能性があります。使用状況ダッシュボードまたは課金設定を確認してください。

   .. image:: img/apt_playground_40mini_3.5.png
      :width: 700
      :align: center

3. APIキーとアシスタントIDの入力
--------------------------------------------------

#. ``keys.py`` ファイルを開くためのコマンドを使用します。

   .. code-block:: shell

      nano ~/pidog/gpt_examples/keys.py

#. コピーしたAPIキーとアシスタントIDを入力します。

   .. code-block:: shell

      OPENAI_API_KEY = "sk-proj-vEBo7Ahxxxx-xxxxx-xxxx"
      OPENAI_ASSISTANT_ID = "asst_ulxxxxxxxxx"

#. ``Ctrl + X``、 ``Y`` 、そして ``Enter`` を押してファイルを保存して終了します。

4. 実行例
----------------------------------
テキスト通信
^^^^^^^^^^^^^^^^^^^
Pidogにマイクがない場合、以下のコマンドを実行してキーボード入力を使用し、テキストでの対話が可能です。

#. 以下のコマンドをsudoを使用して実行します。Pidogのスピーカーはこれがなければ機能しません。このプロセスには時間がかかることがあります。

   .. code-block:: shell

      cd ~/pidog/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_dog.py --keyboard

#. コマンドが正常に実行されると、以下の出力が表示され、Pidogのすべてのコンポーネントが準備完了であることを示します。

   .. code-block:: shell

      vilib 0.3.8 launching ...
      picamera2 0.3.19
      config_file: /home/pi2/.config/pidog/pidog.conf
      robot_hat init ... done
      imu_sh3001 init ... done
      rgb_strip init ... done
      dual_touch init ... done
      sound_direction init ... done
      sound_effect init ... done
      ultrasonic init ... done

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      input:

#. また、ウェブブラウザでPidogのカメラフィードを見るためのリンクが提供されます: ``http://rpi_ip:9000/mjpg`` 。

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. これで、ターミナルウィンドウにコマンドを入力し、Enterキーを押して送信することができます。Pidogの反応には驚かされるかもしれません。

   .. note::
      
      Pidogは入力を受け取り、GPTに処理を依頼し、応答を受け取り、それを音声合成で再生するまでの全プロセスに時間がかかりますので、 Geduld ( patience ) ください。

   .. image:: img/apt_keyboard_input.png
      :width: 700
      :align: center

#. GPT-4Oモデルを使用している場合は、Pidogが見たものに基づいて質問することもできます。

音声通信
^^^^^^^^^^^^^^^^^

Pidogにマイクが装備されている場合、または |link_microphone| をクリックしてマイクを購入することができれば、音声コマンドを使用してPidogと対話することができます。

#. まず、Raspberry Piがマイクを検出しているかを確認してください。

   .. code-block:: shell

      arecord -l

   成功した場合、以下の情報が表示され、マイクが検出されたことが示されます。

   .. code-block:: 
      
      **** List of CAPTURE Hardware Devices ****
      card 3: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

#. 次に、以下のコマンドを実行し、Pidogに話しかけたり、音を出したりしてください。マイクが音を ``op.wav`` ファイルに記録します。「Ctrl + C」を押して録音を停止します。

   .. code-block:: shell

      rec op.wav

#. 最後に、以下のコマンドを使用して録音した音を再生し、マイクが正常に機能していることを確認します。

   .. code-block:: shell

      sudo play op.wav

#. 今、以下のコマンドをsudoを使用して実行してください。Pidogのスピーカーはこれがなければ機能しません。このプロセスには時間がかかります。

   .. code-block:: shell

      cd ~/pidog/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_dog.py

#. コマンドが成功裏に実行されると、以下の出力が表示され、Pidogのすべてのコンポーネントが準備完了であることが示されます。

   .. code-block:: shell
      
      vilib 0.3.8 launching ...
      picamera2 0.3.19
      config_file: /home/pi2/.config/pidog/pidog.conf
      robot_hat init ... done
      imu_sh3001 init ... done
      rgb_strip init ... done
      dual_touch init ... done
      sound_direction init ... done
      sound_effect init ... done
      ultrasonic init ... done

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      listening ...

#. また、ウェブブラウザでPidogのカメラフィードを見るためのリンクが提供されます: ``http://rpi_ip:9000/mjpg`` 。

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. これで、Pidogに話しかけることができ、その反応には驚かされるかもしれません。

   .. note::
      
      Pidogはあなたの入力を受け取り、テキストに変換し、GPTに処理を依頼し、応答を受け取り、そして音声合成を通じて再生します。この全プロセスには時間がかかるので、 Geduld ( patience ) ください。

   .. image:: img/apt_speech_input.png
      :width: 700
      :align: center

#. GPT-4Oモデルを使用している場合、Pidogが見たものに基づいて質問することもできます。

.. raw:: html

   <video controls style = "max-width:90%">
     <source src="_static/video/chatgpt4o.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>

5. パラメータの変更 [オプション]
-------------------------------------------
``gpt_dog.py`` ファイル内で、以下の行を見つけてください。STT 言語、TTS 音量ゲイン、音声役割を設定するためにこれらのパラメータを変更できます。

* **STT（音声からテキストへの変換）** は、PiCar-Xのマイクが音声をキャプチャしてテキストに変換し、GPTに送信するプロセスを指します。この変換の精度と待機時間を向上させるために、言語を指定できます。
* **TTS（テキストから音声への変換）** は、GPTのテキスト応答を音声に変換し、PiCar-Xのスピーカーから再生するプロセスです。TTS出力の音量ゲインを調整し、音声役割を選択できます。

.. code-block:: python

   # openai assistant init
   # =================================================================
   openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'PiDog')
   # LANGUAGE = ['zh', 'en'] # STT 言語コードを設定します, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
   LANGUAGE = []
   VOLUME_DB = 3 # TTS 音量ゲインは、5dB未満が推奨されます
   # TTS 音声役割を選択、"alloy, echo, fable, onyx, nova, shimmer" から選べます
   # https://platform.openai.com/docs/guides/text-to-speech/supported-languages
   TTS_VOICE = 'nova'

* ``LANGUAGE`` 変数:

   * 音声からテキストへの変換（STT）の精度と応答時間を向上させます。
   * ``LANGUAGE = []`` はすべての言語に対応しますが、STTの精度が低下し、待機時間が増加する可能性があります。
   * |link_iso_language_code| の言語コードを使用して、特定の言語を設定することをお勧めします。

* ``VOLUME_DB`` 変数:

   * テキストから音声への変換（TTS）の出力音量を制御します。
   * 値を増やすと音量が上がりますが、音声の歪みを避けるために5dB以下にすることをお勧めします。

* ``TTS_VOICE`` 変数:

   * テキストから音声への変換（TTS）の音声役割を選択します。
   * 利用可能なオプション: ``alloy, echo, fable, onyx, nova, shimmer``。
   * |link_voice_options| からさまざまな声を試して、目的のトーンや対象に合ったものを見つけることができます。現在、利用可能な声は英語用に最適化されています。
