12. Play PiDog with APP
=============================


In this example, we will use SunFounder Controller APP to control PiDog.


You need to download the APP on your phone/tablet first, then connect to the hotspot sent by PiDog, and finally create your own remote control on SunFounder Controller to control PiDog.

Control Pidog with app
----------------------------


#. Install `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ from **APP Store(iOS)** or **Google Play(Android)**.

#. Install ``sunfounder-controller`` module.

    The ``robot-hat``, ``vilib``, and ``picar-x`` modules need to be installed first, for details see: :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Run the Code.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 12_app_control.py

    After the code runs, you will see the following prompt, which means your PiDog has successfully started network communication.

    .. code-block:: 

        Running on: http://192.168.18.138:9000/mjpg

        * Serving Flask app "vilib.vilib" (lazy loading)
        * Environment: development
        * Debug mode: off
        * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)       

#. Connect ``PiDog`` and ``Sunfounder Controller``.

    * Connect your tablet/phone to the WLAN where PiDog is located.

    * Open the ``Sunfounder Controller`` APP. Click the + icon to add a controller.

        .. image:: img/app1.png
      

    * Preset controllers are available for some products, here we choose **PiDog**. Give it a name, or simply tap **Confirm**.

        .. image:: img/app_preset.jpg


    * Once inside, the app will automatically search for the **Mydog**. After a moment, you will see a prompt saying “Connected Successfully.”

        .. image:: img/app_auto_connect.jpg

    .. note::

        * You can also manually click the |app_connect| button. Wait a few seconds, MyDog(IP) will appear, click it to connect.

            .. image:: img/sc_mydog.jpg

#. Run the Controller.

    * When the "Connected Successfully" prompt appears, tap the ▶ button in the upper right corner.

    * The picture taken by the camera will appear on the APP, and now you can control your PiDog with these widgets.

        .. image:: img/sc_run.jpg
    

Here are the functions of the widgets.

* A: Detect the obstacle distance, that is, the reading of the ultrasonic module.
* C: Turn on/off face detection.
* D: Control PiDog's head tilt angle (tilt head).
* E: Sit.
* F: Stand.
* G: Lie.
* I: Scratch PiDog's head.
* N: Bark.
* O: Wag tail.
* P: Pant.
* K: Control PiDog's movement (forward, backward, left and right).
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

Autostart on Boot
-----------------
When controlling Pidog via the APP, you wouldn't want to first log into the Raspberry Pi and keep ``12_app_control.py`` running before connecting with the APP.

There's a more streamlined approach. You can set Pidog to automatically run ``12_app_control.py`` every time it's powered on. After this, you can directly connect to Pidog using the APP and control your robotic dog with ease.

How to set this up?

#. Execute the following commands to install and configure the ``pidog_app`` application and set up WiFi for Pidog.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/bin
        sudo bash pidog_app_install.sh

#. At the end, input ``y`` to reboot Pidog.

    .. image:: img/auto_start.png

#. From then on, you can simply power on Pidog and control it directly using the APP.

.. warning::

    If you wish to run other scripts, first execute ``pidog_app disable`` to turn off the autostart feature.


APP Program Configuration
-----------------------------

You can input the following commands to modify the APP mode's settings.

.. code-block::

    pidog_app <OPTION> [input]

**OPTION**
    * ``-h`` ``help`` : help, show this message
    * ``start`` ``restart`` : restart ``pidog_app`` service
    * ``stop`` : stop ``pidog_app`` service
    * ``disable`` : disable auto-start ``app_controller`` program on bootstrap
    * ``enable`` : enable auto-start ``app_controller`` program on bootstrap
    * ``close_ap`` : close hotspot, disable auto-start hotspot on boot and switch to sta mode
    * ``open_ap`` : open hotspot, enable auto-start hotspot on boot
    * ``ssid`` : set the ssid (network name) of the hotspot
    * ``psk`` : set the password of the hotspot
    * ``country`` : set the country code of the hotspot

