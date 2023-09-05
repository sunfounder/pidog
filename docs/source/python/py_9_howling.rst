9. Howling
===============


PiDog is not only a cute puppy, but also a mighty dog. Come hear it howl!


.. image:: img/py_9.gif

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 9_howling.py

After the program runs, PiDog will sit on the ground and howl.



**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``pidog\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import howling

    my_dog = Pidog()

    sleep(0.5)


    def main():
        my_dog.do_action('sit', speed=50)
        my_dog.head_move([[0, 0, 0]], pitch_comp=-40, immediately=True, speed=80)
        sleep(0.5)
        while True:
            howling(my_dog)


    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()

