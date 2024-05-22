.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

9. PiDog RGB-Streifen
========================

PiDog hat einen RGB-Streifen auf seiner Brust, den PiDog verwenden kann, um Emotionen auszudrücken.

Sie können die folgende Funktion aufrufen, um ihn zu steuern.

.. code-block:: python

  Pidog.rgb_strip.set_mode(style='atmen', color='weiß', bps=1, brightness=1):

* ``style``: Der Beleuchtungsanzeigemodus des RGB-Streifens, die folgenden Werte stehen zur Verfügung:

* ``breath``
* ``boom``
* ``bark``

* ``color``: Die Lichter des RGB-Streifens zeigen die Farben an. Sie können 16-Bit RGB-Werte eingeben, wie z.B. ``#a10a0a``, oder die folgenden Farbnamen verwenden.

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

* ``brightness``: Helligkeit der RGB-Streifenlichter, Sie können einen Gleitkommawert von 0 bis 1 eingeben, z.B. ``0,5``.

* ``delay``: Float, Geschwindigkeit der Animationsanzeige, je kleiner der Wert, desto schneller die Änderung.

Verwenden Sie die folgende Anweisung, um den RGB-Streifen auszuschalten.

.. code-block:: python

  Pidog.rgb_strip.close()

Hier sind Beispiele für ihre Verwendung:

.. code-block:: python

  python
  Copy code
  from pidog import Pidog
  import time

  my_dog = Pidog()

  while True:
      # style="atmen", color="pink"
      my_dog.rgb_strip.set_mode(style="atmen", color='pink')
      time.sleep(3)

      # style:"boom", color="#a10a0a"
      my_dog.rgb_strip.set_mode(style="bellen", color="#a10a0a")
      time.sleep(3)

      # style:"boom", color="#a10a0a", brightness=0,5, bps=2,5
      my_dog.rgb_strip.set_mode(style="boom", color="#a10a0a", bps=2,5, brightness=0,5)
      time.sleep(3)

      # schließen
      my_dog.rgb_strip.close()
      time.sleep(2)