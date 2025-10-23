.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

17. Conversation Textuelle avec Ollama
======================================

Dans cette leçon, vous allez apprendre à utiliser **Ollama**, un outil permettant d’exécuter localement de grands modèles de langage et de vision.  
Nous vous montrerons comment installer Ollama, télécharger un modèle et connecter Pidog à celui-ci.

Avant de Commencer
------------------

Assurez-vous d’avoir terminé :

* :ref:`install_all_modules` — Installer les modules ``robot-hat``, ``vilib``, ``Pidog``, puis exécuter le script ``i2samp.sh``.

.. _download_ollama:

1. Installer Ollama (LLM) et Télécharger un Modèle
--------------------------------------------------

Vous pouvez choisir où installer **Ollama** :

* Sur votre Raspberry Pi (exécution locale)  
* Ou sur un autre ordinateur (Mac/Windows/Linux) dans le **même réseau local**

**Modèles recommandés selon le matériel**

Vous pouvez choisir n’importe quel modèle disponible sur |link_ollama_hub|.  
Les modèles sont proposés en différentes tailles (3B, 7B, 13B, 70B...).  
Les modèles plus petits s’exécutent plus rapidement et nécessitent moins de mémoire, tandis que les plus grands offrent une meilleure qualité mais demandent un matériel plus puissant.

Consultez le tableau ci-dessous pour déterminer quelle taille de modèle convient à votre appareil.

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - Taille du modèle
     - RAM minimale requise
     - Matériel recommandé
   * - ~3B paramètres
     - 8 Go (16 Go préférable)
     - Raspberry Pi 5 (16 Go) ou PC/Mac de milieu de gamme
   * - ~7B paramètres
     - 16 Go+
     - Pi 5 (16 Go, limite) ou PC/Mac de milieu de gamme
   * - ~13B paramètres
     - 32 Go+
     - PC/Mac de bureau avec beaucoup de RAM
   * - 30B+ paramètres
     - 64 Go+
     - Station de travail / serveur / GPU recommandé
   * - 70B+ paramètres
     - 128 Go+
     - Serveur haut de gamme avec plusieurs GPU

**Installation sur Raspberry Pi**

Si vous souhaitez exécuter Ollama directement sur votre Raspberry Pi :

* Utilisez un **système Raspberry Pi OS 64 bits**  
* Fortement recommandé : **Raspberry Pi 5 (16 Go de RAM)**

Exécutez les commandes suivantes :

.. code-block:: bash

   # Installer Ollama
   curl -fsSL https://ollama.com/install.sh | sh

   # Télécharger un modèle léger (pour tester)
   ollama pull llama3.2:3b

   # Test rapide (tapez 'hi' puis Entrée)
   ollama run llama3.2:3b

   # Lancer l’API (port par défaut 11434)
   # Astuce : définir OLLAMA_HOST=0.0.0.0 pour autoriser l’accès depuis le LAN
   OLLAMA_HOST=0.0.0.0 ollama serve

**Installation sur Mac / Windows / Linux (Application de Bureau)**

1. Téléchargez et installez Ollama depuis |link_ollama|  

   .. image:: img/llm_ollama_download.png

2. Ouvrez l’application Ollama, allez dans le **sélecteur de modèles**, et utilisez la barre de recherche pour trouver un modèle. Par exemple, tapez ``llama3.2:3b`` (un modèle petit et léger pour commencer).

   .. image:: img/llm_ollama_choose.png

3. Une fois le téléchargement terminé, tapez quelque chose de simple comme « Hi » dans la fenêtre de chat, Ollama commencera automatiquement à le télécharger lors de la première utilisation.

   .. image:: img/llm_olama_llama_download.png

4. Allez dans **Settings** → activez **Expose Ollama to the network**. Cela permet à votre Raspberry Pi de s’y connecter via le réseau local.

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   Si vous voyez une erreur du type :

   ``Error: model requires more system memory ...``

   Cela signifie que le modèle est trop grand pour votre machine.  
   Utilisez un **modèle plus petit** ou passez sur un ordinateur avec plus de RAM.

2. Tester Ollama
----------------

Une fois Ollama installé et votre modèle prêt, vous pouvez le tester rapidement avec une boucle de chat minimale.

**Étapes**

#. Créez un nouveau fichier :

   .. code-block:: bash

      cd ~/pidog/examples
      nano test_llm_ollama.py

#. Collez le code suivant et enregistrez (``Ctrl+X`` → ``Y`` → ``Entrée``) :

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

   * Vous pouvez choisir **n’importe quel modèle** disponible sur |link_ollama_hub|, mais les modèles plus petits (par ex. ``moondream:1.8b``, ``phi3:mini``) sont recommandés si vous n’avez que 8 à 16 Go de RAM.  
   * Assurez-vous que le modèle spécifié dans le code correspond bien à celui que vous avez déjà téléchargé dans Ollama.  
   * Tapez ``exit`` ou ``quit`` pour arrêter le programme.  
   * Si vous ne pouvez pas vous connecter, assurez-vous qu’Ollama est en cours d’exécution et que les deux appareils sont sur le même LAN si vous utilisez un hôte distant.

Dépannage
---------

* **J’obtiens une erreur du type : `model requires more system memory ...`.**

  * Cela signifie que le modèle est trop volumineux pour votre appareil.  
  * Utilisez un modèle plus petit comme ``moondream:1.8b`` ou ``granite3.2-vision:2b``.  
  * Ou passez sur une machine avec plus de RAM et exposez Ollama au réseau.

* **Le code ne parvient pas à se connecter à Ollama (connexion refusée).**

  Vérifiez les points suivants :
  
  * Assurez-vous qu’Ollama est en cours d’exécution (``ollama serve`` ou que l’application de bureau est ouverte).  
  * Si vous utilisez un ordinateur distant, activez **Expose to network** dans les paramètres d’Ollama.  
  * Vérifiez que l’adresse ``ip="..."`` dans votre code correspond bien à l’adresse IP LAN correcte.  
  * Confirmez que les deux appareils sont bien sur le même réseau local.
