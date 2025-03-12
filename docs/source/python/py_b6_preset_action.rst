.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

6. Do Preset Action
=======================

Some commonly used actions have been pre-written in PiDog's library.
You can call the following function to make PiDog do these actions directly.

.. code-block:: python

    Pidog.do_action(action_name, step_count=1, speed=50)

* ``action_name`` : Action name, the following strings can be written.

    * ``"sit"``
    * ``"half_sit"``
    * ``"stand"``
    * ``"lie"``
    * ``"lie_with_hands_out"``
    * ``"forward"``
    * ``"backward"``
    * ``"turn_left"``
    * ``"turn_right"``
    * ``"trot"``
    * ``"stretch"``
    * ``"push_up"``
    * ``"doze_off"``
    * ``"nod_lethargy"``
    * ``"shake_head"``
    * ``"tilting_head_left"``
    * ``"tilting_head_right"``
    * ``"tilting_head"``
    * ``"head_bark"``
    * ``"head_up_down"``
    * ``"wag_tail"``

* ``step_count`` : How many times to perform this action.
* ``speed`` : How fast to perform the action.

**Here is an example of usage:**

1. Do ten push-ups, then sit on the floor and act cute.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # pushup
        my_dog.do_action("half_sit", speed=60)
        my_dog.do_action("push_up", step_count=10, speed=60)
        my_dog.wait_all_done()
        
        # act cute
        my_dog.do_action("sit", speed=60)
        my_dog.do_action("wag_tail", step_count=100,speed=90)
        my_dog.do_action("tilting_head", step_count=5, speed=20)
        my_dog.wait_head_done()
        
        my_dog.stop_and_lie()

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        print("closing ...")
        my_dog.close()    
