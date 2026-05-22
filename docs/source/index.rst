.. note::

    您好，欢迎加入 SunFounder Raspberry Pi & Arduino & ESP32 爱好者 Facebook 社区！与众多爱好者一起深入了解 Raspberry Pi、Arduino 和 ESP32。

    **为何加入？**

    - **专家支持**：我们的社区和团队将为您提供售后问题和技术难题的帮助。
    - **学习与分享**：交流技巧和教程，提升您的技能。
    - **独家预览**：抢先获取新产品公告和预告。
    - **特别折扣**：享受我们最新产品的专属折扣。
    - **节日促销与赠品**：参与赠品和节日促销活动。

    👉 准备好和我们一起探索和创造了吗？点击 [|link_sf_facebook|] 立即加入！

SunFounder Raspberry Pi Robot - |link_Pi_Dog|
=================================================

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
        * |link_zh_tutorials|

    请点击相应链接，以您偏好的语言查看文档。


PiDog 是一款采用铝合金结构的 Raspberry Pi 宠物机器人。它可以作为一只机械宠物，向您撒娇并与您互动。

它配备了摄像头模块，可以实现颜色识别、人脸检测等功能；
12 个金属齿轮舵机支持它行走、站立、坐下、摇头和各种姿势摆拍；
头部的超声波模块使其能够快速检测前方的障碍物；
特殊的触摸传感器让它能对您的触摸做出响应；
胸口的灯板可以发出多彩的光效，配合 Robot HAT 所配备的扬声器，PiDog 能够表达开心、兴奋等情绪。
此外，PiDog 还配备了声音方向传感器和 6 轴 IMU 模块，以实现更复杂、更有趣的使用场景。


如果您有任何问题，请发送邮件至 service@sunfounder.com，我们会尽快回复。



该产品提供 Standard 和 V2 两个版本。


**Standard 版本**


    .. image:: img/pidog_v1_box.png
     :width: 500


该版本设计兼容大多数 Raspberry Pi 型号，提供套件的全部功能。需要注意的是，其舵机和 Robot HAT 不兼容 Raspberry Pi 5，因此 Standard 版本不适合与 Raspberry Pi 5 搭配使用。


**V2 版本**


    .. image:: img/pidog_v2_box.png
     :width: 500


这一升级版本采用了更新的 Robot HAT 和舵机配置，兼容 Raspberry Pi 3/4/5 和 Zero 2W。这些改进在保持与旧型号向后兼容的同时，扩展了在 Raspberry Pi 5 上的创意应用。

主要技术区别：

* 硬件迭代：V2 重新设计了舵机驱动和 HAT 电路，以满足 RPi5 的 GPIO 电压要求
* 型号覆盖：Standard 支持 RPi 3B+/4B/Zero 2W；V2 增加了对 RPi5 的支持
* 电源管理：V2 优化了供电设计，满足 RPi5 更高的电流需求



**目录**

.. toctree::
    :maxdepth: 2

    About This Kit <self>
    assemble_video
    python/play_with_python
    ai_interaction/ai_interaction
    hardware/cpn_hardware
    appendix
    faq

版权声明
--------------------------

本手册中的所有内容（包括但不限于文字、图片和代码）均归 SunFounder 公司所有。您只能将其用于个人学习、研究、娱乐或其他非商业或非盈利目的，并遵守相关法规和版权法律，不得侵犯作者及相关权利人的合法权益。对于任何未经许可将本手册用于商业盈利的个人或组织，本公司保留追究法律责任的权利。
