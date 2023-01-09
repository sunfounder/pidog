.. _install_all_modules:


Install All the Modules
============================

Make sure you are connected to the Internet and update your system:

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    Python3 related packages must be installed if you are installing the Lite version OS.

    .. raw:: html

        <run></run>

    .. code-block::
    
        sudo apt install git python3-pip python3-setuptools python3-smbus


Install ``robot-hat`` module.


.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

.. note::
    Running ``setup.py`` will download some necessary components. You may fail to download due to network problems. You may need to download again at this time.
    In the following cases, enter ``Y`` and press Enter.
	
	.. image:: img/dowload_code.png

Then download the code and install ``vilib`` module.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

Then download the code and install ``pidog`` module.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone https://github.com/sunfounder/pidog.git
    cd pidog
    sudo python3 setup.py install

This step will take a little time, so please be patient.

Finally, you need to run the script ``i2samp.sh`` to install the components required by the i2s amplifier, otherwise the pislot will have no sound.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pidog
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

Type ``y`` and press ``Enter`` to continue running the script.

.. image:: img/i2s2.png

Type ``y`` and press ``Enter`` to run ``/dev/zero`` in the background.

.. image:: img/i2s3.png

Type ``y`` and press ``Enter`` to restart the machine.

.. note::
    If there is no sound after restarting, you may need to run the ``i2samp.sh`` script multiple times.
