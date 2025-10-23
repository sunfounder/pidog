.. note::

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Profitez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

2. Calibration de PiDog
=============================

**Introduction**

La calibration de votre PiDog est une étape essentielle pour garantir son fonctionnement stable et efficace. Ce processus permet de corriger les déséquilibres ou imprécisions dus à des erreurs d’assemblage ou structurelles. Suivez attentivement les étapes ci-dessous afin d’assurer une marche fluide et des performances optimales.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/calibrate_before.mp4" type="video/mp4">
      Votre navigateur ne supporte pas la balise vidéo.
   </video>

Si l’angle de déviation est trop important, retournez à :ref:`py_servo_adjust` pour régler l’angle du servo à 0°, puis réassemblez le PiDog en suivant les instructions.

**Vidéo de calibration**

Pour un guide détaillé, consultez la vidéo complète de calibration. Elle montre de manière visuelle et étape par étape comment calibrer précisément votre PiDog.

.. note::

   Le kit PiDog comprend une règle de calibration de 90° ou de 60°. La vidéo utilise une règle de 90°, mais la procédure avec une règle de 60° est très similaire. Vous pouvez également vous référer aux étapes illustrées ci-dessous.
    
    .. image:: img/cali_ruler.png
         :width: 400
         :align: center

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/witCWeoHTdk?si=g8_RZDUkfjdwbLZu&amp;start=871&end=1160" title="Lecteur vidéo YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Étapes**

Voici les étapes à suivre :

#. Placez le PiDog sur une surface plane.

   .. image:: img/place-pidog.JPG

#. Accédez au répertoire des exemples PiDog et exécutez le script ``0_calibration.py``.

   .. raw:: html

        <run></run>

   .. code-block::

        cd ~/pidog/examples
        sudo python3 0_calibration.py

#. Une fois le script lancé, une interface interactive s’affichera dans le terminal. Sélectionnez le type de règle de calibration : 1 pour 90°, 2 pour 60°.

    .. image:: img/CALI.slt.1.png

#. Après votre sélection, vous accéderez à l’écran de calibration suivant :

    .. image:: img/CALI.slt.2.png

**Si vous utilisez la règle de 60°**

#. Positionnez la **règle de calibration (plaque acrylique en C)** comme illustré, avec le grand côté sur la surface horizontale. Appuyez sur ``1`` dans le terminal, puis utilisez les touches ``w`` et ``s`` pour aligner les bords.

    .. image:: img/CALI.60.1.JPG

#. Replacez la **règle de calibration** selon l’illustration suivante. Appuyez sur ``2`` dans le terminal, puis ajustez avec ``w`` et ``s`` pour affiner l’alignement.

    .. image:: img/CALI.60.2.JPG

#. Répétez la procédure de calibration pour les servos 3 à 8 afin d’assurer que les quatre pattes du PiDog soient bien calibrées.

**Si vous utilisez la règle de 90°**

#. Positionnez la **règle de calibration (plaque acrylique en C)** comme montré. Appuyez sur ``1`` dans le terminal, puis utilisez ``w`` et ``s`` pour aligner les bords.

    .. image:: img/CALI-1.2.png

#. Replacez la **règle de calibration (plaque acrylique en C)** selon l’illustration. Appuyez sur ``2`` dans le terminal, puis ajustez avec ``w`` et ``s``.

    .. image:: img/CALI-2.2.png

#. Répétez la procédure de calibration pour les servos 3 à 8 afin d’assurer que les quatre pattes du PiDog soient bien calibrées.

**Fin de la calibration**

- Une fois la calibration de tous les servos terminée, exécutez à nouveau les exemples de marche ou de posture du PiDog pour vérifier la fluidité des mouvements.  
- Si vous constatez une déviation, relancez le programme de calibration pour effectuer des ajustements.  
- Il est fortement recommandé d’effectuer cette étape après le premier assemblage pour garantir une stabilité optimale lors du fonctionnement.

.. tip::

   Pour éviter de refaire la calibration, vous pouvez enregistrer les angles des servos ou exporter le fichier de configuration une fois la calibration terminée, afin de pouvoir les restaurer rapidement plus tard.
