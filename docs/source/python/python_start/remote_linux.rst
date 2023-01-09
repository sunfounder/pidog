Linux /Unix Users
==========================


#. Go to **Applications**->\ **Utilities**, find the **Terminal**, and open it.

    .. image:: img/image21.png
        :align: center

#. Check if your Raspberry Pi is on the same network by type in ``ping <hostname>.local``. 

    .. code-block::

        ping raspberrypi.local

    .. image:: img/mac-ping.png
        :width: 550
        :align: center

    * If terminal prompts ``ping: cannot resolve <hostname>.local``, it is possible that the Raspberry Pi failed to connect to the network. Please check the network.
    * If you really can't ping ``<hostname>.local``, try to :ref:`get_ip`  and ``ping <IP address>`` instead. (e.g., ``ping 192.168.6.116``)
    * If multiple prompts like ``64 bytes from <IP address>: icmp_seq=0 ttl=64 time=0.464 ms`` appear, it means your computer can access the Raspberry Pi.




#. Type in ``ssh <username>@<hostname>.local`` (or ``ssh <username>@<IP address>``).

    .. code-block::

        ssh pi@raspberrypi.local

#. The following message may appear.

    .. code-block::

        The authenticity of host 'raspberrypi.local (192.168.6.116)' can't be established.
        ECDSA key fingerprint is SHA256:7ggckKZ2EEgS76a557cddfxFNDOBBuzcJsgaqA/igz4.
        Are you sure you want to continue connecting (yes/no/[fingerprint])? 

    Input \"yes\".

    .. image:: img/mac-ssh-login.png
        :width: 550
        :align: center


#. Input the password you set before. (Mine is ``raspberry``.)


#. We now get the Raspberry Pi connected and are ready to go to the nextstep.

    .. image:: img/mac-ssh-terminal.png
        :width: 550
        :align: center