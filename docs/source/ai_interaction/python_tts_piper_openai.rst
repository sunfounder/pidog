.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

15. TTS avec Piper et OpenAI
========================================================

Dans la leçon précédente, nous avons testé deux moteurs TTS intégrés à Raspberry Pi (**Espeak** et **Pico2Wave**).  
Nous allons maintenant explorer deux options plus puissantes : **Piper** (hors ligne, basé sur un réseau neuronal) et **OpenAI TTS** (en ligne, basé sur le cloud).

* **Piper** : un moteur TTS local qui fonctionne hors ligne sur Raspberry Pi.  
* **OpenAI TTS** : un service en ligne offrant des voix très naturelles et proches de la voix humaine.

Avant de Commencer
------------------------------

Assurez-vous d’avoir terminé :

* :ref:`install_all_modules` — Installez les modules ``robot-hat``, ``vilib``, ``pidog``, puis exécutez le script ``i2samp.sh``.

.. _test_piper:

Tester Piper
------------------

**Étapes pour l’essayer** :

#. Créez un nouveau fichier :

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_tts_piper.py

#. Copiez le code d’exemple ci-dessous dans le fichier. Appuyez sur ``Ctrl+X``, puis ``Y``, et enfin ``Entrée`` pour enregistrer et quitter.

   .. code-block:: python

       from pidog.tts import Piper

       tts = Piper()

       # Liste des langues prises en charge
       print(tts.available_countrys())

       # Liste des modèles pour l’anglais (en_us)
       print(tts.available_models('en_us'))

       # Définir un modèle vocal (téléchargé automatiquement si absent)
       tts.set_model("en_US-amy-low")

       # Dire quelque chose
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()`` : affiche les langues prises en charge.  
   * ``available_models()`` : liste les modèles disponibles pour cette langue.  
   * ``set_model()`` : définit le modèle vocal (téléchargé automatiquement si manquant).  
   * ``say()`` : convertit le texte en parole et le lit.

#. Exécutez le programme :

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. Lors de la première exécution, le modèle vocal sélectionné sera téléchargé automatiquement.

   * Vous devriez alors entendre le Pidog dire : ``Hello! I'm Piper TTS.``

   * Vous pouvez changer de langue/modèle en appelant ``set_model()`` avec un autre nom.

----

Tester OpenAI TTS
-------------------------------

**Obtenir et enregistrer votre clé API**

#. Rendez-vous sur |link_openai_platform| et connectez-vous. Sur la page **API keys**, cliquez sur **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Remplissez les informations (Owner, Name, Project et permissions si nécessaire), puis cliquez sur **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Une fois la clé créée, copiez-la immédiatement — vous ne pourrez plus la consulter par la suite. Si vous la perdez, vous devrez en générer une nouvelle.

   .. image:: img/llm_openai_copy.png

#. Dans votre dossier de projet (par exemple : ``/pidog/examples``), créez un fichier appelé ``secret.py`` :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Collez votre clé dans le fichier :

   .. code-block:: python

       # secret.py
       # Conservez vos clés ici. Ne commitez jamais ce fichier sur Git.
       OPENAI_API_KEY = "sk-xxx"

**Écrire et exécuter un programme de test**

#. Créez un nouveau fichier :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano test_tts_openai.py

#. Copiez le code d’exemple ci-dessous dans le fichier. Appuyez sur ``Ctrl+X``, puis ``Y``, et enfin ``Entrée`` pour enregistrer et quitter.

   .. code-block:: python

      from pidog.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # ou utilisez la version try/except illustrée ci-dessus

      # Initialiser OpenAI TTS
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # modèle TTS à faible latence
      tts.set_voice('alloy')            # choisir une voix

      # Test rapide
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

  Cela signifie que ``secret.py`` n’est pas dans le même dossier que votre fichier Python.  
  Déplacez ``secret.py`` dans le répertoire où vous exécutez le script, par exemple :

  .. code-block:: bash

     ls ~/pidog/examples
     # Assurez-vous de voir les deux : secret.py et votre fichier .py

* **OpenAI : Invalid API key / 401**

  * Vérifiez que vous avez bien collé la clé complète (elle commence par ``sk-``) et qu’il n’y a pas d’espaces ou de retours à la ligne en trop.  
  * Assurez-vous que votre code l’importe correctement :

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Confirmez que votre Raspberry Pi a accès au réseau (essayez : ``ping api.openai.com``).

* **OpenAI : Quota exceeded / billing error**

  * Vous devrez peut-être ajouter des informations de facturation ou augmenter votre quota dans le tableau de bord OpenAI.  
  * Réessayez une fois le problème de compte/facturation résolu.

* **Piper : tts.say() s’exécute mais aucun son**

  * Assurez-vous qu’un modèle vocal est bien présent :

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * Vérifiez que le nom du modèle correspond exactement à celui utilisé dans le code :

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Vérifiez les paramètres de sortie audio/volume sur votre Pi (``alsamixer``) et que les haut-parleurs sont bien connectés et alimentés.

* **Erreurs ALSA / périphérique audio (ex. : “Audio device busy” ou “No such file or directory”)**

  * Fermez les autres programmes utilisant l’audio.  
  * Redémarrez le Pi si le périphérique reste occupé.  
  * Si vous utilisez HDMI ou la prise jack, sélectionnez la bonne sortie audio dans les paramètres de Raspberry Pi OS.

* **Permission refusée lors de l’exécution de Python**

  * Essayez avec ``sudo`` si votre environnement l’exige :

    .. code-block:: bash

       sudo python3 test_tts_piper.py



Comparaison des moteurs TTS
------------------------------------------

.. list-table:: Comparaison des fonctionnalités : Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - Élément
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - Fonctionne sur
     - Intégré au Raspberry Pi (hors ligne)
     - Intégré au Raspberry Pi (hors ligne)
     - Raspberry Pi / PC (hors ligne, nécessite un modèle)
     - Cloud (en ligne, nécessite une clé API)
   * - Qualité vocale
     - Robotique
     - Plus naturelle qu’Espeak
     - Naturelle (TTS neuronal)
     - Très naturelle / proche de la voix humaine
   * - Contrôles
     - Vitesse, hauteur, volume
     - Contrôles limités
     - Choix de différentes voix/modèles
     - Choix du modèle et des voix
   * - Langues
     - Nombreuses (qualité variable)
     - Ensemble limité
     - De nombreuses voix/langues disponibles
     - Meilleure en anglais (autres selon disponibilité)
   * - Latence / vitesse
     - Très rapide
     - Rapide
     - Temps réel sur Pi 4/5 avec modèles “low”
     - Dépend du réseau (généralement faible latence)
   * - Installation
     - Minimale
     - Minimale
     - Télécharger les modèles ``.onnx`` + ``.onnx.json``
     - Créer une clé API, installer le client
   * - Meilleur usage
     - Tests rapides, invites basiques
     - Voix hors ligne légèrement meilleure
     - Projets locaux avec meilleure qualité
     - Qualité maximale, options vocales riches

