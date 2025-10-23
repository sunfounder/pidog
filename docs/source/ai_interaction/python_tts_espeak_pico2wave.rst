.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

14. TTS avec Espeak et Pico2Wave
=================================================

Dans cette leçon, nous allons utiliser deux moteurs de synthèse vocale (TTS) intégrés à Raspberry Pi — **Espeak** et **Pico2Wave** — pour faire parler le Pidog.

Ces deux moteurs sont simples et fonctionnent hors ligne, mais ils ont des rendus vocaux très différents :

* **Espeak** : très léger et rapide, mais la voix est robotique. Vous pouvez régler la vitesse, la hauteur et le volume.  
* **Pico2Wave** : produit une voix plus fluide et naturelle qu’Espeak, mais offre moins d’options de configuration.

Vous entendrez la différence en termes de **qualité vocale** et de **fonctionnalités**.

----

Avant de Commencer
------------------

Assurez-vous d’avoir terminé :

* :ref:`install_all_modules` — Installez les modules ``robot-hat``, ``vilib``, ``pidog``, puis exécutez le script ``i2samp.sh``.

Tester Espeak
--------------------

Espeak est un moteur TTS léger inclus dans Raspberry Pi OS.  
Sa voix est robotique, mais il est très configurable : vous pouvez ajuster le volume, la hauteur, la vitesse, etc.

**Étapes pour l’essayer** :

* Créez un nouveau fichier avec la commande :

  .. code-block:: bash
  
      cd ~/pidog/examples
      sudo nano test_tts_espeak.py

* Copiez ensuite l’exemple de code ci-dessous. Appuyez sur ``Ctrl+X``, puis ``Y``, et enfin ``Entrée`` pour enregistrer et quitter.

  .. code-block:: python
  
      from pidog.tts import Espeak

      tts = Espeak()
  
      # Réglages vocaux optionnels
      # tts.set_amp(100)   # 0 à 200
      # tts.set_speed(150) # 80 à 260
      # tts.set_gap(5)     # 0 à 200
      # tts.set_pitch(50)  # 0 à 99

      # Test rapide
      tts.say("Hello! I'm Espeak TTS.")
  
* Exécutez le programme avec :

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* Vous devriez entendre le Pidog dire : « Hello! I'm Espeak TTS. »  
* Décommentez les lignes de réglage pour expérimenter les effets de ``amp``, ``speed``, ``gap`` et ``pitch`` sur la voix.

----

Tester Pico2Wave
---------------------

Pico2Wave produit une voix plus naturelle et humaine qu’Espeak.  
Il est plus simple à utiliser mais moins flexible — vous ne pouvez modifier que la langue, pas la hauteur ni la vitesse.

**Étapes pour l’essayer** :

* Créez un nouveau fichier avec la commande :

  .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_pico2wave.py

* Copiez ensuite l’exemple de code ci-dessous. Appuyez sur ``Ctrl+X``, puis ``Y``, et enfin ``Entrée`` pour enregistrer et quitter.

  .. code-block:: python
  
      from pidog.tts import Pico2Wave
  
      tts = Pico2Wave()
  
      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
      # Test rapide
      tts.say("Hello! I'm Pico2Wave TTS.")

* Exécutez le programme avec :

  .. code-block:: bash

    sudo python3 test_tts_pico2wave.py

* Vous devriez entendre le Pidog dire : « Hello! I'm Pico2Wave TTS. »  
* Essayez de changer la langue (par exemple ``es-ES`` pour l’espagnol) et écoutez la différence.

----

Dépannage
-------------------

* **Aucun son lors de l’exécution d’Espeak ou de Pico2Wave**

  * Vérifiez que vos haut-parleurs/casques sont bien connectés et que le volume n’est pas coupé.  
  * Faites un test rapide dans le terminal :

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  Si vous n’entendez rien, le problème vient de la **sortie audio**, pas de votre code Python.

* **La voix d’Espeak est trop rapide ou trop robotique**

  * Essayez d’ajuster les paramètres dans votre code :

    .. code-block:: python

       tts.set_speed(120)   # vitesse plus lente
       tts.set_pitch(60)    # hauteur différente

* **Permission refusée lors de l’exécution du code**

  * Essayez d’exécuter avec ``sudo`` :

    .. code-block:: bash

       sudo python3 test_tts_espeak.py


Comparaison : Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Fonctionnalité
     - Espeak
     - Pico2Wave
   * - Qualité vocale
     - Robotique, synthétique
     - Plus naturelle, proche de l’humain
   * - Langues
     - Anglais par défaut
     - Moins nombreuses, mais principales
   * - Réglages possibles
     - Oui (vitesse, hauteur, etc.)
     - Non (langue uniquement)
   * - Performances
     - Très rapide, léger
     - Légèrement plus lent, plus lourd


