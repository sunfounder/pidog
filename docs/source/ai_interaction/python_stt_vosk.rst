.. note::

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Approfondissez vos connaissances sur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez et partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Remises spéciales** : Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et cadeaux** : Participez à des concours et des promotions de vacances.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

16. STT avec Vosk (hors ligne)
==============================================

Vosk est un moteur léger de reconnaissance vocale (STT) qui prend en charge de nombreuses langues et fonctionne entièrement **hors ligne** sur Raspberry Pi.
Vous n'avez besoin d'un accès Internet qu'une seule fois pour télécharger un modèle de langue. Ensuite, tout fonctionne sans connexion réseau.

Dans cette leçon, nous allons :

* Vérifier le microphone sur Raspberry Pi.
* Installer et tester Vosk avec un modèle de langue de votre choix.

Avant de commencer
------------------

Assurez-vous d'avoir terminé :

* :ref:`install_all_modules` — Installez les modules ``robot-hat``, ``vilib``, ``pidog``, puis exécutez le script ``i2samp.sh``.

1. Vérifier votre microphone
-----------------------------

Avant d'utiliser la reconnaissance vocale, assurez-vous que votre microphone USB fonctionne correctement.

#. Listez les périphériques d'enregistrement disponibles :

   .. code-block:: bash

      arecord -l

   Recherchez une ligne comme ``card 1: ... device 0``.

#. Enregistrez un court échantillon (remplacez ``1,0`` par les numéros que vous avez trouvés) :

   .. code-block:: bash

      arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

   * Exemple : si votre périphérique est ``card 2, device 0``, utilisez :

   .. code-block:: bash

      arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

#. Écoutez-le pour confirmer l'enregistrement :

   .. code-block:: bash

      aplay test.wav

#. Ajustez le volume du microphone si nécessaire :

   .. code-block:: bash

      alsamixer

   * Appuyez sur **F6** pour sélectionner votre microphone USB.
   * Trouvez le canal **Mic** ou **Capture**.
   * Assurez-vous qu'il n'est pas muet (**[MM]** signifie muet, appuyez sur ``M`` pour activer le son → devrait afficher **[OO]**).
   * Utilisez les touches ↑ / ↓ pour modifier le volume d'enregistrement.


.. _test_vosk:

2. Tester Vosk
--------------------------

**Étapes pour essayer** :

#. Créez un nouveau fichier :

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_stt_vosk.py

#. Copiez-y le code d'exemple. Appuyez sur ``Ctrl+X``, puis ``Y``, et ``Enter`` pour enregistrer et quitter.

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

#. La première fois que vous exécutez ce code avec une nouvelle langue, Vosk **téléchargera automatiquement le modèle de langue** (par défaut, il téléchargera la version **small**).
   En même temps, il affichera également la liste des langues prises en charge. Ensuite, vous verrez :

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   Cela signifie :

   * Le fichier du modèle (``vosk-model-small-en-us-0.15``) a été téléchargé.
   * La liste des langues prises en charge a été affichée.
   * Le système écoute maintenant — dites quelque chose dans le microphone du Pidog, et le texte reconnu apparaîtra dans le terminal.

   **Conseils** :

   * Gardez le microphone à environ 15–30 cm de distance.
   * Choisissez un modèle qui correspond à votre langue et à votre accent.

**Mode flux (streaming) (optionnel)**

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

* **No such file or directory (lors de l'exécution de `arecord`)**

  Vous avez peut-être utilisé un mauvais numéro de carte/périphérique.
  Exécutez :

  .. code-block:: bash

     arecord -l

  et remplacez ``1,0`` par les numéros affichés pour votre microphone USB.

* **Le fichier enregistré n'a pas de son**

  Ouvrez le mélangeur et vérifiez le volume du microphone :

  .. code-block:: bash

     alsamixer

  * Appuyez sur **F6** pour sélectionner votre microphone USB.
  * Assurez-vous que **Mic/Capture** n'est pas muet (**[OO]** au lieu de **[MM]**).
  * Augmentez le niveau avec ↑.

* **Vosk ne reconnaît pas la parole**

  * Assurez-vous que le **code de langue** correspond à votre modèle (p. ex. ``en-us`` pour l'anglais, ``zh-cn`` pour le chinois).
  * Gardez le microphone à 15–30 cm et évitez le bruit de fond.
  * Parlez clairement et lentement.

* **Latence élevée / reconnaissance lente**

  * Le téléchargement automatique par défaut est un **petit modèle** (plus rapide, mais moins précis).
  * Si c'est encore lent, fermez les autres programmes pour libérer du CPU.
