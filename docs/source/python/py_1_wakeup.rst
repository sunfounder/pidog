1. Wake Up
===============

This is PiDog's first project. It will wake your PiDog from a deep sleep.

.. image:: img/py_wakeup.gif


**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

After the code is executed, 
PiDog will perform the following actions in sequence: 

Stretch, twist, sit, wag its tail, pant.



**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``pidog\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import pant
    from preset_actions import body_twisting

    my_dog = Pidog(head_init_angles=[0, 0, -30])
    sleep(1)

    def wake_up():
        # stretch
        my_dog.rgb_strip.set_mode('listen', color='yellow', bps=0.6, brightness=0.8)
        my_dog.do_action('stretch', speed=50)
        my_dog.head_move([[0, 0, 30]]*2, immediately=True)
        my_dog.wait_all_done()
        sleep(0.2)
        body_twisting(my_dog)
        my_dog.wait_all_done()
        sleep(0.5)
        my_dog.head_move([[0, 0, -30]], immediately=True, speed=90)
        # sit and wag_tail
        my_dog.do_action('sit', speed=25)
        my_dog.wait_legs_done()
        my_dog.do_action('wag_tail', step_count=10, speed=100)
        my_dog.rgb_strip.set_mode('breath', color=[245, 10, 10], bps=2.5, brightness=0.8)
        pant(my_dog, pitch_comp=-30, volume=80)
        my_dog.wait_all_done()
        # hold
        my_dog.do_action('wag_tail', step_count=10, speed=30)
        my_dog.rgb_strip.set_mode('breath', 'pink', bps=0.5)
        while True:
            sleep(1)

    if __name__ == "__main__":
        try:
            wake_up()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()
