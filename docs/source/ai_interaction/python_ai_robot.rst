.. note::

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Approfondissez vos connaissances sur Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes post-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez et partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Remises spéciales** : Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et cadeaux** : Participez à des concours et des promotions de vacances.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ai_voice_assistant_robot:

20. Chien Assistant Vocal IA
============================

Cette leçon transforme votre Pidog en **chien assistant vocal alimenté par IA** 🐶.
Le robot peut se réveiller à votre voix, comprendre ce que vous dites, répondre avec personnalité,
et exprimer ses « émotions » à travers des mouvements, des gestes et des effets lumineux LED.

Vous construirez un **compagnon robotique entièrement interactif** en utilisant :

* **LLM** : Grand modèle de langage (p. ex., OpenAI GPT ou Doubao) pour une conversation naturelle.
* **STT** : Reconnaissance vocale (Speech-to-Text).
* **TTS** : Synthèse vocale (Text-to-Speech) pour des réponses vocales expressives.
* **Capteurs + Actions** : Détection ultrasonique, vision par caméra (optionnelle), capteurs tactiles et mouvements expressifs intégrés.

----

Avant de commencer
------------------

Assurez-vous d'avoir terminé :

* :ref:`install_all_modules` — Installez les modules ``robot-hat``, ``vilib``, ``pidog``, puis exécutez le script ``i2samp.sh``.
* :ref:`test_piper` — Vérifiez les langues prises en charge de **Piper TTS**.
* :ref:`test_vosk` — Vérifiez les langues prises en charge de **Vosk STT**.
* :ref:`py_online_llm` — Cette étape est **très importante** : obtenez votre clé API **OpenAI** ou **Doubao**, ou la clé API de tout autre LLM pris en charge.

Vous devriez déjà avoir :

* Un **microphone** et un **haut-parleur** fonctionnels sur votre Pidog.
* Une **clé API valide** stockée dans ``secret.py``.
* Une connexion réseau stable (une **connexion filaire** est recommandée pour une meilleure stabilité).

----

Exécuter l'exemple
------------------

Les deux versions linguistiques se trouvent dans le même répertoire :

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

Ce qui va se passer
--------------------

Lorsque vous exécutez cet exemple avec succès :

* Le robot **attend le mot de réveil** (p. ex., « Hey Buddy », « 你好 旺财 »).
* Lorsqu'il entend le mot de réveil :

  * La bande LED devient **rose (respirante)** comme indicateur de réveil.
  * Le robot vous salue avec la réponse de réveil définie —
    p. ex., « Hi there! » (via Piper TTS).

* Il commence ensuite **à écouter votre voix** via Vosk STT (ou accepte une saisie clavier si activée).

* Après avoir reconnu ce que vous avez dit, le système :

  * Capture une **image de la caméra** (car ``WITH_IMAGE = True``) et envoie votre message + image au **LLM** (OpenAI ``gpt-4o-mini``).
  * La LED passe au **jaune (écoute/traitement)** pendant que le modèle réfléchit.
  * La réponse du modèle est divisée en deux parties :

    - Texte avant ``ACTIONS:`` → prononcé à voix haute.
    - Mots-clés après ``ACTIONS:`` → associés aux mouvements du robot.

  * Le robot **exécute ces actions** via ``ActionFlow``.
  * Lorsque les actions se terminent, le robot **revient en position ASSISE** et éteint les LED.

* Si le **capteur ultrasonique détecte un obstacle** à moins de 10 cm :

  - Un message est injecté : ``<<<Ultrasonic sense too close: {distance}cm>>>``
  - Le robot recule automatiquement : ``ACTIONS: backward``
  - **L'entrée image est désactivée** pour ce tour.

* Si le **capteur tactile est déclenché** :

  - Pour un toucher **AIMÉ** (p. ex., FRONT_TO_REAR) :

    - Injection : ``<<<Touch style you like: FRONT_TO_REAR>>>``
    - ``ACTIONS: nod`` (réponse positive)

  - Pour un toucher **DÉTESTÉ** (p. ex., REAR_TO_FRONT) :

    - Injection : ``<<<Touch style you hate: REAR_TO_FRONT>>>``
    - ``ACTIONS: backward`` (réaction d'évitement)

* **Cycle des LED :**

  - ``on_start`` → position ASSISE, LED éteintes
  - ``before_listen`` → cyan (prêt)
  - ``before_think`` → jaune (traitement)
  - ``before_say`` → rose (parle)
  - ``after_say`` / ``on_finish_a_round`` → position ASSISE, LED éteintes
  - ``on_stop`` → arrête le flux d'actions et ferme les périphériques

**Exemple d'interaction**

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
   Robot: Ooooh, that's nice!
   ACTIONS: nod

   (Moving too close)
   Robot: Hey hey—too close! Backing up for safety.
   ACTIONS: backward


----

Passer à d'autres LLM ou TTS
-------------------------------

Vous pouvez facilement passer à d'autres LLM, TTS ou langues STT avec seulement quelques modifications :

* LLM pris en charge :

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Vérifiez les langues prises en charge de **Piper TTS**.
* :ref:`test_vosk` — Vérifiez les langues prises en charge de **Vosk STT**.

Pour changer, modifiez simplement la partie d'initialisation dans le code :

.. code-block:: python

  from pidog.llm import OpenAI as LLM

  llm = LLM(
      api_key=API_KEY,
      model="gpt-4o-mini",
  )

  # Set models and languages
  TTS_MODEL = "en_US-ryan-low"
  STT_LANGUAGE = "en-us"

----

Dépannage
--------------

* **Le robot ne répond pas au mot de réveil**

  * Vérifiez si le microphone fonctionne.
  * Assurez-vous que ``WAKE_ENABLE = True``.
  * Ajustez le mot de réveil pour correspondre à votre prononciation.

* **Aucun son du haut-parleur**

  * Vérifiez la configuration du modèle TTS.
  * Testez Piper ou Espeak manuellement.
  * Vérifiez la connexion du haut-parleur et le volume.

* **Erreur de clé API ou timeout**

  * Vérifiez votre clé dans ``secret.py``.
  * Assurez-vous de la connexion réseau.
  * Confirmez que le LLM est pris en charge.

* **Le capteur ultrasonique se déclenche de façon inattendue.**

  * Vérifiez la hauteur et l'angle d'installation du capteur.
  * Ajustez le seuil de distance ``TOO_CLOSE`` dans le code.
