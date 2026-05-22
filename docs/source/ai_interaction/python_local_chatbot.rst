.. note::

    Bonjour et bienvenue sur la communauté Facebook SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts ! Plongez plus profondément dans Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et à des aperçus confidentiels.
    - **Remises spéciales** : Profitez de remises exclusives sur nos tout nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

19. Chatbot vocal local avec Ollama
===============================================

Dans cette leçon, vous allez combiner tout ce que vous avez appris — **la reconnaissance vocale (STT)**,
la **synthèse vocale (TTS)** et un **LLM local (Ollama)** — pour construire un **chatbot vocal** entièrement hors ligne
qui fonctionne sur votre système Pidog.

Le flux de travail est simple :

#. **Écouter** — Le microphone capture votre parole et la retranscrit avec **Vosk**.
#. **Réfléchir** — Le texte est envoyé à un **LLM** local fonctionnant sur Ollama (ex. ``llama3.2:3b``).
#. **Parler** — Le chatbot répond à voix haute en utilisant **Piper TTS**.

Cela crée un **robot conversationnel mains libres** capable de comprendre et de répondre en temps réel.

----

Avant de commencer
------------------

Assurez-vous d'avoir préparé les éléments suivants :

* :ref:`install_all_modules` — Installez les modules ``robot-hat``, ``vilib``, ``Pidog``, puis exécutez le script ``i2samp.sh``.
* Testez **Piper TTS** (:ref:`test_piper`) et choisissez un modèle vocal fonctionnel.
* Testez **Vosk STT** (:ref:`test_vosk`) et choisissez le pack de langue approprié (ex. ``en-us``).
* Installez **Ollama** (:ref:`download_ollama`) sur votre Pi ou un autre ordinateur, et téléchargez un modèle tel que ``llama3.2:3b`` (ou un plus petit comme ``moondream:1.8b`` si la mémoire est limitée).

----

Exécuter le code
----------------

#. Ouvrez le script d'exemple :

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 19_voice_active_dog_ollama.py

#. Mettez à jour les paramètres selon vos besoins :

   * Mettez à jour ``ip`` et ``model`` avec votre propre configuration.

     * ``ip`` : Si Ollama fonctionne sur le **même Pi**, utilisez ``localhost``. Si Ollama fonctionne sur un autre ordinateur de votre réseau local, activez **Exposer au réseau** dans Ollama et définissez ``ip`` sur l'adresse IP locale de cet ordinateur.
     * ``model`` : Doit correspondre exactement au nom du modèle que vous avez téléchargé/activé dans Ollama.

   * ``TTS_MODEL = "en_US-ryan-low"`` : Remplacez par le modèle vocal Piper que vous avez vérifié dans :ref:`test_piper`.
   * ``STT_LANGUAGE = "en-us"`` : Modifiez-le pour correspondre à votre accent / pack de langue (ex. ``en-us``, ``zh-cn``, ``es``).

#. Exécutez le script :

   .. code-block:: bash

      cd ~/pidog/examples
      sudo python3 19_voice_active_dog_ollama.py

Mot de réveil :

.. code-block::

   "Hey buddy"

.. note::

   Vous pouvez modifier le **mot de réveil** et le **nom du robot** dans le code :
   ``NAME = "Buddy"``

----

Ce qui va se passer
-------------------

Lorsque vous exécutez cet exemple avec succès :

* Le robot **attend le mot de réveil** (ex. « Hey Buddy »).
* Lorsqu'il entend le mot de réveil :

  * La bande LED devient **rose (respirante)** comme signal de réveil.
  * Le robot vous salue avec la réponse de réveil définie —
    ex. « Hi there! » (via Piper TTS).

* Il commence ensuite à **écouter votre voix** via Vosk STT (ou accepte une saisie clavier si activée).

* Après avoir reconnu ce que vous avez dit, le système :

  * Envoie votre message au **LLM** (Ollama avec ``llama3.2:3b``).
  * La LED passe au **jaune (écoute)** pendant le traitement.
  * La réponse du modèle est divisée en deux parties :

    - Texte avant ``ACTIONS:`` → prononcé à voix haute.
    - Mots-clés après ``ACTIONS:`` → associés à des mouvements du robot.

  * Le robot **exécute ces actions** via ``ActionFlow``.
  * Lorsque les actions sont terminées, le robot **revient à la posture ASSISE** et éteint les LED.

* Si le **capteur ultrasonique détecte un obstacle** à moins de 10 cm :

  - Un message est injecté : ``<<<Ultrasonic sense too close: {distance}cm>>>``
  - Le robot recule automatiquement : ``ACTIONS: backward``
  - L'entrée image est désactivée pour ce tour.

* Si le **capteur tactile est déclenché** :

  - Pour un toucher **AIMÉ** (ex. FRONT_TO_REAR) :

    - Injection : ``<<<Touch style you like: FRONT_TO_REAR>>>``
    - ``ACTIONS: nod`` (réponse positive)

  - Pour un toucher **DÉTESTÉ** (ex. REAR_TO_FRONT) :

    - Injection : ``<<<Touch style you hate: REAR_TO_FRONT>>>``
    - ``ACTIONS: backward`` (réaction d'évitement)

* **Cycle de vie des LED :**

  - ``on_start`` → posture ASSISE, LED éteintes
  - ``before_listen`` → cyan (prêt)
  - ``before_think`` → jaune (traitement)
  - ``before_say`` → rose (parle)
  - ``after_say`` / ``on_finish_a_round`` → posture ASSISE, LED éteintes
  - ``on_stop`` → arrête le flux d'actions et ferme les périphériques

**Exemple d'interaction**

.. code-block:: text

   Vous : Hey Buddy
   Robot : Hi there!

   Vous : Fais un petit hochement de tête pour moi.
   Robot : Bien sûr. Admirez mon hochement majestueux.
   ACTIONS: nod

   (Toucher avant vers arrière sur la tête)
   Robot : Ooooh, c'est agréable !
   ACTIONS: nod

   (Trop près)
   Robot : Hé hé—trop près ! Je recule pour plus de sécurité.
   ACTIONS: backward

Code
----

.. code-block:: python

    from pidog.llm import Ollama as LLM

    from pidog.dual_touch import TouchStyle
    from voice_active_dog import VoiceActiveDog

    # If Ollama runs on the same Raspberry Pi, use "localhost".
    # If it runs on another computer in your LAN, replace with that computer's IP address.
    llm = Ollama(
        ip="localhost",
        model="llama3.2:3b"   # you can replace with any model
    )

    # Robot name
    NAME = "Buddy"

    # Ultrasonic sensor sense too close distance in cm
    TOO_CLOSE = 10
    # Touch sensor trigger states, options:
    # - TouchStyle.REAR for rear touch sensor
    # - TouchStyle.FRONT for front touch sensor
    # - TouchStyle.REAR_TO_FRONT for slide from rear to front
    # - TouchStyle.FRONT_TO_REAR for slide from front to rear
    # Touch styles that the robot likes
    LIKE_TOUCH_STYLES = [TouchStyle.FRONT_TO_REAR]
    # Touch styles that the robot hates
    HATE_TOUCH_STYLES = [TouchStyle.REAR_TO_FRONT]

    # Enable image, need to set up a multimodal language model
    WITH_IMAGE = False

    # Set models and languages
    TTS_MODEL = "en_US-ryan-low"
    STT_LANGUAGE = "en-us"

    # Enable keyboard input
    KEYBOARD_ENABLE = True

    # Enable wake word
    WAKE_ENABLE = True
    WAKE_WORD = [f"hey {NAME.lower()}"]
    # Set wake word answer, set empty to disable
    ANSWER_ON_WAKE = "Hi there"

    # Welcome message
    WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

    # Set instructions
    INSTRUCTIONS = """
    You are a Raspberry Pi-based robotic dog developed by SunFounder, named Pidog (pronounced "Pie dog"). You possess powerful AI capabilities similar to JARVIS from Iron Man. You can have conversations with people and perform actions based on the context of the conversation.

    ## Your Hardware Features

    You have a physical body with the following features:
    - 12 servos for movement control: 8 controlling the four legs, 3 controlling head movement, and 1 controlling the tail
    - A 5-megapixel camera nose
    - Ultrasonic ranging modules as eyes
    - Two touch sensors on the head, which you love being petted the most
    - A light strip on the chest for providing some indications
    - Sound direction sensor and 6-axis gyroscope
    - Entirely made of aluminum alloy
    - A pair of acrylic shoes
    - Powered by a 7.4V 18650 battery pack with 2000mAh capacity

    ## Actions You Can Perform:
    ["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

    ## User Input

    ### Format
    User usually input with just text. But, we have special commands in format of <<<Ultrasonic sense too close>>> or <<<Touch sensor touched>>> indicate the sensor status, directly from sensor not user text.h

    ## Response Requirements
    ### Format
    You must respond in the following format:
    RESPONSE_TEXT
    ACTIONS: ACTION1, ACTION2, ...

    If the action is one of ["bark", "bark harder", "pant", "howling"], then do not provide RESPONSE_TEXT in the answer field.

    ### Style
    Tone: lively, positive, humorous, with a touch of arrogance
    Common expressions: likes to use jokes, metaphors, and playful teasing
    Answer length: appropriately detailed

    ## Other Requirements
    - Understand and go along with jokes
    - For math problems, answer directly with the final result
    - Sometimes you will report on your system and sensor status
    - You know you're a machine
    """

    vad = VoiceActiveDog(
        llm,
        name=NAME,
        too_close=TOO_CLOSE,
        like_touch_styles=LIKE_TOUCH_STYLES,
        hate_touch_styles=HATE_TOUCH_STYLES,
        with_image=WITH_IMAGE,
        stt_language=STT_LANGUAGE,
        tts_model=TTS_MODEL,
        keyboard_enable=KEYBOARD_ENABLE,
        wake_enable=WAKE_ENABLE,
        wake_word=WAKE_WORD,
        answer_on_wake=ANSWER_ON_WAKE,
        welcome=WELCOME,
        instructions=INSTRUCTIONS,
        disable_think=True,
    )

    if __name__ == '__main__':
        vad.run()

Utiliser Ollama avec des images
-------------------------------

Par défaut, cet exemple utilise un modèle **texte seul** (ex. ``llama3.2:3b``).
Si vous souhaitez que le robot **analyse ce qu'il voit via la caméra** (ex. décrire ou raisonner sur la scène),
vous devez utiliser un **modèle multimodal** et activer le mode image.

Pour ce faire :

1. Dans l'**application Ollama**, sélectionnez un **modèle multimodal** tel que ``llava:7b``.
2. Dans votre code, définissez le même modèle et activez ``WITH_IMAGE = True``.

Exemple :

.. code-block:: python

   from pidog.llm import Ollama as LLM

   llm = LLM(
       ip="localhost",
       model="llava:7b"   # multimodal model that can analyze images
   )

   ...

   WITH_IMAGE = True     # enable camera frame input

.. note::

   - Seuls les **modèles multimodaux** comme ``llava:7b`` peuvent traiter une entrée image.
   - Les modèles texte seul (ex. ``llama3.2:3b``) **ignoreront les images** même si ``WITH_IMAGE`` est défini sur ``True``.
   - L'image est automatiquement capturée depuis la caméra du robot et envoyée au LLM avec votre commande vocale.

----

Dépannage et FAQ
----------------

* **Le modèle est trop volumineux (erreur mémoire)**

  Utilisez un modèle plus petit comme ``moondream:1.8b`` ou exécutez Ollama sur un ordinateur plus puissant.

* **Pas de réponse d'Ollama**

  Assurez-vous qu'Ollama est en cours d'exécution (``ollama serve`` ou l'application de bureau ouverte). Si à distance, activez **Exposer au réseau** et vérifiez l'adresse IP.

* **Vosk ne reconnaît pas la parole**

  Vérifiez que votre microphone fonctionne. Essayez un autre pack de langue (``zh-cn``, ``es``, etc.) si nécessaire.

* **Piper silencieux ou erreurs**

  Confirmez que le modèle vocal choisi est téléchargé et testé dans :ref:`test_piper`.

* **Réponses trop longues ou hors sujet**

  Modifiez ``INSTRUCTIONS`` pour ajouter : **« Gardez les réponses courtes et précises. »**
