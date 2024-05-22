.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _remote_desktop:

Raspberry Piのリモートデスクトップアクセス
==================================================

コマンドラインアクセスよりもグラフィカルユーザーインターフェース（GUI）を好む方のために、Raspberry Piはリモートデスクトップ機能をサポートしています。このガイドでは、リモートアクセス用のVNC（Virtual Network Computing）の設定と使用方法を説明します。

この目的のために `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ の使用を推奨します。

**Raspberry PiでVNCサービスを有効にする**

VNCサービスはRaspberry Pi OSにプリインストールされていますが、デフォルトでは無効になっています。次の手順に従って有効にしてください：

#. Raspberry Piのターミナルで次のコマンドを入力します：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 下矢印キーを使用して **Interfacing Options** に移動し、 **Enter** キーを押します。

    .. image:: img/config_interface.png
        :align: center

#. オプションから **VNC** を選択します。

    .. image:: img/vnc.png
        :align: center

#. 矢印キーを使用して **<Yes>** -> **<OK>** -> **<Finish>** を選択し、VNCサービスの有効化を完了します。

    .. image:: img/vnc_yes.png
        :align: center

**VNC Viewerを使用してログインする**

#. 個人用コンピューターに `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ をダウンロードしてインストールします。

#. インストール後、VNC Viewerを起動します。Raspberry Piのホスト名またはIPアドレスを入力し、Enterキーを押します。

    .. image:: img/vnc_viewer1.png
        :align: center

#. プロンプトが表示されたら、Raspberry Piのユーザー名とパスワードを入力し、 **OK** をクリックします。

    .. image:: img/vnc_viewer2.png
        :align: center

#. これで、Raspberry Piのデスクトップインターフェースにアクセスできます。

    .. image:: img/bullseye_desktop.png
        :align: center
