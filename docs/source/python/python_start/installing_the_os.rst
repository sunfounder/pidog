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
============================================================


**必要なコンポーネント**

* パーソナルコンピュータ
* Micro SDカードとリーダー

1. Raspberry Pi Imagerのインストール
-------------------------------------------

#. `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_ のRaspberry Piソフトウェアダウンロードページにアクセスします。お使いのオペレーティングシステムに対応するImagerのバージョンを選択します。ファイルをダウンロードして開き、インストールを開始します。

    .. image:: img/os_install_imager.png
        :align: center

#. インストール中にセキュリティプロンプトが表示される場合があります。例えば、Windowsでは警告メッセージが表示されることがあります。その場合は、**詳細情報** を選択し、次に **実行** を選択します。画面の指示に従って、Raspberry Pi Imagerのインストールを完了します。

    .. image:: img/os_info.png
        :align: center

#. アイコンをクリックするか、ターミナルで ``rpi-imager`` と入力して、Raspberry Pi Imagerアプリケーションを起動します。

    .. image:: img/os_open_imager.png
        :align: center

2. OSをMicro SDカードにインストール
-------------------------------------

#. リーダーを使用して、SDカードをコンピュータまたはラップトップに挿入します。

#. Imager内で、**Raspberry Pi Device** をクリックし、ドロップダウンリストからRaspberry Piのモデルを選択します。

    .. image:: img/os_choose_device.png
        :align: center

#. **Operating System** を選択し、推奨されるオペレーティングシステムバージョンを選びます。

    .. image:: img/os_choose_os.png
        :align: center

#. **Choose Storage** をクリックし、インストールする適切なストレージデバイスを選択します。

    .. note::

        正しいストレージデバイスを選択してください。混乱を避けるために、複数のストレージデバイスが接続されている場合は、追加のストレージデバイスを取り外してください。

    .. image:: img/os_choose_sd.png
        :align: center

#. **NEXT** をクリックし、次に **EDIT SETTINGS** をクリックしてOS設定をカスタマイズします。

    .. note::

        Raspberry Pi用のモニターがある場合、次のステップをスキップしてインストールを開始するために「はい」をクリックできます。他の設定はモニターで後から調整できます。

    .. image:: img/os_enter_setting.png
        :align: center

#. Raspberry Piの **ホスト名** を定義します。

    .. note::

        ホスト名はRaspberry Piのネットワーク識別子です。 ``<hostname>.local`` または ``<hostname>.lan`` を使用してPiにアクセスできます。

    .. image:: img/os_set_hostname.png
        :align: center

#. Raspberry Piの管理者アカウントのための **ユーザー名** と **パスワード** を作成します。

    .. note::

        一意のユーザー名とパスワードを設定することは、デフォルトのパスワードがないRaspberry Piを保護するために重要です。

    .. image:: img/os_set_username.png
        :align: center

#. ネットワークの **SSID** と **パスワード** を入力して無線LANを設定します。

    .. note::

        ご使用の地域に対応する2文字の `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ を「無線LANの国」に設定してください。

    .. image:: img/os_set_wifi.png
        :align: center


#. Raspberry Piにリモート接続するために、サービスタブでSSHを有効にします。

    * **パスワード認証** には、一般タブでのユーザー名とパスワードを使用します。
    * 公開鍵認証の場合は、「公開鍵認証のみを許可」を選択します。RSAキーがある場合はそれが使用されます。ない場合は、「SSH-keygenを実行」をクリックして新しい鍵ペアを生成します。

    .. image:: img/os_enable_ssh.png
        :align: center

#. **オプション** メニューで、書き込み中のImagerの動作を構成できます。例えば、終了時に音を鳴らす、メディアを取り出す、テレメトリーを有効にするなどです。

    .. image:: img/os_options.png
        :align: center

    
#. OSのカスタマイズ設定の入力が終わったら、 **Save** をクリックしてカスタマイズを保存します。その後、イメージの書き込み時に適用するために **Yes** をクリックします。

    .. image:: img/os_click_yes.png
        :align: center

#. SDカードに既存のデータが含まれている場合、データ損失を防ぐためにバックアップを確保してください。バックアップが不要な場合は、 **Yes** をクリックして続行します。

    .. image:: img/os_continue.png
        :align: center

#. 「書き込み成功」のポップアップが表示されたら、イメージが完全に書き込まれ、検証されたことになります。これで、Micro SDカードからRaspberry Piを起動する準備が整いました！

    .. image:: img/os_finish.png
        :align: center
