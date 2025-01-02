.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_b2_leg_move:

2. 脚の動き
=================

PiDogの脚の動きは、以下の関数によって実装されています。

.. code-block:: python

    Pidog.legs_move(target_angles, immediately=True, speed=50)

* ``target_angles``: 8つのサーボ角度の配列（角度グループと呼ばれる）からなる二次元配列です。これらの角度グループは、8つの足サーボの角度を制御するために使用されます。複数の角度グループが書かれている場合、実行されていない角度グループはキャッシュに保存されます。
* ``immediately``: 関数を呼び出すとき、このパラメータを ``True`` に設定すると、キャッシュはすぐにクリアされて新しく書かれた角度グループが実行されます。パラメータを ``False`` に設定すると、新しく書かれた角度グループが実行キューに追加されます。
* ``speed``: 角度グループの実行速度。

**いくつかの一般的な使用方法を以下に示します：**

1.  即座に行動をとる。

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # 半立ち
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)   


2. 実行キューにいくつかの角度グループを追加する。

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # 半立ち
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # 複数のアクション
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70],
                        [90, -30, -90, 30, 80, 70, -80, -70],
                        [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   

3. 10秒以内に繰り返し行う。

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # 半立ち
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], speed=50)  

    # 腕立て伏せの準備
    my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], immediately=False, speed=20)

    # 腕立て伏せ
    for _ in range(99):
        my_dog.legs_move([[90, -30, -90, 30, 80, 70, -80, -70],
                            [45, 35, -45, -35, 80, 70, -80, -70]],  immediately=False, speed=30)   

    # 10秒間維持
    time.sleep(10)

    # 停止して半立ち
    my_dog.legs_move([[45, 10, -45, -10, 45, 10, -45, -10]], immediately=True, speed=50)  


**PiDogの脚制御には、以下の関数も使用できます**：

.. code-block:: python

    Pidog.is_legs_done()
 
この関数は、キャッシュ内の角度グループが実行されたかどうかを判断するために使用されます。実行された場合は ``True`` を返し、そうでない場合は ``False`` を返します。

.. code-block:: python

    Pidog.wait_legs_done()

キャッシュ内の角度グループが実行されるまでプログラムを一時停止します。

.. code-block:: python

    Pidog.legs_stop() 

キャッシュ内の角度グループを空にします。
