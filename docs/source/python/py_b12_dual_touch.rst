12. PiDogの頭を撫でる
=========================

PiDogの頭にあるタッチスイッチは、どのように触れるかを検出することができます。以下の関数を呼び出して使用できます。

.. code-block:: python

   Pidog.dual_touch.read()

* モジュールを左から右へ（PiDogの向きにとって前から後ろへ）触れると、 ``"LS"`` を返します。
* モジュールを右から左へ触れると、 ``"RS"`` を返します。
* モジュールの左側を触れると、 ``"L"`` を返します。
* モジュールの右側を触れると、 ``"R"`` を返します。
* モジュールが触れられていない場合は、 ``"N"`` を返します。

**使用例を以下に示します**：


.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()
    while True:
        touch_status = my_dog.dual_touch.read()
        print(f"touch_status: {touch_status}")
        time.sleep(0.5)

