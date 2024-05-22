.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Robot HAT
=================

|link_robot_hat_v4| ist eine multifunktionale Erweiterungsplatine, die es ermöglicht, den Raspberry Pi schnell in einen Roboter zu verwandeln. 
Ein MCU ist an Bord, um die PWM-Ausgabe und ADC-Eingabe für den Raspberry Pi zu erweitern, 
sowie ein Motor-Treiber-Chip, ein I2S-Audio-Modul und ein Monolautsprecher. 
Zusätzlich zu den GPIOs, die vom Raspberry Pi selbst herausgeführt werden.

Es kommt auch mit einem Lautsprecher, 
der verwendet werden kann, um Hintergrundmusik, Soundeffekte und TTS-Funktionen zu spielen, um Ihr Projekt interessanter zu machen.

Akzeptiert 7-12V PH2.0 5pin-Stromversorgungseingang mit 2 Batterieanzeigen, 1 Ladeanzeige und 1 Stromversorgungsanzeige. 
Die Platine verfügt auch über eine benutzerfreundliche LED und einen Knopf, um schnell einige Effekte zu testen.

.. image:: img/O1902V40RobotHAT.png

**Power Port**
    * 7-12V PH2.0 3pin-Stromversorgungseingang.
    * Versorgt gleichzeitig den Raspberry Pi und den Robot HAT mit Strom.

**Power Switch**
    * Schaltet die Stromversorgung des Robot HAT ein/aus.
    * Wenn Sie Strom an den Stromversorgungsanschluss anschließen, bootet der Raspberry Pi. Sie müssen jedoch den Stromschalter auf ON stellen, um den Robot HAT zu aktivieren.

**Type-C USB Port**
    * Stecken Sie das Type-C-Kabel ein, um den Akku zu laden.
    * Gleichzeitig leuchtet die Ladeanzeige rot.
    * Wenn der Akku vollständig aufgeladen ist, schaltet sich die Ladeanzeige aus.
    * Wenn das USB-Kabel etwa 4 Stunden nach vollständiger Aufladung noch eingesteckt ist, blinkt die Ladeanzeige, um darauf hinzuweisen.

**Digital Pin**
    * 4-Kanal digitale Pins, D0-D3.

**ADC-Pin**
    * 4-Kanal ADC-Pins, A0-A3.

**PWM-Pin**
    * 12-Kanal PWM-Pins, P0-P11.

**Left/Right Motor Port**
    * 2-Kanal XH2.54 Motoranschlüsse.
    * Der linke Anschluss ist mit GPIO 4 und der rechte Anschluss mit GPIO 5 verbunden.

**I2C Pin and I2C Port**
    * **I2C-Pin**: P2.54 4-Pin-Schnittstelle.
    * **I2C-Anschluss**: SH1.0 4-Pin-Schnittstelle, kompatibel mit QWIIC und STEMMA QT. 
    * Diese I2C-Schnittstellen sind über GPIO2 (SDA) und GPIO3 (SCL) mit der I2C-Schnittstelle des Raspberry Pi verbunden.

**SPI-Pin**
    * P2.54 7-Pin SPI-Schnittstelle.

**UART-Pin**
    * P2.54 4-Pin-Schnittstelle.

**RST Button**
    * Die RST-Taste dient bei Verwendung von Ezblock als Taste, um das Ezblock-Programm neu zu starten. 
    * Wenn Ezblock nicht verwendet wird, hat die RST-Taste keine vordefinierte Funktion und kann vollständig nach Ihren Bedürfnissen angepasst werden.

**USR Button**
    * Die Funktionen der USR-Taste können durch Ihre Programmierung festgelegt werden. (Herunterdrücken führt zu einem Eingang ``0``; Loslassen erzeugt einen Eingang ``1``.)

**Battery Indicator**
    * Zwei LEDs leuchten auf, wenn die Spannung höher als 7,6V ist.
    * Eine LED leuchtet im Bereich von 7,15V bis 7,6V. 
    * Unter 7,15V schalten sich beide LEDs aus.

**Speaker and Speaker Port**
    * **Lautsprecher**: Dies ist ein 2030 Audio-Kammer-Lautsprecher.
    * **Lautsprecheranschluss**: Der Robot HAT ist mit einem integrierten I2S-Audioausgang sowie einem 2030 Audio-Kammer-Lautsprecher ausgestattet, der eine Mono-Soundausgabe bietet.
