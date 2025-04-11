
12. 使用 APP 操控 PiDog 
=============================

在本节中，您将学习如何使用 **SunFounder Controller App** 来控制 PiDog。通过这种方式，您可以更加直观和互动地操控这只机器人狗。

.. raw:: html

   <video width="600" loop autoplay muted>
     <source src="../_static/video/app_control.mp4" type="video/mp4">
     您的浏览器不支持视频播放。
   </video>


首先需要在手机/平板上下载 APP，然后连接到 PiDog 广播的 WLAN，最后在 SunFounder Controller 中创建遥控器，即可开始控制 PiDog。

.. _app_control:

通过 APP 控制 PiDog
----------------------------



要使用 SunFounder Controller APP 控制 PiDog，请按照以下步骤操作：

#. 在 **APP Store(iOS)** 或 **Google Play(Android)** 上安装 `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_。

#. 配置所需模块。

   * 首先需要安装 ``robot-hat``、 ``vilib`` 和 ``picar-x`` 模块，具体请参考 :ref:`install_all_modules` 部分。

     * ``robot-hat``
     * ``vilib``
     * ``picar-x``

   * 然后，安装 ``sunfounder-controller`` 模块：

     .. raw:: html

         <run></run>

     .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. 执行以下命令启动控制脚本：

   .. raw:: html

        <run></run>

   .. code-block::

        cd ~/pidog/examples
        sudo python3 12_app_control.py

   成功运行后，您将看到类似如下提示：

   .. code-block:: 

        Running on: http://192.168.18.138:9000/mjpg

        * Serving Flask app "vilib.vilib" (lazy loading)
        * Environment: development
        * Debug mode: off
        * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)      

   这表示您的 PiDog 已准备好进行网络通信。

#. 连接 PiDog 与 SunFounder Controller。

   * 将手机/平板连接至与 PiDog 相同的 WLAN。

   * 打开 **SunFounder Controller** APP，点击 + 图标添加控制器。

     .. image:: img/app1.png


   * 部分产品提供预设控制器，此处请选择 **PiDog**，输入名称或直接点击 **Confirm** 确认。

     .. image:: img/app_preset.jpg


   * 进入控制器后，APP 将自动搜索 **Mydog**，稍等片刻，屏幕上将提示“Connected Successfully”。

     .. image:: img/app_auto_connect.jpg

     .. note::

        * 您也可以手动点击 |app_connect| 按钮，稍等几秒后，Mydog（IP）将会出现，点击它进行连接。

        .. image:: img/sc_mydog.jpg

#. 启动控制器。

   * 出现“Connected Successfully”提示后，点击右上角的 ▶ 按钮。

   * APP 中将显示摄像头画面，此时您即可使用控制界面来操控 PiDog。

   .. image:: img/sc_run.jpg


以下是各控制部件的功能说明：

* A：检测障碍物距离（超声波模块读取值）。
* C：开启/关闭人脸识别功能。
* D：控制 PiDog 头部的倾斜角度。
* E：坐下。
* F：站立。
* G：躺下。
* I：挠头。
* N：吠叫。
* O：摇尾巴。
* P：喘气。
* K：控制 PiDog 的运动（前进、后退、左转、右转）。
* Q：控制 PiDog 头部朝向。
* J：切换为语音控制模式。支持以下语音指令：

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

设置 PiDog 开机自启动
---------------------------------

为避免每次手动运行 12_app_control.py 脚本，您可以配置 PiDog 在开机时自动启动该脚本：

如何设置？

#. 执行以下命令安装并配置 ``pidog_app`` 应用：

   .. raw:: html

        <run></run>

   .. code-block::

        cd ~/pidog/bin
        sudo bash pidog_app_install.sh

#. 出现提示时，输入 ``y`` 以重启 PiDog。

   .. image:: img/auto_start.png

#. 重启后，PiDog 将自动启动控制脚本。之后您可按 :ref:`app_control` 继续使用。

.. warning::

   如果您希望运行其他脚本，请先执行 ``pidog_app disable`` 禁用自动启动功能。
