.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

5. すべてのアクションの停止
===================================

これまでの章で、PiDogのサーボ制御が3つのスレッドに分かれていることがわかります。
これにより、PiDogの頭部と体が同時に動くことができ、たとえ2行のコードであっても実行できます。

**ここでは、3つのサーボスレッドと共に動作するいくつかの関数を紹介します**：

.. code-block:: python

    Pidog.wait_all_done()
    
足のアクションバッファ、頭部バッファ、尾バッファのすべてのアクションが実行されるのを待ちます

.. code-block:: python

    Pidog.body_stop()
    
足、頭部、尾のすべてのアクションを停止します

.. code-block:: python

    Pidog.stop_and_lie()
    
足、頭部、尾のすべてのアクションを停止し、その後 ``横になる`` ポーズにリセットします

.. code-block:: python

    Pidog.close()
    
すべてのアクションを停止し、 ``横になる`` ポーズにリセットし、プログラムを終了するときに通常使用されるすべてのスレッドを閉じます


**以下は一般的な使用例です：**




.. code-block:: python
    :emphasize-lines: 10,36,45

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # pushup prepare
        my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], speed=30)
        my_dog.head_move([[0, 0, 0]], pitch_comp=-10, speed=80) 
        my_dog.wait_all_done() # wait all the actions to be done
        time.sleep(0.5)

        # pushup 
        leg_pushup_action = [
            [90, -30, -90, 30, 80, 70, -80, -70],
            [45, 35, -45, -35, 80, 70, -80, -70],       
        ]
        head_pushup_action = [
            [0, 0, -30],
            [0, 0, 20],
        ]
        
        # fill action buffers
        for _ in range(50):
            my_dog.legs_move(leg_pushup_action, immediately=False, speed=50)
            my_dog.head_move(head_pushup_action, pitch_comp=-10, immediately=False, speed=50)
        
        # show buffer length
        print(f"legs buffer length (start): {len(my_dog.legs_action_buffer)}")
        
        # keep 5 second & show buffer length
        time.sleep(5)
        print(f"legs buffer length (5s): {len(my_dog.legs_action_buffer)}")
        
        # stop action & show buffer length
        my_dog.stop_and_lie()
        print(f"legs buffer length (stop): {len(my_dog.legs_action_buffer)}")

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        print("closing ...")
        my_dog.close() # close all the servo threads