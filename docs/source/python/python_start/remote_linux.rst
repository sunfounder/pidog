.. note::

    Ciao, benvenuto nella community di SunFounder per appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri membri della community.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con il supporto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Per Utenti Linux/Unix
==========================

#. Individua e apri il **Terminale** sul tuo sistema Linux/Unix.

#. Assicurati che il tuo Raspberry Pi sia connesso alla stessa rete. Verificalo digitando `ping <hostname>.local`. Ad esempio:

    .. code-block::

        ping raspberrypi.local

    Dovresti visualizzare l'indirizzo IP del Raspberry Pi se è connesso alla rete.

    * Se il terminale mostra un messaggio come ``Ping request could not find host pi.local. Please check the name and try again.``, ricontrolla il nome host inserito.
    * Se non riesci a ottenere l'indirizzo IP, controlla le impostazioni di rete o WiFi del Raspberry Pi.

#. Avvia una connessione SSH digitando ``ssh <username>@<hostname>.local`` o ``ssh <username>@<indirizzo IP>``. Ad esempio:

    .. code-block::

        ssh pi@raspberrypi.local

#. Al primo accesso, visualizzerai un messaggio di sicurezza. Digita ``yes`` per procedere.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Inserisci la password che hai impostato in precedenza. Tieni presente che, per motivi di sicurezza, la password non sarà visibile durante la digitazione.

    .. note::
        È normale che i caratteri della password non vengano visualizzati nel terminale. Assicurati semplicemente di inserire la password corretta.

#. Una volta effettuato l'accesso con successo, il tuo Raspberry Pi è connesso e puoi procedere con il prossimo passaggio.
