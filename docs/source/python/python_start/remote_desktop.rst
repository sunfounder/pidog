.. note::

    Ciao, benvenuto nella community di SunFounder per appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri membri della community.

    **Perché unirsi a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con il supporto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _remote_desktop:

Accesso al Desktop Remoto per Raspberry Pi
==============================================

Per coloro che preferiscono un'interfaccia grafica (GUI) rispetto all'accesso tramite riga di comando, Raspberry Pi supporta la funzionalità di desktop remoto. Questa guida ti illustrerà come configurare e utilizzare VNC (Virtual Network Computing) per l'accesso remoto.

Ti consigliamo di utilizzare `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ a questo scopo.

**Abilitazione del Servizio VNC su Raspberry Pi**

Il servizio VNC è preinstallato su Raspberry Pi OS, ma è disabilitato per impostazione predefinita. Segui questi passaggi per abilitarlo:

#. Inserisci il seguente comando nel terminale del Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block::

        sudo raspi-config

#. Naviga fino a **Interfacing Options** utilizzando la freccia in basso e premi **Enter**.

    .. image:: img/config_interface.png
        :align: center

#. Seleziona **VNC** dalle opzioni disponibili.

    .. image:: img/vnc.png
        :align: center

#. Utilizza le frecce per selezionare **<Yes>** -> **<OK>** -> **<Finish>** e conferma l'attivazione del servizio VNC.

    .. image:: img/vnc_yes.png
        :align: center

**Accesso con VNC Viewer**

#. Scarica e installa `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sul tuo computer.

#. Dopo l'installazione, avvia VNC Viewer. Inserisci il nome host o l'indirizzo IP del tuo Raspberry Pi e premi Invio.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Quando richiesto, inserisci il nome utente e la password del tuo Raspberry Pi, quindi clicca su **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Dopo qualche secondo, il desktop di Raspberry Pi OS sarà visualizzato. Ora puoi aprire il Terminale per iniziare a inserire i comandi.

    .. image:: img/bookwarm.png
        :align: center
