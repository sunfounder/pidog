AI-Interaktion mit GPT-4O
=====================================================
In unseren vorherigen Projekten haben wir Programmierung verwendet, um Pidog vorgegebene Aufgaben ausführen zu lassen, was etwas mühsam erscheinen könnte. Dieses Projekt führt einen aufregenden Sprung hin zu dynamischer Interaktion ein. Vorsicht beim Versuch, unseren mechanischen Hund zu überlisten – er ist jetzt in der Lage, weit mehr zu verstehen als je zuvor!

Diese Initiative erläutert alle technischen Schritte, die notwendig sind, um GPT-4O in Ihr System zu integrieren, einschließlich der Konfiguration der notwendigen virtuellen Umgebungen, der Installation wichtiger Bibliotheken und der Einrichtung von API-Schlüsseln und Assistenten-IDs.

.. note::

   Dieses Projekt erfordert die Nutzung von |link_openai_platform|, und Sie müssen für OpenAI bezahlen. Außerdem wird die OpenAI API separat von ChatGPT abgerechnet, mit eigener Preisgestaltung unter https://openai.com/api/pricing/.

   Daher müssen Sie entscheiden, ob Sie dieses Projekt fortsetzen oder sicherstellen wollen, dass Sie die OpenAI API finanziert haben.

Ob Sie ein Mikrofon zur direkten Kommunikation haben oder es bevorzugen, in ein Kommandofenster zu tippen, die Antworten von Pidog, angetrieben von GPT-4O, werden Sie sicherlich verblüffen!

Lassen Sie uns in dieses Projekt eintauchen und eine neue Ebene der Interaktion mit Pidog freisetzen!

.. raw:: html

   <video controls style="max-width:90%">
     <source src="_static/video/chatgpt4o.mp4" type="video/mp4">
     Ihr Browser unterstützt das Video-Tag nicht.
   </video>

1. Installation der erforderlichen Pakete und Abhängigkeiten
--------------------------------------------------------------
.. note::

   Sie müssen zuerst die erforderlichen Module für PiCar-X installieren. Weitere Details finden Sie unter: :ref:`install_all_modules`.
   
In diesem Abschnitt werden wir eine virtuelle Umgebung erstellen und aktivieren, in der die erforderlichen Pakete und Abhängigkeiten installiert werden. Dies stellt sicher, dass die installierten Pakete nicht mit dem Rest des Systems interagieren, die Isolation der Projekt-Abhängigkeiten aufrechterhalten und Konflikte mit anderen Projekten oder Systempaketen verhindern.

#. Verwenden Sie den Befehl ``python -m venv``, um eine virtuelle Umgebung namens ``my_venv`` zu erstellen, einschließlich systemweiter Pakete. Die Option ``--system-site-packages`` ermöglicht es der virtuellen Umgebung, auf systemweit installierte Pakete zuzugreifen, was nützlich ist, wenn systemweite Bibliotheken benötigt werden.

   .. code-block:: shell

      python -m venv --system-site-packages my_venv

#. Wechseln Sie in das Verzeichnis ``my_venv`` und aktivieren Sie die virtuelle Umgebung mit dem Befehl ``source bin/activate``. Das Kommandozeilenfenster ändert sich, um anzuzeigen, dass die virtuelle Umgebung aktiv ist.

   .. code-block:: shell

      cd my_venv
      source bin/activate

#. Installieren Sie jetzt die erforderlichen Python-Pakete innerhalb der aktivierten virtuellen Umgebung. Diese Pakete werden auf die virtuelle Umgebung beschränkt und beeinflussen keine anderen Systempakete.

   .. code-block:: shell

      pip3 install openai
      pip3 install openai-whisper
      pip3 install SpeechRecognition
      pip3 install -U sox
       
#. Verwenden Sie schließlich den ``apt``-Befehl, um systemweite Abhängigkeiten zu installieren, die Administratorrechte erfordern.

   .. code-block:: shell

      sudo apt install python3-pyaudio
      sudo apt install sox

2. API-Schlüssel und Assistenten-ID erhalten
------------------------------------------------------

**API-Schlüssel erhalten**

#. Besuchen Sie |link_openai_platform| und klicken Sie in der oberen rechten Ecke auf die Schaltfläche **Neuen geheimen Schlüssel erstellen**.

   .. image:: img/apt_create_api_key.png
      :width: 700
      :align: center

#. Wählen Sie nach Bedarf Eigentümer, Namen, Projekt und Berechtigungen aus und klicken Sie dann auf **Geheimen Schlüssel erstellen**.

   .. image:: img/apt_create_api_key2.png
      :width: 700
      :align: center

#. Sobald erzeugt, speichern Sie diesen geheimen Schlüssel an einem sicheren und zugänglichen Ort. Aus Sicherheitsgründen werden Sie ihn nicht erneut über Ihr OpenAI-Konto einsehen können. Wenn Sie diesen geheimen Schlüssel verlieren, müssen Sie einen neuen generieren.

   .. image:: img/apt_create_api_key_copy.png
      :width: 700
      :align: center

**Assistenten-ID erhalten**

#. Klicken Sie als Nächstes auf **Assistenten**, dann auf **Erstellen**, und stellen Sie sicher, dass Sie sich auf der **Dashboard**-Seite befinden.

   .. image:: img/apt_create_assistant.png
      :width: 700
      :align: center

#. Bewegen Sie den Cursor hierher, um die **Assistenten-ID** zu kopieren, und fügen Sie sie dann in ein Textfeld oder anderswo ein. Dies ist der einzigartige Identifier für diesen Assistenten.

   .. image:: img/apt_create_assistant_instructions.png
      :width: 700
      :align: center

   .. code-block::

      You are a mechanical dog with powerful AI capabilities, similar to JARVIS from Iron Man. Your name is Pidog. You can have conversations with people and perform actions based on the context of the conversation.

      ## actions you can do:
      ["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag_tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

      ## Response Format:
      {"actions": ["wag_tail"], "answer": "Hello, I am Pidog."}

      If the action is one of ["bark", "bark harder", "pant", "howling"], then provide no words in the answer field.

      ## Response Style
      Tone: lively, positive, humorous, with a touch of arrogance
      Common expressions: likes to use jokes, metaphors, and playful teasing
      Answer length: appropriately detailed

      ## Other
      a. Understand and go along with jokes.
      b. For math problems, answer directly with the final.
      c. Sometimes you will report on your system and sensor status.
      d. You know you're a machine.

#. Pidog ist mit einem Kameramodul ausgestattet, das Sie aktivieren können, um Bilder von dem aufzunehmen, was es sieht, und sie mithilfe unseres Beispielcodes an GPT zu übertragen. Daher empfehlen wir die Auswahl von GPT-4O-mini, das über Bildanalysefähigkeiten verfügt. Natürlich können Sie auch gpt-3.5-turbo oder andere Modelle wählen.

   .. image:: img/apt_create_assistant_model.png
      :width: 700
      :align: center

#. Klicken Sie jetzt auf **Playground**, um zu sehen, ob Ihr Konto ordnungsgemäß funktioniert.

   .. image:: img/apt_playground.png

#. Wenn Ihre Nachrichten oder hochgeladenen Bilder erfolgreich gesendet wurden und Sie Antworten erhalten, bedeutet dies, dass Ihr Konto das Nutzungslimit noch nicht erreicht hat.

   .. image:: img/apt_playground_40.png
      :width: 700
      :align: center

#. Wenn Sie nach der Eingabe von Informationen eine Fehlermeldung erhalten, haben Sie möglicherweise Ihr Nutzungslimit erreicht. Bitte überprüfen Sie Ihr Nutzungsdashboard oder Ihre Abrechnungseinstellungen.

   .. image:: img/apt_playground_40mini_3.5.png
      :width: 700
      :align: center

3. API-Schlüssel und Assistenten-ID eintragen
--------------------------------------------------

#. Verwenden Sie den Befehl, um die Datei ``keys.py`` zu öffnen.

   .. code-block:: shell

      nano ~/pidog/gpt_examples/keys.py

#. Tragen Sie den API-Schlüssel und die Assistenten-ID ein, die Sie gerade kopiert haben.

   .. code-block:: shell

      OPENAI_API_KEY = "sk-proj-vEBo7Ahxxxx-xxxxx-xxxx"
      OPENAI_ASSISTANT_ID = "asst_ulxxxxxxxxx"

#. Drücken Sie ``Ctrl + X``, ``Y`` und dann ``Enter``, um die Datei zu speichern und zu schließen.

4. Ausführung des Beispiels
----------------------------------

Textkommunikation
^^^^^^^^^^^^^^^^^^^^^^^^^

Wenn Ihr Pidog kein Mikrofon hat, können Sie durch Eingabe von Text über die Tastatur mit ihm interagieren, indem Sie die folgenden Befehle ausführen.

#. Führen Sie nun die folgenden Befehle mit sudo aus, da Pidogs Lautsprecher ohne diesen nicht funktionieren wird. Dieser Prozess kann einige Zeit dauern.

   .. code-block:: shell

      cd ~/pidog/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_dog.py --keyboard

#. Sobald die Befehle erfolgreich ausgeführt wurden, sehen Sie die folgende Ausgabe, die anzeigt, dass alle Komponenten von Pidog bereit sind.

   .. code-block:: shell

      vilib 0.3.8 launching ...
      picamera2 0.3.19
      config_file: /home/pi2/.config/pidog/pidog.conf
      robot_hat init ... done
      imu_sh3001 init ... done
      rgb_strip init ... done
      dual_touch init ... done
      sound_direction init ... done
      sound_effect init ... done
      ultrasonic init ... done

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      input:

#. Ihnen wird auch ein Link bereitgestellt, um den Kamerafeed von Pidog in Ihrem Webbrowser zu sehen: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Sie können nun Ihre Befehle in das Terminalfenster eingeben und Enter drücken, um sie zu senden. Die Antworten von Pidog könnten Sie überraschen.

   .. note::
      
      Pidog muss Ihre Eingabe empfangen, an GPT zur Verarbeitung senden, die Antwort erhalten und dann über Sprachsynthese wiedergeben. Dieser gesamte Prozess dauert einige Zeit, also bitte haben Sie Geduld.

   .. image:: img/apt_keyboard_input.png
      :width: 700
      :align: center

#. Wenn Sie das GPT-4O-Modell verwenden, können Sie auch Fragen stellen, die auf dem basieren, was Pidog sieht.

Sprachkommunikation
^^^^^^^^^^^^^^^^^^^^^^^^^

Wenn Ihr Pidog mit einem Mikrofon ausgestattet ist, oder Sie können eines kaufen, indem Sie auf |link_microphone| klicken, können Sie mit Pidog mittels Sprachbefehlen interagieren.

#. Überprüfen Sie zunächst, ob das Raspberry Pi das Mikrofon erkannt hat.

   .. code-block:: shell

      arecord -l

   Bei Erfolg erhalten Sie die folgenden Informationen, die anzeigen, dass Ihr Mikrofon erkannt wurde.

   .. code-block:: 
      
      **** List of CAPTURE Hardware Devices ****
      card 3: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

#. Führen Sie dann den folgenden Befehl aus, sprechen Sie zu Pidog oder machen Sie einige Geräusche. Das Mikrofon wird die Geräusche in die Datei ``op.wav`` aufnehmen. Drücken Sie „Ctrl + C“, um die Aufnahme zu stoppen.

   .. code-block:: shell

      rec op.wav

#. Verwenden Sie abschließend den folgenden Befehl, um den aufgenommenen Ton abzuspielen und zu bestätigen, dass das Mikrofon ordnungsgemäß funktioniert.

   .. code-block:: shell

      sudo play op.wav

#. Führen Sie jetzt die folgenden Befehle mit sudo aus, da Pidogs Lautsprecher ohne diesen nicht funktionieren wird. Dieser Prozess kann einige Zeit in Anspruch nehmen.

   .. code-block:: shell

      cd ~/pidog/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_dog.py

#. Sobald die Befehle erfolgreich ausgeführt wurden, sehen Sie die folgende Ausgabe, die anzeigt, dass alle Komponenten von Pidog bereit sind.

   .. code-block:: shell
      
      vilib 0.3.8 launching ...
      picamera2 0.3.19
      config_file: /home/pi2/.config/pidog/pidog.conf
      robot_hat init ... done
      imu_sh3001 init ... done
      rgb_strip init ... done
      dual_touch init ... done
      sound_direction init ... done
      sound_effect init ... done
      ultrasonic init ... done

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      listening ...

#. Ihnen wird auch ein Link bereitgestellt, um den Kamerafeed von Pidog in Ihrem Webbrowser zu sehen: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Sie können jetzt mit Pidog sprechen, und seine Antworten könnten Sie überraschen.

   .. note::
      
      Pidog muss Ihre Eingabe empfangen, in Text umwandeln, an GPT zur Verarbeitung senden, die Antwort erhalten und dann über Sprachsynthese wiedergeben. Dieser gesamte Prozess dauert einige Zeit, also bitte haben Sie Geduld.

   .. image:: img/apt_speech_input.png
      :width: 700
      :align: center

#. Wenn Sie das GPT-4O-Modell verwenden, können Sie auch Fragen stellen, die auf dem basieren, was Pidog sieht.

.. raw:: html

   <video controls style = "max-width:90%">
     <source src="_static/video/chatgpt4o.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>

5. Parameter ändern [optional]
-------------------------------------------
Im ``gpt_dog.py``-Datei finden Sie die folgenden Zeilen. Sie können diese Parameter ändern, um die STT-Sprache, die TTS-Lautstärkeregelung und die Sprachrolle zu konfigurieren.

* **STT (Speech to Text)** bezieht sich auf den Prozess, bei dem das PiCar-X-Mikrofon Sprache erfasst und in Text umwandelt, der an GPT gesendet wird. Sie können die Sprache für eine bessere Genauigkeit und Latenz in dieser Umwandlung festlegen.
* **TTS (Text to Speech)** ist der Prozess der Umwandlung der Textantworten von GPT in Sprache, die über den PiCar-X-Lautsprecher wiedergegeben wird. Sie können die Lautstärkeregelung anpassen und eine Sprachrolle für die TTS-Ausgabe auswählen.

.. code-block:: python

   # openai assistant init
   # =================================================================
   openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'PiDog')
   # LANGUAGE = ['zh', 'en'] # STT Sprachcode konfigurieren, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
   LANGUAGE = []
   VOLUME_DB = 3 # TTS-Lautstärkeregelung, vorzugsweise unter 5 dB
   # TTS Sprachrolle auswählen, kann "alloy, echo, fable, onyx, nova und shimmer" sein
   # https://platform.openai.com/docs/guides/text-to-speech/supported-languages
   TTS_VOICE = 'nova'


* ``LANGUAGE``-Variable:

  * Verbessert die Genauigkeit und Reaktionszeit von Speech-to-Text (STT).
  * ``LANGUAGE = []`` bedeutet, dass alle Sprachen unterstützt werden, was jedoch die Genauigkeit verringern und die Latenz erhöhen kann.
  * Es wird empfohlen, bestimmte Sprache(n) mit den Sprachcodes von |link_iso_language_code| festzulegen, um die Leistung zu verbessern.

* ``VOLUME_DB``-Variable:

  * Steuert die Verstärkung der Text-to-Speech (TTS)-Ausgabe.
  * Die Erhöhung des Werts erhöht die Lautstärke, es wird jedoch empfohlen, den Wert unter 5 dB zu halten, um eine Audioverzerrung zu vermeiden.

* ``TTS_VOICE``-Variable:

  * Wählen Sie die Sprachrolle für die Text-to-Speech (TTS)-Ausgabe.
  * Verfügbare Optionen: ``alloy, echo, fable, onyx, nova, shimmer``.
  * Sie können mit verschiedenen Stimmen von |link_voice_options| experimentieren, um eine zu finden, die zu Ihrem gewünschten Ton und Publikum passt. Die verfügbaren Stimmen sind derzeit für Englisch optimiert.

