.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

7. PiDog Parle
==========================

PiDog peut émettre des sons, en jouant en fait un fichier audio.

Ces fichiers audio sont enregistrés sous le chemin ``pidog\sounds``, vous pouvez appeler la fonction suivante pour les lire.

.. code-block:: python

   Pidog.speak(name)

* ``name`` : Nom de fichier (sans suffixe), tel que ``"angry"``. ``Pidog`` propose les fichiers audio suivants.

  * ``"angry"``
  * ``"confused_1"``
  * ``"confused_2"``
  * ``"confused_3"``
  * ``"growl_1"``
  * ``"growl_2"``
  * ``"howling"``
  * ``"pant"``
  * ``"single_bark_1"``
  * ``"single_bark_2"``
  * ``"snoring"``
  * ``"woohoo"``

**Voici un exemple d'utilisation :**

.. code-block:: python

    # !/usr/bin/env python3
    ''' play sound effecfs
        Note that you need to run with "sudo"
    API:
        Pidog.speak(name, volume=100)
            play sound effecf in the file "../sounds"
            - name    str, file name of sound effect, no suffix required, eg: "angry"
            - volume  int, volume 0-100, default 100
    '''
    from pidog import Pidog
    import os
    import time

    # changer de répertoire de travail
    abspath = os.path.abspath(os.path.dirname(__file__))
    # print(abspath)
    os.chdir(abspath)

    my_dog = Pidog()

    print("\033[033mNote that you need to run with \"sudo\", otherwise there may be no sound.\033[m")

    # my_dog.speak("angry")
    # time.sleep(2)

    for name in os.listdir('../sounds'):
        name = name.split('.')[0] # supprimer le suffixe
        print(name)
        my_dog.speak(name)
        # my_dog.speak(name, volume=50)
        time.sleep(3) # Notez que la durée de chaque effet sonore est différente
    print("closing ...")
    my_dog.close()
