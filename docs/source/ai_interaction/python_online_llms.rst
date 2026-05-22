.. note::

    Bonjour et bienvenue sur la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des conseils et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos tout nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions de vacances.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur |link_sf_facebook| et rejoignez-nous dès aujourd'hui !

.. _py_online_llm:

18. Connexion aux LLM en Ligne
================================

Dans cette leçon, nous allons apprendre à connecter votre Pidog (ou Raspberry Pi) à différents **grands modèles de langage (LLM) en ligne**.
Chaque fournisseur nécessite une clé API et propose différents modèles parmi lesquels vous pouvez choisir.

Nous verrons comment :

* Créer et sauvegarder vos clés API en toute sécurité.
* Choisir un modèle adapté à vos besoins.
* Exécuter notre code d'exemple pour discuter avec les modèles.

Procédons étape par étape pour chaque fournisseur.

----

Avant de Commencer
------------------

Assurez-vous d'avoir terminé :

* :ref:`install_all_modules` — Installez les modules ``robot-hat``, ``vilib``, ``pidog``, puis exécutez le script ``i2samp.sh``.


OpenAI
----------

OpenAI propose des modèles puissants comme **GPT-4o** et **GPT-4.1** qui peuvent être utilisés pour des tâches de texte et de vision.

Voici comment configurer :

**Obtenir et sauvegarder votre clé API**

#. Allez sur |link_openai_platform| et connectez-vous. Sur la page **API keys**, cliquez sur **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Remplissez les détails (Propriétaire, Nom, Projet et autorisations si nécessaire), puis cliquez sur **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Une fois la clé créée, copiez-la immédiatement — vous ne pourrez plus la revoir. Si vous la perdez, vous devrez en générer une nouvelle.

   .. image:: img/llm_openai_copy.png

#. Dans votre dossier de projet (par exemple : ``/pidog/examples``), créez un fichier nommé ``secret.py`` :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Collez votre clé dans le fichier comme ceci :

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**Activer la facturation et vérifier les modèles**

#. Avant d'utiliser la clé, allez sur la page **Billing** de votre compte OpenAI, ajoutez vos informations de paiement et approvisionnez un petit montant de crédits.

   .. image:: img/llm_openai_billing.png

#. Ensuite, allez sur la page **Limits** pour vérifier quels modèles sont disponibles pour votre compte et copiez l'ID exact du modèle à utiliser dans votre code.

   .. image:: img/llm_openai_models.png

**Tester avec le code d'exemple**

#. Ouvrez le code d'exemple :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle souhaité (par exemple, ``gpt-4o``) :

   .. code-block:: python

       from pidog.llm import OpenAI
       from secret import OPENAI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )

   Sauvegardez et quittez (``Ctrl+X``, puis ``Y``, puis ``Enter``).

#. Enfin, lancez le test :

   .. code-block:: bash

       sudo python3 18.online_llm_test.py


----

Gemini
------------------

Gemini est la famille de modèles d'IA de Google. C'est rapide et excellent pour les tâches polyvalentes.

**Obtenir et sauvegarder votre clé API**

#. Connectez-vous à |link_google_ai|, puis allez sur la page des clés API.

   .. image:: img/llm_gemini_get.png

#. Cliquez sur le bouton **Create API key** dans le coin supérieur droit.

   .. image:: img/llm_gemini_create.png

#. Vous pouvez créer une clé pour un projet existant ou un nouveau projet.

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
        # Store secrets here. Never commit this file to Git.
       GEMINI_API_KEY = "AIxxx"

**Vérifier les modèles disponibles**

Allez sur la page officielle |link_gemini_model|, vous y verrez la liste des modèles, leurs identifiants API exacts et le cas d'utilisation pour lequel chacun est optimisé.

   .. image:: img/llm_gemini_model.png

**Tester avec le code d'exemple**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle souhaité (par exemple, ``gemini-2.5-flash``) :

   .. code-block:: python

       from pidog.llm import Gemini
       from secret import GEMINI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Gemini(
           api_key=GEMINI_API_KEY,
           model="gemini-2.5-flash",
       )

#. Sauvegardez et lancez :

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Qwen
------------------

Qwen est une famille de grands modèles de langage et de modèles multimodaux fournis par Alibaba Cloud.
Ces modèles prennent en charge la génération de texte, le raisonnement et la compréhension multimodale (comme l'analyse d'images).

**Obtenir une clé API**

Pour appeler les modèles Qwen, vous avez besoin d'une **clé API**.
La plupart des utilisateurs internationaux doivent utiliser la console **DashScope International (Model Studio)**.
Les utilisateurs de Chine continentale peuvent utiliser la console **Bailian (百炼)**.

* **Pour les utilisateurs internationaux**

  #. Allez sur la page officielle |link_qwen_inter| de **Alibaba Cloud**.
  #. Connectez-vous ou créez un compte **Alibaba Cloud**.
  #. Accédez à **Model Studio** (choisissez la région Singapour ou Pékin).

      * Si une invite "Activate Now" apparaît en haut de la page, cliquez dessus pour activer Model Studio et recevoir le quota gratuit (Singapour uniquement).
      * L'activation est gratuite — vous ne serez facturé qu'après utilisation de votre quota gratuit.
      * Si aucune invite d'activation n'apparaît, le service est déjà actif.

  #. Allez sur la page **Key Management**. Dans l'onglet **API Key**, cliquez sur **Create API Key**.
  #. Après la création, copiez votre clé API et conservez-la en lieu sûr.

    .. image:: img/llm_qwen_api_key.png
        :width: 800

  .. note::
     Les utilisateurs de Hong Kong, Macao et Taiwan doivent également choisir l'option **International (Model Studio)**.

* **Pour les utilisateurs de Chine continentale**

  Si vous êtes en Chine continentale, vous pouvez utiliser la console **Alibaba Cloud Bailian (百炼)** :

  #. Connectez-vous à |link_aliyun| (console Bailian) et complétez la vérification du compte.
  #. Sélectionnez **Create API Key**. Si un message indique que les services de modèle ne sont pas activés, cliquez sur **Activate**, acceptez les conditions et réclamez votre quota gratuit. Après activation, le bouton **Create API Key** sera activé.

     .. image:: img/llm_qwen_aliyun_create.png

  #. Cliquez à nouveau sur **Create API Key**, vérifiez votre compte, puis cliquez sur **Confirm**.

     .. image:: img/llm_qwen_aliyun_confirm.png

  #. Une fois créée, copiez votre clé API.

     .. image:: img/llm_qwen_aliyun_copy.png

**Sauvegarder votre clé API**

#. Dans votre dossier de projet :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Collez votre clé comme ceci :

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.

        QWEN_API_KEY = "sk-xxx"

**Tester avec le code d'exemple**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle souhaité (par exemple, ``qwen-plus``) :

   .. code-block:: python

      from pidog.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )


#. Lancez avec :

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

Grok (xAI)
------------------
Grok est l'IA conversationnelle de xAI, créée par l'équipe d'Elon Musk. Vous pouvez vous y connecter via l'API xAI.

**Obtenir et sauvegarder votre clé API**

#. Inscrivez-vous pour un compte ici : |link_grok_ai|. Ajoutez d'abord des crédits à votre compte — sinon l'API ne fonctionnera pas.

#. Allez sur la page API Keys, cliquez sur **Create API key**.

   .. image:: img/llm_grok_create.png

#. Saisissez un nom pour la clé, puis cliquez sur **Create API key**.

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
        # Store secrets here. Never commit this file to Git.

        GROK_API_KEY = "xai-xxx"

**Vérifier les modèles disponibles**

Allez sur la page Models de la console xAI. Vous y verrez tous les modèles disponibles pour votre équipe, ainsi que leurs identifiants API exacts — utilisez ces identifiants dans votre code.

   .. image:: img/llm_grok_model.png

**Tester avec le code d'exemple**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle souhaité (par exemple, ``grok-4-latest``) :

   .. code-block:: python

       from pidog.llm import Grok
       from secret import GROK_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. Lancez avec :

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

DeepSeek
------------------

DeepSeek est un fournisseur chinois de LLM qui propose des modèles abordables et performants.

**Obtenir et sauvegarder votre clé API**

#. Connectez-vous à |link_deepseek|.

#. Dans le menu en haut à droite, sélectionnez **API Keys → Create API Key**.

   .. image:: img/llm_deepseek_create.png

#. Saisissez un nom, cliquez sur **Create**, puis copiez la clé.

   .. image:: img/llm_deepseek_copy.png

#. Dans votre dossier de projet :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Ajoutez votre clé :

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**Activer la facturation**

Vous devez d'abord recharger votre compte. Commencez par un petit montant (comme 10 RMB).

   .. image:: img/llm_deepseek_chognzhi.png

**Modèles disponibles**

Au moment de la rédaction (2025-09-12), DeepSeek propose :

* ``deepseek-chat``
* ``deepseek-reasoner``

**Tester avec le code d'exemple**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle souhaité (par exemple, ``deepseek-chat``) :

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

#. Lancez :

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Doubao
------------------
Doubao est la plateforme de modèles d'IA de ByteDance (Volcengine Ark).

**Obtenir et sauvegarder votre clé API**

#. Connectez-vous à |link_doubao|.

#. Dans le menu de gauche, faites défiler jusqu'à **API Key Management → Create API Key**.

   .. image:: img/llm_doubao_create.png

#. Choisissez un nom et cliquez sur **Create**.

   .. image:: img/llm_doubao_name.png

#. Cliquez sur l'icône **Show API Key** et copiez-la.

   .. image:: img/llm_doubao_copy.png

#. Dans votre dossier de projet :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Ajoutez votre clé :

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**Choisir un modèle**

#. Allez sur le marketplace de modèles et choisissez un modèle.

   .. image:: img/llm_doubao_model_select.png

#. Par exemple, choisissez **Doubao-seed-1.6**, puis cliquez sur **API 接入**.

   .. image:: img/llm_doubao_model.png

#. Sélectionnez votre clé API et cliquez sur **Use API**.

   .. image:: img/llm_doubao_use_api.png

#. Cliquez sur **Enable Model**.

   .. image:: img/llm_doubao_kaitong.png

#. Survolez l'ID du modèle pour le copier.

   .. image:: img/llm_doubao_copy_id.png

**Tester avec le code d'exemple**

#. Ouvrez le fichier de test :

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Remplacez le contenu par le code ci-dessous, et mettez à jour ``model="xxx"`` avec le modèle souhaité (par exemple, ``doubao-seed-1-6-250615``) :

   .. code-block:: python

       from pidog.llm import Doubao
       from secret import DOUBAO_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. Lancez avec :

   .. code-block:: bash

       sudo python3 18.online_llm_test.py


General
--------------

Ce projet prend en charge la connexion à plusieurs plateformes LLM via une interface unifiée.
Nous avons une compatibilité intégrée avec :

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)
* **Gemini** (Google AI Studio / Vertex AI)
* **Grok** (xAI)
* **DeepSeek**
* **Qwen (通义千问)**
* **Doubao (豆包)**

De plus, vous pouvez vous connecter à **tout autre service LLM compatible avec le format de l'API OpenAI**.
Pour ces plateformes, vous devrez obtenir manuellement votre **clé API** et le **base_url** correct.

**Obtenir et sauvegarder votre clé API**

#. Obtenez une **clé API** auprès de la plateforme que vous souhaitez utiliser. (Consultez la console officielle de chaque plateforme pour plus de détails.)

#. Dans votre dossier de projet, créez un nouveau fichier :

   .. code-block:: bash

      cd ~/pidog/examples
      nano secret.py

#. Ajoutez votre clé dans ``secret.py`` :

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   Gardez votre clé API privée. Ne téléchargez pas ``secret.py`` dans des dépôts publics.

**Tester avec le code d'exemple**

#. Ouvrez le fichier de test :

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 18.online_llm_test.py

#. Remplacez le contenu d'un fichier Python par l'exemple suivant, et remplissez le ``base_url`` et le ``model`` corrects pour votre plateforme :

   .. note::

      À propos de ``base_url`` :
      Nous prenons en charge le **format API OpenAI**, ainsi que toute API qui lui est **compatible**.
      Chaque fournisseur a son propre ``base_url``. Veuillez consulter sa documentation.

   .. code-block:: python

      from pidog.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # fill in your provider's base_url
          api_key=API_KEY,
          model="your-model-name-here",           # choose a model from your provider
      )


#. Lancez le programme :

   .. code-block:: bash

      python3 18.online_llm_test.py
