.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Ultraschallmodul
================================

.. image:: img/ultrasonic_pic.png
    :width: 400
    :align: center

* **TRIG**: Triggerimpulseingang
* **ECHO**: Echoimpulsausgang
* **GND**: Erdung
* **VCC**: 5V Versorgung

Dies ist der HC-SR04 Ultraschall-Entfernungssensor, der eine berührungslose Messung von 2 cm bis 400 cm mit einer Reichweitengenauigkeit von bis zu 3 mm bietet. Das Modul beinhaltet einen Ultraschallsender, einen Empfänger und eine Steuerschaltung.

Sie müssen nur 4 Pins anschließen: VCC (Strom), Trig (Auslöser), Echo (Empfang) und GND (Erdung), um es leicht für Ihre Messprojekte zu verwenden.

**Merkmale**

* Betriebsspannung: DC5V
* Arbeitsstrom: 16mA
* Arbeitsfrequenz: 40Hz
* Maximale Reichweite: 500cm
* Mindestreichweite: 2cm
* Trigger-Eingangssignal: 10uS TTL-Impuls
* Echo-Ausgangssignal: Eingangs-TTL-Pegelsignal und die Reichweite im Verhältnis
* Anschluss: XH2.54-4P
* Abmessungen: 46x20.5x15 mm

**Prinzip**

Die grundlegenden Prinzipien sind wie folgt:

* Verwendung von IO-Trigger für mindestens 10us Hochpegelsignal.
* Das Modul sendet einen 8-Zyklus-Burst von Ultraschall bei 40 kHz und erkennt, ob ein Pulssignal empfangen wird.
* Echo gibt ein Hochpegelsignal aus, wenn ein Signal zurückkommt; die Dauer des Hochpegels ist die Zeit von der Emission bis zur Rückkehr.
* Entfernung = (Hochpegelzeit x Schallgeschwindigkeit (340M/S)) / 2

    .. image:: img/ultrasonic_prin.jpg
        :width: 800

Formel: 

* us / 58 = Entfernung in Zentimetern
* us / 148 = Entfernung in Zoll
* Entfernung = Hochpegelzeit x Geschwindigkeit (340M/S) / 2

**Anwendungsnotee**

* Dieses Modul sollte nicht unter Strom angeschlossen werden, falls notwendig, sollte der GND des Moduls zuerst verbunden werden. Andernfalls beeinträchtigt es die Arbeit des Moduls.
* Die Fläche des zu messenden Objekts sollte mindestens 0,5 Quadratmeter betragen und so flach wie möglich sein. Andernfalls beeinträchtigt es die Ergebnisse.
