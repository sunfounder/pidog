11. 音の方向検出
================================

PiDogには音の方向を検出するサウンド方向センサーモジュールが搭載されており、近くで手を叩くことでトリガーできます。

**このモジュールの使用は、次の関数を呼び出すことで簡単に行えます**。

.. code-block:: python

    Pidog.ears.isdetected()

音が検出されると ``True`` を返し、そうでなければ ``False`` を返します。

.. code-block:: python

    Pidog.ears.read()

この関数は音源の方向を返します。範囲は0から359で、音が前方から来る場合は0を、右側から来る場合は90を返します。

**このモジュールの使用例は以下の通りです：**

.. code-block:: python

    from pidog import Pidog

    my_dog = Pidog()

    while True:
        if my_dog.ears.isdetected():
            direction = my_dog.ears.read()
            print(f"sound direction: {direction}")
