Download and Run the Code
============================

We can download the files by using ``git clone`` in the command line.

Install ``robot-hat`` module first.

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

    cd /home/pi/picrawler
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

Type ``y`` and press ``Enter`` to continue running the script.

.. image:: img/i2s2.png

Type ``y`` and press ``Enter`` to run ``/dev/zero`` in the background.

.. image:: img/i2s3.png

Type ``y`` and press ``Enter`` to restart the machine.

.. note::
    If there is no sound after restarting, you may need to run the ``i2samp.sh`` script multiple times.
