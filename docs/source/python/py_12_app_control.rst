.. note::

    Ciao, benvenuto nella Community di SunFounder per gli appassionati di Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme a noi e ad altri appassionati.

    **Perché Unirsi a Noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Speciali**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

12. Controlla PiDog con l'APP
================================

In questo esempio, utilizzeremo l'app SunFounder Controller per controllare PiDog.

.. raw:: html

   <video width="600" loop autoplay muted>
      <source src="../_static/video/app_control.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

Devi prima scaricare l'APP sul tuo telefono/tablet, quindi connetterti alla WLAN come PiDog e infine creare il tuo telecomando sul SunFounder Controller per controllare PiDog.

.. _app_control:

Controlla PiDog con l'app
----------------------------

#. Installa `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ da **APP Store (iOS)** o **Google Play (Android)**.

#. Installa il modulo ``sunfounder-controller``.

    I moduli ``robot-hat``, ``vilib`` e ``picar-x`` devono essere installati prima, per maggiori dettagli vedi: :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Esegui il codice.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 12_app_control.py

    Dopo aver avviato il codice, vedrai il seguente messaggio, che indica che PiDog ha avviato correttamente la comunicazione di rete.

    .. code-block:: 

        Running on: http://192.168.18.138:9000/mjpg

        * Serving Flask app "vilib.vilib" (lazy loading)
        * Environment: development
        * Debug mode: off
        * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)       

#. Collega ``PiDog`` e ``Sunfounder Controller``.

    * Collega il tuo tablet/telefono alla WLAN dove è connesso PiDog.

    * Apri l'APP ``Sunfounder Controller``. Clicca sull'icona + per aggiungere un nuovo controller.

        .. image:: img/app1.png

    * Sono disponibili controller predefiniti per alcuni prodotti, qui selezioniamo **PiDog**. Dagli un nome oppure premi direttamente **Conferma**.

        .. image:: img/app_preset.jpg

    * Una volta entrato, l'app cercherà automaticamente il **Mydog**. Dopo pochi secondi, vedrai il messaggio "Connesso con successo".

        .. image:: img/app_auto_connect.jpg

    .. note::

        * Puoi anche cliccare manualmente il pulsante |app_connect|. Dopo alcuni secondi, apparirà MyDog(IP), clicca per connetterti.

            .. image:: img/sc_mydog.jpg

#. Esegui il Controller.

    * Quando appare il messaggio "Connesso con successo", premi il pulsante ▶ nell'angolo in alto a destra.

    * L'immagine acquisita dalla videocamera apparirà nell'APP e ora potrai controllare PiDog utilizzando i vari widget disponibili.

        .. image:: img/sc_run.jpg

Ecco le funzioni dei vari widget.

* A: Rileva la distanza dell'ostacolo, ovvero la lettura del modulo ultrasonico.
* C: Attiva/disattiva il rilevamento del volto.
* D: Controlla l'angolo di inclinazione della testa di PiDog.
* E: Seduto.
* F: In piedi.
* G: Sdraiato.
* I: Gratta la testa di PiDog.
* N: Abbaia.
* O: Scodinzola.
* P: Ansima.
* K: Controlla il movimento di PiDog (avanti, indietro, sinistra, destra).
* Q: Controlla l'orientamento della testa di PiDog.
* J: Passa alla modalità di controllo vocale. Supporta i seguenti comandi vocali:

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

Avvio Automatico all'Accensione
-----------------------------------

Quando controlli PiDog tramite l'APP, non è conveniente dover accedere al Raspberry Pi e avviare manualmente ``12_app_control.py`` ogni volta prima di connetterti.

Esiste un metodo più efficiente. Puoi configurare PiDog in modo che avvii automaticamente ``12_app_control.py`` ogni volta che viene acceso. In questo modo, puoi collegarti direttamente a PiDog utilizzando l'APP e controllare il tuo robot senza ulteriori passaggi.

Come configurarlo?

#. Esegui i seguenti comandi per installare e configurare l'applicazione ``pidog_app`` e impostare il WiFi per PiDog.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/bin
        sudo bash pidog_app_install.sh

#. Alla fine, inserisci ``y`` per riavviare PiDog.

    .. image:: img/auto_start.png

#. Dopo il riavvio, PiDog avvierà automaticamente lo script di controllo. Poi potrai :ref:`app_control`.

.. warning::

    Se desideri eseguire altri script, prima esegui ``pidog_app disable`` per disattivare la funzione di avvio automatico.


.. Configurazione del Programma APP
.. ------------------------------------

.. Puoi inserire i seguenti comandi per modificare le impostazioni della modalità APP.

.. .. code-block::

..     pidog_app <OPTION> [input]

.. **OPTION**
..     * ``-h`` ``help``: guida, mostra questo messaggio
..     * ``start`` ``restart``: riavvia il servizio ``pidog_app``
..     * ``stop``: ferma il servizio ``pidog_app``
..     * ``disable``: disabilita l'avvio automatico del programma ``app_controller``
..     * ``enable``: abilita l'avvio automatico del programma ``app_controller``
..     * ``close_ap``: disabilita l'hotspot, disattiva l'avvio automatico dell'hotspot all'avvio e passa alla modalità ``sta``
..     * ``open_ap``: abilita l'hotspot, attiva l'avvio automatico dell'hotspot all'avvio
..     * ``ssid``: imposta l'SSID (nome della rete) dell'hotspot
..     * ``psk``: imposta la password dell'hotspot
..     * ``country``: imposta il codice paese dell'hotspot

