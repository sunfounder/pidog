.. note::

    Ciao! Benvenuto nella Community di appassionati di Raspberry Pi, Arduino e ESP32 di SunFounder su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _login_windows:

PuTTY
===============

Se sei un utente Windows, puoi utilizzare alcune applicazioni SSH. Qui ti consigliamo `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_.

**Passaggio 1**

Scarica PuTTY.

**Passaggio 2**

Apri PuTTY e clicca su **Session** nella struttura ad albero a sinistra. Inserisci 
l'indirizzo IP del RPi nel campo di testo sotto **Host Name (or IP address)** e **22** 
sotto **Port** (per impostazione predefinita è 22).

.. image:: img/image25.png
    :align: center

**Passaggio 3**

Clicca su **Open**. Tieni presente che al primo accesso alla Raspberry Pi con 
l'indirizzo IP, apparirà un promemoria di sicurezza. Basta cliccare su **Yes**.

**Passaggio 4**

Quando la finestra di PuTTY mostra \"**login as:**\", inserisci \"**pi**\" (il nome 
utente del RPi), e **password**: \"raspberry\" (quella predefinita, se non l'hai cambiata).

.. note::

    Quando inserisci la password, i caratteri non verranno visualizzati nella finestra, il che è normale. Devi solo digitare la password corretta.

    Se accanto a PuTTY appare "inactive", significa che la connessione è stata interrotta e deve essere ristabilita.

.. image:: img/image26.png
    :align: center

**Passaggio 5**


Ora che abbiamo stabilito la connessione con il Raspberry Pi, è il momento di procedere con i passaggi successivi.
