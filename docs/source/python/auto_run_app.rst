.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e a tanti altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

3. Giocare Velocemente con l'App
=================================================

Ora che il tuo PiDog è configurato e pronto all'azione, questa sezione è perfetta per chi è impaziente di esplorare rapidamente tutte le sue funzionalità. Ti guideremo nell'installazione dell'app, nel collegamento fluido del PiDog con il tuo dispositivo mobile e nello scoprire tutte le divertenti funzionalità a portata di mano. Alla fine di questo capitolo, sarai in grado di navigare e giocare con il tuo PiDog utilizzando il tuo dispositivo. Cominciamo e immergiamoci nel mondo della robotica interattiva!

#. Installa il modulo ``sunfounder-controller``.

    I moduli robot-hat, vilib e picar-x devono essere installati prima. Per maggiori dettagli, vedi: :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Esegui i seguenti comandi:

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/bin
        sudo bash pidog_app_install.sh

#. Riavvia PiDog.

#. Installa `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ dall'**App Store (iOS)** o da **Google Play (Android)**.

#. Connettiti alla rete WLAN ``pidog``.

    Ora collega il tuo dispositivo mobile alla rete locale (LAN) trasmessa dal PiDog. In questo modo, il tuo dispositivo mobile e il PiDog saranno sulla stessa rete, facilitando la comunicazione tra le applicazioni sul dispositivo e il PiDog.

    * Trova ``pidog`` nella lista WLAN del telefono (o tablet), inserisci la password ``12345678`` e connettiti.

    * La modalità di connessione predefinita è la modalità AP. Dopo la connessione, potrebbe apparire un messaggio che informa dell'assenza di accesso a Internet su questa rete WLAN. Scegli di continuare a connetterti.

        .. image:: img/app_no_internet.png

#. Apri l'app ``Sunfounder Controller``. Clicca sull'icona + per aggiungere un nuovo telecomando.

    .. image:: img/app1.png

#. Sono disponibili dei controller preimpostati per alcuni prodotti; scegli **PiDog**. Assegna un nome oppure clicca direttamente su **Conferma**.

    .. image:: img/app_preset.jpg

#. All'interno dell'app, verrà avviata automaticamente la ricerca di **Mydog**. Dopo qualche istante, apparirà un messaggio che indica "Connessione riuscita".

    .. image:: img/app_auto_connect.jpg

    .. note::

        * Puoi anche cliccare manualmente sul pulsante |app_connect|. Dopo qualche secondo, apparirà MyDog(IP). Clicca su di esso per connetterti.

            .. image:: img/sc_mydog.jpg

#. Esegui il controller.

    * Quando appare il messaggio "Connessione riuscita", premi il pulsante ▶ in alto a destra.

    * Il feed video della telecamera verrà visualizzato sull'APP, e ora potrai controllare il tuo PiDog con questi widget.

        .. image:: img/sc_run.jpg

Ecco le funzioni dei widget.

* A: Rileva la distanza dagli ostacoli, ovvero la lettura del modulo ad ultrasuoni.
* C: Attiva/disattiva il rilevamento facciale.
* D: Controlla l'inclinazione della testa di PiDog.
* E: Comando "Seduto".
* F: Comando "In piedi".
* G: Comando "Sdraiato".
* I: Gratta la testa di PiDog.
* N: Comando "Abbaia".
* O: Scodinzola.
* P: Ansimare.
* K: Controlla i movimenti di PiDog (avanti, indietro, sinistra, destra).
* Q: Controlla l'orientamento della testa di PiDog.
* J: Attiva la modalità di controllo vocale. Supporta i seguenti comandi vocali:

    * ``forward``
    * ``backward``
    * ``turn left``
    * ``turn right``
    * ``trot``
    * ``stop``
    * ``lie down``
    * ``stand up``
    * ``sit``
    * ``bark``
    * ``bark harder``
    * ``pant``
    * ``wag tail``
    * ``shake head``
    * ``stretch``
    * ``doze off``
    * ``push-up``
    * ``howling``
    * ``twist body``
    * ``scratch``
    * ``handshake``
    * ``high five``

Configurazione del Programma dell'APP
--------------------------------------------

Puoi inserire i seguenti comandi per modificare le impostazioni della modalità APP.

.. code-block::

    pidog_app <OPZIONE> [input]

**OPZIONE**
    * ``-h`` ``help``: mostra questo messaggio di aiuto
    * ``start`` ``restart``: riavvia il servizio pidog_app
    * ``stop``: interrompe il servizio pidog_app
    * ``disable``: disabilita l'avvio automatico del programma app_controller all'avvio del sistema
    * ``enable``: abilita l'avvio automatico del programma app_controller all'avvio del sistema
    * ``close_ap``: disabilita l'hotspot, disattiva l'avvio automatico dell'hotspot e passa alla modalità sta
    * ``open_ap``: abilita l'hotspot, attiva l'avvio automatico dell'hotspot all'avvio
    * ``ssid``: imposta l'SSID (nome rete) dell'hotspot
    * ``psk``: imposta la password dell'hotspot
    * ``country``: imposta il codice paese dell'hotspot
