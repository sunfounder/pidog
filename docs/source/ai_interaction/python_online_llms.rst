.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a los anuncios de nuevos productos y a vistas previas.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_online_llm:

18. Conexión a LLMs en Línea
================================

En esta lección, aprenderás a conectar tu Pidog (o Raspberry Pi) a diferentes **Modelos de Lenguaje Extenso (LLMs)** en línea.  
Cada proveedor requiere una clave API y ofrece distintos modelos entre los que puedes elegir.  

Veremos cómo:

* Crear y guardar tus claves API de forma segura.  
* Elegir un modelo que se ajuste a tus necesidades.  
* Ejecutar nuestro código de ejemplo para chatear con los modelos.

Vamos paso a paso por cada proveedor.

----

Antes de Comenzar
-------------------

Asegúrate de haber completado:

* :ref:`install_all_modules` — Instalar los módulos ``robot-hat``, ``vilib``, ``pidog`` y luego ejecutar el script ``i2samp.sh``.

OpenAI
----------

OpenAI ofrece potentes modelos como **GPT-4o** y **GPT-4.1**, que pueden utilizarse tanto para tareas de texto como de visión.  

Aquí te mostramos cómo configurarlo:

**Obtener y Guardar tu Clave API**

#. Ve a |link_openai_platform| e inicia sesión. En la página **API keys**, haz clic en **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Completa los detalles (Propietario, Nombre, Proyecto y permisos si es necesario), luego haz clic en **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Una vez creada la clave, cópiala de inmediato — no podrás volver a verla. Si la pierdes, tendrás que generar una nueva.

   .. image:: img/llm_openai_copy.png

#. En tu carpeta del proyecto (por ejemplo: ``/pidog/examples``), crea un archivo llamado ``secret.py``:

   .. code-block:: bash
   
       cd ~/pidog/examples
       sudo nano secret.py

#. Pega tu clave en el archivo de la siguiente forma:

   .. code-block:: python
   
       # secret.py
       # Guarda las claves aquí. Nunca subas este archivo a Git.
       OPENAI_API_KEY = "sk-xxx"

**Habilitar pagos y verificar modelos**

#. Antes de usar la clave, ve a la página **Billing** de tu cuenta de OpenAI, añade tus datos de pago y recarga un pequeño saldo de créditos.  

   .. image:: img/llm_openai_billing.png

#. Luego ve a la página **Limits** para verificar qué modelos están disponibles en tu cuenta y copia el ID exacto del modelo que usarás en tu código.  

   .. image:: img/llm_openai_models.png

**Probar con código de ejemplo**

#. Abre el código de ejemplo:

   .. code-block:: bash
   
       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Sustituye el contenido con el siguiente código y actualiza ``model="xxx"`` al modelo que desees (por ejemplo, ``gpt-4o``):

   .. code-block:: python
   
       from pidog.llm import OpenAI
       from secret import OPENAI_API_KEY
       
       INSTRUCTIONS = "Eres un asistente útil."
       WELCOME = "Hola, soy un asistente útil. ¿Cómo puedo ayudarte?"
       
       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )
  
   Guarda y sal (``Ctrl+X``, luego ``Y``, luego ``Enter``).  

#. Finalmente, ejecuta la prueba:


   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py
   

----

Gemini
------------------

Gemini es la familia de modelos de IA de Google. Es rápido y excelente para tareas de propósito general.  

**Obtener y Guardar tu Clave API**

#. Inicia sesión en |link_google_ai| y luego ve a la página de API Keys.

   .. image:: img/llm_gemini_get.png

#. Haz clic en el botón **Create API key** en la esquina superior derecha.

   .. image:: img/llm_gemini_create.png

#. Puedes crear una clave para un proyecto existente o uno nuevo.

   .. image:: img/llm_gemini_choose.png

#. Copia la clave API generada.

   .. image:: img/llm_gemini_copy.png

#. En tu carpeta del proyecto:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Pega la clave:

   .. code-block:: python

        # secret.py
        # Guarda las claves aquí. Nunca subas este archivo a Git.
       GEMINI_API_KEY = "AIxxx"

**Verificar modelos disponibles**

Ve a la página oficial |link_gemini_model|, allí verás la lista de modelos, sus IDs exactos de API y para qué casos de uso está optimizado cada uno.

   .. image:: img/llm_gemini_model.png

**Probar con código de ejemplo**

#. Abre el archivo de prueba:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Sustituye el contenido con el siguiente código y actualiza ``model="xxx"`` al modelo que desees (por ejemplo, ``gemini-2.5-flash``):

   .. code-block:: python

       from pidog.llm import Gemini
       from secret import GEMINI_API_KEY

       INSTRUCTIONS = "Eres un asistente útil."
       WELCOME = "Hola, soy un asistente útil. ¿Cómo puedo ayudarte?"

       llm = Gemini(
           api_key=GEMINI_API_KEY,
           model="gemini-2.5-flash",
       )

#. Guarda y ejecuta:


   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Qwen
------------------

Qwen es una familia de modelos grandes de lenguaje y multimodales proporcionada por Alibaba Cloud.  
Estos modelos admiten generación de texto, razonamiento y comprensión multimodal (como análisis de imágenes).

**Obtener una Clave API**

Para usar los modelos Qwen, necesitas una **Clave API**.  
La mayoría de los usuarios internacionales deben usar la consola **DashScope International (Model Studio)**.  
Los usuarios de China continental pueden usar la consola **Bailian (百炼)**.

* **Para usuarios internacionales**

  #. Ve a la página oficial |link_qwen_inter| en **Alibaba Cloud**.  
  #. Inicia sesión o crea una cuenta en **Alibaba Cloud**.  
  #. Navega a **Model Studio** (elige la región de Singapur o Pekín).  
     
     * Si aparece un mensaje “Activate Now” en la parte superior de la página, haz clic para activar Model Studio y obtener la cuota gratuita (solo Singapur).  
     * La activación es gratuita: solo se te cobrará después de usar la cuota gratuita.  
     * Si no aparece el mensaje de activación, el servicio ya está activo.
  
  #. Ve a la página **Key Management**. En la pestaña **API Key**, haz clic en **Create API Key**.  
  #. Una vez creada, copia tu clave API y guárdala de forma segura.  
  
    .. image:: img/llm_qwen_api_key.png
        :width: 800
  
  .. note::
     Los usuarios de Hong Kong, Macao y Taiwán también deben elegir la opción **International (Model Studio)**.
  
* **Para usuarios de China continental**

  Si estás en China continental, puedes usar la consola **Alibaba Cloud Bailian (百炼)**:
  
  #. Inicia sesión en |link_aliyun| (consola Bailian) y completa la verificación de cuenta.  
  #. Selecciona **Create API Key**. Si aparece un mensaje indicando que los servicios de modelo no están activados, haz clic en **Activate**, acepta los términos y reclama tu cuota gratuita. Después de la activación, el botón **Create API Key** estará habilitado.  
  
     .. image:: img/llm_qwen_aliyun_create.png
  
  #. Haz clic nuevamente en **Create API Key**, verifica tu cuenta y luego haz clic en **Confirm**.  
  
     .. image:: img/llm_qwen_aliyun_confirm.png
  
  #. Una vez creada, copia tu clave API.  
  
     .. image:: img/llm_qwen_aliyun_copy.png

**Guardar tu Clave API**

#. En tu carpeta del proyecto:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Pega tu clave de esta manera:

   .. code-block:: python

        # secret.py
        # Guarda las claves aquí. Nunca subas este archivo a Git.
        
        QWEN_API_KEY = "sk-xxx"

**Probar con código de ejemplo**

#. Abre el archivo de prueba:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Sustituye el contenido con el siguiente código y actualiza ``model="xxx"`` al modelo que desees (por ejemplo, ``qwen-plus``):

   .. code-block:: python
   
      from pidog.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "Eres un asistente útil."
      WELCOME = "Hola, soy un asistente útil. ¿Cómo puedo ayudarte?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )

#. Ejecuta con:


   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

Grok (xAI)
------------------
Grok es la IA conversacional de xAI, creada por el equipo de Elon Musk. Puedes conectarte a ella mediante la API de xAI.

**Obtener y Guardar tu Clave API**

#. Regístrate para obtener una cuenta aquí: |link_grok_ai|. Agrega créditos a tu cuenta primero — de lo contrario, la API no funcionará.

#. Ve a la página de API Keys y haz clic en **Create API key**.  

   .. image:: img/llm_grok_create.png

#. Ingresa un nombre para la clave y haz clic en **Create API key**. 

   .. image:: img/llm_grok_name.png

#. Copia la clave generada y guárdala de forma segura. 

   .. image:: img/llm_grok_copy.png

#. En tu carpeta del proyecto:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Pega tu clave de esta forma:

   .. code-block:: python

        # secret.py
        # Guarda las claves aquí. Nunca subas este archivo a Git.
        
        GROK_API_KEY = "xai-xxx"

**Verificar modelos disponibles**

Ve a la página **Models** en la consola de xAI. Aquí podrás ver todos los modelos disponibles para tu equipo, junto con sus IDs exactos de API — usa estos IDs en tu código.

   .. image:: img/llm_grok_model.png

**Probar con código de ejemplo**

#. Abre el archivo de prueba:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Sustituye el contenido con el siguiente código y actualiza ``model="xxx"`` al modelo que desees (por ejemplo, ``grok-4-latest``):

   .. code-block:: python
   
       from pidog.llm import Grok
       from secret import GROK_API_KEY
   
       INSTRUCTIONS = "Eres un asistente útil."
       WELCOME = "Hola, soy un asistente útil. ¿Cómo puedo ayudarte?"
   
       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. Ejecuta con:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

DeepSeek
------------------

DeepSeek es un proveedor chino de LLM que ofrece modelos potentes a bajo costo.  

**Obtener y Guardar tu Clave API**

#. Inicia sesión en |link_deepseek|. 

#. En el menú superior derecho, selecciona **API Keys → Create API Key**. 

   .. image:: img/llm_deepseek_create.png

#. Ingresa un nombre, haz clic en **Create** y copia la clave.

   .. image:: img/llm_deepseek_copy.png

#. En tu carpeta del proyecto:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Agrega tu clave:

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**Habilitar pagos**

Deberás recargar tu cuenta primero. Comienza con una pequeña cantidad (por ejemplo, ¥10 RMB). 

   .. image:: img/llm_deepseek_chognzhi.png

**Modelos disponibles**

A la fecha (2025-09-12), DeepSeek ofrece:  

* ``deepseek-chat``  
* ``deepseek-reasoner``  

**Probar con código de ejemplo**

#. Abre el archivo de prueba:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Sustituye el contenido con el siguiente código y actualiza ``model="xxx"`` al modelo que desees (por ejemplo, ``deepseek-chat``):

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

#. Ejecuta:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

Doubao
------------------
Doubao es la plataforma de modelos de IA de ByteDance (Volcengine Ark).  

**Obtener y Guardar tu Clave API**

#. Inicia sesión en |link_doubao|.

#. En el menú lateral izquierdo, desplázate hasta **API Key Management → Create API Key**. 

   .. image:: img/llm_doubao_create.png

#. Elige un nombre y haz clic en **Create**.  

   .. image:: img/llm_doubao_name.png

#. Haz clic en el ícono **Show API Key** y copia la clave. 

   .. image:: img/llm_doubao_copy.png

#. En tu carpeta del proyecto:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano secret.py

#. Agrega tu clave:

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**Elegir un modelo**

#. Ve al marketplace de modelos y selecciona uno.  

   .. image:: img/llm_doubao_model_select.png

#. Por ejemplo, elige **Doubao-seed-1.6**, luego haz clic en **API 接入**. 

   .. image:: img/llm_doubao_model.png

#. Selecciona tu clave API y haz clic en **Use API**. 

   .. image:: img/llm_doubao_use_api.png

#. Haz clic en **Enable Model**. 

   .. image:: img/llm_doubao_kaitong.png

#. Pasa el cursor sobre el ID del modelo para copiarlo. 

   .. image:: img/llm_doubao_copy_id.png

**Probar con código de ejemplo**

#. Abre el archivo de prueba:

   .. code-block:: bash

       cd ~/pidog/examples
       sudo nano 18.online_llm_test.py

#. Sustituye el contenido con el siguiente código y actualiza ``model="xxx"`` al modelo que desees (por ejemplo, ``doubao-seed-1-6-250615``):

   .. code-block:: python
   
       from pidog.llm import Doubao
       from secret import DOUBAO_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. Ejecuta con:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

General
--------------

Este proyecto admite la conexión a múltiples plataformas LLM a través de una interfaz unificada.  
Tenemos compatibilidad integrada con:

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)  
* **Gemini** (Google AI Studio / Vertex AI)  
* **Grok** (xAI)  
* **DeepSeek**  
* **Qwen (通义千问)**  
* **Doubao (豆包)**  

Además, puedes conectarte a **cualquier otro servicio LLM compatible con el formato de API de OpenAI**.  
Para esas plataformas, deberás obtener manualmente tu **API Key** y la **base_url** correcta.

**Obtener y Guardar tu Clave API**

#. Obtén una **Clave API** de la plataforma que quieras usar. (Consulta la consola oficial de cada plataforma para más detalles).  

#. En tu carpeta del proyecto, crea un nuevo archivo:

   .. code-block:: bash

      cd ~/pidog/examples
      nano secret.py

#. Agrega tu clave en ``secret.py``:

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   Mantén tu clave API en privado. No subas ``secret.py`` a repositorios públicos.

**Probar con Código de Ejemplo**

#. Abre el archivo de prueba:

   .. code-block:: bash

      cd ~/pidog/examples
      sudo nano 18.online_llm_test.py

#. Sustituye el contenido de un archivo Python con el siguiente ejemplo y completa correctamente ``base_url`` y ``model`` para tu plataforma:

   .. note::

      Sobre ``base_url``:  
      Admitimos el **formato de API de OpenAI**, así como cualquier API que sea **compatible** con él.  
      Cada proveedor tiene su propia ``base_url``. Consulta su documentación.  

   .. code-block:: python

      from pidog.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "Eres un asistente útil."
      WELCOME = "Hola, soy un asistente útil. ¿Cómo puedo ayudarte?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # ingresa la base_url de tu proveedor
          api_key=API_KEY,
          model="nombre-de-tu-modelo-aqui",       # elige un modelo de tu proveedor
      )

#. Ejecuta el programa:


   .. code-block:: bash

      python3 18.online_llm_test.py



