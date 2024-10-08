.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

5. Arrêter toutes les actions
==================================

Après les chapitres précédents, vous avez peut-être remarqué que le contrôle des servomoteurs de PiDog est divisé en trois threads. Cela permet à la tête et au corps de PiDog de bouger simultanément, même en utilisant seulement deux lignes de code.

**Voici quelques fonctions qui gèrent ces trois threads de servomoteurs :**

.. code-block:: python

    Pidog.wait_all_done()
    
Attend que toutes les actions dans les buffers des jambes, de la tête et de la queue soient exécutées.

.. code-block:: python

    Pidog.body_stop()
    
Arrête toutes les actions des jambes, de la tête et de la queue.

.. code-block:: python

    Pidog.stop_and_lie()
    
Arrête toutes les actions des jambes, de la tête et de la queue, puis remet le robot en position "couché".

.. code-block:: python

    Pidog.close()
    
Arrête toutes les actions, remet en position "couché" et ferme tous les threads, généralement utilisé pour quitter un programme.


**Voici quelques exemples d'utilisation courants :**

.. code-block:: python
    :emphasize-lines: 10,36,45

    from pidog import Pidog
    import time

    my_dog = Pidog()

    try:
        # préparation pour les pompes
        my_dog.legs_move([[45, 35, -45, -35, 80, 70, -80, -70]], speed=30)
        my_dog.head_move([[0, 0, 0]], pitch_comp=-10, speed=80) 
        my_dog.wait_all_done() # attendre la fin de toutes les actions
        time.sleep(0.5)

        # pompes 
        leg_pushup_action = [
            [90, -30, -90, 30, 80, 70, -80, -70],
            [45, 35, -45, -35, 80, 70, -80, -70],       
        ]
        head_pushup_action = [
            [0, 0, -30],
            [0, 0, 20],
        ]
        
        # remplir les buffers d'actions
        for _ in range(50):
            my_dog.legs_move(leg_pushup_action, immediately=False, speed=50)
            my_dog.head_move(head_pushup_action, pitch_comp=-10, immediately=False, speed=50)
        
        # afficher la longueur des buffers
        print(f"legs buffer length (start): {len(my_dog.legs_action_buffer)}")
        
        # maintenir pendant 5 secondes et afficher la longueur des buffers
        time.sleep(5)
        print(f"legs buffer length (5s): {len(my_dog.legs_action_buffer)}")
        
        # arrêter les actions et afficher la longueur des buffers
        my_dog.stop_and_lie()
        print(f"legs buffer length (stop): {len(my_dog.legs_action_buffer)}")

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        print("closing ...")
        my_dog.close() # fermer tous les threads des servomoteurs
