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
==========

F1: Welche Versionen von PiDog gibt es?
------------------------------------------------------

PiDog ist in zwei Versionen erhältlich: **Standard** und **V2**.

* **Standard-Version**: Kompatibel mit Raspberry Pi 3B+/4B/Zero 2W, **nicht** kompatibel mit Raspberry Pi 5.  
* **V2-Version**: Kompatibel mit Raspberry Pi 3/4/5 und Zero 2W. Diese Version verbessert die Robot-HAT- und Servotreiber-Schaltungen und bietet eine bessere Stromversorgung für den Pi 5.  
* **Stromversorgung**: Die V2-Version verfügt über ein verbessertes Powermanagement für Anwendungen mit höherem Stromverbrauch.

----

F2: Wie installiere ich die benötigten Module?
--------------------------------------------------

.. code-block:: bash

    # Robot HAT
    git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
    cd robot-hat && sudo python3 install.py

    # Vilib
    git clone https://github.com/sunfounder/vilib.git
    cd vilib && sudo python3 install.py

    # PiDog
    git clone https://github.com/sunfounder/pidog.git --depth 1
    cd pidog && sudo pip3 install . --break

Wenn kein Ton ausgegeben wird:

.. code-block:: bash

    # I2S Audio
    cd ~/robot-hat
    sudo bash i2samp.sh

Führe den Befehl bei Bedarf mehrfach aus.

----

F3: Wie starte ich die erste Demo?
-------------------------------------

.. code-block:: bash

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

PiDog wacht auf, setzt sich hin und wedelt mit dem Schwanz.

----

F4: Welche eingebauten Aktionen und Sounds gibt es?
------------------------------------------------------

* Aktionen: ``stand``, ``sit``, ``wag_tail``, ``trot`` usw.  
* Sounds: ``bark``, ``howling``, ``pant`` usw.

Ausführen mit:

.. code-block:: bash

    sudo python3 2_function_demonstration.py

Gib Zahlen ein, um Aktionen auszulösen.

----

F5: Wie nutzt PiDog Sensoren?
-------------------------------------

* **Ultraschall**: Hinderniserkennung und Patrouille.  
* **Berührungssensor**: Vorderseite = Alarm, Rückseite = positive Reaktion.  
* **Richtungssensor für Geräusche**: Reagiert auf die Richtung, aus der ein Geräusch kommt.

----

F6: Welche KI-Funktionen unterstützt PiDog?
------------------------------------------------------

PiDog integriert **TTS**, **STT** und **LLM**:

* **TTS**: Espeak, Pico2Wave, Piper, OpenAI.  
* **STT**: Vosk (offline).  
* **LLM**: Ollama (lokal), OpenAI (online).

----

F7: Muss ich die Servos kalibrieren?
---------------------------------------------

Ja — **die Servokalibrierung ist sowohl bei der Standard- als auch bei der V2-Version erforderlich**, um stabile Bewegungen zu gewährleisten und Schäden zu vermeiden.

**V2-Version**  

Drücke die **Nullstellungstaste** auf dem Robot HAT, um automatisch alle Servos auf 0° zu setzen.  
Dies vereinfacht den Nullstellungsprozess, ohne ein Skript auszuführen.

**Standard-Version**  

Führe das Nullstellungsskript **vor der Installation** aus:

.. code-block:: bash

   cd ~/pidog/examples
   sudo python3 servo_zeroing.py

Nach der Installation (beide Versionen) überprüfe und justiere die Servo-Winkel manuell, sodass jede Gliedmaße mit der Kalibrierungslehre ausgerichtet ist.  
Dies verhindert Instabilität, Blockierungen oder mechanische Belastung und sorgt für gleichmäßige Bewegungen sowie eine präzise Haltungskontrolle.

----

F8: Warum läuft mein PiDog instabil?
-----------------------------------------------

* Stelle sicher, dass **alle Servos auf 0°** installiert wurden.  
* Überprüfe, ob die Servo-Winkel mit der Kalibrierungslehre (60°/90°) übereinstimmen.  
* Prüfe, ob der Akku vollständig aufgeladen ist.  
* Ziehe alle Servoschrauben fest.

----

F9: Warum funktioniert meine Kamera nicht?
-------------------------------------------

* Achte darauf, dass das Kamerakabel **fest in die CSI-Schnittstelle** eingesteckt ist und die schwarze Verriegelungslasche eingerastet ist.  
* **Schalte den Raspberry Pi aus**, bevor du die Kamera ein- oder aussteckst, um Schäden zu vermeiden.  
* Teste die Kamera mit ``libcamera-hello`` oder ``raspistill``, um die Bildausgabe zu überprüfen.  
* Setze das Kabel erneut ein, wenn es locker oder falsch montiert ist.

----

F10: Warum funktioniert der Lautsprecher nicht?
-----------------------------------------------

* Stelle sicher, dass der Robot HAT-Lautsprecher aktiviert ist. Wenn du noch keinen PiDog-Beispielcode ausgeführt hast, aktiviere ihn zuerst:

  .. code-block:: bash

     robot_hat enable_speaker

  Dies muss nur einmal pro Systemstart durchgeführt werden. Das Ausführen eines beliebigen PiDog-Beispiels (das ``Pidog()`` initialisiert) erledigt dies automatisch.

* Überprüfe, ob die Lautstärke nicht stummgeschaltet ist und der I2S-Audiotreiber installiert wurde.
* Wenn kein Ton zu hören ist, konfiguriere I2S neu:

.. code-block:: bash

    cd ~/robot-hat
    sudo bash i2samp.sh

* Starte den Raspberry Pi nach dem Ausführen des Skripts neu.

----

F11: Warum funktioniert das Mikrofon nicht?
-----------------------------------------------

* Überprüfe, ob das System das Mikrofon erkennt:

.. code-block:: bash

    arecord -l

* Teste die Aufnahmefunktion:

.. code-block:: bash

    arecord -D plughw:1,0 -f cd test.wav

* Wenn keine Audiodaten aufgenommen werden, wähle das richtige Eingabegerät in den Audioeinstellungen aus oder passe die Eingangslautstärke mit ``alsamixer`` an.  
* Stelle sicher, dass kein anderer Prozess das Audioeingabegerät belegt.

----

F12: Warum funktioniert der Richtungssensor für den Ton nicht?
--------------------------------------------------------------

* Überprüfe, ob der Richtungssensor korrekt mit der SPI-Schnittstelle verbunden ist.  
* Stelle sicher, dass alle Kabel fest sitzen und nicht vertauscht sind.  
* Überprüfe die Stromversorgung und achte darauf, dass der Sensor nicht blockiert ist.  
* Starte das Gerät neu und führe das Sensor-Beispielskript erneut aus.

----

F13: Warum reagiert der Berührungssensor nicht?
-----------------------------------------------

* Stelle sicher, dass alle Kabel des Berührungssensors fest verbunden sind.  
* Merke: Ein **LOW-Signal** bedeutet, dass der Sensor berührt wird.  
* Teste den GPIO-Pin mit ``gpio readall`` oder Python-Code, um das Signal zu überprüfen.  
* Kontrolliere die Verkabelung und Ausrichtung erneut.

----

F14: Warum leuchtet die LED-Platine nicht oder blinkt falsch?
-------------------------------------------------------------

* Stelle sicher, dass die LED-Platine mit **3,3 V** betrieben und am I2C-Port angeschlossen ist.  
* Vergewissere dich, dass **I2C auf dem Raspberry Pi aktiviert** ist.  
* Führe den folgenden Befehl aus, um zu prüfen, ob das Board erkannt wird:

.. code-block:: bash

    i2cdetect -y 1

* Wenn kein Gerät erscheint, überprüfe die Verkabelung und starte den Pi neu.

----

F15: Wie wird der PiDog mit Strom versorgt?
-------------------------------------------

* Verwende ein 5V 3A Netzteil mit USB-C.  
* Rote LED = lädt, aus = vollständig geladen.  
* Der Roboter kann während des Ladevorgangs betrieben werden.  
* Wenn die Anzeige nicht leuchtet, lade den Akku zuerst auf.
