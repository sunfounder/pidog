
针对 Windows 用户
==========================

对于 Windows 10 或更高版本的用户，通过以下步骤可以远程登录到 Raspberry Pi：

#. 在您的 Windows 搜索框中搜索 ``powershell``。右键点击 ``Windows PowerShell`` 并选择 ``Run as administrator``。

    .. image:: img/powershell_ssh.png
        :align: center

#. 通过在 PowerShell 中输入 ``ping -4 <hostname>.local`` 来确定您的 Raspberry Pi 的 IP 地址。

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    一旦连接到网络，Raspberry Pi 的 IP 地址将被显示。

    * 如果终端显示 ``Ping request could not find host pi.local. Please check the name and try again.``, 请核实您输入的主机名是否正确。
    * 如果仍然无法检索到 IP 地址，请检查 Raspberry Pi 上的网络或 WiFi 设置。

#. 确认 IP 地址后，使用 ``ssh <username>@<hostname>.local`` 或 ``ssh <username>@<IP address>`` 登录到您的 Raspberry Pi。

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        如果出现错误提示 ``The term 'ssh' is not recognized as the name of a cmdlet...``，可能是您的系统未预装 SSH 工具。在这种情况下，您需要按照 :ref:`openssh_powershell` 手动安装 OpenSSH，或使用 :ref:`login_windows` 中描述的第三方工具。

#. 首次登录时会出现安全消息。输入 ``yes`` 继续。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入您之前设置的密码。请注意，出于安全考虑，输入密码时不会在屏幕上显示。

    .. note::
        输入密码时字符不可见是正常的。确保输入正确的密码。

#. 连接成功后，您的 Raspberry Pi 已准备好进行远程操作。

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center
