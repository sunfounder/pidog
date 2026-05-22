.. note::

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Approfondissez vos connaissances sur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez et partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Remises spéciales** : Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et cadeaux** : Participez à des concours et des promotions de vacances.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

17. Dialogue textuel avec Ollama
================================

Dans cette leçon, vous apprendrez à utiliser **Ollama**, un outil pour exécuter des modèles de langage et de vision localement.
Nous allons vous montrer comment installer Ollama, télécharger un modèle et connecter Pidog à celui-ci.

Avant de commencer
------------------

Assurez-vous d'avoir terminé :

* :ref:`install_all_modules` — Installez les modules ``robot-hat``, ``vilib``, ``Pidog``, puis exécutez le script ``i2samp.sh``.

.. _download_ollama:

1. Installer Ollama (LLM) et télécharger le modèle
----------------------------------------------------

Vous pouvez choisir où installer **Ollama** :

* Sur votre Raspberry Pi (exécution locale)
* Ou sur un autre ordinateur (Mac/Windows/Linux) sur le **même réseau local**

**Modèles recommandés selon le matériel**

Vous pouvez choisir n'importe quel modèle disponible sur |link_ollama_hub|.
Les modèles existent en différentes tailles (3B, 7B, 13B, 70B...).
Les modèles plus petits s'exécutent plus rapidement et nécessitent moins de mémoire, tandis que les modèles plus grands offrent une meilleure qualité mais nécessitent un matériel puissant.

Consultez le tableau ci-dessous pour décider quelle taille de modèle correspond à votre appareil.

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - Taille du modèle
     - RAM minimale requise
     - Matériel recommandé
   * - ~3B paramètres
     - 8 Go (16 Go mieux)
     - Raspberry Pi 5 (16 Go) ou PC/Mac milieu de gamme
   * - ~7B paramètres
     - 16 Go+
     - Pi 5 (16 Go, juste utilisable) ou PC/Mac milieu de gamme
   * - ~13B paramètres
     - 32 Go+
     - PC de bureau / Mac avec RAM élevée
   * - 30B+ paramètres
     - 64 Go+
     - Station de travail / Serveur / GPU recommandé
   * - 70B+ paramètres
     - 128 Go+
     - Serveur haut de gamme avec plusieurs GPU

**Installation sur Raspberry Pi**

Si vous souhaitez exécuter Ollama directement sur votre Raspberry Pi :

* Utilisez un **système d'exploitation Raspberry Pi 64 bits**
* Fortement recommandé : **Raspberry Pi 5 (16 Go de RAM)**

Exécutez les commandes suivantes :

.. code-block:: bash

   # Install Ollama
   curl -fsSL https://ollama.com/install.sh | sh

   # Pull a lightweight model (good for testing)
   ollama pull llama3.2:3b

   # Quick run test (type 'hi' and press Enter)
   ollama run llama3.2:3b

   # Serve the API (default port 11434)
   # Tip: set OLLAMA_HOST=0.0.0.0 to allow access from LAN
   OLLAMA_HOST=0.0.0.0 ollama serve

**Installation sur Mac / Windows / Linux (application de bureau)**

1. Téléchargez et installez Ollama depuis |link_ollama|

   .. image:: img/llm_ollama_download.png

2. Ouvrez l'application Ollama, allez dans le **Sélecteur de modèles** et utilisez la barre de recherche pour trouver un modèle. Par exemple, tapez ``llama3.2:3b`` (un modèle petit et léger pour commencer).

   .. image:: img/llm_ollama_choose.png

3. Une fois le téléchargement terminé, tapez quelque chose de simple comme « Hi » dans la fenêtre de discussion, Ollama commencera automatiquement à le télécharger lors de la première utilisation.

   .. image:: img/llm_olama_llama_download.png

4. Allez dans **Paramètres** → activez **Exposer Ollama au réseau**. Cela permet à votre Raspberry Pi de s'y connecter via le réseau local.

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   Si vous voyez une erreur comme :

   ``Error: model requires more system memory ...``

   Le modèle est trop grand pour votre machine.
   Utilisez un **modèle plus petit** ou passez à un ordinateur avec plus de RAM.

2. Tester Ollama
----------------

Une fois Ollama installé et votre modèle prêt, vous pouvez le tester rapidement avec une boucle de discussion minimale.

**Étapes**

#. Créez un nouveau fichier :

   .. code-block:: bash

      cd ~/pidog/examples
      nano test_llm_ollama.py

#. Collez le code suivant et enregistrez (``Ctrl+X`` → ``Y`` → ``Enter``) :

   .. code-block:: python

      from pidog.llm import Ollama

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      # If Ollama runs on the same Raspberry Pi, use "localhost".
      # If it runs on another computer in your LAN, replace with that computer's IP address.
      llm = Ollama(
          ip="localhost",
          model="llama3.2:3b"   # you can replace with any model
      )

      # Basic configuration
      llm.set_max_messages(20)
      llm.set_instructions(INSTRUCTIONS)
      llm.set_welcome(WELCOME)

      print(WELCOME)

      while True:
          text = input(">>> ")
          if text.strip().lower() in {"exit", "quit"}:
              break

          # Response with streaming output
          response = llm.prompt(text, stream=True)
          for token in response:
              if token:
                  print(token, end="", flush=True)
          print("")

#. Exécutez le programme :

   .. code-block:: bash

      python3 test_llm_ollama.py

#. Vous pouvez maintenant discuter avec Pidog directement depuis le terminal.


   * Vous pouvez choisir **n'importe quel modèle** disponible sur |link_ollama_hub|, mais les modèles plus petits (p. ex. ``moondream:1.8b``, ``phi3:mini``) sont recommandés si vous n'avez que 8 à 16 Go de RAM.
   * Assurez-vous que le modèle que vous spécifiez dans le code correspond au modèle que vous avez déjà téléchargé dans Ollama.
   * Tapez ``exit`` ou ``quit`` pour arrêter le programme.
   * Si vous ne pouvez pas vous connecter, assurez-vous qu'Ollama est en cours d'exécution et que les deux appareils sont sur le même réseau local si vous utilisez un hôte distant.


Dépannage
--------------


* **J'obtiens une erreur comme : `model requires more system memory ...`.**

  * Cela signifie que le modèle est trop grand pour votre appareil.
  * Utilisez un modèle plus petit comme ``moondream:1.8b`` ou ``granite3.2-vision:2b``.
  * Ou passez à une machine avec plus de RAM et exposez Ollama au réseau.

* **Le code ne peut pas se connecter à Ollama (connexion refusée).**

  Vérifiez les points suivants :

  * Assurez-vous qu'Ollama est en cours d'exécution (``ollama serve`` ou l'application de bureau est ouverte).
  * Si vous utilisez un ordinateur distant, activez **Exposer au réseau** dans les paramètres d'Ollama.
  * Vérifiez que ``ip="..."`` dans votre code correspond à la bonne adresse IP locale.
  * Confirmez que les deux appareils sont sur le même réseau local.
