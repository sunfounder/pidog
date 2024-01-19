4. 尾の動き
===================

以下はPiDogの尾を制御する関数です。この関数は :ref:`py_b2_leg_move` と似ています。

.. code-block:: python

    Pidog.tail_move(target_angles, immediately=True, speed=50)

* ``target_angles``: 1つのサーボ角度の配列（角度グループと呼ばれる）からなる二次元配列です。これらの角度グループは、尾のサーボの角度を制御するために使用されます。複数の角度グループが書かれている場合、実行されていない角度グループはキャッシュに保存されます。
* ``immediately``: 関数を呼び出すとき、このパラメータを ``True`` に設定すると、キャッシュはすぐにクリアされて新しく書かれた角度グループが実行されます。パラメータを ``False`` に設定すると、新しく書かれた角度グループが実行キューに追加されます。
* ``speed``: 角度グループの実行速度。

**PiDogの尾サーボ制御には、以下のサポート機能もあります**：

.. code-block:: python

    Pidog.is_tail_done()

実行される予定のバッファ内のすべての尾のアクションが完了しているかどうか

.. code-block:: python

    Pidog.wait_tail_done()

バッファ内のすべての尾のアクションが実行されるまで待ちます

.. code-block:: python

    Pidog.tail_stop()

バッファ内の足のすべての尾のアクションをクリアし、尾サーボを停止させます


**以下は一般的な使用例です**：

1. 10秒間尾を振る。

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    for _ in range(99):
        my_dog.tail_move([[30],[-30]], immediately=False, speed=30)

    # 10秒間維持
    time.sleep(10)

    my_dog.tail_stop()
