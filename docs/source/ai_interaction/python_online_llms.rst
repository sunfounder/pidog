.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_online_llm:

18. Verbindung zu Online-LLMs herstellen
========================================

In dieser Lektion lernst du, wie du deinen Pidog (oder Raspberry Pi) mit verschiedenen **Online-LLMs (Large Language Models)** verbindest.  
Jeder Anbieter erfordert einen API-Schlüssel und bietet unterschiedliche Modelle zur Auswahl an.

Wir werden lernen, wie man:

* API-Schlüssel sicher erstellt und speichert.  
* Ein Modell auswählt, das zu den eigenen Anforderungen passt.  
* Den Beispielcode ausführt, um mit den Modellen zu chatten.

----

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``pidog`` und führe dann das Skript ``i2samp.sh`` aus.

OpenAI
------

OpenAI bietet leistungsstarke Modelle wie **GPT-4o** und **GPT-4.1**, die sowohl Text- als auch Bildverarbeitung unterstützen.  

So richtest du es ein:

**API-Schlüssel abrufen und speichern**

#. Gehe zu |link_openai_platform| und melde dich an. Öffne die Seite **API keys** und klicke auf **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Fülle die Details aus (Owner, Name, Projekt und ggf. Berechtigungen) und klicke auf **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Kopiere den Schlüssel sofort — du wirst ihn später nicht mehr sehen können. Wenn du ihn verlierst, musst du einen neuen erstellen.

   .. image:: img/llm_openai_copy.png

#. Erstelle in deinem Projektordner (z. B. ``/pidog/examples``) eine Datei namens ``secret.py``:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Füge deinen Schlüssel in die Datei ein:

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**Abrechnung aktivieren und Modelle prüfen**

#. Bevor du den Schlüssel verwendest, gehe auf die **Billing**-Seite in deinem OpenAI-Konto, füge Zahlungsinformationen hinzu und lade ein kleines Guthaben auf.

   .. image:: img/llm_openai_billing.png

#. Gehe dann zur **Limits**-Seite, um zu sehen, welche Modelle für dein Konto verfügbar sind. Kopiere die exakte Modell-ID für die Verwendung im Code.

   .. image:: img/llm_openai_models.png

**Mit Beispielcode testen**

#. Öffne den Beispielcode:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt durch folgenden Code und passe ``model="xxx"`` an dein gewünschtes Modell an (z. B. ``gpt-4o``):

   .. code-block:: python

       from pidog.llm import OpenAI
       from secret import OPENAI_API_KEY
       
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
       
       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )

   Speichere und beende (``Ctrl+X``, dann ``Y``, dann ``Enter``).

#. Führe anschließend den Test aus:

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Gemini
------

Gemini ist die KI-Modellfamilie von Google. Sie ist schnell und eignet sich gut für allgemeine Anwendungsfälle.

**API-Schlüssel abrufen und speichern**

#. Melde dich bei |link_google_ai| an und gehe zur API-Key-Seite.

   .. image:: img/llm_gemini_get.png

#. Klicke oben rechts auf **Create API key**.

   .. image:: img/llm_gemini_create.png

#. Erstelle einen Schlüssel für ein bestehendes oder ein neues Projekt.

   .. image:: img/llm_gemini_choose.png

#. Kopiere den generierten API-Schlüssel.

   .. image:: img/llm_gemini_copy.png

#. Öffne in deinem Projektordner die Datei:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Füge den Schlüssel ein:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
        GEMINI_API_KEY = "AIxxx"

**Verfügbare Modelle prüfen**

Gehe zur offiziellen |link_gemini_model|-Seite. Dort findest du eine Liste der Modelle, deren exakte API-IDs und empfohlene Anwendungsfälle.

   .. image:: img/llm_gemini_model.png

**Mit Beispielcode testen**

#. Öffne die Testdatei:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt durch folgenden Code und passe ``model="xxx"`` an das gewünschte Modell an (z. B. ``gemini-2.5-flash``):

   .. code-block:: python

       from pidog.llm import Gemini
       from secret import GEMINI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Gemini(
           api_key=GEMINI_API_KEY,
           model="gemini-2.5-flash",
       )

#. Speichern und ausführen:

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Qwen
------------------

Qwen ist eine Familie von großen Sprach- und Multimodalmodellen, die von Alibaba Cloud bereitgestellt werden.  
Diese Modelle unterstützen Textgenerierung, logisches Schlussfolgern und multimodales Verständnis (z. B. Bildanalyse).

**API-Schlüssel abrufen**

Um Qwen-Modelle aufzurufen, benötigst du einen **API-Schlüssel**.  
Internationale Nutzer verwenden die **DashScope International (Model Studio)** Konsole,  
Nutzer in Festlandchina stattdessen die **Bailian (百炼)** Konsole.

* **Für internationale Nutzer**

  #. Gehe auf die offizielle |link_qwen_inter| Seite auf **Alibaba Cloud**.  
  #. Melde dich an oder erstelle ein **Alibaba Cloud** Konto.  
  #. Navigiere zu **Model Studio** (Region Singapur oder Peking auswählen).  
    
     * Wenn oben eine Meldung „Activate Now“ erscheint, klicke darauf, um Model Studio zu aktivieren und das kostenlose Kontingent (nur Singapur) zu erhalten.  
     * Die Aktivierung ist kostenlos – erst nach Verbrauch des Freikontingents wird abgerechnet.  
     * Wenn keine Aktivierungsaufforderung erscheint, ist der Dienst bereits aktiv.
  
  #. Gehe zur Seite **Key Management**. Klicke auf dem Tab **API Key** auf **Create API Key**.  
  #. Nach der Erstellung kopiere deinen API-Schlüssel und bewahre ihn sicher auf.
  
    .. image:: img/llm_qwen_api_key.png
        :width: 800
  
  .. note::
     Nutzer in Hongkong, Macau und Taiwan sollten ebenfalls die Option **International (Model Studio)** wählen.

* **Für Nutzer in Festlandchina**

  Wenn du dich in Festlandchina befindest, kannst du stattdessen die **Alibaba Cloud Bailian (百炼)** Konsole verwenden:
  
  #. Melde dich bei |link_aliyun| (Bailian-Konsole) an und schließe die Kontoüberprüfung ab.  
  #. Wähle **Create API Key**. Wenn eine Meldung erscheint, dass der Modelldienst nicht aktiviert ist, klicke auf **Activate**, stimme den Bedingungen zu und sichere dir dein kostenloses Kontingent. Danach wird die Schaltfläche **Create API Key** aktiviert.
  
     .. image:: img/llm_qwen_aliyun_create.png
  
  #. Klicke erneut auf **Create API Key**, überprüfe dein Konto und bestätige mit **Confirm**.
  
     .. image:: img/llm_qwen_aliyun_confirm.png
  
  #. Nach der Erstellung kopiere deinen API-Schlüssel.
  
     .. image:: img/llm_qwen_aliyun_copy.png

**API-Schlüssel speichern**

#. In deinem Projektordner:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Füge den Schlüssel wie folgt ein:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
        
        QWEN_API_KEY = "sk-xxx"

**Mit Beispielcode testen**

#. Öffne die Testdatei:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt mit folgendem Code und passe ``model="xxx"`` an das gewünschte Modell an (z. B. ``qwen-plus``):

   .. code-block:: python
   
      from pidog.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )

#. Ausführen mit:


   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

Grok (xAI)
------------------

Grok ist die KI-Chatplattform von xAI, entwickelt vom Team um Elon Musk. Du kannst über die xAI API eine Verbindung zu ihr herstellen.

**API-Schlüssel abrufen und speichern**

#. Registriere dich unter |link_grok_ai|. Lade zuerst Guthaben auf dein Konto — ohne Guthaben funktioniert die API nicht.

#. Gehe zur API-Key-Seite und klicke auf **Create API key**.

   .. image:: img/llm_grok_create.png

#. Gib einen Namen für den Schlüssel ein und klicke auf **Create API key**.

   .. image:: img/llm_grok_name.png

#. Kopiere den generierten Schlüssel und bewahre ihn sicher auf.

   .. image:: img/llm_grok_copy.png

#. In deinem Projektordner:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Füge den Schlüssel ein:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
        
        GROK_API_KEY = "xai-xxx"

**Verfügbare Modelle prüfen**

Gehe zur Modellseite in der xAI-Konsole. Dort kannst du alle für dein Team verfügbaren Modelle sowie deren genaue API-IDs sehen — verwende diese IDs in deinem Code.

   .. image:: img/llm_grok_model.png

**Mit Beispielcode testen**

#. Öffne die Testdatei:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt mit folgendem Code und passe ``model="xxx"`` an dein gewünschtes Modell an (z. B. ``grok-4-latest``):

   .. code-block:: python
   
       from pidog.llm import Grok
       from secret import GROK_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. Führe den Test aus:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

DeepSeek
------------------

DeepSeek ist ein chinesischer Anbieter von LLMs, der leistungsfähige und preiswerte Modelle anbietet.

**API-Schlüssel abrufen und speichern**

#. Melde dich bei |link_deepseek| an.

#. Wähle im Menü oben rechts **API Keys → Create API Key**.

   .. image:: img/llm_deepseek_create.png

#. Gib einen Namen ein, klicke auf **Create** und kopiere den Schlüssel.

   .. image:: img/llm_deepseek_copy.png

#. In deinem Projektordner:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Füge den Schlüssel ein:

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**Abrechnung aktivieren**

Du musst dein Konto zuerst aufladen. Starte mit einem kleinen Betrag (z. B. ¥10 RMB).

   .. image:: img/llm_deepseek_chognzhi.png

**Verfügbare Modelle**

Zum Zeitpunkt (2025-09-12) bietet DeepSeek:

* ``deepseek-chat``  
* ``deepseek-reasoner``

**Mit Beispielcode testen**

#. Öffne die Testdatei:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt mit folgendem Code und passe ``model="xxx"`` an dein gewünschtes Modell an (z. B. ``deepseek-chat``):

   .. code-block:: python
   
       from pidog.llm import Deepseek
       from secret import DEEPSEEK_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Deepseek(
           api_key=DEEPSEEK_API_KEY,
           model="deepseek-chat",
           max_messages=20,
       )

#. Führe das Skript aus:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

Doubao
------------------

Doubao ist die KI-Modellplattform von ByteDance (Volcengine Ark).

**API-Schlüssel abrufen und speichern**

#. Melde dich bei |link_doubao| an.

#. Scrolle im linken Menü nach unten zu **API Key Management → Create API Key**.

   .. image:: img/llm_doubao_create.png

#. Wähle einen Namen und klicke auf **Create**.

   .. image:: img/llm_doubao_name.png

#. Klicke auf das **Show API Key**-Symbol und kopiere den Schlüssel.

   .. image:: img/llm_doubao_copy.png

#. In deinem Projektordner:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Füge den Schlüssel ein:

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**Modell auswählen**

#. Gehe zum Modell-Marktplatz und wähle ein Modell aus.

   .. image:: img/llm_doubao_model_select.png

#. Wähle zum Beispiel **Doubao-seed-1.6** und klicke auf **API 接入**.

   .. image:: img/llm_doubao_model.png

#. Wähle deinen API-Schlüssel aus und klicke auf **Use API**.

   .. image:: img/llm_doubao_use_api.png

#. Klicke auf **Enable Model**.

   .. image:: img/llm_doubao_kaitong.png

#. Fahre mit der Maus über die Modell-ID, um sie zu kopieren.

   .. image:: img/llm_doubao_copy_id.png

**Mit Beispielcode testen**

#. Öffne die Testdatei:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt mit folgendem Code und passe ``model="xxx"`` an das gewünschte Modell an (z. B. ``doubao-seed-1-6-250615``):

   .. code-block:: python
   
       from pidog.llm import Doubao
       from secret import DOUBAO_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. Führe das Skript aus:


   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py


Allgemein
--------------

Dieses Projekt unterstützt die Verbindung zu mehreren LLM-Plattformen über eine einheitliche Schnittstelle.  
Wir bieten integrierte Kompatibilität mit:

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)  
* **Gemini** (Google AI Studio / Vertex AI)  
* **Grok** (xAI)  
* **DeepSeek**  
* **Qwen (通义千问)**  
* **Doubao (豆包)**  

Zusätzlich kannst du dich mit **jeder anderen LLM-Plattform verbinden, die das OpenAI-API-Format unterstützt**.  
Dafür musst du deinen **API-Schlüssel** und die passende **base_url** selbst eintragen.

**API-Schlüssel abrufen und speichern**

#. Besorge einen **API-Schlüssel** von der Plattform, die du verwenden möchtest. (Details findest du in der jeweiligen offiziellen Konsole.)  

#. Erstelle in deinem Projektordner eine neue Datei:

   .. code-block:: bash

      cd ~/pidog/examples
      nano secret.py

#. Füge deinen Schlüssel in ``secret.py`` ein:

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   Bewahre deinen API-Schlüssel sicher auf. Lade ``secret.py`` **niemals** in öffentliche Repositories hoch.

**Mit Beispielcode testen**

#. Öffne die Testdatei:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt der Python-Datei mit folgendem Beispiel und trage die richtige ``base_url`` und das gewünschte ``model`` für deine Plattform ein:

   .. note::

      Über ``base_url``:  
      Wir unterstützen das **OpenAI API-Format** sowie jede API, die **damit kompatibel** ist.  
      Jeder Anbieter hat seine eigene ``base_url``. Sieh in der jeweiligen Dokumentation nach.

   .. code-block:: python

      from pidog.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # trage hier die base_url deines Anbieters ein
          api_key=API_KEY,
          model="your-model-name-here",          # wähle ein Modell deines Anbieters
      )

#. Führe das Programm aus:

   .. code-block:: bash

      python3 18.online_llm_test.py



