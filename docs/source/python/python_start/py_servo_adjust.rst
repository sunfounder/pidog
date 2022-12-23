Servo Adjust
===============

To ensure that the servo has been properly set to 0°, first insert the rocker arm into the servo shaft and then gently rotate the rocker arm to a different angle.

.. image:: img/servo_arm.png

Follow the instructions on the assembly foldout, insert the battery holder cable and turn the power switch to the ON. Wait for 1-2 minutes, there will be a sound to indicate that the Raspberry Pi boots successfully.

.. image:: img/power_on_robothat.png

Now, run ``servo_zeroing.py`` in the ``examples/`` folder.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pidog/examples
    sudo python3 servo_zeroing.py


.. note::
    If you get an error, try re-enabling the Raspberry Pi's I2C port, see: :ref:`i2c_config`.

Next, plug the servo cable into the **any PWM port**.

.. image:: img/pwm_connect.png

At this point you will see the servo arm rotate to a specific position (0°). If the servo arm does not return to 0°, press the RST button to restart the Robot HAT.

Now you can continue the installation as instructed on the assembly foldout.

.. note::

    * Do not unplug this servo cable before fixing it with the servo screw, you can unplug it after fixing it.
    * Do not rotate the servo while it is powered on to avoid damage; if the servo shaft is not inserted at the right angle, pull the servo out and reinsert it.
    * Before assembling each servo, you need to plug the servo cable into PWM pin and turn on the power to set its angle to 0°.

