Für Mac OS X-Benutzer
==========================

Für Mac OS X-Benutzer bietet SSH (Secure Shell) eine sichere und bequeme Methode, um remote auf einen Raspberry Pi zuzugreifen und ihn zu steuern. Dies ist besonders praktisch, wenn Sie mit dem Raspberry Pi remote arbeiten oder wenn er nicht an einen Monitor angeschlossen ist. Mit der Terminal-Anwendung auf einem Mac können Sie diese sichere Verbindung herstellen. Der Prozess beinhaltet einen SSH-Befehl, der den Benutzernamen und den Hostnamen des Raspberry Pi enthält. Bei der ersten Verbindung erscheint eine Sicherheitsaufforderung, die die Authentizität des Raspberry Pi bestätigt.

#. Um eine Verbindung zum Raspberry Pi herzustellen, geben Sie den folgenden SSH-Befehl ein:

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac_vnc14.png

#. Bei Ihrer ersten Anmeldung erscheint eine Sicherheitsmeldung. Antworten Sie mit **yes**, um fortzufahren.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Geben Sie das Passwort für den Raspberry Pi ein. Beachten Sie, dass das Passwort beim Tippen nicht auf dem Bildschirm angezeigt wird, was ein Standard-Sicherheitsmerkmal ist.

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
