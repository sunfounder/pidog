.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts sur Facebook ! Plongez plus profondément dans l’univers de Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d’un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _openssh_powershell:

Installer OpenSSH via Powershell
=====================================

Lorsque vous utilisez ``ssh <username>@<hostname>.local`` (ou ``ssh <username>@<IP address>``) pour vous connecter à votre Raspberry Pi, mais que le message d'erreur suivant apparaît :

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


Cela signifie que votre système d'exploitation est trop ancien et n'a pas `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ préinstallé. Vous devez suivre le tutoriel ci-dessous pour l'installer manuellement.

#. Tapez ``powershell`` dans la barre de recherche de votre bureau Windows, faites un clic droit sur ``Windows PowerShell`` et sélectionnez ``Exécuter en tant qu'administrateur`` dans le menu qui apparaît.

    .. image:: img/powershell_ssh.png
        :align: center

#. Utilisez la commande suivante pour installer ``OpenSSH.Client`` :

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Après l'installation, la sortie suivante sera affichée :

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Vérifiez l'installation en utilisant la commande suivante :

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. À ce stade, le message indiquera que ``OpenSSH.Client`` a été installé avec succès :

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Si le message ci-dessus n'apparaît pas, cela signifie que votre système Windows est encore trop ancien et il est conseillé d'installer un outil SSH tiers, tel que :ref:`login_windows`.

#. Redémarrez PowerShell et continuez à l'exécuter en tant qu'administrateur. À ce stade, vous pourrez vous connecter à votre Raspberry Pi en utilisant la commande ``ssh``. Vous serez alors invité à saisir le mot de passe que vous avez configuré précédemment.

    .. image:: img/powershell_login.png
