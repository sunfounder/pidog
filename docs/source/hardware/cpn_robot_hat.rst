.. note::

    Ciao! Benvenuto nella Community di appassionati di Raspberry Pi, Arduino e ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Robot HAT
==============

|link_robot_hat_v4| è una scheda di espansione multifunzionale che permette al 
Raspberry Pi di trasformarsi rapidamente in un robot. La scheda integra un MCU 
per estendere l'uscita PWM e l'ingresso ADC per il Raspberry Pi, oltre a un chip 
driver per motori, un modulo audio I2S e un altoparlante mono. Sono inoltre presenti 
i GPIO derivati direttamente dal Raspberry Pi.

La scheda include un altoparlante, che può essere utilizzato per riprodurre musica 
di sottofondo, effetti sonori e implementare funzioni TTS (text-to-speech), rendendo 
il tuo progetto più interessante.

Accetta un input di alimentazione PH2.0 a 5 pin da 7-12V con 2 indicatori di batteria, 
1 indicatore di carica e 1 indicatore di alimentazione. La scheda dispone inoltre di un 
LED utilizzabile e di un pulsante che puoi utilizzare per testare rapidamente alcuni effetti.

.. image:: img/O1902V40RobotHAT.png

**Porta di Alimentazione**
    * Ingresso di alimentazione PH2.0 a 3 pin da 7-12V.
    * Alimenta contemporaneamente il Raspberry Pi e il Robot HAT.

**Interruttore di Alimentazione**
    * Accendi/spegni l'alimentazione del Robot HAT.
    * Quando si collega l'alimentazione alla porta di ingresso, il Raspberry Pi si avvia. Tuttavia, è necessario impostare l'interruttore di alimentazione su ON per abilitare il Robot HAT.

**Porta USB di Tipo-C**
    * Inserisci il cavo Type-C per caricare la batteria.
    * L'indicatore di carica si accende di colore rosso.
    * Quando la batteria è completamente carica, l'indicatore di carica si spegne.
    * Se il cavo USB rimane collegato per circa 4 ore dopo la ricarica completa, l'indicatore di carica lampeggerà come promemoria.

**Pin Digitali**
    * 4 canali di pin digitali, D0-D3.

**Pin ADC**
    * 4 canali di pin ADC, A0-A3.

**Pin PWM**
    * 12 canali di pin PWM, P0-P11.

**Porta Motore Sinistra/Destra**
    * 2 porte motore XH2.54.
    * La porta sinistra è collegata a GPIO 4 e la porta destra è collegata a GPIO 5.

**Pin e Porta I2C**
    * **Pin I2C**: Interfaccia a 4 pin P2.54.
    * **Porta I2C**: Interfaccia a 4 pin SH1.0, compatibile con QWIIC e STEMMA QT.
    * Queste interfacce I2C sono collegate all'interfaccia I2C del Raspberry Pi tramite GPIO2 (SDA) e GPIO3 (SCL).

**Pin SPI**
    * Interfaccia SPI a 7 pin P2.54.

**Pin UART**
    * Interfaccia a 4 pin P2.54.

**Pulsante RST**
    * Quando si utilizza Ezblock, il pulsante RST serve per riavviare il programma Ezblock.
    * Se non si utilizza Ezblock, il pulsante RST non ha una funzione predefinita e può essere personalizzato in base alle proprie esigenze.

**Pulsante USR**
    * Le funzioni del pulsante USR possono essere impostate tramite la programmazione. (Premendo si genera un input "0"; rilasciando si genera un input "1".)

**Indicatore di Batteria**
    * Due LED si accendono quando la tensione è superiore a 7,6V.
    * Un LED si accende nel range di 7,15V - 7,6V.
    * Sotto i 7,15V, entrambi i LED si spengono.

**Altoparlante e Porta Altoparlante**
    * **Altoparlante**: Questo è un altoparlante a camera acustica 2030.
    * **Porta Altoparlante**: Il Robot HAT è dotato di uscita audio I2S integrata e di un altoparlante 2030, fornendo un'uscita audio mono.
