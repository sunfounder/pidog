.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

10. Lecture de l'IMU
========================

Grâce au module IMU 6-DOF, PiDog peut déterminer s'il est sur une pente ou s'il est soulevé.

Le module IMU 6-DOF est équipé d'un accéléromètre à 3 axes et d'un gyroscope à 3 axes, permettant de mesurer l'accélération et la vitesse angulaire dans trois directions.

.. note::

    Avant d'utiliser le module, assurez-vous qu'il est correctement assemblé. L'étiquette sur le module vous indiquera s'il est inversé.

**Vous pouvez lire l'accélération avec :**

.. code-block:: python

   ax, ay, az = Pidog.accData

Lorsque PiDog est placé à l'horizontale, l'accélération sur l'axe x (ax) doit être proche de l'accélération de la gravité (1g), avec une valeur de -16384.
Les valeurs sur les axes y et z doivent être proches de 0.

**Utilisez la méthode suivante pour lire la vitesse angulaire :**

.. code-block:: python

   gx, gy, gz = my_dog.gyroData

Lorsque PiDog est positionné à l'horizontale, les trois valeurs doivent être proches de 0.


**Voici quelques exemples d'utilisation du module 6-DOF :**

1. Lire l'accélération et la vitesse angulaire en temps réel.

.. code-block:: python

    from pidog import Pidog
    import time

    my_dog = Pidog()

    my_dog.do_action("pushup", step_count=10, speed=20)

    while True:
        ax, ay, az = my_dog.accData
        gx, gy, gz = my_dog.gyroData
        print(f"accData: {ax/16384:.2f} g ,{ay/16384:.2f} g, {az/16384:.2f} g       gyroData: {gx} °/s, {gy} °/s, {gz} °/s")
        time.sleep(0.2)
        if my_dog.is_legs_done():
            break

    my_dog.stop_and_lie()

    my_dog.close()

2. Calculer l'angle d'inclinaison du corps de PiDog.

.. code-block:: python

    from pidog import Pidog
    import time
    import math

    my_dog = Pidog()

    while True:
        ax, ay, az = my_dog.accData
        body_pitch = math.atan2(ay,ax)/math.pi*180%360-180
        print(f"Body Degree: {body_pitch:.2f} °" )
        time.sleep(0.2)

    my_dog.close()

3. PiDog garde ses yeux horizontaux tout en s'inclinant.

.. code-block:: python

    from pidog import Pidog
    import time
    import math

    my_dog = Pidog()

    while True:
        ax, ay, az = my_dog.accData
        body_pitch = math.atan2(ay,ax)/math.pi*180%360-180
        my_dog.head_move([[0, 0, 0]], pitch_comp=-body_pitch, speed=80)
        time.sleep(0.2)

    my_dog.close()