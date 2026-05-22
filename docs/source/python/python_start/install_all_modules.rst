.. note::

    你好，欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者Facebook社区！与 fellow enthusiasts 一起深入探索 Raspberry Pi、Arduino 和 ESP32。

    **为什么要加入？**

    - **专家支持**：获得社区和团队的帮助，解决售后问题和技术难题。
    - **学习与分享**：交流技巧和教程，提升你的技能。
    - **独家预览**：抢先获取新产品公告和 sneak peeks。
    - **特别折扣**：享受我们最新产品的独家折扣。
    - **节日促销与抽奖**：参与抽奖和节日促销活动。

    👉 准备好和我们一起探索和创造了吗？点击 [|link_sf_facebook|]，立即加入吧！

.. _install_all_modules:

安装所有模块（重要）
==============================================

.. note::

    如果你安装的是精简版操作系统，则必须安装 Python3 相关软件包。

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt install git python3-pip python3-setuptools python3-smbus


#. 安装 ``robot-hat`` 模块。


   .. raw:: html

       <run></run>

   .. code-block::

       cd ~/
       git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
       cd robot-hat
       sudo python3 install.py

#. 安装 ``vilib`` 模块。

   .. raw:: html

       <run></run>

   .. code-block::

       cd ~/
       git clone https://github.com/sunfounder/vilib.git
       cd vilib
       sudo python3 install.py

#. 安装 ``pidog`` 模块。

   .. raw:: html

       <run></run>

   .. code-block::

       cd ~/
       git clone https://github.com/sunfounder/pidog.git --depth 1
       cd pidog
       sudo pip3 install . --break

   此步骤需要一些时间，请耐心等待。

#. 运行脚本 ``i2samp.sh``。

   最后，你需要运行脚本 ``i2samp.sh`` 来安装 i2s 放大器所需的组件，否则机器人将没有声音。

   .. raw:: html

       <run></run>

   .. code-block::

       cd ~/robot-hat
       sudo bash i2samp.sh

   输入 y 并按三次回车键继续执行脚本，在后台启动 /dev/zero，然后重启机器。

   .. note::
       如果重启后没有声音，你可能需要多次运行 ``i2samp.sh`` 脚本。
