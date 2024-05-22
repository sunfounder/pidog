.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

2. PiDog kalibrieren
=============================

**Einführung**

Die Kalibrierung Ihres PiDog ist ein wesentlicher Schritt, um einen stabilen und effizienten Betrieb zu gewährleisten. Dieser Prozess hilft, eventuelle Ungleichgewichte oder Ungenauigkeiten zu korrigieren, die während der Montage oder durch strukturelle Probleme entstanden sein könnten. Folgen Sie diesen Schritten sorgfältig, um sicherzustellen, dass Ihr PiDog stabil läuft und wie erwartet funktioniert.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/calibrate_before.mp4" type="video/mp4">
      Ihr Browser unterstützt das Video-Tag nicht.
   </video>

Wenn der Abweichungswinkel jedoch zu groß ist, müssen Sie trotzdem zu :ref:`py_servo_adjust` zurückkehren, um den Servowinkel auf 0° einzustellen, und dann den Anweisungen folgen, um den PiDog erneut zusammenzubauen.

**Kalibrierungsvideo**

Für eine umfassende Anleitung beachten Sie das vollständige Kalibrierungsvideo. Es bietet einen visuellen Schritt-für-Schritt-Prozess, um Ihren PiDog genau zu kalibrieren.

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/witCWeoHTdk?si=g8_RZDUkfjdwbLZu&amp;start=871&end=1160" title="YouTube-Video-Player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Schritte**

Die spezifischen Schritte sind wie folgt:

#. Stellen Sie den PiDog auf die Basis.

    .. image:: img/place-pidog.JPG

#. Navigieren Sie zum PiDog-Beispielverzeichnis und führen Sie das Skript ``0_calibration.py`` aus.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 0_calibration.py
        
    Nach dem Ausführen des Skripts erscheint eine Benutzeroberfläche in Ihrem Terminal.

    .. image:: img/calibration_1.png

#. Positionieren Sie den **Kalibrierungslineal** (Acryl C) wie im bereitgestellten Bild gezeigt. Drücken Sie im Terminal ``1``, gefolgt von den Tasten ``w`` und ``s``, um die Kanten wie im Bild angezeigt auszurichten.

    .. image:: img/CALI-1.2.png

#. Positionieren Sie den **Kalibrierungslineal** (Acryl C) wie im nächsten Bild dargestellt. Drücken Sie ``2`` im Terminal und verwenden Sie ``w`` und ``s``, um die Kanten wie gezeigt auszurichten.

    .. image:: img/CALI-2.2.png

5. Wiederholen Sie den Kalibrierungsprozess für die verbleibenden Servos (3 bis 8). Stellen Sie sicher, dass alle vier Beine des PiDog kalibriert sind.
