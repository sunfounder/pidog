12. アプリでPiDogを操作する
=============================

この例では、SunFounder Controller APPを使ってPiDogを操作します。

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/app_control.mp4" type="video/mp4">
      お使いのブラウザはビデオタグをサポートしていません。
   </video>

まずは携帯電話/タブレットにAPPをダウンロードし、PiDogが発信するホットスポットに接続し、SunFounder Controllerで独自のリモコンを作成してPiDogを操作します。

アプリでPiDogを操作する
----------------------------

#. **APP Store(iOS)** または **Google Play(Android)** から `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ をインストールします。

#. ``sunfounder-controller`` モジュールをインストールします。

    最初に ``robot-hat`` 、 ``vilib`` 、 ``picar-x`` モジュールをインストールする必要があります。詳細は :ref:`install_all_modules` を参照してください。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. コードを実行します。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 12_app_control.py

    コードを実行すると、以下のプロンプトが表示され、PiDogがネットワーク通信を正常に開始したことがわかります。

    .. code-block:: 

        Running on: http://192.168.18.138:9000/mjpg

        * Serving Flask app "vilib.vilib" (lazy loading)
        * Environment: development
        * Debug mode: off
        * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)       

#. ``PiDog`` と ``Sunfounder Controller`` を接続します。

    * タブレット/携帯電話をPiDogがあるWLANに接続します。

    * ``Sunfounder Controller`` アプリを開き、+アイコンをクリックしてコントローラーを追加します。

        .. image:: img/app1.png
      

    * 一部の製品にはプリセットコントローラーが用意されており、ここでは **PiDog** を選択します。名前を入力するか、そのまま **確認** をタップします。

        .. image:: img/app_preset.jpg


    * 中に入ると、アプリが自動的に **Mydog** を検索します。しばらくすると、「接続成功」というプロンプトが表示されます。

        .. image:: img/app_auto_connect.jpg

    .. note::

        * 手動で |app_connect| ボタンをクリックすることもできます。数秒待ってから、MyDog(IP)が表示されたらクリックして接続します。

            .. image:: img/sc_mydog.jpg

#. コントローラーを実行します。

    * 「接続成功」というプロンプトが表示されたら、右上隅の▶ボタンをタップします。

    * カメラが撮影した画像がアプリに表示され、これらのウィジェットでPiDogを操作できます。

        .. image:: img/sc_run.jpg
    

ウィジェットの機能は以下の通りです。

* **A**: 超音波モジュールの読み取り、つまり障害物の距離を検出します。
* **C**: 顔検出のオン/オフを切り替えます。
* **D**: PiDogの頭の傾き角度を制御します（頭を傾ける）。
* **E**: 座る。
* **F**: 立つ。
* **G**: 横になる。
* **I**: PiDogの頭を撫でる。
* **N**: 吠える。
* **O**: 尻尾を振る。
* **P**: ハアハアする。
* **K**: PiDogの動きを制御します（前進、後退、左右）。
* **Q**: PiDogの頭の向きを制御します。
* **J**: 音声制御モードに切り替えます。次の音声コマンドに対応しています：

    * ``forward``
    * ``backward``
    * ``turn left``
    * ``turn right``
    * ``trot``
    * ``stop``
    * ``lie down`` 
    * ``stand up``
    * ``sit``
    * ``bark``
    * ``bark harder``
    * ``pant``
    * ``wag tail``
    * ``shake head``
    * ``stretch``
    * ``doze off``
    * ``push-up``
    * ``howling``
    * ``twist body``
    * ``scratch``
    * ``handshake``
    * ``high five``

起動時に自動起動
-----------------
アプリでPiDogを制御する際に、まずRaspberry Piにログインして ``12_app_control.py`` を実行してからアプリで接続するのは面倒です。

より簡潔な方法があります。PiDogが電源を入れるたびに ``12_app_control.py`` を自動的に実行するように設定できます。これにより、アプリを使ってPiDogに直接接続し、ロボット犬を簡単に制御できます。

どのように設定するか？

#. 以下のコマンドを実行して、 ``pidog_app`` アプリケーションをインストールおよび設定し、PiDogのWiFiを設定します。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/bin
        sudo bash pidog_app_install.sh

#. 最後に「y」と入力してPiDogを再起動します。

    .. image:: img/auto_start.png

#. それ以降は、PiDogを電源オンにしてアプリで直接操作できます。

.. warning::

    他のスクリプトを実行したい場合は、まず ``pidog_app disable`` を実行して自動起動機能をオフにしてください。


アプリプログラムの設定
-----------------------------

以下のコマンドを入力して、アプリモードの設定を変更できます。

.. code-block::

    pidog_app <OPTION> [input]

**OPTION**
    * ``-h`` ``help``: ヘルプ、このメッセージを表示
    * ``start`` ``restart``: ``pidog_app`` サービスを再起動
    * ``stop``: ``pidog_app`` サービスを停止
    * ``disable``: 起動時に自動起動する ``app_controller`` プログラムを無効にする
    * ``enable``: 起動時に自動起動する ``app_controller`` プログラムを有効にする
    * ``close_ap``: ホットスポットを閉じる、起動時に自動起動するホットスポットを無効にし、STAモードに切り替える
    * ``open_ap``: ホットスポットを開く、起動時に自動起動するホットスポットを有効にする
    * ``ssid``: ホットスポットのSSID（ネットワーク名）を設定
    * ``psk``: ホットスポットのパスワードを設定
    * ``country``: ホットスポットの国コードを設定
