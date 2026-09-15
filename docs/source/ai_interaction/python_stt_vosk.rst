.. note::

    Ciao! Benvenuto nella Community di appassionati di Raspberry Pi, Arduino e ESP32 di SunFounder su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri entusiasti.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e supera le sfide tecniche con l'aiuto del nostro team e della comunità.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anticipo agli annunci dei nuovi prodotti e scopri in anteprima le novità.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Concorsi Festivi**: Partecipa a concorsi e promozioni speciali durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

16. STT con Vosk (Offline)
==============================================

Vosk è un motore di riconoscimento vocale (STT) leggero che supporta molte lingue e funziona completamente **offline** su Raspberry Pi.  
Hai bisogno di una connessione internet solo la prima volta per scaricare un modello linguistico.  
Dopodiché tutto funziona senza rete.

In questa lezione installeremo Vosk e lo proveremo con un modello linguistico a tua scelta.

Prima di iniziare
--------------------

Assicurati di aver completato:

* :ref:`install_all_modules` — Installa i moduli ``robot-hat``, ``vilib``, ``pidog``, poi esegui lo script ``i2samp.sh``.

.. _test_vosk:

1. Test Vosk
--------------------------

**Passaggi per provarlo**:

#. Crea un nuovo file:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano test_stt_vosk.py

#. Copia il codice di esempio al suo interno. Premi ``Ctrl+X``, poi ``Y`` e ``Enter`` per salvare e uscire.

   .. code-block:: python

      from pidog.stt import Vosk

      vosk = Vosk(language="en-us")

      print(vosk.available_languages)

      while True:
          print("Say something")
          result = vosk.listen(stream=False)
          print(result)

#. Esegui il programma:

   .. code-block:: bash

      sudo python3 test_stt_vosk.py

#. La prima volta che esegui il codice con una nuova lingua, Vosk **scaricherà automaticamente il modello linguistico** (per impostazione predefinita scaricherà la versione **small**).  
   Allo stesso tempo stamperà l’elenco delle lingue supportate. Poi vedrai:

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   Questo significa:

   * Il file del modello (``vosk-model-small-en-us-0.15``) è stato scaricato.  
   * L’elenco delle lingue supportate è stato stampato.  
   * Il sistema è ora in ascolto — parla nel microfono del Pidog e il testo riconosciuto apparirà nel terminale.

   **Suggerimenti**:

   * Mantieni il microfono a 15–30 cm dalla bocca.  
   * Scegli un modello che corrisponda alla tua lingua e al tuo accento.

**Modalità Streaming (opzionale)**

Puoi anche trasmettere la voce in tempo reale per vedere i risultati parziali mentre parli:

.. code-block:: python

   from pidog.stt import Vosk

   vosk = Vosk(language="en-us")

   while True:
       print("Say something")
       for result in vosk.listen(stream=True):
           if result["done"]:
               print(f"final:   {result['final']}")
           else:
               print(f"partial: {result['partial']}", end="\r", flush=True)

Risoluzione dei problemi
-----------------------------

* **Il microfono non registra nulla, oppure arecord restituisce “No such file or directory”**

  Probabilmente il numero di scheda/dispositivo è sbagliato, oppure l'ingresso è disattivato. Elenca prima i dispositivi di registrazione:

  .. code-block:: bash

     arecord -l

  Individua il tuo microfono USB e annota i numeri, poi registra un breve campione sostituendo ``1,0`` con i numeri trovati:

  .. code-block:: bash

     arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

  Se la registrazione è ancora silenziosa, apri il mixer:

  .. code-block:: bash

     alsamixer

  Premi **F6** per selezionare il microfono USB, disattiva il mute di **Mic** / **Capture** (**[OO]** invece di **[MM]**) e aumenta il livello con ↑ / ↓.

* **Vosk non riconosce la voce**

  * Assicurati che il **codice lingua** corrisponda al modello (ad es. ``en-us`` per inglese, ``zh-cn`` per cinese).  
  * Mantieni il microfono a 15–30 cm di distanza ed evita rumori di fondo.  
  * Parla chiaramente e lentamente.

* **Alta latenza / riconoscimento lento**

  * Il download automatico predefinito è un **modello small** (più veloce, ma meno accurato).  
  * Se è ancora lento, chiudi altri programmi per liberare CPU.
