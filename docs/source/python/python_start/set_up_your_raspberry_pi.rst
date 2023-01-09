Set up Your Raspberry Pi
============================

If You Have a Screen
-------------------------

If you have a screen, it will be easy for you to operate on the
Raspberry Pi.

**Required Components**

================== =========================
Any Raspberry Pi   1 \* Power Adapter
1 \* Micro SD card 1 \* Screen Power Adapter
1 \* HDMI cable    1 \* Screen
1 \* Mouse         1 \* Keyboard
================== =========================

1. Insert the SD card you’ve set up with Raspberry Pi OS into the micro SD card slot on the underside of your Raspberry Pi.

#. Plug in the Mouse and Keyboard.

#. Connect the screen to Raspberry Pi’s HDMI port and make sure your screen is plugged into a wall socket and switched on.

    .. note::

        If you use a Raspberry Pi 4, you need to connect the screen to the HDMI0 (nearest the power in port).

#. Use the power adapter to power the Raspberry Pi. After a few seconds, the Raspberry Pi OS desktop will be displayed.

    .. image:: img/image20.png
        :align: center

If You Have No Screen
--------------------------

If you don't have a monitor, you can remotely log into your Raspberry Pi.

You can apply the SSH command to open the Raspberry Pi's Bash shell. Bash is the standard default shell for Linux. The shell itself is a command (instruction) when the user uses Unix/Linux. Most of what you need to do can be done through the shell.

If you're not satisfied with using the command window to access your Raspberry Pi, you can also use the remote desktop feature to easily manage files on your Raspberry Pi using a GUI.

See below for detailed tutorials for each system.


.. toctree::

    remote_macosx
    remote_windows
    remote_linux
