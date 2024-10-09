.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a los anuncios de nuevos productos y a vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _openssh_powershell:

Instalar OpenSSH a través de Powershell
============================================

Cuando usas ``ssh <nombre_usuario>@<nombre_host>.local`` (o ``ssh <nombre_usuario>@<dirección_IP>``) para conectarte a tu Raspberry Pi, pero aparece el siguiente mensaje de error:

.. code-block::

    ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
    spelling of the name, or if a path was included, verify that the path is correct and try again.

Significa que el sistema de tu ordenador es demasiado antiguo y no tiene `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstalado. Debes seguir el siguiente tutorial para instalarlo manualmente.

#. Escribe ``powershell`` en el cuadro de búsqueda del escritorio de Windows, haz clic derecho en ``Windows PowerShell`` y selecciona ``Ejecutar como administrador`` en el menú que aparece.

    .. image:: img/powershell_ssh.png
        :align: center

#. Usa el siguiente comando para instalar ``OpenSSH.Client``.

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Después de la instalación, se mostrará la siguiente salida:

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica la instalación utilizando el siguiente comando:

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ahora, te indicará que ``OpenSSH.Client`` se ha instalado correctamente.

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Si no aparece la advertencia anterior, significa que tu sistema Windows aún es demasiado antiguo. Se recomienda instalar una herramienta SSH de terceros, como :ref:`login_windows`.

#. Ahora reinicia PowerShell y vuelve a ejecutarlo como administrador. En este punto, podrás iniciar sesión en tu Raspberry Pi utilizando el comando ``ssh``, donde se te pedirá que introduzcas la contraseña que configuraste previamente.

    .. image:: img/powershell_login.png