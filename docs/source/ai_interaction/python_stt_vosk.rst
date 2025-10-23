.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

16. STT avec Vosk (Hors Ligne)
==============================================

Vosk est un moteur léger de reconnaissance vocale (STT) qui prend en charge de nombreuses langues et fonctionne entièrement **hors ligne** sur Raspberry Pi.  
Vous n’avez besoin d’un accès Internet qu’une seule fois pour télécharger un modèle linguistique. Ensuite, tout fonctionne sans connexion réseau.

Dans cette leçon, nous allons :

* Vérifier le microphone sur le Raspberry Pi.  
* Installer et tester Vosk avec un modèle linguistique choisi.

Avant de Commencer
------------------

Assurez-vous d’avoir terminé :

* :ref:`install_all_modules` — Installer les modules ``robot-hat``, ``vilib``, ``pidog``, puis exécuter le script ``i2samp.sh``.

1. Vérifier Votre Microphone
----------------------------

Avant d’utiliser la reconnaissance vocale, assurez-vous que votre microphone USB fonctionne correctement.

#. Listez les périphériques d’enregistrement disponibles :

   .. code-block:: bash

      arecord -l

   Recherchez une ligne comme ``card 1: ... device 0``.

#. Enregistrez un court échantillon (remplacez ``1,0`` par les numéros trouvés) :

   .. code-block:: bash

      arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

   * Exemple : si votre périphérique est ``card 2, device 0``, utilisez :

   .. code-block:: bash

      arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

#. Relisez l’échantillon pour confirmer l’enregistrement :

   .. code-block:: bash

      aplay test.wav

#. Ajustez le volume du microphone si nécessaire :

   .. code-block:: bash

      alsamixer

   * Appuyez sur **F6** pour sélectionner votre microphone USB.  
   * Trouvez le canal **Mic** ou **Capture**.  
   * Assurez-vous qu’il n’est pas coupé (**[MM]** signifie muet, appuyez sur ``M`` pour réactiver → doit afficher **[OO]**).  
   * Utilisez les flèches ↑ / ↓ pour modifier le volume d’enregistrement.


.. _test_vosk:

2. Tester Vosk
--------------------------

**Étapes pour l’essayer** :

#. Créez un nouveau fichier :

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_stt_vosk.py

#. Copiez l’exemple de code ci-dessous. Appuyez sur ``Ctrl+X``, puis ``Y``, et ``Entrée`` pour enregistrer et quitter.

   .. code-block:: python

      from pidog.stt import Vosk

      vosk = Vosk(language="en-us")

      print(vosk.available_languages)

      while True:
          print("Say something")
          result = vosk.listen(stream=False)
          print(result)

#. Exécutez le programme :

   .. code-block:: bash

      sudo python3 test_stt_vosk.py

#. La première fois que vous exécutez ce code avec une nouvelle langue, Vosk **téléchargera automatiquement le modèle linguistique** (par défaut, il téléchargera la version **small**).  
   En même temps, il affichera la liste des langues prises en charge. Vous verrez alors :

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   Cela signifie :

   * Le fichier du modèle (``vosk-model-small-en-us-0.15``) a été téléchargé.  
   * La liste des langues prises en charge a été affichée.  
   * Le système est maintenant en écoute — parlez dans le microphone de Pidog et le texte reconnu s’affichera dans le terminal.

   **Astuces** :

   * Gardez le microphone à une distance d’environ 15 à 30 cm.  
   * Choisissez un modèle qui correspond à votre langue et à votre accent.

**Mode Streaming (optionnel)**

Vous pouvez également diffuser la parole en continu pour voir les résultats partiels pendant que vous parlez :

.. code-block:: python

   from pidog.stt import Vosk

   vosk = Vosk(language="en-us")

   while True:
       print("Say something")
       for result in vosk.listen(stream=True):
           if result["done"]:
               print(f"final:   {result['final']}")
           else:
               print(f"partial: {result['partial']}", end="\r", flush=True)

Dépannage
-----------------

* **No such file or directory (lors de l’exécution de `arecord`)**

  Vous avez peut-être utilisé un mauvais numéro de carte/périphérique.  
  Exécutez :

  .. code-block:: bash

     arecord -l

  puis remplacez ``1,0`` par les numéros indiqués pour votre microphone USB.

* **Le fichier enregistré n’a pas de son**

  Ouvrez le mixeur et vérifiez le volume du microphone :

  .. code-block:: bash

     alsamixer

  * Appuyez sur **F6** pour sélectionner votre micro USB.  
  * Assurez-vous que **Mic/Capture** n’est pas coupé (**[OO]** au lieu de **[MM]**).  
  * Augmentez le niveau avec ↑.

* **Vosk ne reconnaît pas la parole**

  * Assurez-vous que le **code langue** correspond à votre modèle (par ex. ``en-us`` pour l’anglais, ``zh-cn`` pour le chinois).  
  * Maintenez le microphone à 15–30 cm et évitez les bruits de fond.  
  * Parlez lentement et clairement.

* **Latence élevée / reconnaissance lente**

  * Le téléchargement automatique utilise un **petit modèle** (plus rapide mais moins précis).  
  * Si c’est encore lent, fermez d’autres programmes pour libérer du CPU.
