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

Installare tutti i moduli (Importante)
==============================================

.. note::

   I pacchetti relativi a Python3 devono essere installati se stai utilizzando la versione Lite del sistema operativo.
   
   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       sudo apt install git python3-pip python3-setuptools python3-smbus

#. Installa il modulo ``robot-hat``.

   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
       cd robot-hat
       sudo python3 install.py

#. Installa il modulo ``vilib``.

   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone https://github.com/sunfounder/vilib.git
       cd vilib
       sudo python3 install.py

#. Installa il modulo ``pidog``.

   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/
       git clone https://github.com/sunfounder/pidog.git --depth 1
       cd pidog
       sudo pip3 install . --break

    Questo passaggio potrebbe richiedere un po’ di tempo, quindi sii paziente.

#. Esegui lo script ``i2samp.sh``.

   Infine, devi eseguire lo script ``i2samp.sh`` per installare i componenti necessari per l’amplificatore i2s, altrimenti il robot non avrà audio.
   
   .. raw:: html
   
       <run></run>
   
   .. code-block::
   
       cd ~/robot-hat
       sudo bash i2samp.sh
       
   Digitare ``y`` e premere **Invio** tre volte per continuare lo script, avviare ``/dev/zero`` in background e quindi riavviare il sistema.


   .. note::
       Se dopo il riavvio non si sente alcun suono, potrebbe essere necessario eseguire più volte lo script ``i2samp.sh``.

       Inoltre, se provi a riprodurre audio direttamente (ad es., con ``aplay``) senza aver eseguito prima un esempio PiDog, devi attivare l'altoparlante manualmente:

       .. code-block:: bash

          robot_hat enable_speaker

       È sufficiente farlo una volta per ogni avvio. Eseguire un qualsiasi esempio PiDog (che inizializza ``Pidog()``) lo fa automaticamente.
