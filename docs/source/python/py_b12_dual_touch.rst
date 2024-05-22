.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!


12. Streicheln Sie den Kopf des PiDog
=================================================

Der Touch-Schalter am Kopf des PiDog kann erkennen, wie Sie ihn berühren. Sie können die folgenden Funktionen aufrufen, um ihn zu verwenden.

.. code-block:: python

   Pidog.dual_touch.read()

* Berühren Sie das Modul von links nach rechts (von vorne nach hinten für die Ausrichtung des PiDog), es wird ``"LS"`` zurückgeben.
* Berühren Sie das Modul von rechts nach links, es wird ``"RS"`` zurückgeben.
* Berühren Sie das Modul, wenn die linke Seite des Moduls berührt wird, wird es ``"L"`` zurückgeben.
* Wenn die rechte Seite des Moduls berührt wird, wird es ``"R"`` zurückgeben.
* Wenn das Modul nicht berührt wird, wird es ``"N"`` zurückgeben.

**Hier ist ein Beispiel für seine Verwendung:**

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()
    while True:
        touch_status = my_dog.dual_touch.read()
        print(f"Berührungsstatus: {touch_status}")
        time.sleep(0.5)


