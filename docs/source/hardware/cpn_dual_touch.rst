.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Dualer Berührungssensor
==========================

.. image:: img/cpn_touchswitch.png
   :width: 200
   :align: center

Dualer Berührungssensor, basierend auf zwei ttp223 Berührungssensoren.
Wenn ein Berührungssignal erkannt wird, wird das entsprechende Pin-Niveau auf niedrig gezogen.

TTP223 ist ein IC zur Erkennung von Berührungspads, das 1 Berührungstaste bietet.
Der Berührungserkennungs-IC ist speziell dafür konzipiert, die traditionellen direkten Tasten mit verschiedenen Pad-Größen zu ersetzen.
Es zeichnet sich durch geringen Stromverbrauch und einen weiten Betriebsspannungsbereich aus.

**Spezifikationen**

* Stromversorgung: 2,0V~5,5V
* Signalausgang: Digitales Signal
* Anschluss: SH1.0 4P

**Pinbelegung**

* GND - Ground-Eingang
* VCC - Stromversorgungseingang
* SIG1 - Berührungssignal 1, niedriges Niveau bedeutet Berührung
* SIG2 - Berührungssignal 2, niedriges Niveau bedeutet Berührung
