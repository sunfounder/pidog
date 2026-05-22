.. note::

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et à des aperçus.
    - **Remises spéciales** : Profitez de remises exclusives sur nos tout nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur |link_sf_facebook| et rejoignez-nous dès aujourd'hui !

15. Synthèse vocale avec Piper et OpenAI
========================================================

Dans la leçon précédente, nous avons essayé deux moteurs de synthèse vocale intégrés sur Raspberry Pi (**Espeak** et **Pico2Wave**). Explorons maintenant deux options plus puissantes : **Piper** (hors ligne, basé sur un réseau neuronal) et **OpenAI TTS** (en ligne, dans le cloud).

* **Piper** : un moteur TTS local qui fonctionne hors ligne sur Raspberry Pi.
* **OpenAI TTS** : un service en ligne qui offre des voix très naturelles, proches de l'humain.

Avant de commencer
------------------

Assurez-vous d'avoir réalisé les étapes suivantes :

* :ref:`install_all_modules` — Installez les modules ``robot-hat``, ``vilib``, ``pidog``, puis exécutez le script ``i2samp.sh``.

.. _test_piper:

Tester Piper
------------------

**Étapes pour l'essayer** :

#. Créez un nouveau fichier :

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_piper.py

#. Copiez l'exemple de code ci-dessous dans le fichier. Appuyez sur ``Ctrl+X``, puis ``Y``, et enfin ``Entrée`` pour enregistrer et quitter.

   .. code-block:: python

       from pidog.tts import Piper

       tts = Piper()

       # List supported languages
       print(tts.available_countrys())

       # List models for English (en_us)
       print(tts.available_models('en_us'))

       # Set a voice model (auto-download if not already present)
       tts.set_model("en_US-amy-low")

       # Say something
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()`` : affiche les langues prises en charge.
   * ``available_models()`` : liste les modèles disponibles pour cette langue.
   * ``set_model()`` : définit le modèle vocal (téléchargement automatique s'il est manquant).
   * ``say()`` : convertit le texte en parole et le lit.

#. Exécutez le programme :

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. La première fois que vous l'exécutez, le modèle vocal sélectionné sera téléchargé automatiquement.

   * Vous devriez alors entendre le Pidog dire : ``Hello! I'm Piper TTS.``

   * Vous pouvez passer à un autre modèle linguistique en appelant ``set_model()`` avec un nom différent.


Tester OpenAI TTS
-------------------------------

**Obtenez et enregistrez votre clé API**

#. Allez sur |link_openai_platform| et connectez-vous. Sur la page **API keys**, cliquez sur **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Remplissez les détails (Owner, Name, Project et permissions si nécessaire), puis cliquez sur **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Une fois la clé créée, copiez-la immédiatement — vous ne pourrez plus la voir ensuite. Si vous la perdez, vous devez en générer une nouvelle.

   .. image:: img/llm_openai_copy.png

#. Dans votre dossier de projet (par exemple : ``/pidog/examples``), créez un fichier nommé ``secret.py`` :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Collez votre clé dans le fichier comme ceci :

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**Écrire et exécuter un programme de test**

#. Créez un nouveau fichier :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano test_tts_openai.py

#. Copiez l'exemple de code ci-dessous dans le fichier. Appuyez sur ``Ctrl+X``, puis ``Y``, et enfin ``Entrée`` pour enregistrer et quitter.

   .. code-block:: python

      from pidog.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # or use the try/except version shown above

      # Initialize OpenAI TTS
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # low-latency TTS model
      tts.set_voice('alloy')            # pick a voice

      # Quick hello (sanity check)
      tts.say("Hello! I'm OpenAI TTS.")

#. Exécutez le programme :

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. Vous devriez entendre le Pidog dire :

   ``Hello! I'm OpenAI TTS.``

----

Dépannage
-------------------

* **No module named 'secret'**

  Cela signifie que ``secret.py`` ne se trouve pas dans le même dossier que votre fichier Python.
  Déplacez ``secret.py`` dans le même répertoire où vous exécutez le script, par exemple :

  .. code-block:: bash

     ls ~/pidog/examples
     # Make sure you see both: secret.py and your .py file

* **OpenAI: Invalid API key / 401**

  * Vérifiez que vous avez collé la clé complète (commence par ``sk-``) et qu'il n'y a pas d'espaces ou de sauts de ligne supplémentaires.
  * Assurez-vous que votre code l'importe correctement :

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Confirmez l'accès réseau sur votre Pi (essayez ``ping api.openai.com``).

* **OpenAI: Quota exceeded / billing error**

  * Vous devrez peut-être ajouter un mode de paiement ou augmenter votre quota dans le tableau de bord OpenAI.
  * Réessayez après avoir résolu le problème de compte/facturation.

* **Piper: tts.say() s'exécute mais aucun son**

  * Assurez-vous qu'un modèle vocal est bien présent :

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * Confirmez que le nom de votre modèle correspond exactement dans le code :

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Vérifiez le périphérique de sortie audio et le volume sur votre Pi (``alsamixer``), et assurez-vous que les enceintes sont branchées et sous tension.

* **Erreurs ALSA / périphérique sonore (par ex., "Audio device busy" ou "No such file or directory")**

  * Fermez les autres programmes qui utilisent l'audio.
  * Redémarrez le Pi si le périphérique reste occupé.
  * Pour la sortie HDMI par rapport à la prise casque, sélectionnez le périphérique approprié dans les paramètres audio de Raspberry Pi OS.

* **Permission denied lors de l'exécution de Python**

  * Essayez avec ``sudo`` si votre environnement l'exige :

    .. code-block:: bash

       sudo python3 test_tts_piper.py



Comparaison des moteurs de TTS
------------------------------

.. list-table:: Comparaison des fonctionnalités : Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - Élément
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - Fonctionne sur
     - Intégré sur Raspberry Pi (hors ligne)
     - Intégré sur Raspberry Pi (hors ligne)
     - Raspberry Pi / PC (hors ligne, nécessite un modèle)
     - Cloud (en ligne, nécessite une clé API)
   * - Qualité vocale
     - Robotique
     - Plus naturelle qu'Espeak
     - Naturelle (TTS neuronal)
     - Très naturelle / proche de l'humain
   * - Contrôles
     - Vitesse, hauteur, volume
     - Contrôles limités
     - Choisir différentes voix/modèles
     - Choisir le modèle et les voix
   * - Langues
     - Nombreuses (qualité variable)
     - Ensemble limité
     - Nombreuses voix/langues disponibles
     - Meilleur en anglais (autres langues selon disponibilité)
   * - Latence / vitesse
     - Très rapide
     - Rapide
     - Temps réel sur Pi 4/5 avec les modèles « low »
     - Dépend du réseau (généralement faible latence)
   * - Configuration
     - Minimale
     - Minimale
     - Télécharger les modèles ``.onnx`` + ``.onnx.json``
     - Créer une clé API, installer le client
   * - Idéal pour
     - Tests rapides, invites basiques
     - Voix hors ligne légèrement meilleure
     - Projets locaux avec une meilleure qualité
     - Qualité maximale, options vocales riches
