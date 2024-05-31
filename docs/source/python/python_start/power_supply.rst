.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

3. Stromversorgung für den Raspberry Pi (Wichtig)
====================================================

Laden
-------------------

Stecken Sie das Batteriekabel ein. Anschließend stecken Sie das USB-C-Kabel ein, um die Batterie aufzuladen.
Sie müssen Ihr eigenes Ladegerät bereitstellen; wir empfehlen ein 5V 3A Ladegerät, oder Ihr üblicherweise verwendetes Smartphone-Ladegerät wird ausreichen.

.. image:: img/BTR_IMG_1096.png

.. note::
    Schließen Sie eine externe Typ-C-Stromquelle an den Typ-C-Anschluss auf dem Roboterhut an; er wird sofort mit dem Laden der Batterie beginnen, und eine rote Anzeigeleuchte wird aufleuchten.\
    Wenn die Batterie vollständig aufgeladen ist, wird das rote Licht automatisch erlöschen.


Einschalten
----------------------

Schalten Sie den Netzschalter ein. Die Power-Anzeigeleuchte und die Batteriestandanzeige werden aufleuchten.

.. image:: img/BTR_IMG_1097.png


Warten Sie einige Sekunden, und Sie werden einen leichten Piepton hören, der darauf hinweist, dass der Raspberry Pi erfolgreich gestartet wurde.

.. note::
    Wenn beide Batteriestandanzeigeleuchten ausgeschaltet sind, laden Sie bitte die Batterie auf.
    Wenn Sie längere Programmier- oder Debugging-Sitzungen benötigen, können Sie den Raspberry Pi operational halten, indem Sie gleichzeitig das USB-C-Kabel einstecken, um die Batterie aufzuladen.

18650 Batterie
-----------------------------------

.. image:: img/5pin_battery.jpg

* VCC: Batteriepositivpol, hier gibt es zwei Sätze von VCC und GND, um den Strom zu erhöhen und den Widerstand zu verringern.
* Mittel: Zur Spannungsausgleich zwischen den beiden Zellen und somit zum Schutz der Batterie.
* GND: Negativer Batteriepol.

Dies ist ein maßgefertigtes Batteriepaket von SunFounder, bestehend aus zwei 18650 Batterien mit einer Kapazität von 2000mAh. Der Stecker ist XH2.54 5P, der direkt nach dem Einsetzen in den Schild aufgeladen werden kann.

**Merkmale**

* Batterieladung: 5V/2A
* Batterieausgang: 5V/5A
* Batteriekapazität: 3.7V 2000mAh x 2
* Batterielebensdauer: 90 Minuten
* Batterieladezeit: 130 Minuten
* Stecker: XH2.54 5P
