10. Balance
=============

Da PiDog mit einem 6-DOF-IMU-Modul ausgestattet ist, hat es einen großartigen Sinn für Balance.

In diesem Beispiel können Sie PiDog sanft auf dem Tisch laufen lassen, selbst wenn Sie eine Seite des Tisches anheben, wird PiDog sanft am Hang entlanglaufen.

.. image:: img/py_10.gif

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pidog/examples
    sudo python3 10_balance.py

Nachdem das Programm läuft, sehen Sie eine gedruckte Tastatur im Terminal.
Sie können PiDog steuern, um sanft am Hang zu laufen, indem Sie die folgenden Tasten verwenden.

.. list-table:: 
    :widths: 25 25
    :header-rows: 1

    * - Tasten
      - Funktion
    * -  W
      -  Vorwärts gehen
    * -  E
      -  Stehen
    * -  A
      -  Links drehen
    * -  S
      -  Rückwärts gehen
    * -  D
      -  Rechts drehen
    * -  R
      -  Jeder Druck hebt den Körper leicht an; mehrere Drücke sind für einen bemerkbaren Anstieg notwendig.     
    * -  F
      -  Jeder Druck senkt den Körper ein wenig; es bedarf mehrerer Drücke für einen bemerkbaren Abstieg.
    

**Code**

Bitte finden Sie den Code unter |link_code_10_balance|.
