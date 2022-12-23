Play PiDog with APP
===================


In this example, we will use SunFounder Controller APP to control PiDog.


You need to download the APP on your phone/tablet first, then connect to the hotspot sent by PiDog, and finally create your own remote control on SunFounder Controller to control PiDog.

**How to do?**


#. Install `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ from **APP Store(iOS)** or **Google Play(Android)**.


#. Run the Code。

    .. raw:: html

        <run></run>

    .. code-block::

        cd /home/pi/pidog/examples
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

    * Open the ``Sunfounder Controller`` APP. Click the + icon to add a remote.

        .. image:: img/app1.png
      
    * There are preset controllers for some products in the Preset section. Here we choose PiDog.

    ..[做不了图]

    * Give it a name, then click Confirm.

    ..[做不了图]

    * Now you have entered the inside of the remote control, which has several components for setting. Click the save button in the upper right corner.

    .. image:: img/app_edit.png

    * Next you need to connect PiDog with your device by pressing the connect button.

    .. image:: img/sc_connect.jpg

    * Wait a few seconds, MyDog(IP) will appear, click it to connect.

    .. image:: img/sc_mydog.jpg

    .. note::
        If the automatic connection cannot find the device, please click Scan to search again, or click Manual to input PiDog's IP manually.

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