.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a los anuncios de nuevos productos y a vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _login_windows:

PuTTY
=========================

Si eres un usuario de Windows, puedes utilizar algunas aplicaciones de SSH. Aquí te recomendamos `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_.

**Paso 1**

Descarga PuTTY.

**Paso 2**

Abre PuTTY y haz clic en **Session** en la estructura de árbol a la izquierda. Ingresa la dirección IP de la Raspberry Pi en el cuadro de texto bajo **Host Name (or IP address)** y **22** en **Port** (por defecto es 22).

.. image:: img/image25.png
    :align: center

**Paso 3**

Haz clic en **Open**. Ten en cuenta que cuando inicies sesión por primera vez 
en la Raspberry Pi con la dirección IP, aparecerá un recordatorio de seguridad. 
Solo haz clic en **Yes**.

**Paso 4**

Cuando la ventana de PuTTY muestre \"**login as:**\", escribe \"**pi**\" (el nombre 
de usuario de la Raspberry Pi), y **contraseña**: \"raspberry\" (la predeterminada, 
si no la has cambiado).

.. note::

    Cuando introduces la contraseña, los caracteres no se muestran en la ventana, lo 
    cual es normal. Solo necesitas ingresar la contraseña correcta.
    
    Si al lado de PuTTY aparece "inactive", significa que la conexión se ha interrumpido 
    y debe ser restablecida.
    
.. image:: img/image26.png
    :align: center

**Paso 5**



Ahora tenemos la Raspberry Pi conectada y es el momento de continuar con los siguientes pasos.
