.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

3. パトロール
==============

このプロジェクトでは、PiDogが生き生きとした行動をとります：パトロール。

PiDogは前方に進みますが、前方に障害物がある場合は停止して吠えます。

.. image:: img/py_3.gif

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 3_patrol.py

この例を実行すると、PiDogは尻尾を振り、左右をスキャンし、前方に歩きます。


**コード**

.. note::
    以下のコードを **変更/リセット/コピー/実行/停止** することができます。ただし、それにはまず ``pidog\examples`` のようなソースコードのパスに移動する必要があります。コードを変更した後、直接実行して効果を確認することができます。

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