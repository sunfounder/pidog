.. _pidog_skill:

.. start_using_pidog

21. Utiliser OpenClaw pour contrôler PiDog
============================================


**Qu'est-ce qu'OpenClaw ?**

Considérez-le comme une version améliorée de ChatGPT. Alors que les chatbots traditionnels ne peuvent que parler (générer du texte), OpenClaw peut agir. Il comprend vos instructions en langage naturel et peut effectuer des opérations sur votre ordinateur, comme exécuter des commandes, gérer des fichiers et appeler divers outils.

Voici quelques scénarios d'application fantastiques :

* **Assistant personnel polyvalent :** Laissez-le vous aider à gérer votre emploi du temps, définir des rappels et suivre des tâches. Vous n'avez qu'à le lui dire dans une application de messagerie (comme Telegram, WhatsApp), et il s'en souviendra et exécutera.
* **« Colle » d'automatisation :** Il peut servir de liant pour vos différents services. Par exemple, vous pouvez lui demander de surveiller un site web pour détecter des changements de prix. Dès qu'une baisse de prix est détectée, il peut automatiquement déclencher un workflow d'automatisation n8n pour vous envoyer une notification par e-mail.
* **Assistant de développement dédié :** Demandez-lui de vous aider à gérer des serveurs, exécuter des scripts et vérifier des journaux. Vous pouvez simplement dire « Vérifie la charge système pour moi », et il peut se connecter en SSH à votre serveur, exécuter la commande et vous renvoyer les résultats.
* **« Compagnon de jeu » matériel :** C'est un cas d'utilisation très intéressant. Vous pouvez demander à OpenClaw de contrôler du matériel connecté à un Raspberry Pi. Par exemple, un développeur l'a utilisé pour contrôler un aspirateur robot équipé d'un bras mécanique, ou même pour analyser les données d'un simulateur de course et les afficher sur un écran LED. L'équipe officielle de Raspberry Pi l'a même utilisé pour construire un photomaton automatique pour un mariage, simplement par la conversation, sans écrire une seule ligne de code !


.. important::

   Le Raspberry Pi Zero 2W ne dispose que de 512 Mo de RAM, alors qu'OpenClaw nécessite un minimum de 1 Go. Il ne peut donc pas fonctionner correctement. Un Raspberry Pi 4/5 ou supérieur est recommandé.

Démarrage rapide d'OpenClaw
------------------------------

Si vous souhaitez découvrir la puissance d'OpenClaw aussi rapidement que possible, utilisez cette méthode. Elle installera et lancera automatiquement un assistant de configuration interactif.

1.  Ouvrez le terminal sur votre Raspberry Pi et exécutez directement la commande suivante. Cette commande télécharge le script d'installation depuis le site officiel et l'exécute :

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash

    .. note:: Comme les nouvelles versions sont mises à jour rapidement, il est normal que vos étapes d'installation diffèrent légèrement.

2.  Le script téléchargera et installera automatiquement OpenClaw.

    .. image:: /img/openclaw/install_open_claw.png


3.  Vous verrez ensuite une invite de sécurité vous demandant si vous faites confiance à OpenClaw. Une fois que vous êtes sûr qu'il est sûr et fiable, utilisez les touches fléchées pour naviguer jusqu'à « Yes » et appuyez sur Entrée.

    .. image:: /img/openclaw/security_open_claw.png


4.  Sélectionnez Quick Start, puis appuyez sur Entrée.

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  Sélectionnez votre modèle, puis appuyez sur Entrée. Nous utilisons OpenAI comme exemple ici.

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  Sélectionnez OpenAI API Key.

    .. image:: /img/openclaw/api_key_open_claw.png

7.  Collez la clé API maintenant.

    .. image:: /img/openclaw/paste_api_key_open_claw.png

.. |link_openai_platform| raw:: html

    <a href="https://platform.openai.com/settings/organization/api-keys" target="_blank">OpenAI Platform</a>

8.  Accédez à |link_openai_platform| et connectez-vous. Sur la page **API keys**, cliquez sur **Create new secret key**.

    .. image:: /img/openclaw/llm_openai_create.png

9.  Remplissez les détails (Owner, Name, Project et les permissions si nécessaire), puis cliquez sur **Create secret key**.

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. Une fois la clé créée, copiez-la immédiatement — vous ne pourrez plus la revoir. Si vous la perdez, vous devrez en générer une nouvelle.

    .. image:: /img/openclaw/llm_openai_copy.png

11. Collez la clé dans la configuration d'OpenClaw.

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. Sélectionnez le modèle que vous souhaitez utiliser. Dans cet exemple, nous utiliserons **Keep current**.

    .. image:: /img/openclaw/model_config_open_claw.png

13. Vient ensuite la sélection du canal. Les canaux font référence aux services de communication pris en charge par OpenClaw, tels que Telegram, WhatsApp, Discord, etc. Utilisez la flèche vers le bas pour sélectionner l'option « Skip for now », puis appuyez sur Entrée.

    .. image:: /img/openclaw/channel_open_claw.png

14. Ensuite, vous serez invité à configurer des compétences immédiatement. Sélectionnez « Yes » et appuyez sur Entrée.

    .. image:: /img/openclaw/config_skill_open_claw.png

15. Installez les compétences dont vous avez besoin. Dans l'exemple suivant, nous sélectionnons l'option « Skip for now » (appuyez sur la barre d'espace pour sélectionner), puis appuyez sur Entrée.

    .. image:: /img/openclaw/install_skill_open_claw.png


16. Ensuite, les Hooks ; nous allons cocher « command-logger » et « session-memory ».

    .. image:: /img/openclaw/hooks2_open_claw.png


17. L'installation est maintenant terminée. Vous pouvez démarrer OpenClaw en sélectionnant « Hatch in TUI » et en appuyant sur Entrée.

   .. image:: /img/openclaw/hatch_open_claw.png


.. note::

   Vous pouvez démarrer OpenClaw en entrant la commande suivante :

    .. code-block:: bash

       openclaw tui

   Et vous pouvez appuyer deux fois sur ctrl+c pour quitter l'interface TUI.

------------------------------------------------------------------------

Faire fonctionner PiDog avec OpenClaw
----------------------------------------------

**Qu'est-ce que PiDog Skill ?**

PiDog Skill est une extension pour OpenClaw qui vous permet de contrôler votre robot chien SunFounder PiDog V2 en langage naturel. Au lieu de vous souvenir de paramètres de ligne de commande complexes, vous pouvez simplement dire à OpenClaw ce que vous voulez que PiDog fasse — comme « fais asseoir le chien » ou « mets les lumières LED en violet » — et OpenClaw exécutera automatiquement les commandes appropriées.

Voici quelques choses que vous pouvez faire avec PiDog Skill :

* **Actions de base :** Faire tenir PiDog debout, assis, couché, remuer la queue, aboyer, avancer/reculer ou tourner à gauche/droite
* **Maintien de posture :** Garder PiDog dans une posture spécifique (comme debout) pendant des périodes prolongées
* **Contrôle des lumières LED :** Changer les couleurs des yeux avec des effets comme respiration, écoute, éclat ou lumière fixe
* **Personnalisation des couleurs :** Choisissez parmi rouge, vert, bleu, jaune, violet, rose, cyan, blanc, orange ou des codes hexadécimaux personnalisés

----------------------------------------------------------------

Prérequis
------------------------------

Avant de pouvoir utiliser PiDog Skill avec OpenClaw, assurez-vous d'avoir :

1. **PiDog V2** correctement assemblé et connecté à votre Raspberry Pi
2. **OpenClaw** installé et en cours d'exécution
3. Les répertoires suivants existent sur votre système :

   - ``~/pidog``
   - ``~/robot-hat``
   - ``~/vilib``

Vous pouvez vérifier l'installation en exécutant :

.. code-block:: bash

   python3 -c "import pidog"

Si cette commande s'exécute sans erreur, vous êtes prêt à continuer.

----------------------------------------------------------------

Installer PiDog Skill
------------------------------

Suivez ces étapes pour installer PiDog Skill pour OpenClaw :

1. **Créez le répertoire des compétences** (s'il n'existe pas déjà) :

   .. code-block:: bash

      mkdir -p ~/.openclaw/workspace/skills/

2. **Copiez les fichiers PiDog Skill** dans le répertoire des compétences d'OpenClaw :

   .. code-block:: bash

      cp -r ~/pidog/pidog-control ~/.openclaw/workspace/skills/pidog-control/

   .. note:: Remplacez ``~/pidog-skill`` par le chemin réel où se trouvent vos fichiers PiDog Skill.

3. **Vérifiez l'installation** en vérifiant les fichiers de compétences :

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/pidog-control/scripts/

   Vous devriez voir ``pidog_ctl.py`` et ``pidog_rgb_ctl.py`` dans la sortie.

----------------------------------------------------------------

Tester PiDog Skill
------------------------------

Avant d'utiliser la compétence avec OpenClaw, il est recommandé de tester les fonctionnalités de base directement depuis le terminal.

**Étape 1 : Vérifier l'état de PiDog**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py status

**Étape 2 : Exécuter un test sécurisé**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py safe-test

**Étape 3 : Tester les actions de base**

Faire asseoir PiDog :

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action sit

Faire tenir PiDog debout et maintenir la posture :

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action stand --hold

Faire aboyer PiDog :

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py action bark

**Étape 4 : Tester les lumières LED**

Tester l'effet d'éclat avec la couleur violette :

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple

Tester d'autres effets lumineux :

.. code-block:: bash

   # Effet de respiration avec couleur rouge
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light breath --color red

   # Effet d'écoute avec couleur bleue
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light listen --color blue

   # Éteindre les lumières
   python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light off

----------------------------------------------------------------

Utiliser PiDog Skill dans OpenClaw
----------------------------------

Une fois que vous avez vérifié que PiDog Skill fonctionne depuis la ligne de commande, vous pouvez commencer à l'utiliser dans OpenClaw.

1. **Lancez OpenClaw TUI** :

   .. code-block:: bash

      openclaw tui

2. **Envoyez des commandes en langage naturel** pour contrôler PiDog. Voici quelques exemples :

   * « Fais asseoir le chien »
   * « Fais tenir PiDog debout et reste »
   * « Remue la queue du chien »
   * « Fais aboyer le chien »
   * « Mets les lumières LED en violet avec l'effet d'éclat »
   * « Règle les lumières des yeux sur l'effet de respiration en rouge »
   * « Fais avancer PiDog »

3. **OpenClaw traduira automatiquement** votre demande en la commande appropriée et l'exécutera sur PiDog.

----------------------------------------------------------------

Actions et commandes disponibles
--------------------------------

Voici la liste complète des actions prises en charge par PiDog Skill :

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Action
     - Description
   * - stand
     - Faire tenir PiDog debout
   * - sit
     - Faire asseoir PiDog
   * - lie
     - Faire coucher PiDog
   * - wag-tail
     - Remuer la queue de PiDog
   * - bark
     - Faire aboyer PiDog
   * - forward
     - Avancer
   * - backward
     - Reculer


**Maintien de posture :**

Ajoutez ``--hold`` à n'importe quelle action pour garder PiDog dans cette posture. Par exemple : « stand --hold »

**Effets lumineux :**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Effet
     - Description
   * - off
     - Éteindre toutes les lumières LED
   * - breath
     - Effet de respiration/pulsation douce
   * - listen
     - Mode d'écoute réactif
   * - boom
     - Effet d'éclat dynamique (le plus visible)
   * - solid
     - Lumière fixe constante (utilisez boom pour un meilleur effet)

**Couleurs prises en charge :**

rouge, vert, bleu, jaune, violet, rose, cyan, blanc, orange ou codes hexadécimaux comme ``#FF5733``

----------------------------------------------------------------

Dépannage
------------------------------

Problèmes OpenClaw
^^^^^^^^^^^^^^^^^^^^^^^^

Q. Pendant l'installation, j'obtiens l'erreur ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. Que dois-je faire ?

   Vous pouvez ignorer cela pour le moment, mais vous pourriez rencontrer des problèmes dans les étapes suivantes. Veuillez vous y référer un par un à ce moment-là.


Q. Lorsque j'exécute ``openclaw tui``, j'obtiens l'erreur ``-bash: openclaw: command not found``. Que dois-je faire ?

   Exécutez la commande suivante :

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   Vous devriez maintenant pouvoir démarrer l'interface TUI avec ``openclaw tui``.



Q. Dans ``openclaw tui``, je rencontre ``not connected to gateway — message not sent`` ou le message ``gateway disconnected: closed``.

   Cela signifie que votre service OpenClaw Gateway n'est pas démarré. Ouvrez un autre terminal et exécutez la commande suivante pour démarrer l'OpenClaw Gateway :

   .. code-block:: bash

      openclaw gateway

   Ensuite, redémarrez ``openclaw tui``, et vous pourrez l'utiliser directement.


Q. Je souhaite configurer le service OpenClaw Gateway pour qu'il s'exécute en arrière-plan / démarre automatiquement au démarrage. Comment faire ?

   Normalement, votre service OpenClaw Gateway devrait démarrer automatiquement au démarrage. Si ce n'est pas le cas, vous pouvez le démarrer manuellement avec les commandes suivantes.

   1. Créez le répertoire ``~/.config/systemd/user`` :

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. Créez le fichier ``openclaw-gateway.service`` :

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF


   3. Ensuite, rechargez la configuration systemd :

   .. code-block:: bash

      systemctl --user daemon-reload

   4. Démarrez le service :

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   À ce stade, redémarrez ``openclaw tui``, et vous pourrez l'utiliser directement.

   5. Activez-le pour qu'il démarre au démarrage :

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


Q. Mon OpenClaw ne peut pas agir sur le système, que dois-je faire ?

   Un OpenClaw nouvellement installé peut ne pas avoir la permission d'agir sur votre système Raspberry Pi par défaut ; il ne peut que discuter. Nous devons configurer manuellement les permissions.

   1.  Ouvrez le fichier de configuration d'OpenClaw :

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  Trouvez l'option ``tools`` et modifiez ``profile`` et ``exec`` comme indiqué.

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3.  Enregistrez et quittez.

   4.  Entrez la commande suivante dans le terminal pour redémarrer l'OpenClaw Gateway :

      .. code-block:: bash

         openclaw gateway restart

   Maintenant, OpenClaw devrait avoir les permissions de lecture et d'écriture et être capable d'agir sur votre système Raspberry Pi.

Problèmes PiDog
^^^^^^^^^^^^^^^^^^^^^^^^


Q. PiDog ne répond pas aux commandes. Que dois-je faire ?

   Tout d'abord, vérifiez que PiDog est correctement connecté et allumé. Ensuite, testez la commande de base :

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_ctl.py status

   Si cela échoue, vérifiez que les répertoires requis existent :

      - ``~/pidog``
      - ``~/robot-hat``
      - ``~/vilib``

Q. Le test ``import pidog`` échoue.

   Cela signifie que la bibliothèque Python PiDog n'est pas correctement installée. Veuillez vous référer au guide d'installation officiel de PiDog V2 pour installer les bibliothèques nécessaires.

Q. Les lumières LED ne fonctionnent pas comme prévu.

   Si la lumière fixe ne s'affiche pas clairement, utilisez plutôt l'effet ``boom`` — il produit les résultats les plus visibles :

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple

Q. OpenClaw ne reconnaît pas la compétence PiDog.

   Rappelez à OpenClaw de synchroniser les compétences en disant dans l'interface TUI : *« Please rsync my skills »* ou redémarrez l'OpenClaw Gateway :

   .. code-block:: bash

      openclaw gateway restart

Q. L'action d'aboiement ne sonne pas correctement.

   L'action d'aboiement utilise le son ``single_bark_1`` par défaut. C'est un comportement normal pour PiDog V2.

----------------------------------------------------------------

.. end_using_pidog


..  PiDog skill 短说明

..  把整个目录放到：
..  ~/.openclaw/workspace/skills/pidog-control/

..  这套 skill 适用于按官方教程安装的 SunFounder PiDog V2，默认依赖这些目录存在：
..  - ~/pidog
..  - ~/robot-hat
..  - ~/vilib

..  并且这句要能通过：

..  ```bash
..    python3 -c "import pidog"
..  ```

..  目前支持
..  - 动作：stand sit lie wag-tail bark forward backward turn-left turn-right
..  - 姿态保持：--hold
..  - 灯光：off breath listen boom solid
..  - 颜色：red green blue yellow purple pink cyan white orange 或 #RRGGBB

..  推荐首次测试

..  ```bash
..    python3 skills/pidog-control/scripts/pidog_ctl.py status
..    python3 skills/pidog-control/scripts/pidog_ctl.py safe-test
..    python3 skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple
..  ```

..  常用例子

..  ```bash
..    python3 skills/pidog-control/scripts/pidog_ctl.py action sit
..    python3 skills/pidog-control/scripts/pidog_ctl.py action stand --hold
..    python3 skills/pidog-control/scripts/pidog_ctl.py action bark
..    python3 skills/pidog-control/scripts/pidog_ctl.py light boom --color red
..    python3 skills/pidog-control/scripts/pidog_rgb_ctl.py light boom --color purple
..  ```

..  这台机器上已验证
..  - 动作：stand / sit / lie / wag-tail / bark
..  - 灯光：boom / listen / breath / off
..  - 已现场看到：红、黄、紫 灯效

..  建议默认用法
..  - 动作演示：sit
..  - 灯光演示：boom --color purple
..  - 灯光排障优先用：pidog_rgb_ctl.py

..  注意
..  - bark 实际走的是 single_bark_1
..  - solid 不保证是真正稳定常亮，想要明显效果优先用 boom
