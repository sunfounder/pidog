.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

10. IMU読み取り
==================

6軸IMUモジュールを通じて、PiDogは斜面に立っているか、持ち上げられているかを判断することができます。

6軸IMUモジュールには、3軸加速度計と3軸ジャイロスコープが搭載されており、3方向の加速度と角速度を測定することができます。

.. note::

    モジュールを使用する前に、正しく組み立てられていることを確認してください。モジュールのラベルで、逆さまになっているかどうかを確認できます。

**加速度は次のように読み取ります：**

.. code-block:: python

   ax, ay, az = Pidog.accData

PiDogが水平に置かれている場合、x軸の加速度（つまりax）は重力加速度（1g）に近く、値は-16384に近くなります。
y軸とx軸の値は0に近いです。

**角速度を読み取るには次の方法を使用します**：

.. code-block:: python

   gx, gy, gz = my_dog.gyroData

PiDogが水平に置かれている場合、3つの値はすべて0に近いです。


**6軸モジュールの使用例をいくつか紹介します**：

1. リアルタイムの加速度、角速度を読み取る

  .. code-block:: python
  
      from pidog import Pidog
      import time
  
      my_dog = Pidog()
  
      my_dog.do_action("pushup", step_count=10, speed=20)
  
      while True:
          ax, ay, az = my_dog.accData
          gx, gy, gz = my_dog.gyroData
          print(f"accData: {ax/16384:.2f} g ,{ay/16384:.2f} g, {az/16384:.2f} g       gyroData: {gx} °/s, {gy} °/s, {gz} °/s")
          time.sleep(0.2)
          if my_dog.is_legs_done():
              break
  
      my_dog.stop_and_lie()
  
      my_dog.close()

2. PiDogの体の傾き角度を計算する

  .. code-block:: python
  
      from pidog import Pidog
      import time
      import math
  
      my_dog = Pidog()
  
      while True:
          ax, ay, az = my_dog.accData
          body_pitch = math.atan2(ay,ax)/math.pi*180%360-180
          print(f"Body Degree: {body_pitch:.2f} °" )
          time.sleep(0.2)
  
      my_dog.close()

3. 傾いている間、PiDogは目線を水平に保つ。

  .. code-block:: python
  
      from pidog import Pidog
      import time
      import math
  
      my_dog = Pidog()
  
      while True:
          ax, ay, az = my_dog.accData
          body_pitch = math.atan2(ay,ax)/math.pi*180%360-180
          my_dog.head_move([[0, 0, 0]], pitch_comp=-body_pitch, speed=80)
          time.sleep(0.2)
  
      my_dog.close()
