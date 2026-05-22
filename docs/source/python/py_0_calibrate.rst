.. note::

    你好，欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者Facebook社区！与 fellow enthusiasts 一起深入探索 Raspberry Pi、Arduino 和 ESP32。

    **为什么要加入？**

    - **专家支持**：获得社区和团队的帮助，解决售后问题和技术难题。
    - **学习与分享**：交流技巧和教程，提升你的技能。
    - **独家预览**：抢先获取新产品公告和 sneak peeks。
    - **特别折扣**：享受我们最新产品的独家折扣。
    - **节日促销与抽奖**：参与抽奖和节日促销活动。

    👉 准备好和我们一起探索和创造了吗？点击 [|link_sf_facebook|]，立即加入吧！

2. 校准 PiDog
=============================

**简介**

校准 PiDog 是确保其稳定高效运行的关键步骤。此过程有助于纠正因装配或结构误差导致的任何不平衡或不精确。请仔细按照以下步骤操作，确保你的 PiDog 行走顺畅，性能符合预期。

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/calibrate_before.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

如果偏差角度过大，请返回 :ref:`py_servo_adjust`，将舵机角度设置为 0°，然后按照说明重新组装 PiDog。

**校准视频**

详细指南请参考完整的校准教程视频。该视频将以视觉化方式逐步演示如何精确校准你的 PiDog。

.. note::

   PiDog 套件包含一个 90° 或 60° 的校准尺。视频中使用的是 90° 校准尺，但 60° 的校准过程非常相似。你也可以参考下方的图文分步指南。

    .. image:: img/cali_ruler.png
         :width: 400
         :align: center

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/witCWeoHTdk?si=g8_RZDUkfjdwbLZu&amp;start=871&end=1160" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**步骤**

请按照以下步骤操作：

#. 将 PiDog 放置在平坦的平台上。

   .. image:: img/place-pidog.JPG

#. 进入 PiDog 示例代码目录，运行 ``0_calibration.py`` 脚本。

   .. raw:: html

        <run></run>

   .. code-block::

        cd ~/pidog/examples
        sudo python3 0_calibration.py

#. 运行脚本后，终端将出现一个交互界面。选择你拥有的校准尺类型：
   选项 1 对应 90°，选项 2 对应 60°。

    .. image:: img/CALI.slt.1.png

#. 做出选择后，将出现以下校准界面：

    .. image:: img/CALI.slt.2.png

**如果你使用的是 60° 校准尺**

#. 如图所示放置**校准尺（亚克力 C 形板）**，长边置于水平面上。在终端中按 ``1``，然后使用 ``w`` 和 ``s`` 键调整对齐。

    .. image:: img/CALI.60.1.JPG

#. 按下图所示重新放置**校准尺**。在终端中按 ``2``，然后使用 ``w`` 和 ``s`` 键微调对齐。

    .. image:: img/CALI.60.2.JPG

#. 对舵机 3 至 8 重复校准过程，确保 PiDog 的四条腿均正确校准。

**如果你使用的是 90° 校准尺**

#. 如图所示放置**校准尺（亚克力 C 形板）**。在终端中按 ``1``，然后使用 ``w`` 和 ``s`` 键将其边缘与图示对齐。

    .. image:: img/CALI-1.2.png

#. 如图所示重新放置**校准尺（亚克力 C 形板）**。在终端中按 ``2``，然后再次使用 ``w`` 和 ``s`` 键进行调整。

    .. image:: img/CALI-2.2.png

#. 对舵机 3 至 8 重复校准步骤，确保 PiDog 的四条腿均正确校准。

**完成校准**

- 所有舵机校准完成后，重新运行 PiDog 行走或姿态示例代码，检查动作是否顺畅。
- 如果仍有偏差，请返回校准程序进行微调。
- 强烈建议在初始组装后完成此步骤，以确保运行期间的稳定性能。

.. tip::

   为避免将来重新校准，可以在校准后记录舵机角度或导出配置文件。这样下次可以轻松快速恢复设置。
