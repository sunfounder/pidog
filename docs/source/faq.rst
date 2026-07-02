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

Q1: Welche Versionen von PiDog gibt es?
------------------------------------------------------

PiDog ist in zwei Versionen erhältlich: **V1** und **V2**.

* **V1-Version**: Kompatibel mit Raspberry Pi 3B+/4B/Zero 2W, **nicht** kompatibel mit Raspberry Pi 5.
* **V2-Version**: Kompatibel mit Raspberry Pi 3/4/5 und Zero 2W. Diese Version verbessert die Robot-HAT- und Servotreiber-Schaltungen und bietet eine bessere Stromversorgung für den Pi 5.
* **Stromversorgung**: Die V2-Version verfügt über ein verbessertes Powermanagement für Anwendungen mit höherem Stromverbrauch.

Q2: Wie installiere ich die benötigten Module?
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

Q3: Why do I get a "piper-tts" error during installation?
----------------------------------------------------------

.. important::

   If you see this error during ``pip3 install``:

   .. code-block:: text

       ERROR: Could not find a version that satisfies the requirement piper-tts==1.3.0
       ERROR: No matching distribution found for piper-tts==1.3.0

   It means you are using a **32-bit** Raspberry Pi OS. The ``piper-tts`` package only provides pre-built wheels for **64-bit** systems. Reinstall the OS using the **64-bit** version of Raspberry Pi OS and the installation will succeed.

----

Q4: Wie starte ich die erste Demo?
-------------------------------------

.. code-block:: bash

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

PiDog wacht auf, setzt sich hin und wedelt mit dem Schwanz.

----

Q5: Welche eingebauten Aktionen und Sounds gibt es?
------------------------------------------------------

* Aktionen: ``stand``, ``sit``, ``wag_tail``, ``trot`` usw.
* Sounds: ``bark``, ``howling``, ``pant`` usw.

Ausführen mit:

.. code-block:: bash

    sudo python3 2_function_demonstration.py

Gib Zahlen ein, um Aktionen auszulösen.

----

Q6: Wie nutzt PiDog Sensoren?
-------------------------------------

* **Ultraschall**: Hinderniserkennung und Patrouille.
* **Berührungssensor**: Vorderseite = Alarm, Rückseite = positive Reaktion.
* **Richtungssensor für Geräusche**: Reagiert auf die Richtung, aus der ein Geräusch kommt.

----

Q7: Welche KI-Funktionen unterstützt PiDog?
------------------------------------------------------

PiDog integriert **TTS**, **STT** und **LLM**:

* **TTS**: Espeak, Pico2Wave, Piper, OpenAI.
* **STT**: Vosk (offline).
* **LLM**: Ollama (lokal), OpenAI (online).

----

Q8: Muss ich die Servos kalibrieren?
---------------------------------------------

Ja — **die Servokalibrierung ist sowohl bei der V1- als auch bei der V2-Version erforderlich**, um stabile Bewegungen zu gewährleisten und Schäden zu vermeiden.

**V2-Version**

The Robot HAT on the V2 version has a **zeroing button**. Press it to automatically set all servos to 0° — no script needed.

If your PiDog V2's legs are in the wrong position after assembly (for example, servos appear at strange angles or the robot cannot stand properly), you can use the zero button to fix this:

#. Power on the PiDog.
#. Press the **zero button** on the Robot HAT — all servos will forcibly return to 0°.
#. Reassemble the legs in the correct orientation following the assembly instructions.

For a step-by-step demonstration, watch the video below:

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zmN_mGxTKuU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**V1-Version**

The V1 version uses a script to zero the servos. Run the following command — it will set all servos to 0°:

.. code-block:: bash

   cd ~/pidog/examples
   sudo python3 servo_zeroing.py

This should be done **before installation** to ensure each servo starts from the correct zero position. If your PiDog V1's legs are in the wrong position after assembly, re-run this script to reset all servos to 0°, then reassemble the legs correctly.


----

Q9: Warum läuft mein PiDog instabil?
-----------------------------------------------

* Stelle sicher, dass **alle Servos auf 0°** installiert wurden.
* Überprüfe, ob die Servo-Winkel mit der Kalibrierungslehre (60°/90°) übereinstimmen.
* Prüfe, ob der Akku vollständig aufgeladen ist.
* Ziehe alle Servoschrauben fest.

----

Q10: Servo zeroing works, but calibration example doesn't move any servo?
--------------------------------------------------------------------------

If pressing the zeroing button moves all servos to 0° normally, but the calibration script cannot control any servo, the problem is likely a hardware connection issue between the Raspberry Pi and the Robot HAT.

.. note::

   The zeroing button is only available on **PiDog V2** (which uses Robot HAT V5). PiDog V1 does not have this feature and must use the ``servo_zeroing.py`` script instead.

**Why this happens**

* Servo zeroing is handled **directly by the Robot HAT** — it works independently without the Raspberry Pi.
* Running calibration or any servo control from code requires the Raspberry Pi to communicate with the Robot HAT through the **GPIO header pins**.

**How to diagnose**

This is often caused by poor soldering on either side of the GPIO connection:

* The **Raspberry Pi's 40-pin GPIO header** (especially on Zero 2W, where the header must be soldered on by the user).
* The **Robot HAT's female header pins**.

Take clear, well-lit photos of both sets of pins and send them to SunFounder support at service@sunfounder.com. The team will help identify whether resoldering is needed.

----

Q11: Warum funktioniert meine Kamera nicht?
-------------------------------------------

* Achte darauf, dass das Kamerakabel **fest in die CSI-Schnittstelle** eingesteckt ist und die schwarze Verriegelungslasche eingerastet ist.
* **Schalte den Raspberry Pi aus**, bevor du die Kamera ein- oder aussteckst, um Schäden zu vermeiden.
* Teste die Kamera mit ``libcamera-hello`` oder ``raspistill``, um die Bildausgabe zu überprüfen.
* Setze das Kabel erneut ein, wenn es locker oder falsch montiert ist.

----

Q12: Warum funktioniert der Lautsprecher nicht?
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

Q13: Warum funktioniert das Mikrofon nicht?
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

Q14: Warum funktioniert der Richtungssensor für den Ton nicht?
--------------------------------------------------------------

* Überprüfe, ob der Richtungssensor korrekt mit der SPI-Schnittstelle verbunden ist.
* Stelle sicher, dass alle Kabel fest sitzen und nicht vertauscht sind.
* Überprüfe die Stromversorgung und achte darauf, dass der Sensor nicht blockiert ist.
* Starte das Gerät neu und führe das Sensor-Beispielskript erneut aus.

----

Q15: Warum reagiert der Berührungssensor nicht?
-----------------------------------------------

* Stelle sicher, dass alle Kabel des Berührungssensors fest verbunden sind.
* Merke: Ein **LOW-Signal** bedeutet, dass der Sensor berührt wird.
* Teste den GPIO-Pin mit ``gpio readall`` oder Python-Code, um das Signal zu überprüfen.
* Kontrolliere die Verkabelung und Ausrichtung erneut.

----

Q16: Why is the ultrasonic sensor not working?
-----------------------------------------------

#. Run the ultrasonic test to check the reading:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 ultrasonic_test.py

   If the reading shows **-1**, the sensor is not functioning correctly.

#. Verify the wiring:

   * **White wire** → GPIO **17**
   * **Yellow wire** → GPIO **4**

#. If the wiring is correct and the reading is still -1, contact SunFounder support at service@sunfounder.com for further assistance.

----

Q17: Warum leuchtet die LED-Platine nicht oder blinkt falsch?
-------------------------------------------------------------

* Stelle sicher, dass die LED-Platine mit **3,3 V** betrieben und am I2C-Port angeschlossen ist.
* Vergewissere dich, dass **I2C auf dem Raspberry Pi aktiviert** ist.
* Führe den folgenden Befehl aus, um zu prüfen, ob das Board erkannt wird:

.. code-block:: bash

    i2cdetect -y 1

* Wenn kein Gerät erscheint, überprüfe die Verkabelung und starte den Pi neu.

----

Q18: Warum funktionieren das 6-DOF IMU und die 11-Kanal RGB-Platine nicht?
-------------------------------------------------------------------------------

Wenn sowohl das 6-DOF IMU als auch die 11-Kanal RGB-LED-Platine nicht reagieren, liegt das Problem wahrscheinlich an der gemeinsamen I2C-Verbindung:

#. Überprüfe zunächst, ob die Geräte auf dem I2C-Bus erkannt werden:

   .. code-block:: bash

       sudo i2cdetect -y 1

   Die erwarteten Adressen sind:

   * **0x36** — 6-DOF IMU
   * **0x74** — 11-Kanal RGB-LED-Platine

   Wenn eine oder beide Adressen fehlen, ist das entsprechende Gerät nicht richtig verbunden.

#. Versuche, das 6-DOF IMU an einen anderen Anschluss anzuschließen und teste erneut.
#. Schließe das 6-DOF IMU direkt an den I2C-Anschluss des Robot HAT an und führe den Test aus:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 imu_test.py

#. Wenn das IMU bei direkter Verbindung funktioniert, liegt das Problem am Durchgangsanschluss der 11-Kanal RGB-Platine.
#. Um dies zu bestätigen, schließe die 11-Kanal RGB-Platine direkt an den I2C-Anschluss an und teste:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 rgb_strip_test.py

----

Q19: Wie wird der PiDog mit Strom versorgt?
-------------------------------------------

* Verwende ein 5V 3A Netzteil mit USB-C.
* Rote LED = lädt, aus = vollständig geladen.
* Der Roboter kann während des Ladevorgangs betrieben werden.
* Wenn die Anzeige nicht leuchtet, lade den Akku zuerst auf.

----
