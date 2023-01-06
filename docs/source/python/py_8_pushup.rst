Push Up
=======

PiDog is an exercise-loving robot that will do push-ups with you.

.. image:: img/py_8.gif

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pidog/examples
    sudo python3 8_pushup.py

After the program runs, PiDog will perform a plank, then cycle through push-ups and barks.



**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``pidog\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import pushup, bark

    my_dog = Pidog()

    sleep(0.5)


    def main():
        my_dog.legs_move([[45, -25, -45, 25, 80, 70, -80, -70]], speed=90)
        my_dog.head_move([[0, 0, -20]], speed=90)
        my_dog.wait_all_done()
        sleep(0.2)
        bark(my_dog, [0, 0, -20])
        sleep(0.1)
        bark(my_dog, [0, 0, -20])

        sleep(1)

        while True:
            pushup(my_dog)
            bark(my_dog, [0, 0, -40])
            sleep(0.4)


    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            my_dog.close()
