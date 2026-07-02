FAQ
==========

Q1 : Quelles sont les versions de PiDog disponibles ?
------------------------------------------------------

PiDog existe en versions **V1** et **V2** :

* **Version V1** : Compatible avec Raspberry Pi 3B+/4B/Zero 2W, **non** compatible avec Raspberry Pi 5.
* **Version V2** : Compatible avec Raspberry Pi 3/4/5 et Zero 2W. Elle améliore le Robot HAT et les circuits de commande des servos et offre une meilleure gestion de l'alimentation pour le Pi 5.
* **Alimentation** : La V2 dispose d'une gestion d'alimentation renforcée pour les applications à forte consommation électrique.

Q2 : Comment installer les modules requis ?
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

S'il n'y a pas de son :

.. code-block:: bash

    # I2S Audio
    cd ~/robot-hat
    sudo bash i2samp.sh

Exécutez plusieurs fois si nécessaire.

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

Q4 : Comment exécuter la première démonstration ?
-------------------------------------------------

.. code-block:: bash

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

PiDog se réveillera, s'assiéra et remuera la queue.

----

Q5 : Quelles actions et quels sons intégrés sont disponibles ?
--------------------------------------------------------------

* Actions : ``stand``, ``sit``, ``wag_tail``, ``trot``, etc.
* Sons : ``bark``, ``howling``, ``pant``, etc.

Exécutez :

.. code-block:: bash

    sudo python3 2_function_demonstration.py

Entrez des numéros pour déclencher les actions.

----

Q6 : Comment PiDog utilise-t-il les capteurs ?
----------------------------------------------

* **Ultrason** : Évitement d'obstacles et patrouille.
* **Tactile** : Toucher avant = alerte ; toucher arrière = contentement.
* **Direction sonore** : Réagit à la direction du son.

----

Q7 : Quelles fonctions d'IA PiDog prend-il en charge ?
------------------------------------------------------

PiDog intègre la **TTS**, la **STT** et les **LLM** :

* **TTS** : Espeak, Pico2Wave, Piper, OpenAI.
* **STT** : Vosk (hors ligne).
* **LLM** : Ollama (local), OpenAI (en ligne).

----

Q8 : Dois-je calibrer les servos ?
---------------------------------------------

Oui — **le calibrage des servos est requis pour les versions V1 et V2** afin de garantir des mouvements stables et d'éviter tout dommage.

**Version V2**

The Robot HAT on the V2 version has a **zeroing button**. Press it to automatically set all servos to 0° — no script needed.

If your PiDog V2's legs are in the wrong position after assembly (for example, servos appear at strange angles or the robot cannot stand properly), you can use the zero button to fix this:

#. Power on the PiDog.
#. Press the **zero button** on the Robot HAT — all servos will forcibly return to 0°.
#. Reassemble the legs in the correct orientation following the assembly instructions.

For a step-by-step demonstration, watch the video below:

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zmN_mGxTKuU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Version V1**

The V1 version uses a script to zero the servos. Run the following command — it will set all servos to 0°:

.. code-block:: bash

   cd ~/pidog/examples
   sudo python3 servo_zeroing.py

This should be done **before installation** to ensure each servo starts from the correct zero position. If your PiDog V1's legs are in the wrong position after assembly, re-run this script to reset all servos to 0°, then reassemble the legs correctly.


----

Q9 : Pourquoi mon PiDog marche-t-il de manière instable ?
---------------------------------------------------------

* Confirmez que tous les servos ont été installés à 0°.
* Assurez-vous que les angles des servos correspondent à la règle d'étalonnage (60°/90°).
* Vérifiez que la batterie est complètement chargée.
* Serrez toutes les vis des servos.

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

Q11 : Pourquoi ma caméra ne fonctionne-t-elle pas ?
--------------------------------------------------

* Assurez-vous que le câble de la caméra est **fermement inséré** dans l'interface CSI et que la languette de verrouillage noire est bien sécurisée.
* **Éteignez** le Raspberry Pi avant de brancher ou débrancher la caméra pour éviter tout dommage.
* Testez la caméra avec ``libcamera-hello`` ou ``raspistill`` pour vérifier la sortie image.
* Reconnectez le câble s'il est desserré ou mal installé.

----

Q12 : Pourquoi le haut-parleur ne fonctionne-t-il pas ?
-------------------------------------------------------

* Assurez-vous que le haut-parleur du Robot HAT est activé. Si vous n'avez pas encore exécuté de code d'exemple PiDog, activez-le d'abord :

  .. code-block:: bash

     robot_hat enable_speaker

  Cela ne doit être fait qu'une fois par démarrage. L'exécution de n'importe quel exemple PiDog (qui initialise ``Pidog()``) le fait automatiquement.

* Assurez-vous que le volume n'est pas coupé et que le pilote audio I2S est installé.
* S'il n'y a pas de son, reconfigurez I2S avec les commandes suivantes :

.. code-block:: bash

    cd ~/robot-hat
    sudo bash i2samp.sh

* Redémarrez le Raspberry Pi après avoir exécuté le script.

----

Q13 : Pourquoi le microphone ne fonctionne-t-il pas ?
-----------------------------------------------------

* Vérifiez si le système reconnaît le microphone avec :

.. code-block:: bash

    arecord -l

* Testez la fonction d'enregistrement avec :

.. code-block:: bash

    arecord -D plughw:1,0 -f cd test.wav

* Si aucun audio n'est enregistré, sélectionnez le périphérique d'entrée correct dans les paramètres audio ou utilisez ``alsamixer`` pour régler le volume d'entrée.
* Assurez-vous qu'aucun autre processus n'occupe le périphérique d'entrée audio.

----

Q14 : Pourquoi le capteur de direction sonore ne fonctionne-t-il pas ?
----------------------------------------------------------------------

* Assurez-vous que le capteur de direction sonore est connecté à l'interface SPI correcte.
* Vérifiez que tous les câbles sont bien connectés et non inversés.
* Assurez-vous que l'alimentation est stable et que le capteur n'est pas obstrué.
* Redémarrez l'appareil et essayez d'exécuter à nouveau l'exemple de script du capteur.

----

Q15 : Pourquoi le capteur tactile ne répond-il pas ?
----------------------------------------------------

* Assurez-vous que tous les câbles du capteur tactile sont fermement connectés.
* Rappel : un signal **LOW** signifie que le capteur est touché.
* Testez la broche GPIO avec ``gpio readall`` ou un code Python pour confirmer la détection du signal.
* Revérifiez le câblage et l'orientation.

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

Q17 : Pourquoi la carte LED ne s'allume-t-elle pas ou ne clignote-t-elle pas correctement ?
-------------------------------------------------------------------------------------------

* Vérifiez que la carte LED est alimentée en **3,3 V** et connectée au port I2C.
* Assurez-vous que **I2C est activé** sur le Raspberry Pi.
* Exécutez la commande suivante pour vérifier si la carte est reconnue :

.. code-block:: bash

    i2cdetect -y 1

* Si aucun appareil n'apparaît, revérifiez le câblage et redémarrez le Pi.

----

Q18: Why are the 6-DOF IMU and 11-channel RGB board not working?
-----------------------------------------------------------------

If both the 6-DOF IMU and the 11-channel RGB LED board are not responding, the issue is likely with the shared I2C connection:

#. First, check whether the devices are detected on the I2C bus:

   .. code-block:: bash

       sudo i2cdetect -y 1

   The expected addresses are:

   * **0x36** — 6-DOF IMU
   * **0x74** — 11-channel RGB LED board

   If one or both addresses are missing, the corresponding device is not properly connected.

#. Try connecting the 6-DOF IMU to a different port and test again.
#. Connect the 6-DOF IMU directly to the Robot HAT's I2C port, then run the test:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 imu_test.py

#. If the IMU works when connected directly, the problem is with the 11-channel RGB board's pass-through port.
#. To confirm, connect the 11-channel RGB board directly to the I2C port and test:

   .. code-block:: bash

       cd ~/pidog/test && sudo python3 rgb_strip_test.py

----

Q19 : Comment PiDog est-il alimenté ?
------------------------------------------

* Utilisez un adaptateur secteur Type-C 5V 3A.
* Voyant rouge = en charge, éteint = complètement chargé.
* Vous pouvez l'utiliser pendant qu'il charge.
* Si le voyant ne s'allume pas, chargez-le d'abord.

----
