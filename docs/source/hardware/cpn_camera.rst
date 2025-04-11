摄像头模块
====================================


**描述**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

这是一款5MP的Raspberry Pi摄像头模块，配备了OV5647传感器。它支持即插即用，将附带的排线连接到您的Raspberry Pi的CSI（Camera Serial Interface）端口即可开始使用。

该模块体积小巧，大约25mm x 23mm x 9mm，重量为3g，非常适合移动或其他对尺寸和重量要求严格的应用。摄像头模块具有500万像素的原生分辨率，并配备了一个固定焦点镜头，能够拍摄2592 x 1944像素的静态图像，同时支持1080p30、720p60和640x480p90视频。

.. note:: 

   该模块仅能捕捉图像和视频，不能录制声音。



**规格**

* **静态图像分辨率**：2592×1944
* **支持的视频分辨率**：1080p/30 fps、720p/ 60fps 以及 640 x480p 60/90 视频录制
* **光圈（F）**：1.8
* **视角**：65度
* **尺寸**：24mmx23.5mmx8mm
* **重量**：3g
* **接口**：CSI连接器
* **支持的操作系统**：推荐使用最新版本的Raspberry Pi OS





**组装摄像头模块**

在摄像头模块或Raspberry Pi上，您会找到一个扁平的塑料连接器。小心地拉出黑色固定开关，直到固定开关部分拉出。按照显示的方向将FFC线缆插入塑料连接器中，然后将固定开关推回原位。

如果FFC线缆安装正确，它应该是直的，并且当您轻轻拉动时不会脱落。如果不是，请重新安装。

.. image:: img/connect_ffc.png
.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   安装摄像头时，请确保电源关闭，否则可能会损坏您的摄像头。

.. **启用摄像头接口**

.. 运行以下命令以启用您的Raspberry Pi的摄像头接口。如果您已经启用了它，跳过这步；如果您不确定是否已经启用，继续操作。

.. .. raw:: html

..    <run></run>

.. 
   .. code-block:: 

..    sudo raspi-config

.. **3 Interfacing options**

.. .. image:: img/image282.png
..    :align: center

.. **P1 Camera**

.. .. image:: img/camera_config1.png
..    :align: center

.. **<Yes>, then <Ok> -> <Finish>**

.. .. image:: img/camera_config2.png
..    :align: center

.. 配置完成后，建议重新启动Raspberry Pi。

.. .. raw:: html

..    <run></run>

..
    .. code-block:: 

..    sudo reboot