10. 平衡力展示
==================

由于 PiDog 配备了六自由度惯性测量单元（6-DOF IMU 模块），它拥有出色的动态平衡能力。

在本示例中，你可以让 PiDog 在桌面上平稳行走。即使你抬起桌子的一侧形成缓坡，PiDog 依然能够稳定地在上面行走。

.. image:: img/py_10.gif

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 10_balance.py

程序运行后，终端上会显示一张虚拟键盘说明。
你可以通过按下以下按键，控制 PiDog 在斜坡上平稳行走：


.. list-table:: 
    :widths: 25 25
    :header-rows: 1

    * - 按键
      - 功能说明
    * -  W
      -  前进 
    * -  E
      -  站立 
    * -  A
      -  左转 
    * -  S
      -  后退 
    * -  D
      -  右转 
    * -  R
      -  每按一次，机身略微升高；多次按压可看到明显抬升效果     
    * -  F
      -  每按一次，机身略微降低；多次按压可看到明显下降效果


**代码**


请访问 |link_code_10_balance| 查看完整代码内容。
