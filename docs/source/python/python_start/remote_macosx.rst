.. note::

    Ciao, benvenuto nella community di SunFounder per appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri membri della community.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con il supporto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Per gli Utenti di Mac OS X
===============================

Gli utenti di Mac OS X possono utilizzare SSH (Secure Shell) per accedere e controllare il Raspberry Pi in modo sicuro e comodo da remoto. Questa opzione è particolarmente utile per lavorare con il Raspberry Pi senza un monitor collegato o quando si lavora da remoto. Utilizzando l'applicazione Terminale su un Mac, è possibile stabilire una connessione sicura tramite un semplice comando SSH che include il nome utente e l'hostname del Raspberry Pi. Durante la prima connessione, verrà richiesto di confermare l'autenticità del Raspberry Pi tramite un messaggio di sicurezza.

#. Per connetterti al Raspberry Pi, digita il seguente comando SSH:

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac-ping.png

#. Al primo accesso, apparirà un messaggio di sicurezza. Rispondi con **yes** per procedere.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Inserisci la password del Raspberry Pi. Tieni presente che, per motivi di sicurezza, la password non verrà visualizzata durante la digitazione.

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 
