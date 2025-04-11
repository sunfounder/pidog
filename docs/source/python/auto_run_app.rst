
3. 快速使用App
=================================================

现在您的PiDog已经全部设置好并迫不及待地想要启动，本节非常适合那些渴望快速深入了解并探索其所有功能的用户。我们将引导您完成安装App，无缝连接您的PiDog和您的移动设备，并释放其提供的各种有趣功能，所有操作都在您的指尖完成。本章结束时，您将能够自信地使用您的设备导航并与您的PiDog互动。让我们开始吧，沉浸在交互式机器人的世界中！

#. 安装 ``sunfounder-controller`` 模块。

    需要先安装 robot-hat、vilib 和 picar-x 模块，详情见：:ref:`install_all_modules`。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. 运行以下命令：


    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/bin
        sudo bash pidog_app_install.sh


#. 重启 PiDog。

#. 从 **APP Store(iOS)** 或 **Google Play(Android)** 安装 `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_。

#. 连接到 ``pidog`` WLAN。

    现在，将您的移动设备连接到 PiDog 广播的局域网（LAN）。这样，您的移动设备和 PiDog 将在同一网络上，这将便于移动设备上的应用程序与 PiDog 之间的通信。

    * 在移动电话（平板电脑）的WLAN中找到 ``pidog``，输入密码 ``12345678`` 并连接。

    * 默认连接模式为AP模式。因此连接后，会有提示告诉您这个WLAN网络没有互联网访问，请选择继续连接。

        .. image:: img/app_no_internet.png




#. 打开 ``Sunfounder Controller`` APP。点击加号图标添加遥控器。

        .. image:: img/app1.png

#. 有一些产品可用的预设控制器，在这里我们选择 **PiDog**。给它起个名字，或简单地点击 **确认**。

        .. image:: img/app_preset.jpg


#. 进入应用程序后，它将自动搜索 **Mydog**。片刻之后，您将看到“连接成功”的提示。

        .. image:: img/app_auto_connect.jpg

    .. note::

        * 您也可以手动点击 |app_connect| 按钮。等待几秒钟，MyDog(IP) 将出现，点击它进行连接。

            .. image:: img/sc_mydog.jpg

        * 
#. 运行控制器。

    * 当出现“连接成功”的提示时，点击右上角的 ▶ 按钮。

    * 摄像头画面将出现在APP上，现在您可以用这些小部件控制您的PiDog。

        .. image:: img/sc_run.jpg

以下是小部件的功能介绍。

* A: 检测障碍物距离，即超声波模块的读数。
* C: 开启/关闭面部检测。
* D: 控制PiDog的头部倾斜角度（倾斜头部）。
* E: 坐下。
* F: 站立。
* G: 躺下。
* I: 抓 PiDog 的头。
* N: 吠叫。
* O: 摇尾巴。
* P: 喘气。
* K: 控制 PiDog 的移动（前进、后退、左转和右转）。
* Q: 控制 PiDog 头部的方向。
* J: 切换到语音控制模式。它支持以下语音命令：

    * ``forward``
    * ``backward``
    * ``turn left``
    * ``turn right``
    * ``trot``
    * ``stop``
    * ``lie down``
    * ``stand up``
    * ``sit``
    * ``bark``
    * ``bark harder``
    * ``pant``
    * ``wag tail``
    * ``shake head``
    * ``stretch``
    * ``doze off``
    * ``push-up``
    * ``howling``
    * ``twist body``
    * ``scratch``
    * ``handshake``
    * ``high five``

APP 程序配置
-----------------------------

您可以输入以下命令来修改 APP 模式的设置。

.. code-block::

    pidog_app <OPTION> [input]

**OPTION**
    * ``-h`` ``help`` : 帮助，显示此消息
    * ``start`` ``restart`` : 重新启动 pidog_app 服务
    * ``stop`` : 停止 pidog_app 服务
    * ``disable`` : 禁用启动时自动启动 app_controller 程序
    * ``enable`` : 启用启动时自动启动 app_controller 程序
    * ``close_ap`` : 关闭热点，禁用启动时自动启动热点并切换到 sta 模式
    * ``open_ap`` : 打开热点，启动时启用自动启动热点
    * ``ssid`` : 设置热点的 ssid（网络名称）
    * ``psk`` : 设置热点的密码
    * ``country`` : 设置热点的国家代码
