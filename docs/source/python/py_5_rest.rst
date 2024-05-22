.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

5. 休息
=========

PiDogは地面でうとうとし、周りの音を聞くと混乱して立ち上がり、誰が自分を起こしたのかを見ます。

.. image:: img/py_5.gif

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 5_rest.py

プログラムが実行されると、PiDogは地面に降りて、うとうとするかのように頭と尻尾を振ります。
同時に、音の方向センサーモジュールが動作しています。PiDogが騒音を聞くと、立ち上がって周りを見回し、その後困惑した表情を見せます。
そして再びうとうとします。



**コード**

.. note::
    以下のコードを **変更/リセット/コピー/実行/停止** することができます。ただし、それにはまず ``pidog\examples`` のようなソースコードのパスに移動する必要があります。コードを変更した後、直接実行して効果を確認することができます。

.. raw:: html

    <run></run>

.. code-block:: python

    #!/usr/bin/env python3
    from pidog import Pidog
    from time import sleep
    from preset_actions import shake_head

    my_dog = Pidog()
    sleep(0.1)

    def loop_around(amplitude=60, interval=0.5, speed=100):
        my_dog.head_move([[amplitude,0,0]], immediately=True, speed=speed)
        my_dog.wait_all_done()
        sleep(interval)
        my_dog.head_move([[-amplitude,0,0]], immediately=True, speed=speed)
        my_dog.wait_all_done()
        sleep(interval)
        my_dog.head_move([[0,0,0]], immediately=True, speed=speed)
        my_dog.wait_all_done()

    def is_sound():
        if my_dog.ears.isdetected():
            direction = my_dog.ears.read()
            if direction != 0:
                return True
            else:
                return False
        else:
            return False

    def rest():
        my_dog.wait_all_done()
        my_dog.do_action('lie', speed=50)
        my_dog.wait_all_done()

        while True:
            # Sleeping
            my_dog.rgb_strip.set_mode('breath', 'pink', bps=0.3)
            my_dog.head_move([[0,0,-40]], immediately=True, speed=5)
            my_dog.do_action('doze_off', speed=92)
            # Cleanup sound detection
            sleep(1)
            is_sound()

            # keep sleeping
            while is_sound() is False:
                my_dog.do_action('doze_off', speed=92)
                sleep(0.2)

            # If heard anything, wake up
            # Set light to yellow and stand up
            my_dog.rgb_strip.set_mode('boom', 'yellow', bps=1)
            my_dog.body_stop()
            my_dog.do_action('stand', speed=90)
            my_dog.head_move([[0, 0, 0]], immediately=True, speed=80)
            my_dog.wait_all_done()
            # Look arround
            loop_around(60, 1, 60)
            sleep(0.5)
            # tilt head and being confused
            my_dog.speak('confused_3', volume=80)
            my_dog.do_action('tilting_head_left', speed=80)
            my_dog.wait_all_done()
            sleep(1.2)
            my_dog.head_move([[0, 0, -10]], immediately=True, speed=80)
            my_dog.wait_all_done()
            sleep(0.4)
            # Shake head , mean to ignore it
            shake_head(my_dog)
            sleep(0.2)

            # Lay down again
            my_dog.rgb_strip.set_mode('breath', 'pink', bps=1)
            my_dog.do_action('lie', speed=50)
            my_dog.wait_all_done()
            sleep(1)


    if __name__ == "__main__":
        try:
            rest()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            my_dog.close()