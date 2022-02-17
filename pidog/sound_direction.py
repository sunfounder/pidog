#!/usr/bin/env python3
'''     
                声音方位识别模块 通讯协议

1.通讯格式：master 随机发送16bit数据给slave，然后接收16bit数据
主控接收的16BIT 格式：
    (1) 先接收数据的低8bit，然后接收数据的高8bit
    (2) 遵从MSB传送

2.方向可以侦测360度方向，最小单位是20度。则数据范围为0~355.

3. 流程，主控拉高busy，064B（TR16F064B）开始监测方向。
   当064B识别到方向的时候，会拉低busy线（平时为高）;主控监测到BUSY拉低，发16bit任意数据给064B，
   并接受16bit数据，接受完成后，主控把busy线拉高，再次检测方向.

'''

import spidev
from robot_hat import Pin
from time import sleep

class Sound_direction():
    def __init__(self,busy_pin=6):
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)
        self.spi.max_speed_hz = 500000
        self.spi.no_cs = True

        self.busy = Pin(busy_pin)
        self.cs = Pin(8)

    def read(self):
        self.cs.value(0)
        _, _ = self.spi.xfer2([0,0])  # ignore the fist value read
        l_val, h_val = self.spi.xfer2([0,0])
        val = (h_val << 8)+ l_val
        val = (360+160-val)%360  # Convert zero
        # sleep(0.02)
        # self.cs.value(1)
        # print('l_val, h_val : %s,%s'%(l_val, h_val))
        return val

    def isdetected(self):
        return self.busy.value() == 0


if __name__ == "__main__":
    
    sd = Sound_direction()
    # while sd.cs.value():
    #     sleep(0.05)
    print('start')
    while True:
        # sd.cs.value()
        
        if sd.isdetected():
            sleep(0.2)
            print(sd.read())
        sleep(0.2)


      