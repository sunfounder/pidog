
Interaction avec l'IA à l'aide de GPT-4O
==============================================

Dans nos projets précédents, nous utilisions la programmation pour diriger Pidog dans des tâches prédéfinies, ce qui pouvait sembler un peu monotone. Ce projet introduit une avancée passionnante vers une interaction plus dynamique. Attention à ne pas essayer de tromper notre chien mécanique : il est désormais capable de comprendre bien plus qu'auparavant !

Cette initiative détaille toutes les étapes techniques nécessaires pour intégrer GPT-4O dans votre système, y compris la configuration des environnements virtuels, l'installation des bibliothèques essentielles, ainsi que la configuration des clés API et des identifiants d'assistant.

.. note::

   Ce projet nécessite l'utilisation de |link_openai_platform|, et vous devez souscrire un abonnement à OpenAI. De plus, l'API OpenAI est facturée séparément de ChatGPT, avec ses propres tarifs disponibles à l'adresse suivante : https://openai.com/api/pricing/.

   Vous devez donc décider si vous souhaitez poursuivre ce projet ou vous assurer que vous avez suffisamment financé l'API OpenAI.

Que vous ayez un microphone pour communiquer directement ou que vous préfériez taper dans une fenêtre de commande, les réponses de Pidog alimentées par GPT-4O vont certainement vous étonner !

Plongeons dans ce projet et découvrons un nouveau niveau d'interaction avec Pidog !

.. raw:: html

   <video controls style = "max-width:90%">
     <source src="_static/video/chatgpt4o.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>


1. Installation des packages et des dépendances nécessaires
--------------------------------------------------------------
.. note::
   Vous devez d'abord installer les modules nécessaires pour PiCar-X. Pour plus de détails, veuillez vous référer à : :ref:`install_all_modules`.
   
Dans cette section, nous allons créer et activer un environnement virtuel, y installer les packages et dépendances nécessaires. Cela garantit que les packages installés n'interfèrent pas avec le reste du système, tout en maintenant l'isolation des dépendances du projet et en évitant les conflits avec d'autres projets ou packages système.

#. Utilisez la commande ``python -m venv`` pour créer un environnement virtuel nommé ``my_venv``, en incluant les packages au niveau du système. L'option ``--system-site-packages`` permet à l'environnement virtuel d'accéder aux packages installés globalement, ce qui est utile lorsque des bibliothèques système sont nécessaires.

   .. code-block:: shell

      python -m venv --system-site-packages my_venv

#. Passez dans le répertoire ``my_venv`` et activez l'environnement virtuel avec la commande ``source bin/activate``. Le prompt de la console changera pour indiquer que l'environnement est actif.

   .. code-block:: shell

      cd my_venv
      source bin/activate

#. Installez maintenant les packages Python requis dans l'environnement activé. Ces packages seront isolés à cet environnement virtuel et n'affecteront pas les autres packages système.

   .. code-block:: shell

      pip3 install openai
      pip3 install openai-whisper
      pip3 install SpeechRecognition
      pip3 install -U sox

#. Enfin, utilisez la commande ``apt`` pour installer les dépendances système qui nécessitent des privilèges administrateur.

   .. code-block:: shell

      sudo apt install python3-pyaudio
      sudo apt install sox


2. Obtenez la clé API et l'ID de l'assistant
--------------------------------------------------

**Obtenir la clé API**

#. Rendez-vous sur |link_openai_platform| et cliquez sur le bouton **Create new secret key** en haut à droite.

   .. image:: img/apt_create_api_key.png
      :width: 700
      :align: center

#. Sélectionnez le propriétaire, le nom, le projet et les autorisations nécessaires, puis cliquez sur **Create secret key**.

   .. image:: img/apt_create_api_key2.png
      :width: 700
      :align: center

#. Une fois la clé générée, enregistrez-la dans un endroit sûr et accessible. Pour des raisons de sécurité, vous ne pourrez plus la visualiser à nouveau depuis votre compte OpenAI. Si vous perdez cette clé secrète, vous devrez en générer une nouvelle.

   .. image:: img/apt_create_api_key_copy.png
      :width: 700
      :align: center

**Obtenir l'ID de l'assistant**

#. Ensuite, cliquez sur **Assistants**, puis sur **Create**, en veillant à être sur la page **Dashboard**.

   .. image:: img/apt_create_assistant.png
      :width: 700
      :align: center

#. Placez le curseur ici pour copier l'**ID de l'assistant**, puis collez-le dans une boîte de texte ou ailleurs. Il s'agit de l'identifiant unique de cet Assistant.

   .. image:: img/apt_create_assistant_id.png
      :width: 700
      :align: center

#. Choisissez un nom au hasard, puis copiez le contenu suivant dans la zone **Instructions** pour décrire votre Assistant.

   .. image:: img/apt_create_assistant_instructions.png
      :width: 700
      :align: center

   .. code-block::

      Vous êtes un chien mécanique doté de puissantes capacités d'IA, semblable à JARVIS de Iron Man. Votre nom est Pidog. Vous pouvez discuter avec les gens et effectuer des actions en fonction du contexte de la conversation.

      ## actions you can do:
      ["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag_tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

      ## Response Format:
      {"actions": ["wag_tail"], "answer": "Hello, I am Pidog."}

      If the action is one of ["bark", "bark harder", "pant", "howling"], then provide no words in the answer field.

      ## Style de réponse
      Ton : vif, positif, humoristique, avec une touche d'arrogance.
      Expressions fréquentes : aime utiliser des blagues, des métaphores et des taquineries ludiques.
      Longueur de la réponse : suffisamment détaillée.

      ## Autres
      a. Comprend et s'adapte aux blagues.
      b. Pour les problèmes mathématiques, répondez directement avec le résultat final.
      c. Parfois, vous rapporterez votre état système et capteur.
      d. Vous savez que vous êtes une machine.
#. Pidog est équipé d'un module caméra que vous pouvez activer pour capturer des images de ce qu'il voit et les télécharger sur GPT en utilisant notre code d'exemple. Nous recommandons donc d'opter pour le modèle GPT-4O, qui dispose de capacités d'analyse d'images. Bien entendu, vous pouvez également choisir gpt-3.5-turbo ou d'autres modèles.

   .. image:: img/apt_create_assistant_model.png
      :width: 700
      :align: center

#. Cliquez maintenant sur **Playground** pour vérifier si votre compte fonctionne correctement.

   .. image:: img/apt_playground.png

#. Si vos messages ou images téléchargées sont envoyés avec succès et que vous recevez des réponses, cela signifie que votre compte n'a pas atteint la limite d'utilisation.

   .. image:: img/apt_playground_40.png
      :width: 700
      :align: center

#. Si vous rencontrez un message d'erreur après avoir saisi des informations, il est possible que vous ayez atteint votre limite d'utilisation. Veuillez vérifier votre tableau de bord d'utilisation ou les paramètres de facturation.

   .. image:: img/apt_playground_40mini_3.5.png
      :width: 700
      :align: center

3. Saisir la clé API et l'ID de l'assistant
-------------------------------------------------

#. Utilisez la commande suivante pour ouvrir le fichier ``keys.py``.

   .. code-block:: shell

      nano ~/pidog/gpt_examples/keys.py

#. Renseignez la clé API et l'ID de l'assistant que vous venez de copier.

   .. code-block:: shell

      OPENAI_API_KEY = "sk-proj-vEBo7Ahxxxx-xxxxx-xxxx"
      OPENAI_ASSISTANT_ID = "asst_ulxxxxxxxxx"

#. Appuyez sur ``Ctrl + X``, ``Y``, puis ``Entrée`` pour enregistrer le fichier et quitter.

4. Exécution de l'exemple
-----------------------------

Communication par texte
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si votre Pidog n'est pas équipé d'un microphone, vous pouvez utiliser la saisie de texte au clavier pour interagir avec lui en exécutant les commandes suivantes.

#. Exécutez maintenant les commandes suivantes en utilisant sudo, car le haut-parleur de Pidog ne fonctionnera pas sans cela. Le processus prendra un certain temps pour se terminer.

   .. code-block:: shell

      cd ~/pidog/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_dog.py --keyboard

#. Une fois les commandes exécutées avec succès, vous verrez le message suivant indiquant que tous les composants de Pidog sont prêts.

   .. code-block:: shell

      vilib 0.3.8 launching ...
      picamera2 0.3.19
      config_file: /home/pi2/.config/pidog/pidog.conf
      robot_hat init ... done
      imu_sh3001 init ... done
      rgb_strip init ... done
      dual_touch init ... done
      sound_direction init ... done
      sound_effect init ... done
      ultrasonic init ... done

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      input:

#. Un lien sera également fourni pour voir le flux vidéo de la caméra de Pidog sur votre navigateur web : ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Vous pouvez maintenant taper vos commandes dans la fenêtre du terminal et appuyer sur Entrée pour les envoyer. Les réponses de Pidog pourraient bien vous surprendre.

   .. note::
      
      Pidog doit recevoir votre saisie, l'envoyer à GPT pour traitement, recevoir la réponse, puis la lire via la synthèse vocale. Tout ce processus prend du temps, alors soyez patient.

   .. image:: img/apt_keyboard_input.png
      :width: 700
      :align: center

#. Si vous utilisez le modèle GPT-4O, vous pouvez également poser des questions basées sur ce que Pidog voit.

Communication vocale
^^^^^^^^^^^^^^^^^^^^^^^^^^

Si votre Pidog est équipé d'un microphone, ou si vous pouvez en acheter un en cliquant sur |link_microphone|, vous pouvez interagir avec Pidog en utilisant des commandes vocales.

#. Tout d'abord, vérifiez que le Raspberry Pi a détecté le microphone.

   .. code-block:: shell

      arecord -l

   Si c'est le cas, vous recevrez les informations suivantes, indiquant que votre microphone a bien été détecté.

   .. code-block:: 
      
      **** List of CAPTURE Hardware Devices ****
      card 3: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

#. Exécutez la commande suivante, puis parlez à Pidog ou faites du bruit. Le microphone enregistrera les sons dans le fichier ``op.wav``. Appuyez sur ``Ctrl + C`` pour arrêter l'enregistrement.

   .. code-block:: shell

      rec op.wav

#. Enfin, utilisez la commande ci-dessous pour lire le son enregistré et vérifier que le microphone fonctionne correctement.

   .. code-block:: shell

      sudo play op.wav

#. Exécutez maintenant les commandes suivantes avec sudo, car le haut-parleur de Pidog ne fonctionnera pas sans cela. Le processus prendra un certain temps pour se terminer.

   .. code-block:: shell

      cd ~/pidog/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_dog.py

#. Une fois les commandes exécutées avec succès, vous verrez le message suivant indiquant que tous les composants de Pidog sont prêts.

   .. code-block:: shell
      
      vilib 0.3.8 launching ...
      picamera2 0.3.19
      config_file: /home/pi2/.config/pidog/pidog.conf
      robot_hat init ... done
      imu_sh3001 init ... done
      rgb_strip init ... done
      dual_touch init ... done
      sound_direction init ... done
      sound_effect init ... done
      ultrasonic init ... done

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      listening ...

#. Un lien sera également fourni pour voir le flux vidéo de la caméra de Pidog sur votre navigateur web : ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Vous pouvez maintenant parler à Pidog, et ses réponses pourraient bien vous surprendre.

   .. note::
      
      Pidog doit recevoir votre saisie, la convertir en texte, l'envoyer à GPT pour traitement, recevoir la réponse, puis la lire via la synthèse vocale. Tout ce processus prend du temps, alors soyez patient.

   .. image:: img/apt_speech_input.png
      :width: 700
      :align: center

#. Si vous utilisez le modèle GPT-4O, vous pouvez également poser des questions basées sur ce que Pidog voit.

.. raw:: html

   <video controls style = "max-width:90%">
     <source src="_static/video/chatgpt4o.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>

5. Modifier les paramètres [optionnel]
-------------------------------------------
Dans le fichier ``gpt_dog.py``, localisez les lignes suivantes. Vous pouvez modifier ces paramètres pour configurer la langue STT, le gain de volume TTS et le rôle de la voix.

* **STT (Speech to Text)** fait référence au processus où le microphone du PiCar-X capte la parole et la convertit en texte à envoyer à GPT. Vous pouvez spécifier la langue pour une meilleure précision et une latence réduite dans cette conversion.
* **TTS (Text to Speech)** est le processus de conversion des réponses textuelles de GPT en parole, diffusée par le haut-parleur du PiCar-X. Vous pouvez ajuster le gain de volume et sélectionner un rôle vocal pour la sortie TTS.

.. code-block:: python

   # openai assistant init
   # =================================================================
   openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'PiDog')
   # LANGUAGE = ['zh', 'en'] # configurer le code de langue STT, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
   LANGUAGE = []
   VOLUME_DB = 3 # gain de volume TTS, de préférence inférieur à 5db
   # sélectionner le rôle vocal TTS, peut être "alloy, echo, fable, onyx, nova, et shimmer"
   # https://platform.openai.com/docs/guides/text-to-speech/supported-languages
   TTS_VOICE = 'nova'

* Variable ``LANGUAGE``:

  * Améliore la précision et le temps de réponse du Speech-to-Text (STT).
  * ``LANGUAGE = []`` signifie prendre en charge toutes les langues, mais cela peut réduire la précision du STT et augmenter la latence.
  * Il est recommandé de définir la/les langue(s) spécifique(s) à l'aide des codes de langue de |link_iso_language_code| pour améliorer les performances.

* Variable ``VOLUME_DB``:

  * Contrôle le gain appliqué à la sortie Text-to-Speech (TTS).
  * Augmenter la valeur augmentera le volume, mais il est préférable de maintenir la valeur en dessous de 5dB pour éviter les distorsions audio.

* Variable ``TTS_VOICE``:

  * Sélectionnez le rôle vocal pour la sortie Text-to-Speech (TTS).
  * Options disponibles: ``alloy, echo, fable, onyx, nova, shimmer``.
  * Vous pouvez expérimenter différentes voix depuis |link_voice_options| pour trouver celle qui convient à votre ton et à votre audience souhaitée. Les voix disponibles sont actuellement optimisées pour l'anglais.
