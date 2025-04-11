
针对 Mac OS X 用户
==========================

对于 Mac OS X 用户，SSH（安全壳）提供了一种安全且便捷的方式，用于远程访问和控制 Raspberry Pi。这在远程工作或 Raspberry Pi 未连接显示器时尤为方便。使用 Mac 上的 Terminal 应用程序，您可以建立这种安全连接。此过程涉及使用 Raspberry Pi 的用户名和主机名的 SSH 命令。在初次连接时，安全提示将要求确认 Raspberry Pi 的真实性。

#. 要连接到 Raspberry Pi，请输入以下 SSH 命令：

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac-ping.png

#. 首次登录时将出现安全消息。回答 **yes** 继续。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入 Raspberry Pi 的密码。请注意，出于安全考虑，输入密码时不会在屏幕上显示。

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

        