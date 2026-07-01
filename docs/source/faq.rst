FAQ
==========

Q1: What versions of PiDog are available?
------------------------------------------------------

PiDog comes in **Standard** and **V2** versions:

* **Standard Version**: Compatible with Raspberry Pi 3B+/4B/Zero 2W, **not** compatible with Raspberry Pi 5.  
* **V2 Version**: Compatible with Raspberry Pi 3/4/5 and Zero 2W. It improves Robot HAT and servo driver circuits and provides better power support for Pi 5.  
* **Power Supply**: V2 has enhanced power management for higher power consumption applications.

Q2: How do I install the required modules?
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

If there's no sound:

.. code-block:: bash

    # I2S Audio
    cd ~/robot-hat
    sudo bash i2samp.sh

Run multiple times if needed.

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

Q4: How do I run the first demo?
-------------------------------------

.. code-block:: bash

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

PiDog will wake up, sit down, and wag its tail.

----

Q5: What built-in actions and sounds are available?
------------------------------------------------------

* Actions: ``stand``, ``sit``, ``wag_tail``, ``trot``, etc.  
* Sounds: ``bark``, ``howling``, ``pant``, etc.

Run:

.. code-block:: bash

    sudo python3 2_function_demonstration.py

Enter numbers to trigger actions.

----

Q6: How does PiDog use sensors?
-------------------------------------

* **Ultrasonic**: Obstacle avoidance and patrol.  
* **Touch**: Front touch = alert; back touch = enjoyment.  
* **Sound Direction**: Responds to the direction of sound.

----

Q7: What AI features does PiDog support?
------------------------------------------------------

PiDog integrates with **TTS**, **STT**, and **LLM**:

* **TTS**: Espeak, Pico2Wave, Piper, OpenAI.  
* **STT**: Vosk (offline).  
* **LLM**: Ollama (local), OpenAI (online).

----

Q8: Do I need to calibrate the servos?
---------------------------------------------

Yes — **servo calibration is required for both V1 and V2 versions** to ensure stable movement and prevent damage.

**V2 Version**

The Robot HAT on the V2 version has a **zeroing button**. Press it to automatically set all servos to 0° — no script needed.

If your PiDog V2's legs are in the wrong position after assembly (for example, servos appear at strange angles or the robot cannot stand properly), you can use the zero button to fix this:

#. Power on the PiDog.
#. Press the **zero button** on the Robot HAT — all servos will forcibly return to 0°.
#. Reassemble the legs in the correct orientation following the assembly instructions.

For a step-by-step demonstration, watch the video below:

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zmN_mGxTKuU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**V1 Version**

The V1 version uses a script to zero the servos. Run the following command — it will set all servos to 0°:

.. code-block:: bash

   cd ~/pidog/examples
   sudo python3 servo_zeroing.py

This should be done **before installation** to ensure each servo starts from the correct zero position. If your PiDog V1's legs are in the wrong position after assembly, re-run this script to reset all servos to 0°, then reassemble the legs correctly.


----

Q9: Why is my PiDog walking unstably?
-----------------------------------------------

* Confirm all servos were installed at 0°.  
* Ensure servo angles match the calibration ruler (60°/90°).  
* Check that the battery is fully charged.  
* Tighten all servo screws.

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

Q11: Why is my camera not working?
--------------------------------------

* Ensure the camera cable is **firmly inserted** into the CSI interface and the black locking tab is secured.  
* **Power off** the Raspberry Pi before plugging or unplugging the camera to prevent damage.  
* Test the camera using ``libcamera-hello`` or ``raspistill`` to verify image output.  
* Re-seat the cable if it is loose or improperly installed.

----

Q12: Why isn’t the speaker working?
--------------------------------------

* Make sure the Robot HAT speaker is enabled. If you haven’t run any PiDog example code yet, enable it first:

  .. code-block:: bash

     robot_hat enable_speaker

  This only needs to be done once per boot. Running any PiDog example (which initializes ``Pidog()``) does this automatically.

* Ensure the volume is not muted and the I2S audio driver is installed.
* If there’s no sound, reconfigure I2S with the following:

.. code-block:: bash

    cd ~/robot-hat
    sudo bash i2samp.sh

* Restart the Raspberry Pi after running the script.

----

Q13: Why isn’t the microphone working?
--------------------------------------

* Check whether the system recognizes the microphone with:

.. code-block:: bash

    arecord -l

* Test the recording function with:

.. code-block:: bash

    arecord -D plughw:1,0 -f cd test.wav

* If no audio is recorded, select the correct input device in the audio settings or use ``alsamixer`` to adjust input volume.  
* Make sure no other process is occupying the audio input device.

----

Q14: Why isn’t the sound direction sensor working?
-------------------------------------------------------

* Ensure the sound direction sensor is connected to the correct SPI interface.  
* Check that all cables are securely connected and not reversed.  
* Make sure the power supply is stable and the sensor is not obstructed.  
* Reboot the device and try running the sensor example script again.

----

Q15: Why doesn't the touch sensor respond?
----------------------------------------------

* Ensure all touch sensor cables are firmly connected.  
* Remember: a **LOW** signal means the sensor is being touched.  
* Test the GPIO pin with ``gpio readall`` or Python code to confirm signal detection.  
* Re-check wiring and orientation.

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

Q17: Why is the LED board not lighting up or blinking incorrectly?
---------------------------------------------------------------------

* Verify the LED board is powered by **3.3V** and connected to the I2C port.
* Make sure **I2C is enabled** on the Raspberry Pi.
* Run the following command to check if the board is recognized:

.. code-block:: bash

    i2cdetect -y 1

* If no device appears, recheck wiring and restart the Pi.

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

Q19: How does PiDog get power?
------------------------------------------

* Use a 5V 3A Type-C power adapter.  
* Red light = charging, off = fully charged.  
* You can power it while charging.  
* If the indicator doesn’t light, charge it first.

----

