.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

Linux/Unixユーザー向け
==========================

#. Linux/Unixシステムで**ターミナル**を探して開きます。

#. Raspberry Piが同じネットワークに接続されていることを確認します。 ``ping <hostname>.local`` と入力して確認してください。例えば：

    .. code-block::

        ping raspberrypi.local

    Raspberry Piがネットワークに接続されている場合は、IPアドレスが表示されます。

    * ターミナルに ``Ping request could not find host pi.local. Please check the name and try again.`` のようなメッセージが表示された場合は、入力したホスト名を再確認してください。
    * IPアドレスが取得できない場合は、Raspberry PiのネットワークまたはWiFi設定を調べてください。

#. ``ssh <username>@<hostname>.local`` または ``ssh <username>@<IP address>`` と入力してSSH接続を開始します。例えば：

    .. code-block::

        ssh pi@raspberrypi.local

#. 初めてログインする際、セキュリティメッセージが表示されます。「yes」と入力して進行します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 以前に設定したパスワードを入力します。セキュリティ上の理由から、入力中にパスワードが表示されないことに注意してください。

    .. note::
        パスワードの文字がターミナルに表示されないのは正常です。正しいパスワードを入力するようにしてください。

#. 正常にログインできたら、Raspberry Piは接続され、次のステップに進む準備が整いました。
