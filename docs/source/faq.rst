.. note::

    Bonjour et bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes post-achat et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions et cadeaux festifs** : Participez à des tirages au sort et à des promotions spéciales.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

FAQ
==========

Q1 : Quelles versions de PiDog sont disponibles ?
------------------------------------------------------

PiDog est disponible en deux versions : **Standard** et **V2** :

* **Version Standard** : Compatible avec Raspberry Pi 3B+/4B/Zero 2W, **non** compatible avec Raspberry Pi 5.  
* **Version V2** : Compatible avec Raspberry Pi 3/4/5 et Zero 2W. Elle améliore le Robot HAT et les circuits des servomoteurs et offre une meilleure alimentation pour le Pi 5.  
* **Alimentation** : La V2 dispose d’une gestion d’alimentation renforcée pour les applications à consommation plus élevée.

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
    cd pidog && sudo python3 setup.py install

S’il n’y a pas de son :

.. code-block:: bash

    # Audio I2S
    cd ~/robot-hat
    sudo bash i2samp.sh

Répétez plusieurs fois si nécessaire.

----

Q3 : Comment exécuter la première démo ?
--------------------------------------------------

.. code-block:: bash

    cd ~/pidog/examples
    sudo python3 1_wake_up.py

PiDog se réveillera, s’assiéra et remuera la queue.

----

Q4 : Quelles actions et sons intégrés sont disponibles ?
---------------------------------------------------------------------

* Actions : ``stand``, ``sit``, ``wag_tail``, ``trot``, etc.  
* Sons : ``bark``, ``howling``, ``pant``, etc.

Exécutez :

.. code-block:: bash

    sudo python3 2_function_demonstration.py

Entrez un numéro pour déclencher une action.

----

Q5 : Comment PiDog utilise-t-il les capteurs ?
--------------------------------------------------------

* **Ultrasonique** : Évitement d’obstacles et patrouille.  
* **Tactile** : Touche avant = alerte ; touche arrière = plaisir.  
* **Direction du son** : Réagit à la direction de la source sonore.

----

Q6 : Quelles fonctionnalités IA PiDog prend-il en charge ?
-----------------------------------------------------------------

PiDog s’intègre avec **TTS**, **STT** et **LLM** :

* **TTS** : Espeak, Pico2Wave, Piper, OpenAI.  
* **STT** : Vosk (hors ligne).  
* **LLM** : Ollama (local), OpenAI (en ligne).

----

Q7 : Faut-il calibrer les servomoteurs ?
---------------------------------------------

Oui — **la calibration des servos est nécessaire pour les versions Standard et V2** afin d’assurer des mouvements stables et d’éviter tout dommage.

**Version V2**  

Appuyez sur le **bouton de remise à zéro** du Robot HAT pour définir automatiquement tous les servos à 0°. Cela simplifie grandement le processus sans script.

**Version Standard** 

Exécutez le script de remise à zéro **avant l’installation** :

.. code-block:: bash

   cd ~/pidog/examples
   sudo python3 servo_zeroing.py

Après l’installation (pour les deux versions), vérifiez et ajustez manuellement les angles des servos pour aligner chaque membre avec la règle de calibration. Cela permet d’éviter les déséquilibres, blocages ou contraintes mécaniques et garantit une marche fluide ainsi qu’un contrôle précis des postures.


Q8 : Pourquoi mon PiDog marche-t-il de manière instable ?
--------------------------------------------------------------------

* Vérifiez que tous les servomoteurs ont bien été installés à **0°**.  
* Assurez-vous que les angles des servos correspondent à la règle de calibration (60°/90°).  
* Vérifiez que la batterie est complètement chargée.  
* Serrez toutes les vis des servos.

----

Q9 : Pourquoi ma caméra ne fonctionne-t-elle pas ?
--------------------------------------------------------

* Assurez-vous que le câble de la caméra est **fermement inséré** dans l’interface CSI et que la languette noire est bien verrouillée.  
* **Éteignez** le Raspberry Pi avant de brancher ou débrancher la caméra pour éviter tout dommage.  
* Testez la caméra avec ``libcamera-hello`` ou ``raspistill`` pour vérifier la sortie d’image.  
* Rebranchez le câble s’il est desserré ou mal inséré.

----

Q10 : Pourquoi le haut-parleur ne fonctionne-t-il pas ?
--------------------------------------------------------------------

* Vérifiez que le volume n’est pas coupé et que le pilote audio I2S est bien installé.  
* Si aucun son n’est émis, reconfigurez I2S avec la commande suivante :

.. code-block:: bash

    cd ~/robot-hat
    sudo bash i2samp.sh

* Redémarrez le Raspberry Pi après avoir exécuté le script.

----

Q11 : Pourquoi le microphone ne fonctionne-t-il pas ?
-----------------------------------------------------------

* Vérifiez si le système reconnaît le microphone avec :

.. code-block:: bash

    arecord -l

* Testez la fonction d’enregistrement avec :

.. code-block:: bash

    arecord -D plughw:1,0 -f cd test.wav

* Si aucun son n’est enregistré, sélectionnez le bon périphérique d’entrée dans les paramètres audio ou utilisez ``alsamixer`` pour ajuster le volume d’entrée.  
* Assurez-vous qu’aucun autre processus n’utilise le périphérique audio d’entrée.

----

Q12 : Pourquoi le capteur de direction sonore ne fonctionne-t-il pas ?
----------------------------------------------------------------------------

* Assurez-vous que le capteur de direction sonore est connecté à la bonne interface SPI.  
* Vérifiez que tous les câbles sont bien fixés et non inversés.  
* Assurez-vous que l’alimentation est stable et que le capteur n’est pas obstrué.  
* Redémarrez l’appareil et relancez le script d’exemple du capteur.

----

Q13 : Pourquoi le capteur tactile ne réagit-il pas ?
---------------------------------------------------------

* Assurez-vous que tous les câbles du capteur tactile sont fermement connectés.  
* Rappel : un signal **LOW** signifie que le capteur est touché.  
* Testez la broche GPIO avec ``gpio readall`` ou du code Python pour confirmer la détection du signal.  
* Vérifiez le câblage et l’orientation.

----

Q14 : Pourquoi la carte LED ne s’allume-t-elle pas ou clignote-t-elle de façon incorrecte ?
---------------------------------------------------------------------------------------------

* Vérifiez que la carte LED est alimentée en **3,3 V** et connectée au port I2C.  
* Assurez-vous que **I2C est activé** sur le Raspberry Pi.  
* Exécutez la commande suivante pour vérifier si la carte est détectée :

.. code-block:: bash

    i2cdetect -y 1

* Si aucun périphérique n’apparaît, vérifiez le câblage et redémarrez le Raspberry Pi.

----

Q15 : Comment PiDog est-il alimenté ?
------------------------------------------

* Utilisez un adaptateur secteur Type-C 5 V 3 A.  
* Lumière rouge = en charge, éteinte = charge complète.  
* Vous pouvez l’alimenter tout en le chargeant.  
* Si le témoin ne s’allume pas, chargez d’abord la batterie.
