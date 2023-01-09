Windows Users
=======================


If you're a Windows user, you can use Windows PowerShell to login Raspberry Pi remotely.

#. Press the ``windows`` + ``R`` shortcut key in your keyboard to open the **Run** program. Then type **powershell** in the input box. 

    .. image:: img/sp221221_135900.png
        :align: center

#. Check if your Raspberry Pi is on the same network by type in ``ping <hostname>.local``. 

    .. code-block::

        ping raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    * If terminal prompts ``Ping request could not find host <hostname>.local``, it is possible that the Raspberry Pi failed to connect to the network.lease check the network.
    * If you really can't ping ``<hostname>.local``, try to :ref:`get_ip`  and ``ping <IP address>`` instead. (e.g., ``ping 192.168.6.116``)
    * If multiple prompts like "Reply from <IP address>: bytes=32 time<1ms TTL=64" appear, it means your computer can access the Raspberry Pi.


#. Type in ``ssh <username>@<hostname>.local`` (or ``ssh <username>@<IP address>``).

    .. code-block::

        ssh pi@raspberrypi.local


#. The following message may appear.

    .. code-block::

        The authenticity of host 'raspberrypi.local (192.168.6.116)' can't be established.
        ECDSA key fingerprint is SHA256:7ggckKZ2EEgS76a557cddfxFNDOBBuzcJsgaqA/igz4.
        Are you sure you want to continue connecting (yes/no/[fingerprint])? 

    Input \"yes\".

#. Input the password you set before. (Mine is ``raspberry``.)

    .. note::
        When you input the password, the characters do not display on
        window accordingly, which is normal. What you need is to input the
        correct password.

#. We now get the Raspberry Pi connected and are ready to go to the next step.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center

Remote Desktop
------------------

If you're not satisfied with using the command window to access your Raspberry Pi, you can also use the remote desktop feature to easily manage files on your Raspberry Pi using a GUI.

Here we use `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_.

**Enable VNC service**

The VNC service has been installed in the system. By default, VNC is
disabled. You need to enable it in config.

#. Input the following command:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

    .. image:: img/image287.png
        :align: center

#. Choose **3** **Interfacing Options** by press the down arrow key on your keyboard, then press the **Enter** key.

    .. image:: img/image282.png
        :align: center

#. Then **P3 VNC**. 

    .. image:: img/image288.png
        :align: center

#. Use the arrow keys on the keyboard to select **<Yes>** -> **<OK>** -> **<Finish>** to complete the setup.

    .. image:: img/mac_vnc8.png
        :align: center

**Login to VNC**

#. You need to download and install the `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ on personal computer.

#.  Open it once the installation is complete. Then, enter the host name or IP address and press Enter.

    .. image:: img/vnc_viewer1.png
        :align: center

#. After entering your Raspberry Pi name and password, click **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Now you can see the desktop of the Raspberry Pi.

    .. image:: img/image294.png
        :align: center
