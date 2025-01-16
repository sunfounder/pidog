.. note::

    Ciao, benvenuto nella Community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime speciali.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_all_modules:

5. Installazione di tutti i Moduli (Importante)
=================================================

#. Aggiorna il tuo sistema.

    Assicurati di essere connesso a Internet e aggiorna il sistema:

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt update
        sudo apt upgrade

    .. note::

        I pacchetti correlati a Python3 devono essere installati se stai utilizzando la versione Lite del sistema operativo.

        .. raw:: html

            <run></run>

        .. code-block::
        
            sudo apt install git python3-pip python3-setuptools python3-smbus


#. Installa il modulo ``robot-hat``.


    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
        cd robot-hat
        sudo python3 setup.py install



#. Installa il modulo ``vilib``.


    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone -b picamera2 https://github.com/sunfounder/vilib.git
        cd vilib
        sudo python3 install.py




#. Scarica il codice.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/
        git clone https://github.com/sunfounder/pidog.git --depth 1

#. Installa il modulo ``pidog``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd pidog
        sudo python3 setup.py install

    Questo passaggio richiederà un po' di tempo, quindi ti preghiamo di avere pazienza.

#. Esegui lo script ``i2samp.sh``.

    Infine, è necessario eseguire lo script ``i2samp.sh`` per installare i componenti richiesti dall'amplificatore i2s, altrimenti il robot non emetterà alcun suono.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog
        sudo bash i2samp.sh
        
    .. image:: img/i2s.png

    Digita ``y`` e premi ``Enter`` per continuare l'esecuzione dello script.

    .. image:: img/i2s2.png

    Digita ``y`` e premi ``Enter`` per eseguire ``/dev/zero`` in background.

    .. image:: img/i2s3.png

    Digita ``y`` e premi ``Enter`` per riavviare il sistema.

    .. note::
        Se dopo il riavvio non c'è suono, potrebbe essere necessario eseguire più volte lo script ``i2samp.sh``.
