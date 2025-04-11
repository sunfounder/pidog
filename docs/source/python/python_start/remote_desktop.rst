.. _remote_desktop: 

树莓派远程桌面访问
==================================================

对于那些偏好图形用户界面（GUI）而非命令行访问的用户来说，树莓派支持远程桌面功能。本指南将引导您设置并使用 VNC（虚拟网络计算）进行远程访问。

我们推荐使用 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ 来实现这一功能。

**在树莓派上启用 VNC 服务**

VNC 服务在树莓派 OS 中预装但默认禁用。按照以下步骤启用它：

#. 在树莓派终端输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 使用向下箭头键导航至 **Interfacing Options**，然后按 **Enter**。

    .. image:: img/config_interface.png
        :align: center

#. 从选项中选择 **VNC**。

    .. image:: img/vnc.png
        :align: center

#. 使用箭头键选择 **<Yes>** -> **<OK>** -> **<Finish>** 并完成 VNC 服务的激活。

    .. image:: img/vnc_yes.png
        :align: center

**通过 VNC Viewer 登录**

#. 在您的个人电脑上下载并安装 `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_。

#. 安装完毕后，启动 VNC Viewer。输入您的树莓派的主机名或 IP 地址，然后按 Enter。

    .. image:: img/vnc_viewer1.png
        :align: center

#. 当系统提示时，输入您树莓派的用户名和密码，然后点击 **OK**。

    .. image:: img/vnc_viewer2.png
        :align: center

#. 几秒钟后，树莓派 OS 桌面将显示出来。现在您可以打开终端开始输入命令了。

    .. image:: img/bookwarm.png
        :align: center
