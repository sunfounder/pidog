2. PiDogのキャリブレーション
=============================

**イントロダクション**

PiDogをキャリブレーションすることは、安定して効率的に動作させるために不可欠なステップです。このプロセスは、組み立て中や構造上の問題から生じる可能性のある不均衡や不正確さを修正するのに役立ちます。PiDogがしっかりと歩き、期待通りに動作するように、これらの手順に注意深く従ってください。

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/calibrate_before.mp4" type="video/mp4">
      お使いのブラウザはビデオタグをサポートしていません。
   </video>


しかし、偏差角が大きすぎる場合は、 :ref:`py_servo_adjust` に戻ってサーボの角度を0°に設定し、その後の指示に従ってPiDogを再組み立てる必要があります。

**キャリブレーションビデオ**

包括的なガイドについては、完全なキャリブレーションビデオを参照してください。これには、PiDogを正確にキャリブレーションするための視覚的なステップバイステッププロセスが含まれています。

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/witCWeoHTdk?si=g8_RZDUkfjdwbLZu&amp;start=871&end=1160" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**手順**

具体的な手順は以下の通りです：

#. PiDogをベースに置きます。

    .. image:: img/place-pidog.JPG

#. PiDogのexamplesディレクトリに移動し、 ``0_calibration.py`` スクリプトを実行します。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 0_calibration.py
        
    スクリプトを実行すると、ターミナルにユーザーインターフェースが表示されます。

    .. image:: img/calibration_1.png

#. 提供された画像に示されているように、 **キャリブレーションルーラー** （アクリルC）を配置します。ターミナルで ``1`` を押し、続いて ``w`` と ``s`` キーを使って画像に示されているように端を揃えます。

    .. image:: img/CALI-1.2.png

#. 次の画像に示されたように、 **キャリブレーションルーラー** （アクリルC）を再配置します。ターミナルで ``2`` を押し、続いて ``w`` と ``s`` を使って端を揃えます。

    .. image:: img/CALI-2.2.png

5. 残りのサーボ（3〜8）に対してキャリブレーションプロセスを繰り返します。PiDogの4本の脚すべてがキャリブレーションされていることを確認してください。
