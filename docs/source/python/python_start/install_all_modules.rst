.. _install_all_modules:

5. 安装所有模块（重要）
==============================================

.. note::

    如果你使用的是 Lite 版本的操作系统，必须先安装 Python3 相关依赖。

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt install git python3-pip python3-setuptools python3-smbus


#. 安装 ``robot-hat`` 模块

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
        cd robot-hat
        sudo python3 install.py


#. 安装 ``vilib`` 模块

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone https://github.com/sunfounder/vilib.git
        cd vilib
        sudo python3 install.py


#. 安装 ``pidog`` 模块

    .. raw:: html

        <run></run>

    .. code-block:: bash

        cd ~/
        git clone https://github.com/sunfounder/pidog.git --depth 1
        cd pidog
        sudo pip3 install . --break

    这一步会花一些时间，请耐心等待。


#. 运行 ``i2samp.sh`` 脚本

    最后，需要运行 ``i2samp.sh`` 来安装 I2S 功放所需的组件，否则机器人将没有声音输出。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/robot-hat
        sudo bash i2samp.sh
        
    .. image:: img/i2s.png

    输入 ``y`` 并按 ``Enter`` 继续运行脚本。

    .. image:: img/i2s2.png

    再次输入 ``y`` 并按 ``Enter`` 来在后台运行 ``/dev/zero``。

    .. image:: img/i2s3.png

    再次输入 ``y`` 并按 ``Enter`` 重启设备。

    .. note::
        如果重启后仍然没有声音，可能需要多次运行 ``i2samp.sh`` 脚本。
