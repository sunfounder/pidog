.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

6. Be Picked Up
===================

Try lifting your PiDog from the ground, PiDog will feel like it can fly, and it will cheer in a superman pose.

.. image:: img/py_6.gif

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 6_be_picked_up.py

After the program runs, the 6-DOF IMU Module will always calculate the acceleration in the vertical direction.
If PiDog is calculated to be in a state of weightlessness, PiDog assumes a superman pose and cheers.
Otherwise, consider PiDog to be on flat ground and make a standing pose.



**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``pidog\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep

    my_dog = Pidog()
    sleep(0.1)


    def fly():
        my_dog.rgb_strip.set_mode('boom', color='red', bps=3)
        my_dog.legs.servo_move([45, -45, 90, -80, 90, 90, -90, -90], speed=60)
        my_dog.do_action('wag_tail', step_count=10, speed=100)
        my_dog.speak('woohoo', volume=80)
        my_dog.wait_legs_done()
        sleep(1)

    def stand():
        my_dog.rgb_strip.set_mode('breath', color='green', bps=1)
        my_dog.do_action('stand', speed=60)
        my_dog.wait_legs_done()
        sleep(1)

    def be_picked_up():
        isUp = False
        upflag = False
        downflag = False

        stand()

        while True:
            ax = my_dog.accData[0]
            print('ax: %s, is up: %s' % (ax, isUp))

            # gravity : 1G = -16384
            if ax < -18000: # if down, acceleration is in the same direction as gravity, ax < -1G
                my_dog.body_stop()
                if upflag == False:
                    upflag = True
                if downflag == True:
                    isUp = False
                    downflag = False
                    stand()

            if ax > -13000: # if up, acceleration is the opposite of gravity, ax will > -1G
                my_dog.body_stop()
                if upflag == True:
                    isUp = True
                    upflag = False
                    fly()
                if downflag == False:
                    downflag = True

            sleep(0.02)


    if __name__ == "__main__":
        try:
            be_picked_up()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()