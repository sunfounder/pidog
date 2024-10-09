.. note::

    Ciao! Benvenuto nella Community di appassionati di Raspberry Pi, Arduino e ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _filezilla:

Software Filezilla
=======================

.. image:: img/filezilla_icon.png

Il File Transfer Protocol (FTP) è un protocollo di comunicazione standard utilizzato per trasferire file tra un server e un client all'interno di una rete.

Filezilla è un software open source che supporta non solo FTP, ma anche FTP su TLS (FTPS) e SFTP. Possiamo utilizzare Filezilla per caricare file locali (come immagini e audio) su Raspberry Pi oppure per scaricare file da Raspberry Pi al computer locale.

**Passaggio 1**: Scaricare Filezilla.

Scarica il client dal `Filezilla's official website <https://filezilla-project.org/>`_. Filezilla ha un ottimo tutorial, puoi fare riferimento a: `Documentazione - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.

**Passaggio 2**: Collegamento a Raspberry Pi.

Dopo una rapida installazione, aprilo e `connect it to an FTP server <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Ha tre modalità di connessione; qui utilizziamo la barra di **Connessione Rapida**. Inserisci il **nome host/IP**, **nome utente**, **password** e **porta (22)**, quindi clicca su **Connessione Rapida** o premi **Invio** per collegarti al server.

.. image:: img/filezilla_connect.png

.. note::

    La Connessione Rapida è un buon modo per testare le tue credenziali di accesso. Se desideri creare una voce permanente, puoi selezionare **File** -> **Copia Connessione Corrente in Gestione Siti** dopo una Connessione Rapida riuscita, inserire il nome e fare clic su **OK**. La prossima volta potrai collegarti selezionando il sito precedentemente salvato all'interno di **File** -> **Gestione Siti**.

    .. image:: img/ftp_site.png

**Passaggio 3**: Caricare/scaricare file.

Puoi caricare file locali su Raspberry Pi tramite il drag-and-drop oppure scaricare i file presenti su Raspberry Pi sul tuo computer locale.

.. image:: img/upload_ftp.png
