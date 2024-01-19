9. PiDogのRGBストリップ
========================

PiDogの胸にはRGBストリップがあり、PiDogはこれを使って感情を表現することができます。

以下の関数を呼び出して制御することができます。

.. code-block:: python

    Pidog.rgb_strip.set_mode(style='breath', color='white', bps=1, brightness=1):

* ``style``: RGBストリップの照明表示モードで、以下の値が利用可能です。

  * ``breath``
  * ``boom``
  * ``bark``

* ``color`` : RGBストリップのライトの色を表示します。16進数のRGB値を入力することができます。例えば ``#a10a0a`` 、または以下の色名。

  * ``"white"``
  * ``"black"``
  * ``"white"``
  * ``"red"``
  * ``"yellow"``
  * ``"green"``
  * ``"blue"``
  * ``"cyan"``
  * ``"magenta"``
  * ``"pink"``

* ``brightness``: RGBストリップライトの表示の明るさを設定します。0から1までの浮動小数点値を入力することができます。例えば ``0.5``。

* ``delay``: Float, アニメーションの表示速度で、値が小さいほど変化が速くなります。

RGBストリップを無効にするには、以下のステートメントを使用します。

.. code-block:: python

    Pidog.rgb_strip.close()


使用例を以下に示します：


.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    while True:
        # style="breath", color="pink"
        my_dog.rgb_strip.set_mode(style="breath", color='pink')
        time.sleep(3)

        # style:"boom", color="#a10a0a"
        my_dog.rgb_strip.set_mode(style="bark", color="#a10a0a")
        time.sleep(3)

        # style:"boom", color="#a10a0a", brightness=0.5, bps=2.5
        my_dog.rgb_strip.set_mode(style="boom", color="#a10a0a", bps=2.5, brightness=0.5)
        time.sleep(3)

        # close
        my_dog.rgb_strip.close()
        time.sleep(2)

