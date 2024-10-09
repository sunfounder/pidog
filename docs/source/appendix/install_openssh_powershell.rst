.. note::

    Ciao! Benvenuto nella Community di appassionati di Raspberry Pi, Arduino e ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _openssh_powershell:

Installare OpenSSH tramite Powershell
=======================================

Quando utilizzi ``ssh <nome_utente>@<nome_host>.local`` (o ``ssh <nome_utente>@<indirizzo_IP>``) per connetterti al tuo Raspberry Pi e compare il seguente messaggio di errore:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


Significa che il tuo sistema operativo è troppo vecchio e non ha `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstallato. Dovrai seguire il tutorial qui sotto per installarlo manualmente.

#. Digita ``powershell`` nella barra di ricerca del desktop di Windows, fai clic destro su ``Windows PowerShell`` e seleziona ``Esegui come amministratore`` dal menu che appare.

    .. image:: img/powershell_ssh.png
        :align: center

#. Usa il seguente comando per installare ``OpenSSH.Client``.

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Al termine dell'installazione, verrà visualizzato il seguente output.

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica l'installazione utilizzando il seguente comando.

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ora vedrai che ``OpenSSH.Client`` è stato installato correttamente.

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning::
        Se il messaggio sopra non appare, significa che il tuo sistema Windows è ancora troppo obsoleto e ti consigliamo di installare uno strumento SSH di terze parti, come :ref:`login_windows`.

#. Ora riavvia PowerShell e continua a eseguirlo come amministratore. A questo punto, sarai in grado di accedere al tuo Raspberry Pi utilizzando il comando ``ssh``, dove ti verrà richiesto di inserire la password che hai configurato in precedenza.

    .. image:: img/powershell_login.png