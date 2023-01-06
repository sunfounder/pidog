Balance
=======


Because PiDog is equipped with a 6-DOF IMU module, it has a great sense of balance.

In this example, you can make PiDog walk smoothly on the table, even if you lift one side of the table, PiDog will walk smoothly on the gentle slope.


.. image:: img/py_10.gif

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pidog/examples
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

.. .. note::
..     You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``pidog\examples``. After modifying the code, you can run it directly to see the effect.

.. .. raw:: html

..     <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from time import sleep
    from pidog import Pidog
    from pidog.walk import Walk
    import readchar
    import threading
    import os

    my_dog = Pidog()

    sleep(0.5)

    usage = '''
    Pidog          Balance         Ctrl + C to Exit
    ...
    '''

    stand_coords = [[[0, 80], [0, 80], [0, 80], [0, 80]]]
    forward_coords = Walk(fb=Walk.FORWARD, lr=Walk.STRAIGHT).get_coords()
    backward_coords = Walk(fb=Walk.BACKWARD, lr=Walk.STRAIGHT).get_coords()
    turn_left_coords = Walk(fb=Walk.FORWARD, lr=Walk.LEFT).get_coords()
    turn_right_coords = Walk(fb=Walk.FORWARD, lr=Walk.RIGHT).get_coords()

    current_coords = stand_coords
    current_pose = {'x': 0, 'y': 0, 'z': 80}
    current_rpy = {'roll': 0, 'pitch': 0, 'yaw': 0}
    thread_start = True


    def move_thread():
        while thread_start:
            for coord in current_coords:
                # print(coord)
                my_dog.set_rpy(**current_rpy, pid=True)
                my_dog.set_pose(**current_pose)
                my_dog.set_legs(coord)
                angles = my_dog.pose2legs_angle()
                my_dog.legs.servo_move(angles, speed=98)


    t = threading.Thread(target=move_thread)


    def main():
        global current_coords, current_pose, current_rpy, thread_start
        my_dog.do_action('stand', speed=80)
        my_dog.wait_legs_done()
        t.start()

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(usage)
            key = readchar.readkey()
            if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
                thread_start = False
                break
            elif key == 'w':
                current_coords = forward_coords
            elif key == 's':
                current_coords = backward_coords
            elif key == 'a':
                current_coords = turn_left_coords
            elif key == 'd':
                current_coords = turn_right_coords
            elif key == 'e':
                current_coords = stand_coords
            elif key == 'r':
                current_pose['z'] += 1
                if current_pose['z'] > 90:
                    current_pose['z'] = 90
            elif key == 'f':
                current_pose['z'] -= 1
                if current_pose['z'] < 30:
                    current_pose['z'] = 30


    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            pass
        finally:
            t.join()
            my_dog.close()
