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

Q3: How do I run the first demo?
-------------------------------------

.. code-block:: bash

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

PiDog will wake up, sit down, and wag its tail.

----

Q4: What built-in actions and sounds are available?
------------------------------------------------------

* Actions: ``stand``, ``sit``, ``wag_tail``, ``trot``, etc.  
* Sounds: ``bark``, ``howling``, ``pant``, etc.

Run:

.. code-block:: bash

    sudo python3 2_function_demonstration.py

Enter numbers to trigger actions.

----

Q5: How does PiDog use sensors?
-------------------------------------

* **Ultrasonic**: Obstacle avoidance and patrol.  
* **Touch**: Front touch = alert; back touch = enjoyment.  
* **Sound Direction**: Responds to the direction of sound.

----

Q6: What AI features does PiDog support?
------------------------------------------------------

PiDog integrates with **TTS**, **STT**, and **LLM**:

* **TTS**: Espeak, Pico2Wave, Piper, OpenAI.  
* **STT**: Vosk (offline).  
* **LLM**: Ollama (local), OpenAI (online).

----

Q7: Do I need to calibrate the servos?
---------------------------------------------

Yes — **servo calibration is required for both Standard and V2 versions** to ensure stable movement and prevent damage.

**V2 Version**  

Press the **zeroing button** on the Robot HAT to automatically set all servos to 0°. This simplifies the zeroing process without running a script.

**Standard Version** 

Run the zeroing script **before installation**:

.. code-block:: bash

   cd ~/pidog/examples
   sudo python3 servo_zeroing.py

After installation (both versions), manually verify and fine-tune servo angles to align each limb with the calibration ruler to avoid instability, blocking, or mechanical stress and ensure smooth walking and accurate posture control.

----

Q8: Why is my PiDog walking unstably?
-----------------------------------------------

* Confirm all servos were installed at 0°.  
* Ensure servo angles match the calibration ruler (60°/90°).  
* Check that the battery is fully charged.  
* Tighten all servo screws.

----

Q9: Why is my camera not working?
--------------------------------------

* Ensure the camera cable is **firmly inserted** into the CSI interface and the black locking tab is secured.  
* **Power off** the Raspberry Pi before plugging or unplugging the camera to prevent damage.  
* Test the camera using ``libcamera-hello`` or ``raspistill`` to verify image output.  
* Re-seat the cable if it is loose or improperly installed.

----

Q10: Why isn’t the speaker working?
--------------------------------------

* Ensure the volume is not muted and the I2S audio driver is installed.  
* If there’s no sound, reconfigure I2S with the following:

.. code-block:: bash

    cd ~/robot-hat
    sudo bash i2samp.sh

* Restart the Raspberry Pi after running the script.

----

Q11: Why isn’t the microphone working?
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

Q12: Why isn’t the sound direction sensor working?
-------------------------------------------------------

* Ensure the sound direction sensor is connected to the correct SPI interface.  
* Check that all cables are securely connected and not reversed.  
* Make sure the power supply is stable and the sensor is not obstructed.  
* Reboot the device and try running the sensor example script again.

----

Q13: Why doesn't the touch sensor respond?
----------------------------------------------

* Ensure all touch sensor cables are firmly connected.  
* Remember: a **LOW** signal means the sensor is being touched.  
* Test the GPIO pin with ``gpio readall`` or Python code to confirm signal detection.  
* Re-check wiring and orientation.

----

Q14: Why is the LED board not lighting up or blinking incorrectly?
---------------------------------------------------------------------

* Verify the LED board is powered by **3.3V** and connected to the I2C port.  
* Make sure **I2C is enabled** on the Raspberry Pi.  
* Run the following command to check if the board is recognized:

.. code-block:: bash

    i2cdetect -y 1

* If no device appears, recheck wiring and restart the Pi.

----

Q15: How does PiDog get power?
------------------------------------------

* Use a 5V 3A Type-C power adapter.  
* Red light = charging, off = fully charged.  
* You can power it while charging.  
* If the indicator doesn’t light, charge it first.

----

