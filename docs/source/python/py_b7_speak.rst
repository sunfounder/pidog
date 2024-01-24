7. PiDog spricht
==========================

PiDog kann Geräusche machen, es spielt eigentlich eine Audiodatei ab.

Diese Audiodateien sind unter dem Pfad ``pidog\sounds`` gespeichert, und Sie können die folgende Funktion aufrufen, um sie abzuspielen.

.. code-block:: python

   Pidog.speak(name)

* ``name``: Dateiname (ohne Suffix), wie z.B. ``"angry"``. ``Pidog`` bietet die folgenden Audiodateien.

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

**Hier ist ein Beispiel für die Nutzung:**

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

    # Arbeitsverzeichnis ändern
    abspath = os.path.abspath(os.path.dirname(__file__))
    # print(abspath)
    os.chdir(abspath)

    my_dog = Pidog()

    print("\033[033mBeachten Sie, dass Sie mit \"sudo\" ausführen müssen, sonst gibt es möglicherweise keinen Ton.\033[m")

    # my_dog.speak("angry")
    # time.sleep(2)

    for name in os.listdir('../sounds'):
        name = name.split('.')[0] # Suffix entfernen
        print(name)
        my_dog.speak(name)
        # my_dog.speak(name, volume=50)
        time.sleep(3) # Beachten Sie, dass die Dauer jedes Soundeffekts unterschiedlich ist
    print("Schließe ...")
    my_dog.close()
