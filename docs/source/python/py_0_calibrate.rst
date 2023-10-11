2. Calibrate the PiDog
=============================
It is recommended that you calibrating the Pidog after assembling it. The servo angle will be tilted due to possible deviations during assembly or limitations of the servo itself, so you can get the servo to a perfect state by calibrating it, usually the calibration angle is -5~5°.

But if the deviation angle is too big, you still have to go back to :ref:`py_servo_adjust` to set the servo angle to 0°, and then follow the instructions to reassemble the Pidog.


Of course you can skip this chapter if you think the assembly is perfect and doesn't require calibration.


The specific steps are as follows:

1. Put the PiDog on the base.

.. image:: img/place-pidog.JPG

2. Run the ``0_calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 0_calibration.py
        
    After running the above code, you will see the following interface displayed in the terminal.

    .. image:: img/calibration_1.png


3. Place the square (Acrylic C) to the position shown in the picture. Press ``1`` in the terminal, then press ``w``, ``s`` to make the two edges marked in the figure coincide.

.. image:: img/CALI-1.2.png

4. Place the square (Acrylic C) to the position shown in the picture. Press ``2`` in the terminal, then press ``w``, ``s`` to make the two edges marked in the figure coincide.

.. image:: img/CALI-2.2.png

5. Configure the remaining ``3``, ``4``, ``5``, ``6``, ``7``, ``8`` servos in turn, and calibrate all four feet .