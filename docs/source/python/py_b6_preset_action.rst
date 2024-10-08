.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

6. Exécuter une action prédéfinie
=======================================

Certaines actions fréquemment utilisées ont été préécrites dans la bibliothèque de PiDog. Vous pouvez utiliser la fonction suivante pour faire exécuter ces actions directement par PiDog.

.. code-block:: python

    Pidog.do_action(action_name, step_count=1, speed=50)

* ``action_name`` : Nom de l'action. Les chaînes de caractères suivantes peuvent être utilisées.

    * ``"sit"``
    * ``"half_sit"``
    * ``"stand"``
    * ``"lie"``
    * ``"lie_with_hands_out"``
    * ``"forward"``
    * ``"backward"``
    * ``"turn_left"``
    * ``"turn_right"``
    * ``"trot"``
    * ``"stretch"``
    * ``"pushup"``
    * ``"doze_off"``
    * ``"nod_lethargy"``
    * ``"shake_head"``
    * ``"tilting_head_left"``
    * ``"tilting_head_right"``
    * ``"tilting_head"``
    * ``"head_bark"``
    * ``"head_up_down"``
    * ``"wag_tail"``

* ``step_count`` : Combien de fois effectuer cette action.
* ``speed`` : Vitesse d'exécution de l'action.

**Voici un exemple d'utilisation :**

1. Faire dix pompes, puis s'asseoir au sol et faire le mignon.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # pompes
        my_dog.do_action("half_sit", speed=60)
        my_dog.do_action("pushup", step_count=10, speed=60)
        my_dog.wait_all_done()
        
        # faire le mignon
        my_dog.do_action("sit", speed=60)
        my_dog.do_action("wag_tail", step_count=100,speed=90)
        my_dog.do_action("tilting_head", step_count=5, speed=20)
        my_dog.wait_head_done()
        
        my_dog.stop_and_lie()

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        print("closing ...")
        my_dog.close()    