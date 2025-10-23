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

Die Kalibrierung Ihres PiDog ist ein entscheidender Schritt, um einen stabilen und effizienten Betrieb sicherzustellen. Durch diesen Vorgang werden Ungleichgewichte oder Ungenauigkeiten korrigiert, die durch Montage- oder Strukturfehler entstehen können. Bitte folgen Sie den Anweisungen sorgfältig, um sicherzustellen, dass Ihr PiDog reibungslos läuft und wie erwartet funktioniert.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/calibrate_before.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

Wenn der Abweichungswinkel jedoch zu groß ist, kehren Sie zu :ref:`py_servo_adjust` zurück, setzen Sie den Servowinkel auf 0° und montieren Sie den PiDog gemäß der Anleitung erneut.

**Kalibrierungsvideo**

Für eine detaillierte Anleitung sehen Sie sich das vollständige Kalibrierungsvideo an. Das Video zeigt Schritt für Schritt anschaulich, wie Sie Ihren PiDog präzise kalibrieren.

.. note::

   Im PiDog-Bausatz ist ein Kalibrierungslineal mit 90° oder 60° enthalten. In unserem Video wird ein 90°-Lineal verwendet, aber der Vorgang für 60° ist weitgehend derselbe. Sie können sich auch die untenstehenden detaillierten Bild- und Textanweisungen ansehen.
    
    .. image:: img/cali_ruler.png
         :width: 400
         :align: center

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/witCWeoHTdk?si=g8_RZDUkfjdwbLZu&amp;start=871&end=1160" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Schritte**

Gehen Sie wie folgt vor:

#. Platzieren Sie den PiDog auf einer ebenen Fläche.

   .. image:: img/place-pidog.JPG

#. Wechseln Sie in das Beispielverzeichnis des PiDog und führen Sie das Skript ``0_calibration.py`` aus.

   .. raw:: html

        <run></run>

   .. code-block::

        cd ~/pidog/examples
        sudo python3 0_calibration.py
        
#. Nach dem Start des Skripts erscheint ein interaktives Terminalmenü. Wählen Sie je nach Typ Ihres Kalibrierungslineals: Wählen Sie die erste Option für 90° oder die zweite für 60°.

    .. image:: img/CALI.slt.1.png

#. Danach gelangen Sie zur folgenden Kalibrierungsoberfläche:

    .. image:: img/CALI.slt.2.png

**Wenn Sie ein 60°-Kalibrierungslineal verwenden**

#. Platzieren Sie das **Kalibrierungslineal (Acryl-C-Platte)** wie gezeigt, mit der langen Seite auf der horizontalen Fläche. Drücken Sie im Terminal ``1`` und verwenden Sie die Tasten ``w`` und ``s``, um die Kante auszurichten.

    .. image:: img/CALI.60.1.JPG

#. Platzieren Sie das **Kalibrierungslineal** wie unten gezeigt neu. Drücken Sie im Terminal ``2`` und justieren Sie erneut mit ``w`` und ``s``.

    .. image:: img/CALI.60.2.JPG

#. Wiederholen Sie diesen Kalibriervorgang für Servos 3 bis 8, um sicherzustellen, dass alle vier Beine des PiDog korrekt kalibriert sind.

**Wenn Sie ein 90°-Kalibrierungslineal verwenden**

#. Platzieren Sie das **Kalibrierungslineal (Acryl-C-Platte)** wie auf dem Bild gezeigt. Drücken Sie im Terminal ``1`` und verwenden Sie ``w`` und ``s``, um die Kante korrekt auszurichten.

    .. image:: img/CALI-1.2.png

#. Platzieren Sie das **Kalibrierungslineal** erneut wie abgebildet. Drücken Sie im Terminal ``2`` und justieren Sie mit ``w`` und ``s``.

    .. image:: img/CALI-2.2.png

#. Wiederholen Sie diesen Kalibriervorgang für Servos 3 bis 8, um sicherzustellen, dass alle vier Beine des PiDog korrekt kalibriert sind.

**Kalibrierung abschließen**

- Nachdem alle Servos kalibriert wurden, können Sie die Geh- oder Bewegungsbeispiele des PiDog erneut ausführen, um die Stabilität zu überprüfen.  
- Wenn eine Abweichung festgestellt wird, können Sie das Kalibrierungsprogramm erneut aufrufen, um Feinjustierungen vorzunehmen.  
- Es wird dringend empfohlen, diesen Schritt nach der ersten Montage durchzuführen, um einen stabilen Betrieb sicherzustellen.

.. tip::

   Um eine erneute Kalibrierung zu vermeiden, können Sie nach Abschluss der Kalibrierung die Servowinkel notieren oder die Konfigurationsdatei exportieren, um sie später schnell wiederherzustellen.
