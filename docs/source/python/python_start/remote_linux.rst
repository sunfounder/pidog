
对于 Linux/Unix 用户
==========================

#. 在您的 Linux/Unix 系统上找到并打开 **Terminal** 。

#. 确保您的 Raspberry Pi 连接到同一网络。通过输入 `ping <hostname>.local` 来验证。例如：

    .. code-block::

        ping raspberrypi.local

    如果连接到网络，您应该看到 Raspberry Pi 的 IP 地址。

    * 如果终端显示消息 ``Ping request could not find host pi.local. Please check the name and try again.``, 请仔细检查您输入的主机名。
    * 如果您无法检索到 IP 地址，请检查 Raspberry Pi 的网络或 WiFi 设置。

#. 通过输入 ``ssh <username>@<hostname>.local`` 或 ``ssh <username>@<IP address>`` 来启动 SSH 连接。例如：

    .. code-block::

        ssh pi@raspberrypi.local

#. 首次登录时，您会遇到一个安全提示消息。输入 ``yes`` 继续。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入您之前设置的密码。请注意，出于安全原因，输入时密码不会显示。

    .. note::        
        密码字符在终端不显示是正常的。只需确保输入正确的密码。

#. 成功登录后，您的 Raspberry Pi 现已连接，您可以继续进行下一步。
