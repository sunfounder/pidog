.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ai_voice_assistant_robot:

20. Chien Assistant Vocal IA
================================

Cette leçon transforme votre Pidog en un **chien assistant vocal alimenté par l’IA** 🐶.  
Le robot peut se réveiller à votre voix, comprendre ce que vous dites, répondre avec personnalité,  
et exprimer ses « émotions » à travers des mouvements, des gestes et des effets lumineux LED.

Vous allez construire un **compagnon robotique entièrement interactif** en utilisant :

* **LLM** : Large Language Model (par ex. OpenAI GPT ou Doubao) pour une conversation naturelle.  
* **STT** : Speech-to-Text pour la reconnaissance vocale.  
* **TTS** : Text-to-Speech pour des réponses vocales expressives.  
* **Capteurs + Actions** : Détection ultrasonique, vision par caméra (optionnelle), capteurs tactiles et mouvements expressifs intégrés.

----

Avant de Commencer
------------------

Assurez-vous d’avoir terminé :

* :ref:`install_all_modules` — Installer les modules ``robot-hat``, ``vilib``, ``pidog``, puis exécuter le script ``i2samp.sh``.  
* :ref:`test_piper` — Vérifier les langues prises en charge par **Piper TTS**.  
* :ref:`test_vosk` — Vérifier les langues prises en charge par **Vosk STT**.  
* :ref:`py_online_llm` — Cette étape est **très importante** : obtenez votre clé API **OpenAI** ou **Doubao**, ou la clé API d’un autre LLM pris en charge.

Vous devez déjà disposer de :

* Un **microphone** et un **haut-parleur** fonctionnels sur votre Pidog.  
* Une **clé API valide** enregistrée dans ``secret.py``.  
* Une connexion réseau stable (une **connexion filaire** est recommandée pour plus de stabilité).

----

Exécuter l’Exemple
------------------

Les deux versions linguistiques sont placées dans le même répertoire :

.. code-block:: bash

   cd ~/pidog/examples

**Version anglaise** (OpenAI GPT, instructions en anglais) :

.. code-block:: bash

   sudo python3 20_voice_active_dog_gpt.py

* LLM : ``OpenAI GPT-4o-mini``  
* TTS : ``en_US-ryan-low`` (Piper)  
* STT : Vosk (``en-us``)

Mot de réveil :

.. code-block::

   "Hey buddy"

---

**Version chinoise** (Doubao, instructions en chinois) :

.. code-block:: bash

   sudo python3 20_voice_active_dog_doubao_cn.py

* LLM : ``Doubao-seed-1-6-250615``  
* TTS : ``zh_CN-huayan-x_low`` (Piper)  
* STT : Vosk (``cn``)

Mot de réveil :

.. code-block::

   "你好 旺财"

.. note::

   Vous pouvez modifier le **mot de réveil** et le **nom du robot** dans le code :
   ``NAME = "Buddy"`` ou ``NAME = "旺财"``  
   ``WAKE_WORD = ["hey buddy"]`` ou ``WAKE_WORD = ["你好 旺财"]``

----

Ce qui va se Passer
-------------------

Lorsque vous exécutez cet exemple avec succès :

* Le robot **attend le mot de réveil** (par ex. « Hey Buddy », « 你好 旺财 »).  
* Lorsqu’il entend le mot de réveil :

  * La bande LED devient **rose (effet de respiration)** comme signal de réveil.  
  * Le robot vous salue avec la réponse de réveil définie —  
    par ex. « Salut ! » (via Piper TTS).

* Il commence ensuite à **écouter votre voix** grâce à Vosk STT (ou accepte une saisie clavier si activé).

* Après avoir reconnu ce que vous avez dit, le système :

  * Capture une **image de la caméra** (car ``WITH_IMAGE = True``) et envoie votre message + image au **LLM** (OpenAI ``gpt-4o-mini``).  
  * La LED passe en **jaune (écoute/traitement)** pendant que le modèle réfléchit.  
  * La réponse du modèle est divisée en deux parties :

    - Texte avant ``ACTIONS:`` → prononcé à voix haute.  
    - Mots-clés après ``ACTIONS:`` → associés aux mouvements du robot.

  * Le robot **exécute ces actions** via ``ActionFlow``.  
  * Lorsque les actions sont terminées, le robot **revient en posture ASSISE** et éteint les LEDs.

* Si le **capteur ultrason détecte un obstacle** à moins de 10 cm :

  - Un message est injecté : ``<<<Détection ultrason trop proche : {distance}cm>>>``  
  - Le robot recule automatiquement : ``ACTIONS: backward``  
  - **L’entrée image est désactivée** pour ce tour.

* Si le **capteur tactile est déclenché** :

  - Pour un **TOUCHER AIMÉ** (par ex. FRONT_TO_REAR) :

    - Injection : ``<<<Style de toucher apprécié : FRONT_TO_REAR>>>``  
    - ``ACTIONS: nod`` (réponse positive)

  - Pour un **TOUCHER DÉTESTÉ** (par ex. REAR_TO_FRONT) :

    - Injection : ``<<<Style de toucher détesté : REAR_TO_FRONT>>>``  
    - ``ACTIONS: backward`` (réaction d’évitement)

* **Cycle de vie des LEDs :**  

  - ``on_start`` → posture ASSISE, LEDs éteintes  
  - ``before_listen`` → cyan (prêt)  
  - ``before_think`` → jaune (en traitement)  
  - ``before_say`` → rose (en train de parler)  
  - ``after_say`` / ``on_finish_a_round`` → posture ASSISE, LEDs éteintes  
  - ``on_stop`` → arrêt du flux d’action et fermeture des périphériques

**Exemple d’interaction**

.. code-block:: text

   You: Hey Buddy
   Robot: Hi there!

   You: What do you see in front of you?
   Robot: I can see a notebook and a blue mug on the table.
   ACTIONS: think

   You: Do a little nod for me.
   Robot: Of course. Watch my majestic nod.
   ACTIONS: nod

   (Front-to-rear touch on the head)
   Robot: Ooooh, that’s nice!
   ACTIONS: nod

   (Moving too close)
   Robot: Hey hey—too close! Backing up for safety.
   ACTIONS: backward


----

Passer à d’Autres LLM ou TTS
----------------------------

Vous pouvez facilement passer à d’autres LLM, TTS ou langues STT avec seulement quelques modifications :

* LLM pris en charge :

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Vérifiez les langues prises en charge par **Piper TTS**.  
* :ref:`test_vosk` — Vérifiez les langues prises en charge par **Vosk STT**.  

Pour changer, modifiez simplement la partie d’initialisation dans le code :

.. code-block:: python

  from pidog.llm import OpenAI as LLM

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # Définir les modèles et les langues
  TTS_MODEL = "en_US-ryan-low"
  STT_LANGUAGE = "en-us"

----

Dépannage
---------

* **Le robot ne répond pas au mot de réveil**  

  * Vérifiez si le microphone fonctionne.  
  * Assurez-vous que ``WAKE_ENABLE = True``.  
  * Ajustez le mot de réveil pour correspondre à votre prononciation.

* **Aucun son ne sort du haut-parleur**
 
  * Vérifiez la configuration du modèle TTS.  
  * Testez Piper ou Espeak manuellement.  
  * Vérifiez la connexion et le volume du haut-parleur.

* **Erreur de clé API ou délai d’expiration (timeout)** 
 
  * Vérifiez votre clé dans ``secret.py``.  
  * Assurez la connexion réseau.  
  * Confirmez que le LLM est pris en charge.

* **Le capteur ultrason se déclenche de manière inattendue.**  

  * Vérifiez la hauteur et l’angle d’installation du capteur.  
  * Ajustez le seuil de distance ``TOO_CLOSE`` dans le code.
