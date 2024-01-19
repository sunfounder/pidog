1. PiDogの初期化
============================

PiDogの機能は ``Pidog`` クラスに記述されており、このクラスのプロトタイプは以下のようになります。

.. code-block:: python

    Class: Pidog()

    __init__(leg_pins=DEFAULT_LEGS_PINS, 
            head_pins=DEFAULT_HEAD_PINS,
            tail_pin=DEFAULT_TAIL_PIN,
            leg_init_angles=None,
            head_init_angles=None,
            tail_init_angle=None)


PiDogは、以下に示すようないくつかの方法でインスタンス化する必要があります。

1. 初期化の最も単純なステップは以下の通りです。

.. code-block:: python

    # Pidogクラスをインポート
    from pidog import Pidog

    # PiDogのインスタンスを作成
    my_dog = Pidog()

2. PiDogには12個のサーボがあり、インスタンス化する際に初期化することができます。

.. code-block:: python

    # Pidogクラスをインポート
    from pidog import Pidog

    # カスタム初期化サーボ角度でPiDogのインスタンスを作成
    my_dog = Pidog(leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )

``Pidog`` クラスでは、サーボは3つのグループに分かれています。

* ``leg_init_angles``: この配列では、8つの値が8つのサーボの角度を決定し、制御するサーボ（ピン番号）は ``2, 3, 7, 8, 0, 1, 10, 11`` です。展開図からこれらのサーボの位置がわかります。

* ``head_init_angles``: 3つの値の配列で、PiDogの頭部のヨー、ロール、ピッチサーボ（ ``番号 4, 6, 5`` ）を制御し、体のヨー、ロール、ピッチ、または偏向に反応します。

* ``tail_init_angle``: この配列には1つの値のみがあり、尾サーボ（ ``9`` ）を制御するために専用です。


3. ``Pidog`` は、サーボの順番が異なる場合にロボットをインスタンス化する際にサーボのシリアル番号を再定義することができます。

.. code-block:: python

    # Pidogクラスをインポート
    from pidog import Pidog

    # カスタム初期化ピン＆サーボ角度でPiDogのインスタンスを作成
    my_dog = Pidog(leg_pins=[2, 3, 7, 8, 0, 1, 10, 11], 
                    head_pins=[4, 6, 5],
                    tail_pin=[9],
                    leg_init_angles = [25, 25, -25, -25, 70, -45, -70, 45],
                    head_init_angles = [0, 0, -25],
                    tail_init_angle= [0]
                )
