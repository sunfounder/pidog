7. 人脸跟踪
======================

在本项目中，PiDog 将安静地坐在原地。当你鼓掌时，它会转头看你，并在识别到你后和你打招呼。

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/face_track.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 7_face_track.py

代码运行后，PiDog 会启动摄像头并打开人脸检测功能。
你可以在浏览器中访问 ``http://+ PiDog's IP +/mjpg``（例如： ``http://192.168.18.138:9000/mjpg`` ）以查看摄像头画面。

接着，PiDog 将坐下并启用声音方向传感器模块来监听你的鼓掌方向。
当 PiDog 听到掌声（或其他响声）时，它会转头朝声源方向寻找你。

如果它检测到人脸（识别到目标），就会摇尾巴并发出汪汪叫声向你问好。



**代码**

.. note::
    你可以对以下代码进行 **修改/重置/复制/运行/停止**。请确保进入源码路径（如 ``pidog\examples``）后进行操作。修改后可直接运行查看效果。

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

    def face_track():
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=True, web=True)
        Vilib.human_detect_switch(True)
        sleep(0.2)
        print('start')
        yaw = 0
        roll = 0
        pitch = 0
        flag = False
        direction = 0

        my_dog.do_action('sit', speed=50)
        my_dog.head_move([[yaw, 0, pitch]], pitch_comp=-40, immediately=True, speed=80)
        my_dog.wait_all_done()
        sleep(0.5)
        # 清除伺服器动作造成的声音干扰
        if my_dog.ears.isdetected():    
            direction = my_dog.ears.read()

        while True:
            if flag == False:
                my_dog.rgb_strip.set_mode('breath', 'pink', bps=1)
            # 如果检测到声音，则转向
            if my_dog.ears.isdetected():
                flag = False
                direction = my_dog.ears.read()
                pitch = 0
                if direction > 0 and direction < 160:
                    yaw = -direction
                    if yaw < -80:
                        yaw = -80
                elif direction > 200 and direction < 360:
                    yaw = 360 - direction
                    if yaw > 80:
                        yaw = 80
                my_dog.head_move([[yaw, 0, pitch]], pitch_comp=-40, immediately=True, speed=80)
                my_dog.wait_head_done()
                sleep(0.05)

            ex = Vilib.detect_obj_parameter['human_x'] - 320
            ey = Vilib.detect_obj_parameter['human_y'] - 240
            people = Vilib.detect_obj_parameter['human_n']

            # 如果识别到人脸，向其打招呼
            if people > 0 and flag == False:
                flag = True
                my_dog.do_action('wag_tail', step_count=2, speed=100)
                bark(my_dog, [yaw, 0, 0], pitch_comp=-40, volume=80)
                if my_dog.ears.isdetected():
                    direction = my_dog.ears.read()

            if ex > 15 and yaw > -80:
                yaw -= 0.5 * int(ex/30.0+0.5)

            elif ex < -15 and yaw < 80:
                yaw += 0.5 * int(-ex/30.0+0.5)

            if ey > 25:
                pitch -= 1*int(ey/50+0.5)
                if pitch < - 30:
                    pitch = -30
            elif ey < -25:
                pitch += 1*int(-ey/50+0.5)
                if pitch > 30:
                    pitch = 30

            print('direction: %s |number: %s | ex, ey: %s, %s | yrp: %s, %s, %s '
                % (direction, people, ex, ey, round(yaw, 2), round(roll, 2), round(pitch, 2)),
                end='\r',
                flush=True,
                )
            my_dog.head_move([[yaw, 0, pitch]], pitch_comp=-40, immediately=True, speed=100)
            sleep(0.05)


    if __name__ == "__main__":
        try:
            face_track()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            Vilib.camera_close()
            my_dog.close()
