.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_servo_adjust:

7. Servoeinstellung (Wichtig)
===========================================

Der Winkelbereich des Servos liegt zwischen -90° und 90°, aber der in der Fabrik eingestellte Winkel ist zufällig, vielleicht 0°, vielleicht 45°. Wenn wir ihn mit einem solchen Winkel direkt montieren, führt das zu einem chaotischen Zustand, nachdem der Roboter den Code ausführt, oder schlimmer noch, es kann dazu führen, dass der Servo blockiert und durchbrennt.

Daher müssen wir zuerst alle Servowinkel auf 0° einstellen und sie dann montieren, damit der Servowinkel in der Mitte ist, egal in welche Richtung er sich dreht.

#. Um sicherzustellen, dass der Servo korrekt auf 0° eingestellt wurde, stecken Sie zuerst den Servoarm auf die Servoachse und drehen Sie dann vorsichtig den Schwenkarm in einen anderen Winkel. Dieser Servoarm dient nur dazu, Ihnen deutlich zu zeigen, dass sich der Servo dreht.

    .. image:: img/servo_arm.png
        :align: center


#. Führen Sie jetzt ``servo_zeroing.py`` im Ordner ``examples/`` aus.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 servo_zeroing.py


    .. note::
        Wenn ein Fehler auftritt, versuchen Sie, den I2C-Port des Raspberry Pi erneut zu aktivieren, siehe: :ref:`i2c_spi_config`.

#. Stecken Sie als nächstes das Servokabel in den P11-Anschluss, wie folgt. Gleichzeitig werden Sie sehen, dass sich der Servoarm in eine Position dreht (Dies ist die 0°-Position, die eine zufällige Position sein kann und möglicherweise nicht vertikal oder parallel ist.).

    .. image:: img/servo_pin11.jpg


#. Entfernen Sie jetzt den Servoarm und stellen Sie sicher, dass das Servokabel angeschlossen bleibt, und schalten Sie den Strom nicht aus. Fahren Sie dann mit der Montage gemäß der Papieranleitung fort.

.. note::

    * Ziehen Sie dieses Servokabel nicht ab, bevor es mit der Servoschraube befestigt ist; Sie können es abziehen, nachdem es befestigt wurde.
    * Drehen Sie den Servo nicht, während er eingeschaltet ist, um Schäden zu vermeiden. Wenn die Servoachse nicht im richtigen Winkel eingesteckt ist, ziehen Sie den Servo heraus und stecken Sie ihn erneut ein.
    * Bevor Sie jeden Servo montieren, müssen Sie das Servokabel in den PWM-Pin stecken und den Strom einschalten, um seinen Winkel auf 0° zu setzen.
