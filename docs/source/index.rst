SunFounder Raspberry Pi 机器人 - |link_Pi_Dog|  
=======================================================

* |link_PiDog|  

.. image:: img/pidog.jpg  
    :width: 300  
    :align: center  

感谢您选择我们的 |link_Pi_Dog|。  

.. note::  
    本文档提供以下语言版本。  

        * |link_german_tutorials|  
        * |link_jp_tutorials|  
        * |link_en_tutorials|  
        * |link_fr_tutorials|  
        * |link_es_tutorials|  
        * |link_it_tutorials|  
    
    请点击相应的链接，以便以您偏好的语言查看文档。  

PiDog 是一款 Raspberry Pi 宠物机器人，采用铝合金结构。它可以充当机械宠物，向您展示可爱，并与您互动。  

它配备了一个摄像头模块，可以执行颜色识别、人脸检测等项目；  
12 个金属齿轮伺服电机支持其行走、站立、坐下、摇头，并摆出各种姿势；  
头部的超声波模块使其能够快速检测前方的障碍物；  
特制触摸传感器让它能响应您的触摸；  
胸部的灯光板可以发出多彩的灯光效果，并且配备的机器人 HAT 扬声器使 PiDog 能够表达喜悦、兴奋等情感。  
此外，PiDog 还配备了声音方向传感器和 6 自由度 IMU 模块，以实现更复杂和有趣的使用场景。  

如有任何问题，请发送电子邮件至 service@sunfounder.com，我们将尽快回复。  

该产品有两个版本：标准版和 V2 版。

**标准版**

此版本设计与大多数 Raspberry Pi 模型兼容，提供完整的套件功能。需要注意的是，它的伺服电机和机器人 HAT 与 Raspberry Pi 5 不兼容，因此标准版不适用于该型号。

**V2 版**

此升级版具有更新的 Robot HAT 和伺服配置，支持 Raspberry Pi 3/4/5 和 Zero W。增强功能使其能够在 Raspberry Pi 5 上实现更广泛的创意应用，同时保持向下兼容早期型号。

主要技术区别：

* 硬件迭代：V2 重新设计了伺服驱动和 HAT 电路，以适应 RPi5 的 GPIO 电压要求  
* 支持型号：标准版支持 RPi 3B+/4B/Zero 2W；V2 版增加了对 RPi5 的支持  
* 电源管理：V2 优化了对 RPi5 更高电流需求的电源供给  

**内容**  

.. toctree::  
    :maxdepth: 2  

    About This Kit <self>
    assemble_video
    python/play_with_python
    hardware/cpn_hardware
    appendix/appendix

版权声明  
--------------------------

本手册中的所有内容，包括但不限于文本、图片和代码，均为 SunFounder 公司所有。您仅可在相关法规和版权法规定下，出于个人学习、研究、娱乐或其他非商业性、非盈利性目的使用，不得侵犯作者及相关权利人的合法权利。任何个人或组织未经许可擅自将这些内容用于商业牟利，SunFounder 公司保留采取法律行动的权利。

