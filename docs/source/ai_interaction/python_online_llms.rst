.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_online_llm:

18. Connexion aux LLM en Ligne
==============================

Dans cette leçon, nous allons apprendre à connecter votre Pidog (ou Raspberry Pi) à différents **grands modèles de langage en ligne (LLM)**.  
Chaque fournisseur nécessite une clé API et propose différents modèles parmi lesquels vous pouvez choisir.

Nous allons voir comment :

* Créer et enregistrer vos clés API en toute sécurité.  
* Choisir un modèle adapté à vos besoins.  
* Exécuter notre code d’exemple pour discuter avec les modèles.

Allons-y étape par étape pour chaque fournisseur.

----

Avant de Commencer
------------------

Assurez-vous d’avoir terminé :

* :ref:`install_all_modules` — Installer les modules ``robot-hat``, ``vilib``, ``pidog``, puis exécuter le script ``i2samp.sh``.

OpenAI
------

OpenAI propose des modèles puissants comme **GPT-4o** et **GPT-4.1** qui peuvent être utilisés pour des tâches textuelles et visuelles.

Voici comment le configurer :

**Obtenir et Enregistrer votre Clé API**

#. Allez sur |link_openai_platform| et connectez-vous. Sur la page **API keys**, cliquez sur **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Remplissez les détails (Propriétaire, Nom, Projet et autorisations si nécessaire), puis cliquez sur **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Une fois la clé créée, copiez-la immédiatement — vous ne pourrez plus la voir ensuite. Si vous la perdez, vous devrez en générer une nouvelle.

   .. image:: img/llm_openai_copy.png

#. Dans votre dossier de projet (par exemple : ``/pidog/examples``), créez un fichier appelé ``secret.py`` :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Collez votre clé dans le fichier comme ceci :

   .. code-block:: python

       # secret.py
       # Conservez vos clés ici. Ne commitez jamais ce fichier sur Git.
       OPENAI_API_KEY = "sk-xxx"

**Activer la facturation et vérifier les modèles**

#. Avant d’utiliser la clé, allez sur la page **Billing** de votre compte OpenAI, ajoutez vos informations de paiement et créditez un petit montant.

   .. image:: img/llm_openai_billing.png

#. Ensuite, rendez-vous sur la page **Limits** pour vérifier quels modèles sont disponibles pour votre compte et copiez l’identifiant exact du modèle à utiliser dans votre code.

   .. image:: img/llm_openai_models.png

**Tester avec le code d’exemple**

#. Ouvrez le code d’exemple :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle souhaité (par exemple ``gpt-4o``) :

   .. code-block:: python

       from pidog.llm import OpenAI
       from secret import OPENAI_API_KEY
       
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
       
       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )

   Enregistrez et quittez (``Ctrl+X``, puis ``Y``, puis ``Entrée``).

#. Enfin, exécutez le test :


   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py
   

----

Gemini
------------------

Gemini est la famille de modèles d’IA de Google. Il est rapide et très efficace pour les tâches générales.

**Obtenir et Enregistrer votre Clé API**

#. Connectez-vous sur |link_google_ai|, puis accédez à la page des clés API.

   .. image:: img/llm_gemini_get.png

#. Cliquez sur le bouton **Create API key** en haut à droite.

   .. image:: img/llm_gemini_create.png

#. Vous pouvez créer une clé pour un projet existant ou en créer un nouveau.

   .. image:: img/llm_gemini_choose.png

#. Copiez la clé API générée.

   .. image:: img/llm_gemini_copy.png

#. Dans votre dossier de projet :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Collez la clé :

   .. code-block:: python

        # secret.py
        # Conservez vos clés ici. Ne commitez jamais ce fichier sur Git.
        GEMINI_API_KEY = "AIxxx"

**Vérifier les modèles disponibles**

Allez sur la page officielle |link_gemini_model|, où vous trouverez la liste des modèles, leurs identifiants exacts d’API, ainsi que les cas d’usage pour lesquels chacun est optimisé.

   .. image:: img/llm_gemini_model.png

**Tester avec le code d’exemple**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle souhaité (par exemple ``gemini-2.5-flash``) :

   .. code-block:: python

       from pidog.llm import Gemini
       from secret import GEMINI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Gemini(
           api_key=GEMINI_API_KEY,
           model="gemini-2.5-flash",
       )

#. Enregistrez et exécutez :


   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Qwen
------------------

Qwen est une famille de grands modèles de langage et multimodaux développée par Alibaba Cloud.  
Ces modèles prennent en charge la génération de texte, le raisonnement et la compréhension multimodale (comme l’analyse d’images).

**Obtenir une Clé API**

Pour appeler les modèles Qwen, vous avez besoin d’une **clé API**.  
La plupart des utilisateurs internationaux doivent utiliser la console **DashScope International (Model Studio)**.  
Les utilisateurs situés en Chine continentale peuvent utiliser la console **Bailian (百炼)**.

* **Pour les Utilisateurs Internationaux**

  #. Rendez-vous sur la page officielle |link_qwen_inter| sur **Alibaba Cloud**.  
  #. Connectez-vous ou créez un compte **Alibaba Cloud**.  
  #. Accédez à **Model Studio** (choisissez la région Singapour ou Pékin).
    
     * Si une invite « Activate Now » apparaît en haut de la page, cliquez dessus pour activer Model Studio et obtenir votre quota gratuit (Singapour uniquement).  
     * L’activation est gratuite — vous ne serez facturé qu’après l’utilisation de votre quota gratuit.  
     * Si aucune invite n’apparaît, le service est déjà activé.

  #. Allez sur la page **Key Management**. Dans l’onglet **API Key**, cliquez sur **Create API Key**.  
  #. Après la création, copiez votre clé API et conservez-la en lieu sûr.

    .. image:: img/llm_qwen_api_key.png
        :width: 800

  .. note::
     Les utilisateurs de Hong Kong, Macao et Taïwan doivent également choisir l’option **International (Model Studio)**.

* **Pour les Utilisateurs en Chine Continentale**

  Si vous êtes en Chine continentale, vous pouvez utiliser la console **Alibaba Cloud Bailian (百炼)** :

  #. Connectez-vous à |link_aliyun| (console Bailian) et effectuez la vérification de votre compte.  
  #. Sélectionnez **Create API Key**. Si un message indique que les services de modèle ne sont pas activés, cliquez sur **Activate**, acceptez les conditions et réclamez votre quota gratuit. Après activation, le bouton **Create API Key** sera disponible.

     .. image:: img/llm_qwen_aliyun_create.png

  #. Cliquez à nouveau sur **Create API Key**, vérifiez votre compte, puis cliquez sur **Confirm**.

     .. image:: img/llm_qwen_aliyun_confirm.png

  #. Une fois la clé créée, copiez-la.

     .. image:: img/llm_qwen_aliyun_copy.png

**Enregistrer votre Clé API**

#. Dans votre dossier de projet :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Collez votre clé ainsi :

   .. code-block:: python

        # secret.py
        # Conservez vos clés ici. Ne commitez jamais ce fichier sur Git.
        
        QWEN_API_KEY = "sk-xxx"

**Tester avec le Code d’Exemple**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle souhaité (par exemple ``qwen-plus``) :

   .. code-block:: python

      from pidog.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )

#. Exécutez avec :

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

Grok (xAI)
------------------
Grok est l’IA conversationnelle de xAI, créée par l’équipe d’Elon Musk. Vous pouvez vous y connecter via l’API xAI.

**Obtenir et Enregistrer votre Clé API**

#. Inscrivez-vous ici : |link_grok_ai|. Ajoutez des crédits à votre compte avant de continuer — sinon l’API ne fonctionnera pas.

#. Accédez à la page des clés API et cliquez sur **Create API key**.

   .. image:: img/llm_grok_create.png

#. Entrez un nom pour la clé, puis cliquez sur **Create API key**.

   .. image:: img/llm_grok_name.png

#. Copiez la clé générée et conservez-la en lieu sûr.

   .. image:: img/llm_grok_copy.png

#. Dans votre dossier de projet :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Collez votre clé comme ceci :

   .. code-block:: python

        # secret.py
        # Conservez vos clés ici. Ne commitez jamais ce fichier sur Git.
        
        GROK_API_KEY = "xai-xxx"

**Vérifier les modèles disponibles**

Allez sur la page « Models » dans la console xAI. Vous y trouverez tous les modèles disponibles pour votre équipe, ainsi que leurs identifiants exacts d’API — utilisez ces identifiants dans votre code.

   .. image:: img/llm_grok_model.png

**Tester avec le Code d’Exemple**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle souhaité (par exemple ``grok-4-latest``) :

   .. code-block:: python

       from pidog.llm import Grok
       from secret import GROK_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. Exécutez avec :

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

DeepSeek
------------------

DeepSeek est un fournisseur chinois de LLM offrant des modèles abordables et performants.

**Obtenir et Enregistrer votre Clé API**

#. Connectez-vous à |link_deepseek|.

#. Dans le menu en haut à droite, sélectionnez **API Keys → Create API Key**.

   .. image:: img/llm_deepseek_create.png

#. Entrez un nom, cliquez sur **Create**, puis copiez la clé.

   .. image:: img/llm_deepseek_copy.png

#. Dans votre dossier de projet :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Ajoutez votre clé :

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**Activer la Facturation**

Vous devrez recharger votre compte avant utilisation. Commencez par un petit montant (par exemple ¥10 RMB).

   .. image:: img/llm_deepseek_chognzhi.png

**Modèles Disponibles**

À la date du 12 septembre 2025, DeepSeek propose :

* ``deepseek-chat``  
* ``deepseek-reasoner``

**Tester avec le Code d’Exemple**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle souhaité (par exemple ``deepseek-chat``) :

   .. code-block:: python

       from pidog.llm import Deepseek
       from secret import DEEPSEEK_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Deepseek(
           api_key=DEEPSEEK_API_KEY,
           model="deepseek-chat",
           max_messages=20,
       )

#. Exécutez :

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

Doubao
------------------
Doubao est la plateforme de modèles d’IA de ByteDance (Volcengine Ark).

**Obtenir et Enregistrer votre Clé API**

#. Connectez-vous à |link_doubao|.

#. Dans le menu de gauche, descendez jusqu’à **API Key Management → Create API Key**.

   .. image:: img/llm_doubao_create.png

#. Choisissez un nom et cliquez sur **Create**.

   .. image:: img/llm_doubao_name.png

#. Cliquez sur l’icône **Show API Key** et copiez la clé.

   .. image:: img/llm_doubao_copy.png

#. Dans votre dossier de projet :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Ajoutez votre clé :

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**Choisir un Modèle**

#. Rendez-vous sur la place de marché des modèles et choisissez un modèle.

   .. image:: img/llm_doubao_model_select.png

#. Par exemple, choisissez **Doubao-seed-1.6**, puis cliquez sur **API 接入**.

   .. image:: img/llm_doubao_model.png

#. Sélectionnez votre clé API et cliquez sur **Use API**.

   .. image:: img/llm_doubao_use_api.png

#. Cliquez sur **Enable Model**.

   .. image:: img/llm_doubao_kaitong.png

#. Survolez l’ID du modèle pour le copier.

   .. image:: img/llm_doubao_copy_id.png

**Tester avec le Code d’Exemple**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle souhaité (par exemple ``doubao-seed-1-6-250615``) :

   .. code-block:: python

       from pidog.llm import Doubao
       from secret import DOUBAO_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. Exécutez avec :


   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py


Général
--------------

Ce projet prend en charge la connexion à plusieurs plateformes LLM via une interface unifiée.  
Nous avons intégré la compatibilité avec :

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)  
* **Gemini** (Google AI Studio / Vertex AI)  
* **Grok** (xAI)  
* **DeepSeek**  
* **Qwen (通义千问)**  
* **Doubao (豆包)**

En outre, vous pouvez vous connecter à **tout autre service LLM compatible avec le format d’API OpenAI**.  
Pour ces plateformes, vous devrez obtenir manuellement votre **clé API** et la **base_url** correcte.

**Obtenir et Enregistrer votre Clé API**

#. Obtenez une **clé API** depuis la plateforme que vous souhaitez utiliser. (Voir la console officielle de chaque plateforme pour plus de détails.)

#. Dans votre dossier de projet, créez un nouveau fichier :

   .. code-block:: bash

      cd ~/pidog/examples
      nano secret.py

#. Ajoutez votre clé dans ``secret.py`` :

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   Gardez votre clé API privée. Ne téléversez pas ``secret.py`` dans des dépôts publics.

**Tester avec le Code d’Exemple**

#. Ouvrez le fichier de test :

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 18.online_llm_test.py

#. Remplacez le contenu d’un fichier Python par l’exemple ci-dessous, et remplissez les champs ``base_url`` et ``model`` avec les valeurs correspondant à votre plateforme :

   .. note::

      À propos de ``base_url`` :  
      Nous prenons en charge le **format d’API OpenAI** ainsi que toute API **compatible**.  
      Chaque fournisseur a sa propre ``base_url``. Veuillez consulter leur documentation.

   .. code-block:: python

      from pidog.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # renseignez ici la base_url de votre fournisseur
          api_key=API_KEY,
          model="your-model-name-here",           # choisissez un modèle chez votre fournisseur
      )

#. Exécutez le programme :

   .. code-block:: bash

      python3 18.online_llm_test.py



