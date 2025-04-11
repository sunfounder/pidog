.. _install_os_sd:

2. 安装操作系统
============================================================


**所需组件**

* 个人电脑
* 微型SD卡及读卡器

1. 安装 Raspberry Pi Imager
----------------------------------

#. 访问 Raspberry Pi 软件下载页面 `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_。选择与您的操作系统兼容的 Imager 版本。下载并打开文件开始安装。

    .. image:: img/os_install_imager.png
        :align: center

#. 安装过程中可能会出现安全提示，具体取决于您的操作系统。例如，Windows 可能会显示警告消息。在这种情况下，选择 **More info** 然后 **Run anyway** 。按照屏幕上的指导完成 Raspberry Pi Imager 的安装。

    .. image:: img/os_info.png
        :align: center

#. 通过点击其图标或在终端输入 ``rpi-imager`` 来启动 Raspberry Pi Imager 应用程序。

    .. image:: img/os_open_imager.png
        :align: center

2. 将操作系统安装到微型SD卡
--------------------------------

#. 使用读卡器将您的SD卡插入计算机或笔记本电脑。

#. 在 Imager 中，点击 **Raspberry Pi Device** 并从下拉列表中选择 Raspberry Pi 型号。

    .. image:: img/os_choose_device.jpg
        :align: center

#. 选择 **Operating System** 并选择推荐的操作系统版本。

    .. image:: img/os_choose_os1.png
        :align: center

#. 点击 **Choose Storage** 并选择适当的存储设备进行安装。

    .. note::

        确保选择正确的存储设备。为避免混淆，如果连接了多个存储设备，请断开其他存储设备。

    .. image:: img/os_choose_sd.png
        :align: center

#. 点击 **NEXT** 然后 **EDIT SETTINGS** 来定制您的操作系统设置。

    .. note::

        如果您有 Raspberry Pi 的显示器，您可以跳过接下来的步骤并点击 'Yes' 开始安装。稍后可以在显示器上调整其他设置。

    .. image:: img/os_enter_setting.jpg
        :align: center

#. 为您的 Raspberry Pi 定义一个 **hostname**。

    .. note::

        Hostname 是您的 Raspberry Pi 的网络标识符。您可以使用 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问您的 Pi。

    .. image:: img/os_set_hostname.jpg
        :align: center

#. 为 Raspberry Pi 的管理员账户创建一个 **Username** 和 **Password**。

    .. note::

        为您的 Raspberry Pi 设定独特的用户名和密码对于安全至关重要，因为它没有默认密码。

    .. image:: img/os_set_username.jpg
        :align: center

#. 通过提供您网络的 **SSID** 和 **Password** 配置无线局域网。

    .. note::

        设置 ``Wireless LAN country`` 为与您所在地相对应的两个字母 `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

    .. image:: img/os_set_wifi.jpg
        :align: center


#. 要远程连接到您的 Raspberry Pi，请在 Services 标签中启用 SSH。

    * 对于 **password authentication**，使用 General 标签中的用户名和密码。
    * 对于公钥认证，请选择 "Allow public-key authentication only"。如果您有 RSA 密钥，将会使用该密钥。如果没有，请点击 "Run SSH-keygen" 生成新的密钥对。

    .. image:: img/os_enable_ssh.png
        :align: center

#. **Options** 菜单让您可以配置 Imager 在写入过程中的行为，包括写入完成时播放声音、完成时弹出媒体和启用遥测。

    .. image:: img/os_options.png
        :align: center


#. 完成输入操作系统定制设置后，点击 **Save** 保存您的定制。然后点击 **Yes** 在写入映像时应用它们。

    .. image:: img/os_click_yes.jpg
        :align: center

#. 如果 SD 卡中包含现有数据，请确保备份以防数据丢失。如果不需要备份，点击 **Yes** 继续。

    .. image:: img/os_continue.png
        :align: center

#. 当您看到 "Write Successful" 弹窗时，您的映像已经完全写入并验证。您现在可以准备使用微型SD卡启动 Raspberry Pi 了！

    .. image:: img/os_finish.png
        :align: center

#. 现在您可以将设置了 Raspberry Pi OS 的 SD 卡插入位于 Raspberry Pi 底部的微型SD卡插槽中。

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center