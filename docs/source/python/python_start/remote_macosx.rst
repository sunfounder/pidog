Mac OS Xユーザー向け
==========================

Mac OS Xユーザーにとって、SSH（Secure Shell）はRaspberry Piへのリモートアクセスと制御を安全かつ便利に行う方法を提供します。これは、Raspberry Piをリモートで作業する場合や、モニターに接続されていない場合に特に便利です。Macのターミナルアプリケーションを使用すると、この安全な接続を確立できます。このプロセスには、Raspberry Piのユーザー名とホスト名を含むSSHコマンドが含まれます。初回接続時には、Raspberry Piの認証性を確認するセキュリティプロンプトが表示されます。

#. Raspberry Piに接続するには、次のSSHコマンドを入力します：

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac_vnc14.png

#. 初めてログインする際にセキュリティメッセージが表示されます。 **yes** と応答して進行します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Raspberry Piのパスワードを入力します。入力しているパスワードが画面に表示されないことに注意してください。これは標準的なセキュリティ機能です。

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 

