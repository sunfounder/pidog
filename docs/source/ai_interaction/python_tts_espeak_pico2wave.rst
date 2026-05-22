.. note::

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Approfondissez vos connaissances sur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez et partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Remises spéciales** : Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et cadeaux** : Participez à des concours et des promotions de vacances.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

14. TTS avec Espeak et Pico2Wave
=================================================

Dans cette leçon, nous allons utiliser deux moteurs de synthèse vocale (TTS) intégrés sur Raspberry Pi — **Espeak** et **Pico2Wave** — pour faire parler le Pidog.

Ces deux moteurs sont simples et fonctionnent hors ligne, mais ils sonnent assez différemment :

* **Espeak** : très léger et rapide, mais la voix est robotique. Vous pouvez ajuster la vitesse, la hauteur et le volume.
* **Pico2Wave** : produit une voix plus douce et plus naturelle qu'Espeak, mais offre moins d'options de configuration.

Vous entendrez la différence en termes de **qualité vocale** et de **fonctionnalités**.

----

Avant de commencer
------------------

Assurez-vous d'avoir terminé :

* :ref:`install_all_modules` — Installez les modules ``robot-hat``, ``vilib``, ``pidog``, puis exécutez le script ``i2samp.sh``.

Test d'Espeak
------------------

Espeak est un moteur TTS léger inclus dans Raspberry Pi OS.
Sa voix sonne de manière robotique, mais il est hautement configurable : vous pouvez ajuster le volume, la hauteur, la vitesse, etc.

**Étapes pour essayer** :

* Créez un nouveau fichier avec la commande :

  .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_espeak.py

* Copiez-y ensuite le code d'exemple. Appuyez sur ``Ctrl+X``, puis ``Y``, et enfin ``Enter`` pour enregistrer et quitter.

  .. code-block:: python

      from pidog.tts import Espeak

      tts = Espeak()

      # Optional voice tuning
      # tts.set_amp(100)   # 0 to 200
      # tts.set_speed(150) # 80 to 260
      # tts.set_gap(5)     # 0 to 200
      # tts.set_pitch(50)  # 0 to 99

      # Quick hello (sanity check)
      tts.say("Hello! I'm Espeak TTS.")

* Exécutez le programme avec :

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* Vous devriez entendre le Pidog dire : « Hello! I'm Espeak TTS. »
* Décommentez les lignes de réglage vocal dans le code pour expérimenter comment ``amp``, ``speed``, ``gap`` et ``pitch`` affectent le son.

----

Test de Pico2Wave
---------------------

Pico2Wave produit une voix plus naturelle, plus humaine qu'Espeak.
Il est plus simple à utiliser mais moins flexible — vous ne pouvez changer que la langue, pas la hauteur ni la vitesse.

**Étapes pour essayer** :

* Créez un nouveau fichier avec la commande :

  .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_pico2wave.py

* Copiez-y ensuite le code d'exemple. Appuyez sur ``Ctrl+X``, puis ``Y``, et enfin ``Enter`` pour enregistrer et quitter.

  .. code-block:: python

      from pidog.tts import Pico2Wave

      tts = Pico2Wave()

      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT

      # Quick hello (sanity check)
      tts.say("Hello! I'm Pico2Wave TTS.")

* Exécutez le programme avec :

  .. code-block::

    sudo python3 test_tts_pico2wave.py

* Vous devriez entendre le Pidog dire : « Hello! I'm Pico2Wave TTS. »
* Essayez de changer la langue (par exemple, ``es-ES`` pour l'espagnol) et écoutez la différence.

----

Dépannage
-------------------

* **Aucun son lors de l'exécution d'Espeak ou Pico2Wave**

  * Vérifiez que vos haut-parleurs/casques sont connectés et que le volume n'est pas muet.
  * Effectuez un test rapide dans le terminal :

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  Si vous n'entendez rien, le problème vient de la sortie audio, pas de votre code Python.

* **La voix d'Espeak semble trop rapide ou trop robotique**

  * Essayez d'ajuster les paramètres dans votre code :

    .. code-block:: python

       tts.set_speed(120)   # slower
       tts.set_pitch(60)    # different pitch

* **Permission refusée lors de l'exécution du code**

  * Essayez d'exécuter avec ``sudo`` :

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
     - Plus naturelle, humaine
   * - Langues
     - Anglais par défaut
     - Moins, mais les courantes
   * - Réglable
     - Oui (vitesse, hauteur, etc.)
     - Non (langue uniquement)
   * - Performances
     - Très rapide, léger
     - Légèrement plus lent, plus lourd
