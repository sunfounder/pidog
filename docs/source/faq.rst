.. note:: 

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Enthusiasten aus.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu erweitern.
    - **Exklusive Vorschauen**: Erhalte frühen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

FAQ
===========================

Q1: Zum Fehler "pinctrl: not found"
-------------------------------------------------------------------

Wenn du den Fehler siehst:

.. code-block::

    pinctrl: not found

bedeutet das, dass du das Bullseye-System installiert hast. Es wird empfohlen, stattdessen das **Bookworm-System** zu installieren.

Q2: Über das Batterieladegerät
-------------------------------------------------------------------

Um die Batterie aufzuladen, schließen Sie einfach ein 5V/2A Type-C-Netzteil an den Stromanschluss des Robot Hat an. Es ist nicht erforderlich, den Netzschalter des Robot Hat während des Ladevorgangs einzuschalten.
Das Gerät kann auch während des Ladevorgangs verwendet werden.

.. image:: img/robot_hat_pic.png
    :align: center
    :width: 500

Während des Ladevorgangs wird die Eingangsleistung durch den Ladechip verstärkt, um die Batterie zu laden und gleichzeitig den DC-DC-Wandler für die externe Nutzung zu versorgen. Die Ladeleistung beträgt dabei ungefähr 10W.
Wenn der externe Stromverbrauch über einen längeren Zeitraum hoch bleibt, kann die Batterie die Stromversorgung ergänzen, ähnlich wie bei der Nutzung eines Telefons während des Ladevorgangs. Beachten Sie jedoch die Kapazität der Batterie, um ein vollständiges Entladen während gleichzeitiger Nutzung und Aufladung zu vermeiden.
