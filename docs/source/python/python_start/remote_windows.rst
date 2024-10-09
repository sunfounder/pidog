.. note::

    Ciao e benvenuto nella community di SunFounder su Facebook per gli appassionati di Raspberry Pi, Arduino ed ESP32! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri membri della community.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con il supporto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Per Utenti Windows
=======================

Gli utenti di Windows 10 o versioni successive possono accedere al Raspberry Pi in remoto seguendo i passaggi descritti di seguito:

#. Cerca ``powershell`` nella barra di ricerca di Windows. Fai clic con il pulsante destro del mouse su ``Windows PowerShell`` e seleziona ``Esegui come amministratore``.

    .. image:: img/powershell_ssh.png
        :align: center

#. Determina l'indirizzo IP del tuo Raspberry Pi digitando ``ping -4 <hostname>.local`` in PowerShell.

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    L'indirizzo IP del Raspberry Pi verrà visualizzato una volta che è connesso alla rete.

    * Se il terminale mostra il messaggio ``Impossibile trovare l'host pi.local. Controllare il nome e riprovare.``, verifica che il nome dell'host sia corretto.
    * Se l'indirizzo IP non è ancora rilevabile, controlla le impostazioni di rete o WiFi sul Raspberry Pi.

#. Una volta confermato l'indirizzo IP, accedi al Raspberry Pi utilizzando il comando ``ssh <username>@<hostname>.local`` o ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Se appare un errore come ``Il termine 'ssh' non è riconosciuto come nome di un cmdlet...``, il tuo sistema potrebbe non avere gli strumenti SSH preinstallati. In questo caso, è necessario installare manualmente OpenSSH seguendo le istruzioni in :ref:`openssh_powershell` o utilizzare uno strumento di terze parti descritto in :ref:`login_windows`.

#. Durante il primo accesso, apparirà un messaggio di sicurezza. Digita ``yes`` per continuare.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Inserisci la password impostata in precedenza. Nota che, per motivi di sicurezza, i caratteri della password non verranno visualizzati durante la digitazione.

    .. note::
        L'assenza di caratteri visibili durante la digitazione della password è normale. Assicurati di inserire la password correttamente.

#. Una volta connesso, il tuo Raspberry Pi è pronto per essere utilizzato da remoto.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center
