10. Balance
=============


Because PiDog is equipped with a 6-DOF IMU module, it has a great sense of balance.

In this example, you can make PiDog walk smoothly on the table, even if you lift one side of the table, PiDog will walk smoothly on the gentle slope.


.. image:: img/py_10.gif

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 10_balance.py

After the program is running, you will see a printed keyboard on the terminal.
You can control PiDog to walk smoothly on the ramp by typing the below keys.


.. list-table:: 
    :widths: 25 25
    :header-rows: 1

    * - Keys
      - Function
    * -  W
      -  Forward 
    * -  E
      -  Stand 
    * -  A
      -  Turn Left 
    * -  S
      -  Backward 
    * -  D
      -  Turn Right 
    * -  R
      -  Up     
    * -  F
      -  Down 
    

**Code**


Please find the code in |link_code_10_balance|.
