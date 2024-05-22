.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

3. Quick Play with the App
=================================================

Now that your PiDog is all set up and raring to go, this section is perfect for those eager to dive in and explore all its features in a jiffy. We'll walk you through the process of installing the app, seamlessly connecting your PiDog with your mobile device, and unleashing the myriad of fun functionalities it offers, all at your fingertips. By the end of this chapter, you'll be confidently navigating and playing with your PiDog using your device. Let's get started and immerse ourselves in the world of interactive robotics!

#. Install ``sunfounder-controller`` module.

    The robot-hat, vilib, and picar-x modules need to be installed first, for details see: :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Run the following commands:


    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/bin
        sudo bash pidog_app_install.sh


#. Restart PiDog.

#. Install `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ from **APP Store(iOS)** or **Google Play(Android)**.

#. Connect to ``pidog`` WLAN.

    Now, connect your mobile device to the local area network (LAN) broadcast by the PiDog. This way, your mobile device and the PiDog will be on the same network, which will facilitate communication between the applications on your mobile device and the PiDog.

    * Find ``pidog`` on the WLAN of the mobile phone (tablet), enter the password ``12345678`` and connect to it.

    * The default connection mode is AP mode. So after you connect, there will be a prompt telling you that there is no Internet access on this WLAN network, please choose to continue connecting.

        .. image:: img/app_no_internet.png




#. Open the ``Sunfounder Controller`` APP. Click the + icon to add a remote.

        .. image:: img/app1.png

#. Preset controllers are available for some products, here we choose **PiDog**. Give it a name, or simply tap **Confirm**.

        .. image:: img/app_preset.jpg


#. Once inside, the app will automatically search for the **Mydog**. After a moment, you will see a prompt saying “Connected Successfully.”

        .. image:: img/app_auto_connect.jpg

    .. note::

        * You can also manually click the |app_connect| button. Wait a few seconds, MyDog(IP) will appear, click it to connect.

            .. image:: img/sc_mydog.jpg

        * 
#. Run the Controller.

    * When the "Connected Successfully" prompt appears, tap the ▶ button in the upper-right corner.

    * The camera feed will appear on the APP, and now you can control your PiDog with these widgets.

        .. image:: img/sc_run.jpg

Here are the functions of the widgets.

* A: Detect the obstacle distance, that is, the reading of the ultrasonic module.
* C: Turn on/off face detection.
* D: Control PiDog's head tilt angle (tilt head).
* E: Sit.
* F: Stand.
* G: Lie down.
* I: Scratch PiDog's head.
* N: Bark.
* O: Wag tail.
* P: Pant.
* K: Control PiDog's movement (forward, backward, left, and right).
* Q: Controls the orientation of PiDog's head.
* J: Switch to voice control mode. It supports the following voice commands:

    * ``forward``
    * ``backward``
    * ``turn left``
    * ``turn right``
    * ``trot``
    * ``stop``
    * ``lie down``
    * ``stand up``
    * ``sit``
    * ``bark``
    * ``bark harder``
    * ``pant``
    * ``wag tail``
    * ``shake head``
    * ``stretch``
    * ``doze off``
    * ``push-up``
    * ``howling``
    * ``twist body``
    * ``scratch``
    * ``handshake``
    * ``high five``

APP Program Configuration
-----------------------------

You can input the following commands to modify the APP mode's settings.

.. code-block::

    pidog_app <OPTION> [input]

**OPTION**
    * ``-h`` ``help`` : help, show this message
    * ``start`` ``restart`` : restart pidog_app service
    * ``stop`` : stop pidog_app service
    * ``disable`` : disable auto-start app_controller program on bootstrap
    * ``enable`` : enable auto-start app_controller program on bootstrap
    * ``close_ap`` : close hotspot, disable auto-start hotspot on boot and switch to sta mode
    * ``open_ap`` : open hotspot, enable auto-start hotspot on boot
    * ``ssid`` : set the ssid (network name) of the hotspot
    * ``psk`` : set the password of the hotspot
    * ``country`` : set the country code of the hotspot

