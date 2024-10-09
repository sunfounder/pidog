.. note::

    Ciao, benvenuto nella community di appassionati di Raspberry Pi, Arduino ed ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto del nostro team e della community.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e a preview speciali.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_servo_adjust:

7. Regolazione del Servo (Importante)
========================================

L'intervallo dell'angolo del servo è compreso tra -90° e 90°, ma l'angolo impostato in fabbrica è casuale, potrebbe essere 0°, oppure 45°; se montiamo il servo con un angolo casuale, questo potrebbe causare problemi durante l'esecuzione del codice del robot, o peggio, bloccare il servo e causarne il surriscaldamento e il guasto.

Quindi, è necessario impostare tutti gli angoli del servo a 0° prima dell'assemblaggio, in modo che l'angolo del servo sia centrato e possa ruotare correttamente in entrambe le direzioni.

#. Per assicurarsi che il servo sia correttamente impostato a 0°, inserire prima il braccio del servo nell'albero del servo e quindi ruotare delicatamente il braccio verso un angolo diverso. Questo braccio serve solo a far capire chiaramente che il servo sta ruotando.

    .. image:: img/servo_arm.png
        :align: center

#. Ora, eseguire il file ``servo_zeroing.py`` nella cartella ``examples/``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/pidog/examples
        sudo python3 servo_zeroing.py

    .. note::
        Se si verifica un errore, provare a riattivare la porta I2C del Raspberry Pi, vedere: :ref:`i2c_spi_config`.

#. Successivamente, collegare il cavo del servo alla porta P11 come illustrato di seguito. Allo stesso tempo, vedrai il braccio del servo ruotare in una posizione (questa è la posizione a 0°, che può essere casuale e non necessariamente verticale o parallela).

    .. image:: img/servo_pin11.jpg

#. Ora, rimuovere il braccio del servo, assicurandosi che il cavo del servo rimanga collegato, e non spegnere l'alimentazione. Quindi, continuare con l'assemblaggio seguendo le istruzioni cartacee.

.. note::

    * Non scollegare il cavo del servo prima di fissarlo con la vite del servo; puoi scollegarlo solo dopo averlo fissato.
    * Non ruotare il servo mentre è alimentato per evitare danni; se l'albero del servo non è inserito con l'angolazione corretta, estrai il servo e reinseriscilo.
    * Prima di assemblare ciascun servo, è necessario collegare il cavo del servo al pin PWM e accendere l'alimentazione per impostare l'angolo a 0°.
