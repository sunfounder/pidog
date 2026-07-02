常见问题
==========

Q1：PiDog 有哪些版本？
------------------------------------------------------

PiDog 分为 **V1 版**\  和 **V2 版**\ ：

* **V1 版**\ ：兼容 Raspberry Pi 3B+/4B/Zero 2W，**不**\ 兼容 Raspberry Pi 5。
* **V2 版**\ ：兼容 Raspberry Pi 3/4/5 和 Zero 2W。改进了 Robot HAT 和舵机驱动电路，为 Pi 5 提供更好的供电支持。
* **电源供应**：V2 版增强了电源管理，适用于更高功耗的应用场景。

Q2：如何安装所需模块？
--------------------------------------------------

.. code-block:: bash

    # Robot HAT
    git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
    cd robot-hat && sudo python3 install.py

    # Vilib
    git clone https://github.com/sunfounder/vilib.git
    cd vilib && sudo python3 install.py

    # PiDog
    git clone https://github.com/sunfounder/pidog.git --depth 1
    cd pidog && sudo pip3 install . --break

如果没有声音：

.. code-block:: bash

    # I2S 音频
    cd ~/robot-hat
    sudo bash i2samp.sh

如有需要可多次运行。

----

Q3: Why do I get a "piper-tts" error during installation?
----------------------------------------------------------

.. important::

   If you see this error during ``pip3 install``:

   .. code-block:: text

       ERROR: Could not find a version that satisfies the requirement piper-tts==1.3.0
       ERROR: No matching distribution found for piper-tts==1.3.0

   It means you are using a **32-bit** Raspberry Pi OS. The ``piper-tts`` package only provides pre-built wheels for **64-bit** systems. Reinstall the OS using the **64-bit** version of Raspberry Pi OS and the installation will succeed.

----

Q4：如何运行第一个示例？
-------------------------------------

.. code-block:: bash

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

PiDog 将会醒来、坐下并摇动尾巴。

----

Q5：有哪些内置动作和声音可用？
------------------------------------------------------

* 动作：``stand``、``sit``、``wag_tail``、``trot`` 等。
* 声音：``bark``、``howling``、``pant`` 等。

运行：

.. code-block:: bash

    sudo python3 2_function_demonstration.py

输入数字触发相应动作。

----

Q6：PiDog 如何使用传感器？
-------------------------------------

* **超声波**：避障与巡线 patrol。
* **触摸**：前部触摸 = 警觉；背部触摸 = 享受。
* **声音方向**：响应声音的来源方向。

----

Q7：PiDog 支持哪些 AI 功能？
------------------------------------------------------

PiDog 集成了 **TTS**、**STT** 和 **LLM**：

* **TTS**：Espeak、Pico2Wave、Piper、OpenAI。
* **STT**：Vosk（离线）。
* **LLM**：Ollama（本地）、OpenAI（在线）。

----

Q8：是否需要校准舵机？
---------------------------------------------

是的——**V1 版和 V2 版都需要校准舵机**，以确保运动稳定并防止损坏。

**V2 版**

The Robot HAT on the V2 version has a **zeroing button**. Press it to automatically set all servos to 0° — no script needed.

If your PiDog V2's legs are in the wrong position after assembly (for example, servos appear at strange angles or the robot cannot stand properly), you can use the zero button to fix this:

#. Power on the PiDog.
#. Press the **zero button** on the Robot HAT — all servos will forcibly return to 0°.
#. Reassemble the legs in the correct orientation following the assembly instructions.

For a step-by-step demonstration, watch the video below:

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zmN_mGxTKuU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**V1 版**

The V1 version uses a script to zero the servos. Run the following command — it will set all servos to 0°:

.. code-block:: bash

   cd ~/pidog/examples
   sudo python3 servo_zeroing.py

This should be done **before installation** to ensure each servo starts from the correct zero position. If your PiDog V1's legs are in the wrong position after assembly, re-run this script to reset all servos to 0°, then reassemble the legs correctly.


----

Q9：为什么我的 PiDog 行走不稳定？
-----------------------------------------------

* 确认所有舵机在 0° 位置安装。
* 确保舵机角度与校准尺（60°/90°）匹配。
* 检查电池是否已充满电。
* 拧紧所有舵机螺丝。

----

Q10: Servo zeroing works, but calibration example doesn't move any servo?
--------------------------------------------------------------------------

If pressing the zeroing button moves all servos to 0° normally, but the calibration script cannot control any servo, the problem is likely a hardware connection issue between the Raspberry Pi and the Robot HAT.

.. note::

   The zeroing button is only available on **PiDog V2** (which uses Robot HAT V5). PiDog V1 does not have this feature and must use the ``servo_zeroing.py`` script instead.

**Why this happens**

* Servo zeroing is handled **directly by the Robot HAT** — it works independently without the Raspberry Pi.
* Running calibration or any servo control from code requires the Raspberry Pi to communicate with the Robot HAT through the **GPIO header pins**.

**How to diagnose**

This is often caused by poor soldering on either side of the GPIO connection:

* The **Raspberry Pi's 40-pin GPIO header** (especially on Zero 2W, where the header must be soldered on by the user).
* The **Robot HAT's female header pins**.

Take clear, well-lit photos of both sets of pins and send them to SunFounder support at service@sunfounder.com. The team will help identify whether resoldering is needed.

----

Q11：为什么我的摄像头不工作？
--------------------------------------

* 确保摄像头排线**牢固插入** CSI 接口，黑色锁扣已扣紧。
* 在插拔摄像头之前，请**关闭** Raspberry Pi 电源，以免损坏。
* 使用 ``libcamera-hello`` 或 ``raspistill`` 测试摄像头，确认图像输出正常。
* 如果排线松动或安装不当，请重新插拔。

----

Q12：为什么扬声器不工作？
--------------------------------------

* 确保 Robot HAT 扬声器已激活。如果您还没有运行过任何 PiDog 示例代码，请先激活它：

  .. code-block:: bash

     robot_hat enable_speaker

  每次开机只需执行一次。运行任何 PiDog 示例（会初始化 ``Pidog()``）都会自动完成此操作。

* 确保音量未静音，且 I2S 音频驱动已安装。
* 如果没有声音，按照以下步骤重新配置 I2S：

.. code-block:: bash

    cd ~/robot-hat
    sudo bash i2samp.sh

* 运行脚本后重启 Raspberry Pi。

----

Q13：为什么麦克风不工作？
--------------------------------------

* 检查系统是否识别麦克风：

.. code-block:: bash

    arecord -l

* 测试录音功能：

.. code-block:: bash

    arecord -D plughw:1,0 -f cd test.wav

* 如果没有录到音频，在音频设置中选择正确的输入设备，或使用 ``alsamixer`` 调节输入音量。
* 确保没有其他进程占用音频输入设备。

----

Q14：为什么声音方向传感器不工作？
-------------------------------------------------------

* 确保声音方向传感器连接到正确的 SPI 接口。
* 检查所有线缆是否连接牢固且没有接反。
* 确保电源稳定且传感器未被遮挡。
* 重启设备，然后重新运行传感器示例脚本。

----

Q15：为什么触摸传感器无响应？
----------------------------------------------

* 确保所有触摸传感器线缆连接牢固。
* 请注意：**低电平**\ 信号表示传感器正在被触摸。
* 使用 ``gpio readall`` 或 Python 代码测试 GPIO 引脚，确认信号检测是否正常。
* 重新检查接线和方向。

----

Q16: Why is the ultrasonic sensor not working?
-----------------------------------------------

#. Run the ultrasonic test to check the reading:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 ultrasonic_test.py

   If the reading shows **-1**, the sensor is not functioning correctly.

#. Verify the wiring:

   * **White wire** → GPIO **17**
   * **Yellow wire** → GPIO **4**

#. If the wiring is correct and the reading is still -1, contact SunFounder support at service@sunfounder.com for further assistance.

----

Q17：为什么 LED 板不亮或闪烁异常？
---------------------------------------------------------------------

* 确认 LED 板由 **3.3V** 供电并连接到 I2C 端口。
* 确保 Raspberry Pi 上已**启用 I2C**。
* 运行以下命令检查 LED 板是否被识别：

.. code-block:: bash

    i2cdetect -y 1

* 如果没有检测到设备，重新检查接线并重启 Pi。

----

Q18: Why are the 6-DOF IMU and 11-channel RGB board not working?
-----------------------------------------------------------------

If both the 6-DOF IMU and the 11-channel RGB LED board are not responding, the issue is likely with the shared I2C connection:

#. First, check whether the devices are detected on the I2C bus:

   .. code-block:: bash

       sudo i2cdetect -y 1

   The expected addresses are:

   * **0x36** — 6-DOF IMU
   * **0x74** — 11-channel RGB LED board

   If one or both addresses are missing, the corresponding device is not properly connected.

#. Try connecting the 6-DOF IMU to a different port and test again.
#. Connect the 6-DOF IMU directly to the Robot HAT's I2C port, then run the test:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 imu_test.py

#. If the IMU works when connected directly, the problem is with the 11-channel RGB board's pass-through port.
#. To confirm, connect the 11-channel RGB board directly to the I2C port and test:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 rgb_strip_test.py

----

Q19：PiDog 如何获取电源？
------------------------------------------

* 使用 5V 3A Type-C 电源适配器。
* 红灯 = 充电中，灯灭 = 已充满。
* 可以边充电边使用。
* 如果指示灯不亮，请先充电。

----
