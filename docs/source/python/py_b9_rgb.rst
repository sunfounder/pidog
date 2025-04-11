
9. PiDog RGB 灯带
==========================

PiDog 胸前配有一条 RGB 灯带，可用于表达情绪。

你可以通过以下函数控制 RGB 灯带的显示效果：

.. code-block:: python

    Pidog.rgb_strip.set_mode(style='breath', color='white', bps=1, brightness=1):

* ``style``：RGB 灯带的显示模式，可用值如下：

  * ``breath`` （呼吸）
  * ``boom`` （爆闪）
  * ``bark`` （吠叫）

* ``color``：RGB 灯带显示的颜色，可以使用 16 位 RGB 色值（如 ``#a10a0a``），也可以使用以下颜色名称：

  * ``"white"`` 白色
  * ``"black"`` 黑色
  * ``"red"`` 红色
  * ``"yellow"`` 黄色
  * ``"green"`` 绿色
  * ``"blue"`` 蓝色
  * ``"cyan"`` 青色
  * ``"magenta"`` 品红
  * ``"pink"`` 粉色

* ``brightness``：灯光亮度，输入 0 到 1 之间的浮点数，例如 ``0.5``。

* ``bps``：动画播放速度，值越小变化越快。


使用以下指令可以关闭 RGB 灯带：

.. code-block:: python

    Pidog.rgb_strip.close()


以下是一些使用示例：

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    while True:
        # 呼吸模式，粉色
        my_dog.rgb_strip.set_mode(style="breath", color='pink')
        time.sleep(3)

        # 吠叫模式，自定义颜色
        my_dog.rgb_strip.set_mode(style="bark", color="#a10a0a")
        time.sleep(3)

        # 爆闪模式，设置亮度和速度
        my_dog.rgb_strip.set_mode(style="boom", color="#a10a0a", bps=2.5, brightness=0.5)
        time.sleep(3)

        # 关闭灯带
        my_dog.rgb_strip.close()
        time.sleep(2)

