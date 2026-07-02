.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32に関する情報を、他の愛好者と一緒に深掘りしていきましょう。

    **なぜ参加するべきか？**

    - **専門的なサポート**：購入後の問題や技術的な課題を、コミュニティやチームのサポートで解決しましょう。
    - **学びと共有**：ヒントやチュートリアルを交換して、スキルを向上させましょう。
    - **限定プレビュー**：新製品の発表前にアクセスし、先取り情報を得ることができます。
    - **特別割引**：最新製品に対する限定割引を楽しみましょう。
    - **季節ごとのキャンペーンとプレゼント企画**：プレゼント企画やホリデーキャンペーンに参加しましょう。

    👉 私たちと一緒に探索し、創造を始めませんか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

FAQ
==========

Q1: PiDog にはどのバージョンがありますか？
------------------------------------------------------

PiDog には **V1** バージョンと **V2** バージョンがあります：

* **V1 バージョン**：Raspberry Pi 3B+/4B/Zero 2W に対応。Raspberry Pi 5 には **非対応**。
* **V2 バージョン**：Raspberry Pi 3/4/5 および Zero 2W に対応。Robot HAT とサーボドライバー回路が改良され、Pi 5 への電力供給も強化されています。
* **電源供給**：V2 は消費電力の大きいアプリケーション向けに電源管理が強化されています。

Q2: 必要なモジュールはどのようにインストールしますか？
---------------------------------------------------------------

.. code-block:: bash

    # Robot HAT
    git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
    cd robot-hat && sudo python3 install.py

    # Vilib
    git clone https://github.com/sunfounder/vilib.git
    cd vilib && sudo python3 install.py

    # PiDog
    git clone https://github.com/sunfounder/pidog.git --depth 1
    cd pidog && sudo pip3 install . --break

音声が出ない場合は以下を実行してください：

.. code-block:: bash

    # I2S オーディオ
    cd ~/robot-hat
    sudo bash i2samp.sh

必要に応じて複数回実行します。

----

Q3: Why do I get a "piper-tts" error during installation?
----------------------------------------------------------

.. important::

   If you see this error during ``pip3 install``:

   .. code-block:: text

       ERROR: Could not find a version that satisfies the requirement piper-tts==1.3.0
       ERROR: No matching distribution found for piper-tts==1.3.0

   It means you are using a **32-bit** Raspberry Pi OS. The ``piper-tts`` package only provides pre-built wheels for **64-bit** systems. Reinstall the OS using the **64-bit** version of Raspberry Pi OS and the installation will succeed.

----

Q4: 最初のデモはどのように実行しますか？
------------------------------------------------

.. code-block:: bash

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

PiDog が起動し、座ってしっぽを振ります。

----

Q5: どのような組み込みアクションやサウンドがありますか？
------------------------------------------------------------------

* アクション： ``stand``、 ``sit``、 ``wag_tail``、 ``trot`` など
* サウンド： ``bark``、 ``howling``、 ``pant`` など

実行コマンド：

.. code-block:: bash

    sudo python3 2_function_demonstration.py

数字を入力してアクションをトリガーします。

----

Q6: PiDog はセンサーをどのように使いますか？
-------------------------------------------------

* **超音波センサー**：障害物回避と巡回
* **タッチセンサー**：前側のタッチ＝警戒、後ろのタッチ＝喜び
* **音源方向**：音の方向に反応します

----

Q7: PiDog はどのような AI 機能をサポートしていますか？
------------------------------------------------------

PiDog は **TTS**、**STT**、および **LLM** と統合されています：

* **TTS**：Espeak、Pico2Wave、Piper、OpenAI
* **STT**：Vosk（オフライン）
* **LLM**：Ollama（ローカル）、OpenAI（オンライン）

----

Q8: サーボのキャリブレーションは必要ですか？
---------------------------------------------

はい。**V1 バージョンと V2 バージョンの両方でキャリブレーションが必要** です。これにより安定した動作を実現し、破損を防ぎます。

**V2 バージョン**

The Robot HAT on the V2 version has a **zeroing button**. Press it to automatically set all servos to 0° — no script needed.

If your PiDog V2's legs are in the wrong position after assembly (for example, servos appear at strange angles or the robot cannot stand properly), you can use the zero button to fix this:

#. Power on the PiDog.
#. Press the **zero button** on the Robot HAT — all servos will forcibly return to 0°.
#. Reassemble the legs in the correct orientation following the assembly instructions.

For a step-by-step demonstration, watch the video below:

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zmN_mGxTKuU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**V1 バージョン**

The V1 version uses a script to zero the servos. Run the following command — it will set all servos to 0°:

.. code-block:: bash

   cd ~/pidog/examples
   sudo python3 servo_zeroing.py

This should be done **before installation** to ensure each servo starts from the correct zero position. If your PiDog V1's legs are in the wrong position after assembly, re-run this script to reset all servos to 0°, then reassemble the legs correctly.


----

Q9: なぜ PiDog の歩行が不安定なのですか？
-----------------------------------------------

* すべてのサーボが 0° の状態で取り付けられていることを確認してください。
* サーボ角度がキャリブレーション定規（60°／90°）と一致しているか確認してください。
* バッテリーが十分に充電されていることを確認してください。
* サーボのネジをしっかりと締めてください。

----

Q10: Servo zeroing works, but calibration example doesn't move any servo?
--------------------------------------------------------------------------

If pressing the zeroing button moves all servos to 0° normally, but the calibration script cannot control any servo, the problem is likely a hardware connection issue between the Raspberry Pi and the Robot HAT.

.. note::

   The zeroing button is only available on **PiDog V2** (which uses Robot HAT V5). PiDog V1 does not have this feature and must use the ``servo_zeroing.py`` script instead.

**Why this happens**

* Servo zeroing is handled **directly by the Robot HAT** — it works independently without the Raspberry Pi.
* Running calibration or any servo control from code requires the Raspberry Pi to communicate with the Robot HAT through the **GPIO header pins**.

**How to diagnose**

This is often caused by poor soldering on either side of the GPIO connection:

* The **Raspberry Pi's 40-pin GPIO header** (especially on Zero 2W, where the header must be soldered on by the user).
* The **Robot HAT's female header pins**.

Take clear, well-lit photos of both sets of pins and send them to SunFounder support at service@sunfounder.com. The team will help identify whether resoldering is needed.

----

Q11: カメラが動作しないのはなぜですか？
--------------------------------------

* カメラケーブルが **CSI インターフェースにしっかりと差し込まれ**、黒いロックタブが固定されていることを確認してください。
* カメラの抜き差しは、Raspberry Pi の電源を **オフにしてから** 行ってください（破損防止）。
* ``libcamera-hello`` または ``raspistill`` を使用してカメラが画像を出力するかテストしてください。
* ケーブルが緩んでいたり正しく接続されていない場合は、再度差し込み直してください。

----

Q12: スピーカーが動作しないのはなぜですか？
-----------------------------------------------------

* Robot HATのスピーカーが有効化されていることを確認してください。まだPiDogのサンプルコードを実行していない場合は、先に有効化してください：

  .. code-block:: bash

     robot_hat enable_speaker

  これは起動ごとに1回だけ実行すれば十分です。PiDogのサンプルコード（``Pidog()`` を初期化するもの）を実行すると、自動的に有効化されます。

* 音量がミュートされていないか、I2S オーディオドライバがインストールされているか確認してください。
* 音が出ない場合は、以下のコマンドで I2S を再設定します：

.. code-block:: bash

    cd ~/robot-hat
    sudo bash i2samp.sh

* スクリプト実行後、Raspberry Pi を再起動してください。

----

Q13: マイクが動作しないのはなぜですか？
--------------------------------------------------

* 以下のコマンドでシステムがマイクを認識しているか確認します：

.. code-block:: bash

    arecord -l

* 以下で録音テストを行います：

.. code-block:: bash

    arecord -D plughw:1,0 -f cd test.wav

* 音声が録音されない場合は、正しい入力デバイスが選択されているか確認し、 ``alsamixer`` で入力音量を調整してください。
* 他のプロセスがオーディオ入力デバイスを使用していないか確認してください。

----

Q14: 音源方向センサーが動作しないのはなぜですか？
-------------------------------------------------------

* 音源方向センサーが正しい SPI インターフェースに接続されていることを確認してください。
* すべてのケーブルがしっかりと接続され、逆向きになっていないか確認してください。
* 電源供給が安定していること、センサーが遮られていないことを確認してください。
* デバイスを再起動し、センサーのサンプルスクリプトを再実行してください。

----

Q15: タッチセンサーが反応しないのはなぜですか？
----------------------------------------------------------

* タッチセンサーのケーブルがしっかりと接続されていることを確認してください。
* **LOW 信号** はセンサーが触られている状態を意味します。
* ``gpio readall`` または Python コードで GPIO ピンの信号をテストしてください。
* 配線と接続方向を再確認してください。

----

Q16: Why is the ultrasonic sensor not working?
-----------------------------------------------

#. Run the ultrasonic test to check the reading:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 ultrasonic_test.py

   If the reading shows **-1**, the sensor is not functioning correctly.

#. Verify the wiring:

   * **White wire** → GPIO **17**
   * **Yellow wire** → GPIO **4**

#. If the wiring is correct and the reading is still -1, contact SunFounder support at service@sunfounder.com for further assistance.

----

Q17: LED ボードが点灯しない、または点滅が不正なのはなぜですか？
---------------------------------------------------------------------

* LED ボードが **3.3V** で給電され、I2C ポートに接続されていることを確認してください。
* Raspberry Pi で **I2C が有効** になっていることを確認してください。
* 次のコマンドでボードが認識されているか確認します：

.. code-block:: bash

    i2cdetect -y 1

* デバイスが表示されない場合は、配線を再確認し、Pi を再起動してください。

----

Q18: Why are the 6-DOF IMU and 11-channel RGB board not working?
-----------------------------------------------------------------

If both the 6-DOF IMU and the 11-channel RGB LED board are not responding, the issue is likely with the shared I2C connection:

#. First, check whether the devices are detected on the I2C bus:

   .. code-block:: bash

       sudo i2cdetect -y 1

   The expected addresses are:

   * **0x36** — 6-DOF IMU
   * **0x74** — 11-channel RGB LED board

   If one or both addresses are missing, the corresponding device is not properly connected.

#. Try connecting the 6-DOF IMU to a different port and test again.
#. Connect the 6-DOF IMU directly to the Robot HAT's I2C port, then run the test:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 imu_test.py

#. If the IMU works when connected directly, the problem is with the 11-channel RGB board's pass-through port.
#. To confirm, connect the 11-channel RGB board directly to the I2C port and test:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 rgb_strip_test.py

----

Q19: PiDog はどのように電源を供給しますか？
-----------------------------------------------------

* 5V 3A の Type-C 電源アダプタを使用します。
* 赤いランプ＝充電中、消灯＝充電完了です。
* 充電しながら動作させることができます。
* インジケータが点灯しない場合は、まず充電してください。

----
