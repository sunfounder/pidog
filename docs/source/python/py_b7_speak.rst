7. PiDog 发声  
==========================

PiDog 可以发出声音，实际上是播放一段音频文件。

这些音频文件保存在 ``pidog\sounds`` 路径下，你可以调用以下函数进行播放：

.. code-block:: python

   Pidog.speak(name)

* ``name``：音频文件名（不带后缀），如 ``"angry"``。  
  ``Pidog`` 目前提供以下音效文件：

  * ``"angry"``          —— 愤怒
  * ``"confused_1"``     —— 疑惑1
  * ``"confused_2"``     —— 疑惑2
  * ``"confused_3"``     —— 疑惑3
  * ``"growl_1"``        —— 低吼1
  * ``"growl_2"``        —— 低吼2
  * ``"howling"``        —— 嚎叫
  * ``"pant"``           —— 喘气
  * ``"single_bark_1"``  —— 吠叫1
  * ``"single_bark_2"``  —— 吠叫2
  * ``"snoring"``        —— 打鼾
  * ``"woohoo"``         —— 欢呼

**以下是一个使用示例：**

.. code-block:: python

    # !/usr/bin/env python3
    ''' play sound effecfs
        Note that you need to run with "sudo"
    API:
        Pidog.speak(name, volume=100)
            play sound effecf in the file "../sounds"
            - name    str, file name of sound effect, no suffix required, eg: "angry"
            - volume  int, volume 0-100, default 100
    '''
    from pidog import Pidog
    import os
    import time

    # 切换工作目录
    abspath = os.path.abspath(os.path.dirname(__file__))
    # print(abspath)
    os.chdir(abspath)

    my_dog = Pidog()

    print("\033[033mNote that you need to run with \"sudo\", otherwise there may be no sound.\033[m")

    # my_dog.speak("angry")
    # time.sleep(2)

    for name in os.listdir('../sounds'):
        name = name.split('.')[0] # 去除文件后缀
        print(name)
        my_dog.speak(name)
        # my_dog.speak(name, volume=50)
        time.sleep(3) # 每段音效的时长不同，建议适当等待
    print("closing ...")
    my_dog.close()