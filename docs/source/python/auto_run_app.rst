3. Quickly Use the APP
=================================================

If you want to directly control PiDog through the APP after booting, please follow the steps below to install the autostart program.

1. Run the following commands:


.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/bin
    sudo bash pidog_app_install.sh


2. Restart PiDog.

3. Install `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ from **APP Store(iOS)** or **Google Play(Android)**.

4. Connect your phone (or tablet) to the hotspot network emitted by PiDog. Default SSID= ``pidog`` , PSK= ``12345678``

5. Open the ``Sunfounder Controller`` APP. Click the + icon to add a remote.

        .. image:: img/app1.png

#. There are preset controllers for some products in the Preset section. Here we choose PiDog.

        .. image:: img/app_preset-1.png

#. Give it a name, then click Confirm.

        .. image:: img/app_preset-2.png

#. You've now entered the remote control interface, which has several components for setting. Click the save button in the upper-right corner.

        .. image:: img/app_preset-3.png

#. Next, you need to connect PiDog with your device by pressing the connect button.

        .. image:: img/sc_connect.jpg

#. Wait a few seconds, MyDog(IP) will appear, click it to connect.

        .. image:: img/sc_mydog.jpg

    .. note::
        If the automatic connection can't find the device, please click Scan to search again, or click Manual to input PiDog's IP manually.

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

