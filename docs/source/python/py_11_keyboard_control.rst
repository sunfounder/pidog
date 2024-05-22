.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

11. PiDog mit Tastatur steuern
======================================

In diesem Beispiel werden wir die Tastatur verwenden, um PiDog zu steuern. Sie können diese Tasten im Terminal drücken, um es handeln zu lassen.

.. list-table:: 
    :widths: 25 50 25 50 25 50
    :header-rows: 1

    * - Keys
      - Function
      - Keys
      - Function
      - Keys
      - Function  
    * - 1
      - doze off
      - q
      - bark harder
      - a
      - turn left
    * - 2
      - push-up
      - w
      - forward
      - s
      - backward
    * - 3
      - howling
      - e
      - pant
      - d
      - turn right
    * - 4
      - twist body
      - r
      - wag tail
      - f
      - shake head
    * - 5
      - scratch
      - t
      - hake head
      - g
      - high five
    * - u
      - head roll
      - U
      - head roll+
      - z
      - lie
    * - i
      - head pitch
      - I
      - head pitch+
      - x
      - stand up
    * - o
      - head roll
      - O
      - head roll+
      - c
      - sit
    * - j
      - head yaw
      - J
      - head yaw+
      - v
      - stretch
    * - k
      - head pitch
      - K
      - head pitch+
      - m
      - head reset
    * - l
      - head yaw
      - L
      - head yaw+
      - W
      - trot

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 11_keyboard_control.py

Nachdem das Programm gestartet wurde, sehen Sie eine gedruckte Tastatur im Terminal. Jetzt können Sie PiDog mit der Tastatur im Terminal steuern.

**Code**

Bitte finden Sie den Code unter |link_code_11_keyboard_control|.
