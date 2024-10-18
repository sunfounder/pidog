.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

2. Kalibrierung des PiDog
=============================

**Einführung**

Die Kalibrierung Ihres PiDog ist ein wesentlicher Schritt, um einen stabilen und effizienten Betrieb sicherzustellen. Dieser Prozess hilft, Ungleichgewichte oder Ungenauigkeiten zu korrigieren, die während der Montage oder durch strukturelle Probleme entstanden sein könnten. Folgen Sie diesen Schritten sorgfältig, um sicherzustellen, dass Ihr PiDog stabil läuft und wie erwartet funktioniert.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/calibrate_before.mp4" type="video/mp4">
      Ihr Browser unterstützt das Video-Tag nicht.
   </video>


Wenn der Abweichungswinkel jedoch zu groß ist, müssen Sie trotzdem zu :ref:py_servo_adjust zurückkehren, um den Servo-Winkel auf 0° einzustellen und dann den Anweisungen folgen, um den PiDog neu zu montieren.

**Kalibrierungsvideo**

Für eine umfassende Anleitung sehen Sie sich das vollständige Kalibrierungsvideo an. Es bietet eine visuelle Schritt-für-Schritt-Anleitung, um Ihren PiDog genau zu kalibrieren.

.. note::

   Das Pidog-Kit kann mit einem 90°- oder 60°-Lineal geliefert werden. Unser Kalibrierungsvideo verwendet das 90°-Lineal, aber die 60°-Version folgt einem ähnlichen Prozess. Sie können sich auch die detaillierten Schritte unten ansehen.
 
.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/witCWeoHTdk?si=g8_RZDUkfjdwbLZu&amp;start=871&end=1160" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Schritte**

Die spezifischen Schritte sind wie folgt:

#. Setzen Sie den PiDog auf die Basis.

   .. image:: img/place-pidog.JPG

#. Navigieren Sie zum Beispielverzeichnis von PiDog und führen Sie das Skript `0_calibration.py` aus.

   .. raw:: html

        <run></run>

   .. code-block::

        cd ~/pidog/examples
        sudo python3 0_calibration.py
        
#. Nach dem Ausführen des Skripts erscheint eine Benutzeroberfläche im Terminal. Hier müssen Sie Ihr Kalibrierungslineal auswählen (60° oder 90°). Wenn Ihr Kit ein 90°-Kalibrierungslineal hat, wählen Sie die erste Option; wenn es ein 60°-Lineal ist, wählen Sie die zweite Option.

   .. image:: img/CALI.slt.1.png

#. Nach der Auswahl gelangen Sie zur folgenden Oberfläche:

   .. image:: img/CALI.slt.2.png



90°-Lineal
------------------------------


#. Positionieren Sie das **Kalibrierungslineal** (Acryl C) wie im bereitgestellten Bild gezeigt. Drücken Sie im Terminal `1`, gefolgt von den Tasten w und s, um die Kanten wie im Bild angegeben auszurichten.

   .. image:: img/CALI-1.2.png

#. Positionieren Sie das **Kalibrierungslineal** (Acryl C) neu, wie im nächsten Bild dargestellt. Drücken Sie im Terminal `2`, und verwenden Sie dann w und s, um die Kanten wie gezeigt auszurichten.

   .. image:: img/CALI-2.2.png

#. Wiederholen Sie den Kalibrierungsprozess für die verbleibenden Servos (3 bis 8). Stellen Sie sicher, dass alle vier Beine des PiDog kalibriert sind.



60°-Lineal
------------------------------

#. Positionieren Sie das **Kalibrierungslineal** (Acryl C) wie im bereitgestellten Bild gezeigt. Legen Sie die lange Seite auf eine ebene Fläche. Drücken Sie im Terminal `1`, gefolgt von den Tasten w und s, um die Kanten wie im Bild angegeben auszurichten.

   .. image:: img/CALI.60.1.JPG

#. Positionieren Sie das **Kalibrierungslineal** (Acryl C) neu, wie im nächsten Bild dargestellt. Drücken Sie im Terminal `2`, und verwenden Sie dann w und s, um die Kanten wie gezeigt auszurichten.

   .. image:: img/CALI.60.2.JPG

#. Wiederholen Sie den Kalibrierungsprozess für die verbleibenden Servos (3 bis 8). Stellen Sie sicher, dass alle vier Beine des PiDog kalibriert sind.
