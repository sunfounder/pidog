.. note::

    Ciao, benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto del nostro team e della community.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e a preview speciali.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_os_sd:

2. Installazione del Sistema Operativo
==========================================

**Componenti Necessari**

* Un computer
* Una scheda Micro SD e un lettore


1. Installa Raspberry Pi Imager
-----------------------------------

#. Visita la pagina di download del software Raspberry Pi su `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Scegli la versione del software Imager compatibile con il tuo sistema operativo. Scarica e apri il file per avviare l'installazione.

    .. image:: img/os_install_imager.png
        :align: center

#. Durante l'installazione, a seconda del sistema operativo, potrebbe apparire un messaggio di sicurezza. Ad esempio, su Windows potrebbe apparire un messaggio di avviso. In tal caso, seleziona **Ulteriori informazioni** e poi **Esegui comunque**. Segui le istruzioni a schermo per completare l'installazione del Raspberry Pi Imager.

    .. image:: img/os_info.png
        :align: center

#. Avvia l'applicazione Raspberry Pi Imager cliccando sull'icona o digitando ``rpi-imager`` nel terminale.

    .. image:: img/os_open_imager.png
        :align: center

2. Installa il Sistema Operativo sulla Micro SD
----------------------------------------------------

#. Inserisci la tua scheda SD nel computer o nel laptop utilizzando un lettore.

#. All'interno dell'Imager, clicca su **Raspberry Pi Device** e seleziona il modello Raspberry Pi dal menu a tendina.

    .. image:: img/os_choose_device.png
        :align: center

#. Seleziona **Sistema Operativo** e scegli la versione consigliata del sistema operativo.

    .. image:: img/os_choose_os.png
        :align: center

#. Clicca su **Scegli Memoria** e seleziona il dispositivo di archiviazione corretto per l'installazione.

    .. note::

        Assicurati di selezionare il dispositivo di archiviazione giusto. Per evitare confusione, scollega eventuali dispositivi di archiviazione aggiuntivi se sono collegati.

    .. image:: img/os_choose_sd.png
        :align: center

#. Clicca su **AVANTI** e poi su **MODIFICA IMPOSTAZIONI** per personalizzare le impostazioni del tuo sistema operativo.

    .. note::

        Se disponi di un monitor per il tuo Raspberry Pi, puoi saltare i passaggi successivi e cliccare 'Sì' per avviare l'installazione. Puoi modificare le altre impostazioni più tardi direttamente dal monitor.

    .. image:: img/os_enter_setting.png
        :align: center

#. Definisci un **hostname** per il tuo Raspberry Pi.

    .. note::

        L'hostname è l'identificativo di rete del tuo Raspberry Pi. Puoi accedere al tuo Pi utilizzando ``<hostname>.local`` o ``<hostname>.lan``.

    .. image:: img/os_set_hostname.png
        :align: center

#. Crea un **Nome Utente** e una **Password** per l'account amministratore del Raspberry Pi.

    .. note::

        Stabilire un nome utente e una password unici è fondamentale per garantire la sicurezza del tuo Raspberry Pi, poiché non ha una password predefinita.

    .. image:: img/os_set_username.png
        :align: center

#. Configura la rete wireless inserendo l'**SSID** e la **Password** del tuo network.

    .. note::

        Imposta il ``Paese della LAN Wireless`` utilizzando il codice a due lettere `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ corrispondente alla tua posizione.

    .. image:: img/os_set_wifi.png
        :align: center

#. Per connetterti in remoto al tuo Raspberry Pi, abilita SSH nella scheda dei Servizi.

    * Per l'**autenticazione con password**, utilizza il nome utente e la password della scheda Generale.
    * Per l'autenticazione con chiave pubblica, scegli "Consenti solo l'autenticazione con chiave pubblica". Se hai una chiave RSA, verrà utilizzata. In caso contrario, clicca su "Esegui SSH-keygen" per generare una nuova coppia di chiavi.

    .. image:: img/os_enable_ssh.png
        :align: center

#. Il menu **Opzioni** ti permette di configurare il comportamento dell'Imager durante la scrittura, includendo la possibilità di riprodurre un suono al termine, espellere il supporto al termine e abilitare la telemetria.

    .. image:: img/os_options.png
        :align: center

#. Una volta completata la personalizzazione delle impostazioni del sistema operativo, clicca su **Salva** per salvarle. Quindi clicca su **Sì** per applicarle durante la scrittura dell'immagine.

    .. image:: img/os_click_yes.png
        :align: center

#. Se la scheda SD contiene dati esistenti, assicurati di eseguire un backup per evitare la perdita di dati. Procedi cliccando **Sì** se non è necessario alcun backup.

    .. image:: img/os_continue.png
        :align: center

#. Quando appare il popup "Scrittura completata con successo", significa che l'immagine è stata scritta e verificata correttamente. Ora sei pronto per avviare il Raspberry Pi dalla scheda Micro SD!

    .. image:: img/os_finish.png
        :align: center

#. Ora puoi inserire la scheda SD configurata con Raspberry Pi OS nello slot microSD situato sul lato inferiore del Raspberry Pi.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center
