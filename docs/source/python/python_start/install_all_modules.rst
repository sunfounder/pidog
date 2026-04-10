.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _install_all_modules:

Install All the Modules(Important)
==============================================

.. note::

    Python3 related packages must be installed if you are installing the Lite version OS.

    .. raw:: html

        <run></run>

    .. code-block::
    
        sudo apt install git python3-pip python3-setuptools python3-smbus


#. Install ``robot-hat`` module.


   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
       cd robot-hat
       sudo python3 install.py
   
#. Install ``vilib`` module.

   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone https://github.com/sunfounder/vilib.git
       cd vilib
       sudo python3 install.py

#. Install ``pidog`` module.

   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone https://github.com/sunfounder/pidog.git --depth 1
       cd pidog
       sudo pip3 install . --break

   This step will take a little time, so please be patient.

#. Run the script ``i2samp.sh``.

   Finally, you need to run the script ``i2samp.sh`` to install the components required by the i2s amplifier, otherwise the robot will have no sound.
   
   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/robot-hat
       sudo bash i2samp.sh
       
   Type y and press Enter three times to continue the script, start /dev/zero in the background, and then restart the machine.
   
   .. note::
       If there is no sound after restarting, you may need to run the ``i2samp.sh`` script multiple times.
