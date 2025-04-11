
.. _py_ball_track:

13. 追踪红球
======================

PiDog 会安静地坐在原地。
当你在它面前放一个红球时，它会站起来，然后开始追逐这个红球。

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/bull_track.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 13_ball_track.py


运行代码后，PiDog 将启动摄像头。
您可以在浏览器中访问 ``http://+ PiDog's IP +/mjpg``（例如 ``http://192.168.18.138:9000/mjpg``）查看摄像头画面。


**代码**

.. note::
    您可以 **修改 / 重置 / 复制 / 运行 / 停止** 下方的代码。但在此之前，请确保您已经进入源码路径，例如 ``pidog\examples``。修改后即可直接运行查看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from vilib import Vilib
    from preset_actions import bark

    my_dog = Pidog()

    sleep(0.1)

    STEP = 0.5

    def delay(time):
        my_dog.wait_legs_done()
        my_dog.wait_head_done()
        sleep(time)

    def ball_track():
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=True, web=True)
        Vilib.color_detect_switch(True)
        sleep(0.2)
        print('start')
        yaw = 0
        roll = 0
        pitch = 0
        flag = False
        direction = 0

        my_dog.do_action('stand', speed=50)
        my_dog.head_move([[yaw, 0, pitch]], immediately=True, speed=80)
        delay(0.5)

        while True:

            ball_x = Vilib.detect_obj_parameter['color_x'] - 320
            ball_y = Vilib.detect_obj_parameter['color_y'] - 240
            width = Vilib.detect_obj_parameter['color_w']

            if ball_x > 15 and yaw > -80:
                yaw -= STEP

            elif ball_x < -15 and yaw < 80:
                yaw += STEP

            if ball_y > 25:
                pitch -= STEP
                if pitch < - 40:
                    pitch = -40
            elif ball_y < -25:
                pitch += STEP
                if pitch > 20:
                    pitch = 20

            print(f"yaw: {yaw}, pitch: {pitch}, width: {width}")

            my_dog.head_move([[yaw, 0, pitch]], immediately=True, speed=100)
            if width == 0:
                pitch = 0
                yaw = 0
            elif width < 300:
                if my_dog.is_legs_done():
                    if yaw < -30:
                        print("turn right")
                        my_dog.do_action('turn_right', speed=98)
                    elif yaw > 30:
                        print("turn left")
                        my_dog.do_action('turn_left', speed=98)
                    else:
                        my_dog.do_action('forward', speed=98)
            sleep(0.02)


    if __name__ == "__main__":
        try:
            ball_track()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            Vilib.camera_close()
            my_dog.close()
