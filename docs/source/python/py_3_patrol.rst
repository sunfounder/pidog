.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

3. Patrol
==============

In this project, PiDog makes a vivid behavior: patrolling.

PiDog will walk forward, if there is an obstacle in front of it, it will stop and bark.


.. image:: img/py_3.gif

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 3_patrol.py

After running this example, PiDog will wag its tail, scan left and right, and walk forward.





**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``pidog\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python


    #!/usr/bin/env python3
    import time
    from pidog import Pidog
    from preset_actions import bark

    t = time.time()
    my_dog = Pidog()
    my_dog.do_action('stand', speed=80)
    my_dog.wait_all_done()
    time.sleep(.5)

    DANGER_DISTANCE = 15

    stand = my_dog.legs_angle_calculation([[0, 80], [0, 80], [30, 75], [30, 75]])

    def patrol():
        distance = round(my_dog.ultrasonic.read_distance(), 2)
        print(f"distance: {distance} cm", end="", flush=True)

        # danger
        if distance < DANGER_DISTANCE:
            print("\033[0;31m DANGER !\033[m")
            my_dog.body_stop()
            head_yaw = my_dog.head_current_angles[0]
            # my_dog.rgb_strip.set_mode('boom', 'red', bps=2)
            my_dog.rgb_strip.set_mode('bark', 'red', bps=2)
            my_dog.tail_move([[0]], speed=80)
            my_dog.legs_move([stand], speed=70)
            my_dog.wait_all_done()
            time.sleep(0.5)
            bark(my_dog, [head_yaw, 0, 0])

            while distance < DANGER_DISTANCE:
                distance = round(my_dog.ultrasonic.read_distance(), 2)
                if distance < DANGER_DISTANCE:
                    print(f"distance: {distance} cm \033[0;31m DANGER !\033[m")
                else:
                    print(f"distance: {distance} cm", end="", flush=True)
                time.sleep(0.01)
        # safe
        else:
            print("")
            my_dog.rgb_strip.set_mode('breath', 'white', bps=0.5)
            my_dog.do_action('forward', step_count=2, speed=98)
            my_dog.do_action('shake_head', step_count=1, speed=80)
            my_dog.do_action('wag_tail', step_count=5, speed=99)


    if __name__ == "__main__":
        try:
            while True:
                patrol()
                time.sleep(0.01)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()