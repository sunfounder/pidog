.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook!  
    Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

FAQ
===========================

P1: Sobre el error "pinctrl: not found".
-------------------------------------------------------------------

Si encuentras el siguiente error:

.. code-block::

    pinctrl: not found

Esto indica que has instalado el sistema Bullseye. Se recomienda instalar el sistema **Bookworm** en su lugar.

Q2: Sobre el cargador de batería
-------------------------------------------------------------------

Para cargar la batería, simplemente conecta una fuente de alimentación Type-C de 5V/2A al puerto de alimentación del Robot Hat. No es necesario encender el interruptor de alimentación del Robot Hat durante la carga.
También puedes usar el dispositivo mientras cargas la batería.

.. image:: img/robot_hat_pic.png
    :align: center
    :width: 500

Durante la carga, la energía de entrada es amplificada por el chip de carga para cargar la batería y, al mismo tiempo, alimentar el convertidor DC-DC para uso externo, con una potencia de carga de aproximadamente 10W.
Si el consumo de energía externa se mantiene alto durante un período prolongado, la batería puede complementar el suministro de energía, de manera similar a usar un teléfono mientras se carga. Sin embargo, ten en cuenta la capacidad de la batería para evitar que se agote por completo durante el uso y la carga simultáneos.

