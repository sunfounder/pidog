.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

2. OSのインストール
=======================

**必要なコンポーネント**

* Raspberry Pi 5B
* パーソナルコンピュータ
* マイクロSDカード 

**インストール手順**

#. `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_ のRaspberry Piソフトウェアダウンロードページを訪れてください。お使いのオペレーティングシステムに対応するImagerバージョンを選択します。ファイルをダウンロードして開き、インストールを開始します。

    .. image:: img/os_install_imager.png

#. インストール中に、オペレーティングシステムによってはセキュリティプロンプトが表示される場合があります。例えば、Windowsでは警告メッセージが表示されることがあります。その場合は、 **詳細情報** を選択してから **とにかく実行** を選択します。画面上の指示に従って、Raspberry Pi Imagerのインストールを完了します。

    .. image:: img/os_info.png

#. SDカードをコンピュータまたはラップトップのSDカードスロットに挿入します。

#. Raspberry Pi Imagerアプリケーションをクリックするか、ターミナルで ``rpi-imager`` と入力して起動します。

    .. image:: img/os_open_imager.png

#. **CHOOSE DEVICE** をクリックして、リストから特定のRaspberry Piモデルを選択します（注：Raspberry Pi 5は適用されません）。

    .. image:: img/os_choose_device.png

#. **CHOOSE OS** を選択し、 **Raspberry Pi OS (Legacy)** を選びます。

    .. warning::

        * スピーカーが動作しないため、 **Bookworm** バージョンはインストールしないでください。
        * **Debian Bullseye** バージョンの **Raspberry Pi OS (Legacy)** をインストールする必要があります。

            .. image:: img/os_choose_os.png

#. **Choose Storage** をクリックして、インストールに適したストレージデバイスを選択します。

    .. note::

        正しいストレージデバイスを選択してください。混乱を避けるために、複数のストレージデバイスが接続されている場合は、追加のデバイスを切断してください。

    .. image:: img/os_choose_sd.png

#. **NEXT** をクリックし、 **EDIT SETTINGS** をクリックしてOSの設定をカスタマイズします。Raspberry Pi用のモニターがある場合は、次のステップをスキップして「Yes」をクリックしてインストールを開始します。他の設定は後でモニター上で調整します。

    .. image:: img/os_enter_setting.png

#. Raspberry Piの **ホスト名** を定義します。

    .. note::

        ホスト名はRaspberry Piのネットワーク識別子です。 ``<hostname>.local`` または ``<hostname>.lan`` を使用してPiにアクセスできます。

    .. image:: img/os_set_hostname.png

#. Raspberry Piの管理者アカウント用に **ユーザー名** と **パスワード** を作成します。

    .. note::

        デフォルトパスワードがないため、独自のユーザー名とパスワードを設定することがRaspberry Piのセキュリティにとって重要です。

    .. image:: img/os_set_username.png

#. ワイヤレスLANを設定し、ネットワークの **SSID** と **パスワード** を入力します。

    .. note::

        ``Wireless LAN country`` を、お住まいの場所に対応する2文字の `ISO/IEC alpha2コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ に設定してください。

    .. image:: img/os_set_wifi.png

#. **SERVICES** をクリックし、安全なパスワードベースのリモートアクセスのために **SSH** を有効にします。設定を保存することを忘れないでください。

    .. image:: img/os_enable_ssh.png

#. **Yes** をクリックして選択した設定を確認します。

    .. image:: img/os_click_yes.png

#. SDカードに既存のデータがある場合は、データ損失を防ぐためにバックアップしてください。バックアップが不要な場合は、「Yes」をクリックして進行します。

    .. image:: img/os_continue.png

#. OSのインストールプロセスがSDカード上で開始されます。完了時に確認ダイアログが表示されます。

    .. image:: img/os_finish.png
        :align: center


#. Raspberry Pi OSがセットアップされたSDカードを、Raspberry Piの裏側にあるmicroSDカードスロットに挿入します。

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center
