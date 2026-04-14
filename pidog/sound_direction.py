#!/usr/bin/env python3
'''
                声音方位识别模块 通讯协议

1.通讯格式: master 随机发送16bit数据给slave,然后接收16bit数据
主控接收的16BIT 格式：
    (1) 先接收数据的低8bit,然后接收数据的高8bit
    (2) 遵从MSB传送

2.方向可以侦测360度方向,最小单位是20度。则数据范围为0~355.

3. 流程,主控拉高busy,064B(TR16F064B)开始监测方向。
   当064B识别到方向的时候,会拉低busy线(平时为高);主控监测到BUSY拉低,发16bit任意数据给064B,
   并接受16bit数据,接受完成后,主控把busy线拉高,再次检测方向.


        Sound Location Recognition Module Communication Protocol

1. Communication format: master randomly sends 16bit data to slave, and then receives 16bit data
16BIT format received by the master:
     (1) First receive the lower 8 bits of the data, and then receive the upper 8 bits of the data
     (2) Comply with MSB transmission

2. The direction can detect 360 degree direction, the minimum unit is 20 degrees. The data range is 0~355.

3. In the process, the master pulls up busy, and 064B (TR16F064B) starts to monitor the direction.
    When 064B recognizes the direction, it will pull down the busy line (usually high); the master monitors that BUSY is pulled low, and sends 16bit arbitrary data to 064B,
    And accept 16bit data, after the acceptance is completed, the main control pulls up the busy line and detects the direction again.

'''

import spidev
import lgpio
from time import sleep
from robot_hat.pin import Pin


class SoundDirection():
    CS_DELAY_US = 500  # us
    CLOCK_SPEED = 10000000  # 10 MHz

    def __init__(self, busy_pin=6):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.busy_pin = busy_pin
        # Use shared Pin._chip to avoid handle conflict
        if Pin._chip is None:
            Pin._chip = lgpio.gpiochip_open(0)
        self._chip = Pin._chip
        self.busy_reset()

    def busy_reset(self):
        """Reset busy line: pull HIGH (output), then monitor (input)."""
        # Free GPIO first (may fail if not claimed, that's OK)
        try:
            lgpio.gpio_free(self._chip, self.busy_pin)
        except:
            pass

        # Pull busy line HIGH to start direction detection
        lgpio.gpio_claim_output(self._chip, self.busy_pin, 1)
        sleep(0.01)

        # Switch to input mode to monitor when 064B pulls it LOW
        lgpio.gpio_free(self._chip, self.busy_pin)
        lgpio.gpio_claim_input(self._chip, self.busy_pin)

    def read(self):
        """Read sound direction angle (0-359) or -1 if no valid data."""
        result = self.spi.xfer2([0, 0, 0, 0, 0, 0], self.CLOCK_SPEED, self.CS_DELAY_US)

        l_val, h_val = result[4:]  # ignore first two values
        dir = -1
        if h_val != 255:
            dir = (h_val << 8) + l_val
            dir = (360 + 160 - dir) % 360  # Convert zero reference
        self.busy_reset()
        return dir

    def isdetected(self):
        """Check if sound direction is detected (busy line pulled LOW by 064B)."""
        return lgpio.gpio_read(self._chip, self.busy_pin) == 0

    def close(self):
        self.spi.close()
        try:
            lgpio.gpio_free(self._chip, self.busy_pin)
        except:
            pass

if __name__ == '__main__':
    sd = SoundDirection()
    while True:
        if sd.isdetected():
            print(f"Sound detected at {sd.read()} degrees")
        sleep(0.2)