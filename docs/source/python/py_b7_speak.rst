7. PiDogが話す
==========================

PiDogは音を出すことができ、実際にはオーディオの一部を再生しています。

これらのオーディオは ``pidog\sounds`` のパスに保存されており、以下の関数を呼び出して再生することができます。

.. code-block:: python

   Pidog.speak(name)

* ``name``: ファイル名（接尾辞なし）、例えば ``"angry"`` 。 ``Pidog`` は以下のオーディオを提供しています。

  * ``"angry"``
  * ``"confused_1"``
  * ``"confused_2"``
  * ``"confused_3"``
  * ``"growl_1"``
  * ``"growl_2"``
  * ``"howling"``
  * ``"pant"``
  * ``"single_bark_1"``
  * ``"single_bark_2"``
  * ``"snoring"``
  * ``"woohoo"``

**使用例を以下に示します**：


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

    # change working directory
    abspath = os.path.abspath(os.path.dirname(__file__))
    # print(abspath)
    os.chdir(abspath)

    my_dog = Pidog()

    print("\033[033mNote that you need to run with \"sudo\", otherwise there may be no sound.\033[m")

    # my_dog.speak("angry")
    # time.sleep(2)

    for name in os.listdir('../sounds'):
        name = name.split('.')[0] # remove suffix
        print(name)
        my_dog.speak(name)
        # my_dog.speak(name, volume=50)
        time.sleep(3) # Note that the duration of each sound effect is different
    print("closing ...")
    my_dog.close()