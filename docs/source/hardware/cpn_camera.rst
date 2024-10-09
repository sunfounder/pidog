.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Sumérgete más profundamente en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a los anuncios de nuevos productos y a vistas previas.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Módulo de Cámara
=============================

**Descripción**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Este es un módulo de cámara Raspberry Pi de 5 MP con sensor OV5647. Es "plug and play": conecta el cable de cinta incluido al puerto CSI (Camera Serial Interface) de tu Raspberry Pi y estará listo para usar.

La placa es pequeña, de aproximadamente 25 mm x 23 mm x 9 mm, y pesa 3 g, lo que la hace ideal para aplicaciones móviles u otras en las que el tamaño y el peso son factores críticos. El módulo de cámara tiene una resolución nativa de 5 megapíxeles y cuenta con una lente de enfoque fijo que captura imágenes estáticas a 2592 x 1944 píxeles, además de ser compatible con video en 1080p30, 720p60 y 640x480p90.

.. note:: 

   El módulo solo puede capturar imágenes y videos, no sonido.

**Especificaciones**

* **Resolución de imágenes estáticas**: 2592×1944 
* **Resolución de video compatible**: 1080p/30 fps, 720p/60 fps y 640 x 480p a 60/90 fps 
* **Apertura (F)**: 1.8 
* **Ángulo de visión**: 65 grados 
* **Dimensiones**: 24 mm x 23.5 mm x 8 mm 
* **Peso**: 3 g 
* **Interfaz**: Conector CSI 
* **Sistema operativo compatible**: Raspberry Pi OS (se recomienda la versión más reciente) 


**Montaje del Módulo de Cámara**


En el módulo de la cámara o en la Raspberry Pi, encontrarás un conector de plástico plano. Tira con cuidado del interruptor de fijación negro hasta que se deslice parcialmente hacia afuera. Inserta el cable FFC en el conector de plástico en la dirección mostrada y empuja el interruptor de fijación de nuevo en su lugar.


Si el cable FFC está instalado correctamente, estará recto y no se saldrá al tirar suavemente de él. Si no es así, vuelve a instalarlo.

.. image:: img/connect_ffc.png
.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   No instales la cámara con la alimentación encendida, ya que podrías dañar el módulo.

.. **Enable the Camera Interface**

.. Run the following command to enable the camera interface of your Raspberry Pi. If you have enabled it, skip this; if you do not know whether you have done that or not, please continue.

.. .. raw:: html

..    <run></run>

.. .. code-block:: 

..    sudo raspi-config

.. **3 Interfacing options**

.. .. image:: img/image282.png
..    :align: center

.. **P1 Camera**

.. .. image:: img/camera_config1.png
..    :align: center

.. **<Yes>, then <Ok> -> <Finish>**

.. .. image:: img/camera_config2.png
..    :align: center

.. After the configuration is complete, it is recommended to reboot the Raspberry Pi.

.. .. raw:: html

..    <run></run>

.. .. code-block:: 

..    sudo reboot