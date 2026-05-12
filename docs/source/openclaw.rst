
.. _pidog_skill:

.. start_using_pidog

21. OpenClawを使用したPiDogの制御
========================================

**OpenClawとは何ですか？**

これはChatGPTのアップグレード版と考えてください。従来のチャットボットは会話（テキスト生成）しかできませんが、OpenClawは行動を起こせます。自然言語の指示を理解し、コマンドの実行、ファイル管理、各種ツールの呼び出しなど、実際にコンピュータ上で操作を実行できます。

以下は素晴らしい応用事例です：

* **個人用万能アシスタント：** スケジュール管理、リマインダー設定、タスク追跡を任せられます。チャットアプリ（Telegram、WhatsAppなど）で指示するだけで、記憶して実行します。
* **自動化の「接着剤」：** 様々なサービスの結びつけ役として機能します。例えば、Webサイトの価格変更を監視させ、値下がりを検出したら自動的にn8n自動化ワークフローを起動して、メール通知を送信できます。
* **専用開発アシスタント：** サーバー管理、スクリプト実行、ログ確認などを手伝わせられます。「システム負荷を確認して」と言うだけで、サーバーにSSH接続してコマンドを実行し、結果を返してくれます。
* **ハードウェアの「遊び相手」：** これは非常に興味深い用途です。Raspberry Piに接続されたハードウェアをOpenClawに制御させられます。例えば、開発者はこれを使って機械アーム付きのロボット掃除機を制御したり、レーシングシミュレーターのデータを分析してLED画面に表示させたりしました。Raspberry Pi公式チームも、コードを一行も書かずに会話だけで結婚式用の自動写真ブースを構築しました！


.. important::

   Raspberry Pi Zero 2Wは512MBのRAMしかありませんが、OpenClawには最低1GBが必要です。そのため、適切に動作しません。Raspberry Pi 4/5以上をお勧めします。

OpenClawのクイックスタート
------------------------------

OpenClawの能力をできるだけ早く体験したい場合は、この方法を使用してください。自動的にインストールされ、対話型セットアップウィザードが起動します。

1.  Raspberry Piのターミナルを開き、次のコマンドを直接実行します。このコマンドは公式サイトからインストールスクリプトをダウンロードして実行します：

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash
   
    .. note:: 新バージョンは急速に更新されるため、インストール手順が若干異なる場合があっても正常です。

2.  スクリプトは自動的にOpenClawをダウンロードしてインストールします。

    .. image:: /img/openclaw/install_open_claw.png

3.  次に、OpenClawを信頼するかどうかを尋ねるセキュリティプロンプトが表示されます。安全で信頼できると確認できたら、矢印キーで「Yes」に移動し、Enterを押します。

    .. image:: /img/openclaw/security_open_claw.png

4.  Quick Startを選択し、Enterを押します。

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  使用するModelを選択し、Enterを押します。ここでは例としてOpenAIを使用します。

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  OpenAI API Keyを選択します。

    .. image:: /img/openclaw/api_key_open_claw.png

7.  APIキーを貼り付けます。

    .. image:: /img/openclaw/paste_api_key_open_claw.png

.. |link_openai_platform| raw:: html

    <a href="https://platform.openai.com/settings/organization/api-keys" target="_blank">OpenAI Platform</a>

8.  |link_openai_platform| にアクセスしてログインします。**API keys** ページで **Create new secret key** をクリックします。

    .. image:: /img/openclaw/llm_openai_create.png

9.  詳細情報（所有者、名前、プロジェクト、必要に応じて権限）を入力し、**Create secret key** をクリックします。

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. キーが作成されたら、すぐにコピーします。二度と表示されなくなります。紛失した場合は、新しいものを生成する必要があります。

    .. image:: /img/openclaw/llm_openai_copy.png

11. キーをOpenClawの設定に貼り付けます。

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. 使用するModelを選択します。この例では **Keep current** を使用します。

    .. image:: /img/openclaw/model_config_open_claw.png

13. 次はチャンネル選択です。チャンネルとは、OpenClawが対応する通信サービス（Telegram、WhatsApp、Discordなど）を指します。下矢印キーを使って「Skip for now」オプションを選択し、Enterを押します。

    .. image:: /img/openclaw/channel_open_claw.png

14. 次に、すぐにスキルを設定するかどうか尋ねられます。「Yes」を選択し、Enterを押します。

    .. image:: /img/openclaw/config_skill_open_claw.png

15. 必要なスキルをインストールします。次の例では、「Skip for now」オプションを選択し（スペースバーを押して選択）、Enterを押します。

    .. image:: /img/openclaw/install_skill_open_claw.png

16. 次はフックです。「command-logger」と「session-memory」をオンにします。

    .. image:: /img/openclaw/hooks2_open_claw.png

17. インストールが完了しました。「Hatch in TUI」を選択してEnterを押すと、OpenClawを起動できます。

   .. image:: /img/openclaw/hatch_open_claw.png

.. note:: 
   
   次のコマンドを入力してもOpenClawを起動できます：

    .. code-block:: bash

       openclaw tui

   TUIインターフェースを終了するには、ctrl+cを二度押します。

------------------------------------------------------------------------

OpenClawにPiDogを操作させる
----------------------------------------------

**PiDogスキルとは？**

PiDogスキルはOpenClawの拡張機能で、自然言語を通じてSunFounder PiDog V2ロボット犬を制御できるようにします。複雑なコマンドラインパラメータを覚える代わりに、「犬を座らせて」や「LEDライトを紫色にして」など、PiDogにしてほしいことをOpenClawに話すだけで、OpenClawが適切なコマンドを自動的に実行します。

PiDogスキルでできることの例：

* **基本動作：** PiDogを立たせる、座らせる、寝かせる、しっぽを振る、吠える、前進/後退する、左右に向きを変える
* **姿勢維持：** PiDogを特定の姿勢（立っているなど）に長時間保つ
* **LEDライト制御：** 呼吸、傾聴、ブーム、点灯などの効果で目の色を変える
* **色のカスタマイズ：** 赤、緑、青、黄、紫、ピンク、水色、白、橙、またはカスタムの16進数カラーコードから選択

----------------------------------------------------------------

前提条件
------------------------------

OpenClawでPiDogスキルを使用する前に、以下のものがあることを確認してください：

1.  **PiDog V2** が適切に組み立てられ、Raspberry Piに接続されていること
2.  **OpenClaw** がインストールされ、実行されていること
3.  以下のディレクトリがシステム上に存在すること：

   - ``~/pidog``
   - ``~/robot-hat``
   - ``~/vilib``

次のコマンドを実行してインストールを確認できます：

.. code-block:: bash

   python3 -c "import pidog"

このコマンドがエラーなく実行されれば、準備は完了です。

----------------------------------------------------------------

PiDogスキルのインストール
------------------------------

以下の手順に従って、OpenClaw用のPiDogスキルをインストールします：

1.  **スキルディレクトリを作成します** （まだ存在しない場合） ：

   .. code-block:: bash

      mkdir -p ~/.openclaw/workspace/skills/

2.  **PiDogスキルファイルを** OpenClawのスキルディレクトリにコピーします：

   .. code-block:: bash

      cp -r ~/pidog/pidog-control ~/.openclaw/workspace/skills/pidog-control/

   .. note:: ``~/pidog-skill`` は、PiDogスキルファイルが実際に配置されているパスに置き換えてください。

3.  **インストールを確認します**。スキルファイルを確認します：

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/pidog-control/scripts/

   出力に ``pidog_ctl.py`` と ``pidog_rgb_ctl.py`` が表示されるはずです。

----------------------------------------------------------------

PiDogスキルのテスト
------------------------------

OpenClawでスキルを使用する前に、端末から直接基本機能をテストすることをお勧めします。

**手順1：PiDogの状態を確認**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py status

**手順2：安全なテストを実行**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py safe-test

**手順3：基本動作をテスト**

PiDogを座らせる：

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action sit

PiDogを立たせ、姿勢を維持する：

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action stand --hold

PiDogに吠えさせる：

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action bark

**手順4：LEDライトをテスト**

紫色のブーム光効果をテスト：

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple

他の光効果をテスト：

.. code-block:: bash

   # 赤色の呼吸効果
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light breath --color red

   # 青色の傾聴効果
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light listen --color blue

   # ライトを消す
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light off

----------------------------------------------------------------

OpenClawでのPiDogスキルの使用
--------------------------------------

PiDogスキルがコマンドラインから動作することを確認したら、OpenClaw内で使用を開始できます。

1.  **OpenClaw TUIを起動します**：

   .. code-block:: bash

      openclaw tui

2.  **自然言語コマンドを送信して** PiDogを制御します。以下は例です：

   * 「犬を座らせて」
   * 「PiDogを立たせて、そのまま動かさないで」
   * 「犬のしっぽを振って」
   * 「犬に吠えさせて」
   * 「LEDライトをブーム効果で紫色にして」
   * 「目のライトを呼吸効果で赤色に設定して」
   * 「PiDogを前進させて」

3.  **OpenClawは自動的に** あなたの要求を適切なコマンドに変換し、PiDog上で実行します。

----------------------------------------------------------------

利用可能な動作とコマンド
------------------------------

以下はPiDogスキルで対応している動作の完全なリストです：

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 動作
     - 説明
   * - stand
     - PiDogを立たせる
   * - sit
     - PiDogを座らせる
   * - lie
     - PiDogを寝かせる
   * - wag-tail
     - PiDogのしっぽを振る
   * - bark
     - 吠え声を出す
   * - forward
     - 前進する
   * - backward
     - 後退する

**姿勢維持：**

任意の動作に ``--hold`` を追加すると、PiDogをその姿勢に保ちます。例：「stand --hold」

**光効果：**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 効果
     - 説明
   * - off
     - すべてのLEDライトを消す
   * - breath
     - 優しい呼吸・脈動効果
   * - listen
     - 反応する傾聴モード
   * - boom
     - 動的な破裂効果（最も目立ちます）
   * - solid
     - 一定の安定した光（より良い効果を得るにはブームを使用してください）

**対応している色：**

赤、緑、青、黄、紫、ピンク、水色、白、橙、または ``#FF5733`` のような16進数コード

----------------------------------------------------------------

トラブルシューティング
------------------------------

OpenClawの問題
^^^^^^^^^^^^^^^^^^^^^^^^

Q. インストール中に ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service`` というエラーが出ます。どうすればいいですか？

   今のところは無視しても構いませんが、次の手順で問題が発生する可能性があります。その時点でそれぞれを参照してください。

Q. ``openclaw tui`` を実行すると、``-bash: openclaw: command not found`` というエラーが出ます。どうすればいいですか？

   次のコマンドを実行してください：

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   これで ``openclaw tui`` でTUIインターフェースを起動できるようになります。

Q. ``openclaw tui`` で ``not connected to gateway — message not sent`` または ``gateway disconnected: closed`` というメッセージが表示されます。

   これはOpenClaw Gatewayサービスが起動していないためです。別の端末を開き、次のコマンドを実行してOpenClaw Gatewayを起動してください：

   .. code-block:: bash

      openclaw gateway

   その後 ``openclaw tui`` を再起動すると、直接使用できます。

Q. OpenClaw Gatewayサービスをバックグラウンドで実行/起動時に自動起動するように設定したいです。どうすればいいですか？

   通常、OpenClaw Gatewayサービスは起動時に自動的に開始されるはずです。もし開始されない場合は、次のコマンドで手動で開始できます。

   1. ``~/.config/systemd/user`` ディレクトリを作成します：

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user

   2. ``openclaw-gateway.service`` ファイルを作成します：

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF

   3. 次にsystemd設定を再読み込みします：

   .. code-block:: bash

      systemctl --user daemon-reload

   4. サービスを起動します：

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   この時点で ``openclaw tui`` を再起動すると、直接使用できます。

   5. 起動時に自動起動するように有効化します：

   .. code-block:: bash

      systemctl --user enable openclaw-gateway

Q. OpenClawがシステムを操作できません。どうすればいいですか？

   インストールしたばかりのOpenClawは、デフォルトではRaspberry Piシステムを操作する権限がない可能性があります。会話しかできません。権限を手動で設定する必要があります。

   1.  OpenClawの設定ファイルを開きます：

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  ``tools`` オプションを見つけ、``profile`` と ``exec`` を表示されているように変更します。

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3.  保存して終了します。

   4.  端末で次のコマンドを入力して、OpenClaw Gatewayを再起動します：

      .. code-block:: bash

         openclaw gateway restart

   これで、OpenClawは読み書き権限を持ち、Raspberry Piシステムを操作できるようになります。

PiDogの問題
^^^^^^^^^^^^^^^^^^^^^^^^

Q. PiDogがコマンドに応答しません。どうすればいいですか？

   まず、PiDogが適切に接続され、電源が入っていることを確認してください。次に基本コマンドをテストします：

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py status

   これが失敗する場合は、必要なディレクトリが存在するか確認してください：

      - ``~/pidog``
      - ``~/robot-hat``
      - ``~/vilib``

Q. ``import pidog`` のテストが失敗します。

   これはPiDog Pythonライブラリが適切にインストールされていないことを意味します。必要なライブラリをインストールするために、PiDog V2の公式インストールガイドを参照してください。

Q. LEDライトが期待通りに動作しません。

   点灯（ソリッド）がはっきり見えない場合は、代わりに ``boom`` 効果を使用してください。これが最も目立つ結果をもたらします：

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple

Q. OpenClawがPiDogスキルを認識しません。

   TUIで「私のスキルを同期してください」と話しかけてOpenClawにスキルの同期を促すか、OpenClaw Gatewayを再起動してください：

   .. code-block:: bash

      openclaw gateway restart

Q. 吠える動作の音が正しくありません。

   吠える動作はデフォルトで ``single_bark_1`` という音を使用します。これはPiDog V2の通常の動作です。