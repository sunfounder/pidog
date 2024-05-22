.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

3. 頭の動き
================

PiDogの頭部サーボの制御は、以下の関数によって実装されています。

.. code-block:: python

    Pidog.head_move(target_yrps, roll_comp=0, pitch_comp=0, immediately=True, speed=50)

* ``target_angles``: 3つのサーボ角度の配列（角度グループと呼ばれる）からなる二次元配列です。これらの角度グループは、頭部の3つのサーボの角度を制御するために使用されます。複数の角度グループが書かれている場合、実行されていない角度グループはキャッシュに保存されます。
* ``roll_comp``: ロール軸に対する角度補正を提供します。
* ``pitch_comp``: ピッチ軸に対する角度補正を提供します。
* ``immediately``: 関数を呼び出すとき、このパラメータを ``True`` に設定すると、キャッシュはすぐにクリアされて新しく書かれた角度グループが実行されます。パラメータを ``False`` に設定すると、新しく書かれた角度グループが実行キューに追加されます。
* ``speed``: 角度グループの実行速度。

**PiDogの頭部サーボ制御には、以下のサポート機能もあります**：

.. code-block:: python

    Pidog.is_head_done()

実行される予定のバッファ内のすべての頭部アクションが完了しているかどうか

.. code-block:: python

    Pidog.wait_head_done()

バッファ内のすべての頭部アクションが実行されるまで待ちます

.. code-block:: python

    Pidog.head_stop()

バッファ内の足のすべての頭部アクションをクリアし、頭部サーボを停止させます

**以下は一般的な使用例です**：

1. 5回うなずく。

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(5):
        my_dog.head_move([[0, 0, 30],[0, 0, -30]], speed=80)
        my_dog.wait_head_done()
        time.sleep(0.5)

2. 10秒間頭を振る。

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.head_move([[30, 0, 0],[-30, 0, 0]], immediately=False, speed=30)

    # 10秒間維持
    time.sleep(10)

    my_dog.head_move([[0, 0, 0]], immediately=True, speed=80)

3. 座っているか半立ちしているかにかかわらず、PiDogは頭を振るときに頭を水平に保ちます。

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    # アクションリスト
    shake_head = [[30, 0, 0],[-30, 0, 0]]
    half_stand_leg = [[45, 10, -45, -10, 45, 10, -45, -10]]
    sit_leg = [[30, 60, -30, -60, 80, -45, -80, 45]]

    while True:
        # 半立ちで頭を振る
        my_dog.legs_move(half_stand_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=0, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)

        # 座って頭を振る
        my_dog.legs_move(sit_leg, speed=30)
        for _ in range(5):
            my_dog.head_move(shake_head, pitch_comp=-30, speed=50)
        my_dog.wait_head_done()
        time.sleep(0.5)
