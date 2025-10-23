
2. 校准 PiDog
=============================

**简介**

校准您的 PiDog 是确保其稳定高效运行的关键步骤。该过程有助于修正因组装或结构误差造成的不平衡或不准确。请仔细按照以下步骤操作，以确保 PiDog 行走平稳，表现如预期。

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/calibrate_before.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>


但如果偏差角度过大，请返回 :ref:`py_servo_adjust`，将舵机角度设为 0°，然后按照说明重新组装 PiDog。


**校准视频**

如需详细指南，请参考完整的校准教学视频。视频将以直观的方式逐步展示如何准确校准您的 PiDog。

.. note::

   PiDog 套件中附带 90° 或 60° 校准尺。我们的视频中使用的是 90° 尺，但 60° 的校准过程也大致相同。您也可以参考下方的详细图文步骤。
    
    .. image:: img/cali_ruler.png
         :width: 400
         :align: center

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/witCWeoHTdk?si=g8_RZDUkfjdwbLZu&amp;start=871&end=1160" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**步骤**

具体操作如下：

#. 将 PiDog 放置在平台上。

   .. image:: img/place-pidog.JPG

#. 进入 PiDog 示例代码目录，并运行 ``0_calibration.py`` 脚本。

   .. raw:: html

        <run></run>

   .. code-block::

        cd ~/pidog/examples
        sudo python3 0_calibration.py
        
#. 运行脚本后，终端会出现交互界面。请根据您手中的校准尺类型选择：若为 90°，选第一项；若为 60°，选第二项。

    .. image:: img/CALI.slt.1.png

#. 选择后，您将进入以下校准界面：

    .. image:: img/CALI.slt.2.png

**如果你的是60° 校准尺**

#. 如图所示摆放 **校准尺（亚克力C板）**，将其长边置于水平面上。在终端按 ``1``，使用 ``w`` 和 ``s`` 键调整边缘对齐。

    .. image:: img/CALI.60.1.JPG

#. 根据下图重新放置 **校准尺**。在终端按 ``2``，再通过 ``w`` 和 ``s`` 键进行微调。

    .. image:: img/CALI.60.2.JPG

#. 重复第 3 至第 8 舵机的校准过程，确保 PiDog 四条腿均已完成校准。

**如果你的是90° 校准尺**

#. 按图示放置 **校准尺（亚克力C板）**。在终端中按 ``1``，然后使用 ``w`` 和 ``s`` 键调整，使边缘对齐图示位置。

    .. image:: img/CALI-1.2.png

#. 重新摆放 **校准尺（亚克力C板）**，如图所示。终端按 ``2``，再使用 ``w`` 和 ``s`` 调整边缘对齐。

    .. image:: img/CALI-2.2.png

#. 重复第 3 至第 8 舵机的校准操作，确保 PiDog 的四条腿都已完成校准。


**完成校准**

- 完成全部舵机的校准后，可重新运行 PiDog 的行走或姿态示例代码，检查动作是否平稳。  
- 若发现偏差，可再次进入校准程序进行微调。  
- 建议首次组装完成后一定要完成此步骤，以确保后续运行稳定。

.. tip::

   为避免再次校准，可在校准完成后记录舵机角度或导出配置文件，方便下次快速恢复。
