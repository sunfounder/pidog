.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

2. Calibrate the PiDog
=============================

**Introduction**

Calibrating your PiDog is an essential step to ensure its stable and efficient operation. This process helps correct any imbalances or inaccuracies that might have arisen during assembly or from structural issues. Follow these steps carefully to ensure your PiDog walks steadily and performs as expected.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/calibrate_before.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>


But if the deviation angle is too big, you still have to go back to :ref:`py_servo_adjust` to set the servo angle to 0°, and then follow the instructions to reassemble the PiDog.

**Calibrate Video**

For a comprehensive guide, refer to the full calibration video. It provides a visual step-by-step process to accurately calibrate your PiDog.

.. note::

   The Pidog kit may come with a 90° or 60° ruler. Our calibration video uses the 90° ruler, but the 60° version follows a similar process. You can also refer to the detailed steps below.
 
.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/witCWeoHTdk?si=g8_RZDUkfjdwbLZu&amp;start=871&end=1160" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Steps**

The specific steps are as follows:

#. Put the PiDog on the base.

   .. image:: img/place-pidog.JPG

#. Navigate to the PiDog examples directory and run the ``0_calibration.py`` script.

   .. raw:: html

        <run></run>

   .. code-block::

        cd ~/pidog/examples
        sudo python3 0_calibration.py
        
#. Upon running the script, a user interface will appear in your terminal. Here, you need to select your calibration ruler (60° or 90°).If your kit has a 90° calibration ruler, select the first option; if it is a 60° one, select the second option.

    .. image:: img/CALI.slt.1.png

#. After selecting, you will enter the following interface:

.. image:: img/CALI.slt.2.png



90° Ruler
------------------------------


#. Position the **Calibration Ruler** (Acrylic C) as shown in the provided image. In the terminal, press ``1``, followed by ``w`` and ``s`` keys to align the edges as indicated in the image.

    .. image:: img/CALI-1.2.png

#. Reposition the **Calibration Ruler** (Acrylic C) as illustrated in the next image. Press ``2`` in the terminal, then use ``w`` and ``s`` to align the edges as shown.

    .. image:: img/CALI-2.2.png

#. Repeat the calibration process for the remaining servos (3 to 8). Ensure all four legs of the PiDog are calibrated.



60° Ruler
------------------------------

#. Position the **Calibration Ruler** (Acrylic C) as shown in the provided image. Place its long side on a level surface. In the terminal, press ``1``, followed by ``w`` and ``s`` keys to align the edges as indicated in the image.

    .. image:: img/CALI.60.1.JPG

#. Reposition the **Calibration Ruler** (Acrylic C) as illustrated in the next image. Press ``2`` in the terminal, then use ``w`` and ``s`` to align the edges as shown.

    .. image:: img/CALI.60.2.JPG

#. Repeat the calibration process for the remaining servos (3 to 8). Ensure all four legs of the PiDog are calibrated.


