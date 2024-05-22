.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _install_all_modules:

5. すべてのモジュールをインストールする（重要）
================================================

#. システムを更新します。

    インターネットに接続していることを確認し、システムを更新してください：

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt update
        sudo apt upgrade

    .. note::

        LiteバージョンのOSをインストールする場合は、Python3関連のパッケージがインストールされている必要があります。

        .. raw:: html

            <run></run>

        .. code-block::
        
            sudo apt install git python3-pip python3-setuptools python3-smbus

#. ``robot-hat`` モジュールをインストールします。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
        cd robot-hat
        sudo python3 setup.py install

#. ``vilib`` モジュールをインストールします。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone -b picamera2 https://github.com/sunfounder/vilib.git
        cd vilib
        sudo python3 install.py

#. コードをダウンロードします。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone https://github.com/sunfounder/pidog.git

#. ``pidog`` モジュールをインストールします。

    .. raw:: html

        <run></run>

    .. code-block::

        cd pidog
        sudo python3 setup.py install

    このステップには少し時間がかかるので、気長にお待ちください。

#. スクリプト ``i2samp.sh`` を実行します。

    最後に、i2sアンプに必要なコンポーネントをインストールするためのスクリプト ``i2samp.sh`` を実行する必要があります。そうしないと、ロボットに音が出ません。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog
        sudo bash i2samp.sh
        
    .. image:: img/i2s.png

    ``y`` と入力し、 ``Enter`` を押してスクリプトの実行を続行します。

    .. image:: img/i2s2.png

    ``y`` と入力し、 ``Enter`` を押して ``/dev/zero`` をバックグラウンドで実行します。

    .. image:: img/i2s3.png

    ``y`` と入力し、 ``Enter`` を押してマシンを再起動します。

    .. note::
        再起動後に音が出ない場合は、 ``i2samp.sh`` スクリプトを複数回実行する必要があるかもしれません。
