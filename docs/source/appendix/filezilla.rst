.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a los anuncios de nuevos productos y a vistas previas.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _filezilla:

Software Filezilla
==========================

.. image:: img/filezilla_icon.png

El Protocolo de Transferencia de Archivos (FTP) es un protocolo de comunicación estándar utilizado para la transferencia de archivos entre un servidor y un cliente en una red de computadoras.

Filezilla es un software de código abierto que no solo admite FTP, sino también FTP sobre TLS (FTPS) y SFTP. Podemos usar Filezilla para subir archivos locales (como imágenes y audios, etc.) a la Raspberry Pi, o descargar archivos de la Raspberry Pi al equipo local.

**Paso 1**: Descargar Filezilla.

Descarga el cliente desde el `Filezilla's official website <https://filezilla-project.org/>`_, Filezilla cuenta con un excelente tutorial que puedes consultar en: `Documentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.

**Paso 2**: Conectar a Raspberry Pi

Después de una rápida instalación, ábrelo y ahora `connect it to an FTP server <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Hay 3 formas de conectarse, en este caso utilizamos la barra de **Conexión Rápida**. Ingresa el **nombre del host/IP**, **nombre de usuario**, **contraseña** y **puerto (22)**, luego haz clic en **Conexión Rápida** o presiona **Enter** para conectarte al servidor.

.. image:: img/filezilla_connect.png

.. note::

    Conexión Rápida es una buena forma de probar tu información de inicio de sesión. Si deseas crear una entrada permanente, puedes seleccionar **Archivo** -> **Copiar la Conexión Actual al Gestor de Sitios** después de una Conexión Rápida exitosa, ingresa el nombre y haz clic en **Aceptar**. La próxima vez podrás conectarte seleccionando el sitio guardado previamente dentro de **Archivo** -> **Gestor de Sitios**.

    .. image:: img/ftp_site.png

**Paso 3**: Subir/descargar archivos.

Puedes subir archivos locales a la Raspberry Pi arrastrándolos y soltándolos, o descargar los archivos dentro de la Raspberry Pi a tu equipo local.

.. image:: img/upload_ftp.png
