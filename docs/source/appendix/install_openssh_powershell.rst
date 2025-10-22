.. _openssh_powershell: 

通过 PowerShell 安装 OpenSSH
==================================

当您使用 ``ssh <username>@<hostname>.local`` （或 ``ssh <username>@<IP address>`` ）尝试连接到您的 Raspberry Pi 时，却出现以下错误消息。

    .. code-block:: 

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


这表示您的计算机系统较旧，尚未预装 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_，您需要按照以下教程手动安装。

#. 在您的 Windows 桌面搜索框中输入 ``powershell``，右键点击 ``Windows PowerShell``，并从弹出的菜单中选择 ``以管理员身份运行``。

    .. image:: img/powershell_ssh.png
        :align: center

#. 使用以下命令安装 ``OpenSSH.Client``。

    .. code-block:: 

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. 安装后，将返回以下输出。

    .. code-block:: 

        Path          :
        Online        : True
        RestartNeeded : False

#. 通过以下命令验证安装。

    .. code-block:: 

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. 现在会显示 ``OpenSSH.Client`` 已成功安装。

    .. code-block:: 

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        如果没有出现上述提示，说明您的 Windows 系统过于陈旧，建议安装第三方 SSH 工具，如 :ref:`login_windows`。

#. 重新启动 PowerShell 并继续以管理员身份运行。此时，您将能够使用 ``ssh`` 命令登录到您的 Raspberry Pi，在此过程中，系统会提示您输入之前设置的密码。

    .. image:: img/powershell_login.png