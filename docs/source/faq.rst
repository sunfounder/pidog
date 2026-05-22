FAQ
==========

Q1 : Quelles sont les versions de PiDog disponibles ?
------------------------------------------------------

PiDog existe en versions **Standard** et **V2** :

* **Version Standard** : Compatible avec Raspberry Pi 3B+/4B/Zero 2W, **non** compatible avec Raspberry Pi 5.
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

Q3 : Comment exécuter la première démonstration ?
-------------------------------------------------

.. code-block:: bash

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

PiDog se réveillera, s'assiéra et remuera la queue.

----

Q4 : Quelles actions et quels sons intégrés sont disponibles ?
--------------------------------------------------------------

* Actions : ``stand``, ``sit``, ``wag_tail``, ``trot``, etc.
* Sons : ``bark``, ``howling``, ``pant``, etc.

Exécutez :

.. code-block:: bash

    sudo python3 2_function_demonstration.py

Entrez des numéros pour déclencher les actions.

----

Q5 : Comment PiDog utilise-t-il les capteurs ?
----------------------------------------------

* **Ultrason** : Évitement d'obstacles et patrouille.
* **Tactile** : Toucher avant = alerte ; toucher arrière = contentement.
* **Direction sonore** : Réagit à la direction du son.

----

Q6 : Quelles fonctions d'IA PiDog prend-il en charge ?
------------------------------------------------------

PiDog intègre la **TTS**, la **STT** et les **LLM** :

* **TTS** : Espeak, Pico2Wave, Piper, OpenAI.
* **STT** : Vosk (hors ligne).
* **LLM** : Ollama (local), OpenAI (en ligne).

----

Q7 : Dois-je calibrer les servos ?
---------------------------------------------

Oui — **le calibrage des servos est requis pour les versions Standard et V2** afin de garantir des mouvements stables et d'éviter tout dommage.

**Version V2**

Appuyez sur le **bouton de mise à zéro** du Robot HAT pour régler automatiquement tous les servos à 0°. Cela simplifie le processus de mise à zéro sans exécuter de script.

**Version Standard**

Exécutez le script de mise à zéro **avant l'installation** :

.. code-block:: bash

   cd ~/pidog/examples
   sudo python3 servo_zeroing.py

Après l'installation (les deux versions), vérifiez manuellement et ajustez finement les angles des servos pour aligner chaque membre avec la règle d'étalonnage afin d'éviter l'instabilité, les blocages ou les contraintes mécaniques et d'assurer une marche fluide et un contrôle précis de la posture.

----

Q8 : Pourquoi mon PiDog marche-t-il de manière instable ?
---------------------------------------------------------

* Confirmez que tous les servos ont été installés à 0°.
* Assurez-vous que les angles des servos correspondent à la règle d'étalonnage (60°/90°).
* Vérifiez que la batterie est complètement chargée.
* Serrez toutes les vis des servos.

----

Q9 : Pourquoi ma caméra ne fonctionne-t-elle pas ?
--------------------------------------------------

* Assurez-vous que le câble de la caméra est **fermement inséré** dans l'interface CSI et que la languette de verrouillage noire est bien sécurisée.
* **Éteignez** le Raspberry Pi avant de brancher ou débrancher la caméra pour éviter tout dommage.
* Testez la caméra avec ``libcamera-hello`` ou ``raspistill`` pour vérifier la sortie image.
* Reconnectez le câble s'il est desserré ou mal installé.

----

Q10 : Pourquoi le haut-parleur ne fonctionne-t-il pas ?
-------------------------------------------------------

* Assurez-vous que le volume n'est pas coupé et que le pilote audio I2S est installé.
* S'il n'y a pas de son, reconfigurez I2S avec les commandes suivantes :

.. code-block:: bash

    cd ~/robot-hat
    sudo bash i2samp.sh

* Redémarrez le Raspberry Pi après avoir exécuté le script.

----

Q11 : Pourquoi le microphone ne fonctionne-t-il pas ?
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

Q12 : Pourquoi le capteur de direction sonore ne fonctionne-t-il pas ?
----------------------------------------------------------------------

* Assurez-vous que le capteur de direction sonore est connecté à l'interface SPI correcte.
* Vérifiez que tous les câbles sont bien connectés et non inversés.
* Assurez-vous que l'alimentation est stable et que le capteur n'est pas obstrué.
* Redémarrez l'appareil et essayez d'exécuter à nouveau l'exemple de script du capteur.

----

Q13 : Pourquoi le capteur tactile ne répond-il pas ?
----------------------------------------------------

* Assurez-vous que tous les câbles du capteur tactile sont fermement connectés.
* Rappel : un signal **LOW** signifie que le capteur est touché.
* Testez la broche GPIO avec ``gpio readall`` ou un code Python pour confirmer la détection du signal.
* Revérifiez le câblage et l'orientation.

----

Q14 : Pourquoi la carte LED ne s'allume-t-elle pas ou ne clignote-t-elle pas correctement ?
-------------------------------------------------------------------------------------------

* Vérifiez que la carte LED est alimentée en **3,3 V** et connectée au port I2C.
* Assurez-vous que **I2C est activé** sur le Raspberry Pi.
* Exécutez la commande suivante pour vérifier si la carte est reconnue :

.. code-block:: bash

    i2cdetect -y 1

* Si aucun appareil n'apparaît, revérifiez le câblage et redémarrez le Pi.

----

Q15 : Comment PiDog est-il alimenté ?
------------------------------------------

* Utilisez un adaptateur secteur Type-C 5V 3A.
* Voyant rouge = en charge, éteint = complètement chargé.
* Vous pouvez l'utiliser pendant qu'il charge.
* Si le voyant ne s'allume pas, chargez-le d'abord.

----
