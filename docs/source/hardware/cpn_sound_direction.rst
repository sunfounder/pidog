Sound Direction Sensor
=====================================

.. image:: img/cpn_sound.png
   :width: 400
   :align: center

Dies ist ein Modul zur Erkennung von Schallrichtungen. Es ist mit 3 Mikrofonen ausgestattet, die Schallquellen aus allen Richtungen erkennen können, und verfügt über einen TR16F064B, der zur Verarbeitung von Schallsignalen und zur Berechnung der Schallrichtung verwendet wird. Die kleinste Aufklärungseinheit dieses Moduls beträgt 20 Grad, und der Datenbereich liegt zwischen 0~355.

Datenübertragungsprozess: Der Hauptcontroller zieht den BUSY-Pin hoch, und TR16F064B beginnt mit der Überwachung der Richtung. Wenn 064B die Richtung erkennt, zieht es den BUSY-Pin nach unten;
Wenn der Hauptcontroller erkennt, dass BUSY niedrig ist, sendet er 16bit beliebige Daten an 064B (folgt der MSB-Übertragung) und akzeptiert 16bit Daten, die die von 064B verarbeiteten Schallrichtungsdaten sind.
Nach Abschluss zieht der Hauptcontroller den BUSY-Pin hoch, um die Richtung erneut zu erkennen.

**Spezifikationen**

* Stromversorgung: 3.3V
* Kommunikation: SPI
* Anschluss: PH2.0 7P
* Schallerkennungswinkelbereich 360°
* Spracherkennungswinkelgenauigkeit ~10°

**Pinbelegung**

* GND - Ground-Eingang
* VCC - 3.3V Stromversorgungseingang
* MOSI - SPI MOSI
* MISO - SPI MISO
* SCLK - SPI-Uhr
* CS - SPI Chip-Auswahl
* BUSY - Beschäftigungserkennung
