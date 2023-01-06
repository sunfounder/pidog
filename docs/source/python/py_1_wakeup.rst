Wake Up
=======

This is PiDog's first project. It will wake your PiDog from a deep sleep.

.. image:: img/py_wakeup.gif


**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pidog/examples
    sudo python3 1_wakeup.py

After the code is executed, 
PiDog will perform the following actions in sequence: 

Stretch, twist, sit, wag its tail, pant.



**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``pidog\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from pidog import Pidog
    from time import sleep
    from preset_actions import pant
    from preset_actions import body_twisting

    my_dog = Pidog()
    sleep(0.5)


    def wake_up():
        my_dog.rgb_strip.set_mode(
            'breath', front_color='yellow', brightness=0.8, delay=0.095)
        my_dog.head_move([[0, 0, 30]]*2, immediately=True)
        my_dog.do_action('stretch', wait=True, speed=20)
        my_dog.wait_all_done()
        sleep(0.2)
        body_twisting(my_dog)
        my_dog.wait_all_done()
        sleep(0.2)
        my_dog.head_move([[0, 0, -30]], immediately=True, speed=90)
        my_dog.do_action('sit', wait=False, speed=50)
        my_dog.wait_legs_done()
        my_dog.do_action('wag_tail', step_count=10, wait=False, speed=100)
        my_dog.rgb_strip.set_mode('breath', front_color=[
                                245, 10, 10], brightness=0.8, delay=0.002)
        pant(my_dog, pitch_comp=-30)
        my_dog.wait_all_done()
        my_dog.rgb_strip.close()


    if __name__ == "__main__":
        try:
            wake_up()
        except KeyboardInterrupt:
            pass
        finally:
            my_dog.close()
