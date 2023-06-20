#!/usr/bin/env python3
import time
from smbus import SMBus
import numpy as np
import math

class RGBStrip():
    # preset colors define
    COLORS = {
        'white':   [255, 255, 255],
        'black':   [0,   0,   0],
        'red':     [255,   0,   0],
        'yellow':  [255, 225,   0],
        'green':   [0, 255,   0],
        'blue':    [0,   0, 255],
        'cyan':    [0, 255, 255],
        'magenta': [255,   0, 255],
        'pink':    [255, 100, 100]
    }

    # styles define
    STYLES = [
        "monochromatic",
        "breath",
        "boom",
        "bark",
        "speak",
        "listen",
    ]

    MIN_DELAY = 0.05

    # region constants
    CONFIGURE_CMD_PAGE = 0XFD
    FRAME1_PAGE = 0x00
    FRAME2_PAGE = 0x01
    FUNCTION_PAGE = 0X0B
    LED_VAF_PAGE = 0X0D

    CONFIGURATION_REG = 0X00
    PICTURE_DISPLAY_REG = 0X01
    DISPLAY_OPTION_REG = 0X05
    BREATH_CTL_REG = 0X08
    BREATH_CTL_REG2 = 0X09
    SW_SHUT_DOWN_REG = 0X0A

    AUDIO_GAIN_CTL_REG = 0X0B
    STAGGERED_DELAY_REG = 0X0D
    SLEW_RATE_CTL_REG = 0X0E
    CURRENT_CTL_REG = 0X0F
    VAF_CTL_REG = 0X14
    VAF_CTL_REG2 = 0X15

    MSKSTD1 = (0x3 << 0)
    MSKSTD2 = (0x3 << 2)
    MSKSTD3 = (0x3 << 4)
    MSKSTD4 = (0x3 << 6)
    CONST_STD_GROUP1 = 0x00
    CONST_STD_GROUP2 = 0x55
    CONST_STD_GROUP3 = 0xAA
    CONST_STD_GROUP4 = 0xFF

    MSKVAF1 = (0x4 << 0)
    MSKVAF2 = (0x4 << 4)
    MSKVAF3 = (0x4 << 0)
    MSKFORCEVAFTIME_CONST = (0x0 << 3)
    MSKFORCEVAFCTL_ALWAYSON = (0x0 << 6)
    MSKFORCEVAFCTL_DISABLE = (0x2 << 6)
    MSKCURRENT_CTL_EN = (0x1 << 7)
    CONST_CURRENT_STEP_20mA = (0x19 << 0)
    mskBLINK_FRAME_300 = (0x0 << 6)
    mskBLINK_EN = (0x1 << 3)
    mskBLINK_DIS = (0x0 << 3)
    mskBLINK_PERIOD_TIME_CONST = (0x7 << 0)

    Type3Vaf = [
        # Frame 1
        0x50, 0x55, 0x55, 0x55,  # C1-A ~ C1-P
        0x00, 0x00, 0x00, 0x00,  # C2-A ~ C2-P
        0x00, 0x00, 0x00, 0x00,  # C3-A ~ C3-P
        0x15, 0x54, 0x55, 0x55,  # C4-A ~ C4-P
        0x00, 0x00, 0x00, 0x00,  # C5-A ~ C5-P
        0x00, 0x00, 0x00, 0x00,  # C6-A ~ C6-P
        0x55, 0x05, 0x55, 0x55,  # C7-A ~ C7-P
        0x00, 0x00, 0x00, 0x00,  # C8-A ~ C8-P
        # Frame 2
        0x00, 0x00, 0x00, 0x00,  # C9-A ~ C9-P
        0x55, 0x55, 0x41, 0x55,  # C10-A ~ C10-P
        0x00, 0x00, 0x00, 0x00,  # C11-A ~ C11-P
        0x00, 0x00, 0x00, 0x00,  # C12-A ~ C12-P
        0x55, 0x55, 0x55, 0x50,  # C13-A ~ C13-P
        0x00, 0x00, 0x00, 0x00,  # C14-A ~ C14-P
        0x00, 0x00, 0x00, 0x00,  # C15-A ~ C15-P
        0x00, 0x00, 0x00, 0x00,  # C16-A ~ C16-P
    ]
    # endregion constants

    def __init__(self, addr=0X74, nums=8):
        """
        :param addr: i2c address
        :nums: number of lights
        """
        self.light_num = nums

        self.style = 'breath',
        self.color = 'white',
        self.brightness = 1,
        self.delay = 0.1
        self.frames = []
        self.current_frame = 0
        self.bps = 1.5 # beats per second
        self.is_changed = False

        # Initial
        # =================================================================
        self.bus = SMBus(1)
        self.addr = addr

        # Setting SLED1735 Ram Page to Function Page
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FUNCTION_PAGE)
        # System must go to SW shutdowm mode when initialization
        self.write_cmd(self.SW_SHUT_DOWN_REG, 0x0)
        # Setting Matrix Type = Type3
        self.write_cmd(self.PICTURE_DISPLAY_REG, 0x10)
        self.write_cmd(self.STAGGERED_DELAY_REG, ((self.MSKSTD4 & self.CONST_STD_GROUP4) | (self.MSKSTD3 & self.CONST_STD_GROUP3) | (
            self.MSKSTD2 & self.CONST_STD_GROUP2) | (self.MSKSTD1 & self.CONST_STD_GROUP1)))  # Setting Staggered Delay
        self.write_cmd(self.SLEW_RATE_CTL_REG, 0x1)  # Enable Slew Rate control
        # VAF Control settings base on the LED type.
        self.write_cmd(self.VAF_CTL_REG, (self.MSKVAF2 | self.MSKVAF1))
        self.write_cmd(self.VAF_CTL_REG2, (self.MSKFORCEVAFCTL_DISABLE |
                       self.MSKFORCEVAFTIME_CONST | self.MSKVAF3))
        # Setting LED driving current = 20mA and Enable current control
        self.write_cmd(self.CURRENT_CTL_REG,
                       (self.MSKCURRENT_CTL_EN | self.CONST_CURRENT_STEP_20mA))
        # Init Frame1Page(Clear all Ram) Setting SLED1735 Ram Page to Frame 1 Page
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME1_PAGE)
        # send 0xB3 bytes length Data From address 0x00
        self.write_Ndata(0x00, 0X00, 0XB3)
        # Clear Type3 Frame 2 Page
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME2_PAGE)
        # send 0xB3 bytes length Data From address 0x00
        self.write_Ndata(0x00, 0X00, 0XB3)
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.LED_VAF_PAGE)
        self.write_Ndata(0X00, self.Type3Vaf, 0X40)
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FUNCTION_PAGE)
        # After initialization , system back to SW Normal mode.
        self.write_cmd(self.SW_SHUT_DOWN_REG, 0x1)
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME1_PAGE)
        # Clear LED CTL Registers (Frame1Page)
        self.write_Ndata(0X00, 0XFF, 0X10)
        self.write_Ndata(0x20, 0x00, 0X80)
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME2_PAGE)
        # Clear LED CTL Registers (Frame1Page)
        self.write_Ndata(0X00, 0XFF, 0X10)
        self.write_Ndata(0x20, 0x00, 0X80)

    # i2c communicate
    # =================================================================
    def write_cmd(self, reg, cmd):
        self.bus.write_byte_data(self.addr, reg, cmd)

    def write_Ndata(self, startaddr, data, length):
        addr = startaddr
        if isinstance(data, int):
            for i in range(length):
                self.write_cmd(addr, data)
                addr += 1
        elif isinstance(data, list):
            for i in range(length):
                self.write_cmd(addr, data[i])
                addr += 1

    # display fuction
    # =================================================================
    def display(self, image):
        """
        Display the rgb datas

        :param image: rgb datas, should be a x*3 array 
        :type image: list [[r, g, b], [r, g, b], ...]
        """
        # 'lambda x: x[0]'  same as  'fun(x): return x[0]'
        reds = list(map(lambda x: x[0], image))
        greens = list(map(lambda x: x[1], image))
        blues = list(map(lambda x: x[2], image))
        revert_image = [reds, greens, blues]

        reg = 0x20  # Register start address of a page
        empty = 0  # Register address vacancy position (needs to be filled with 0)
        pos = 0  # data position, index

        for i in range(3):
            # Set the page to write
            if i == 0:
                self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME1_PAGE)  
            elif reg == 0x20:
                self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME2_PAGE)

            color = i % 3
            data = revert_image[color][pos*14:(pos+1)*14]
            data.insert(empty, 0)  # The written data is filled with 0
            data.insert(empty + 1, 0)

            self.bus.write_i2c_block_data(self.addr, reg, data)
            if color == 2:
                empty += 3
                pos += 1
            reg += 0x10
            if reg == 0xA0:
                reg = 0x20

    # 
    # calulate rgb data of different styles
    # =================================================================
    def monochromatic(self, color="white"):
        """
        monochromatic style
        """
        color = [i*self.brightness for i in color]
        return color

    def Normal_distribution_calculate(self, u, sig, A, x, offset):
        """
        Normal distribution calculate

        :param u: mathematical expectation, average value, affects the x position of the highest point 
        :type u: float or int
        :param sig: standard deviation, affects the magnitude and range of the central area
        :type sig: float or int
        :param A: amplitude ratio
        :type  A: float or int
        :param x: x pos
        :type x: int
        :param offset: amplitude offset
        :type offset: float or int
        :return: Normal distribution y(x)
        :rtype: float or int
        """
        y = A*np.exp(-(x-u)**2/(2*sig**2))/(math.sqrt(2*math.pi)*sig) + offset
        return y

    def cos_func(self, peak, a, x, offset=0):
        """
        cos fuction

        :param peak:
        :param a: multiple
        :param x: xpos
        :return: result, float  or int
        """
        return (peak/2.0) * math.cos(a*x + offset) + peak/2

    def breath(self, frame_index, light_index, color='pink', A=5, sig=2):
        """
        breath style, from dark to bright, and then from bright to dark

        :param frame_index: the index of the frame
        :type frame_index: int
        :param light_index: the index of the light
        :type light_index: int
        :param color: rgb display color
        :type color: str , 1*3 list, tuple, eg: "white", "WHITE", "#a2c20c", 0xa2c20c, [168, 192, 203], (168, 192, 203)
        :param A: amplitude ratio
        :type  A: float or int
        :param sig: standard deviation
        :type sig: float or int
        :return list of 11*[r, g, b] values
        :rtype: list, 11*[int, int, int]
        """
        # https://www.geogebra.org/calculator/qz3vsjjn
        u = 5
        color = [i*self.brightness for i in color]
        multiple = float(2*math.pi/(self.max_frames)) # multiple, period = max_frames
        offset = -self.cos_func(1, multiple, frame_index)
        brightness = self.Normal_distribution_calculate(u, sig, A, light_index, offset)
        return list([max(0, int(c * brightness)) for c in color])

    def boom(self, frame_index, light_index, color='pink', A=5, sig=2):
        """
        boom style, from dark to bright (from middle to both sides)

        :param frame_index: the index of the frame
        :type frame_index: int
        :param light_index: the index of the light
        :type light_index: int
        :param color: rgb display color
        :type color: str , 1*3 list, tuple, eg: "white", "WHITE", "#a2c20c", 0xa2c20c, [168, 192, 203], (168, 192, 203)
        :param A: amplitude ratio
        :type  A: float or int
        :param sig: standard deviation
        :type sig: float or int
        :return: list of 11*[r, g, b] values
        :rtype: list, 11*[int, int, int]
        """
        # https://www.geogebra.org/calculator/gpmxfpks
        u = 5
        color = [i*self.brightness for i in color]
        multiple = float(2*math.pi/(self.max_frames*2.0)) # multiple, period = 2*max_frames
        offset = -self.cos_func(1, multiple, frame_index)
        brightness = self.Normal_distribution_calculate(u, sig, A, light_index, offset)
        return list([max(0, int(c * brightness)) for c in color])

    def bark(self, frame_index, light_index, color='pink', A=2.5, sig=1):
        """
        bark style, from middle to both sides

        :param frame_index: the index of the frame
        :type frame_index: int
        :param light_index: the index of the light
        :type light_index: int
        :param color: rgb display color
        :type color: str , 1*3 list, tuple, eg: "white", "WHITE", "#a2c20c", 0xa2c20c, [168, 192, 203], (168, 192, 203)
        :param A: amplitude ratio
        :type  A: float or int
        :param sig: standard deviation
        :type sig: float or int
        :return: list of 11*[r, g, b] values
        :rtype: list, 11*[int, int, int]
        """
        # https://www.geogebra.org/calculator/yyemmqht
        color = [i*self.brightness for i in color]
        peak = (self.light_num-1)/2
        multiple = float(2*math.pi/(self.max_frames*2.0)) # multiple, period = 2*max_frames
        u_offset = self.cos_func(peak, multiple, frame_index)
        if light_index <= peak:
            u = u_offset 
        else:
            u = 2*peak - u_offset
        brightness = self.Normal_distribution_calculate(u, sig, A, light_index, 0)
        return list([max(0, int(c * brightness)) for c in color])

    def speak(self, frame_index, light_index, color='pink', A=2.5, sig=1):
        """
        speak style, from middle to both sides, then from both sides to middle

        """
        # https://www.geogebra.org/calculator/tpzypj5s
        color = [i*self.brightness for i in color]
        peak = (self.light_num-1)/2
        multiple = float(2*math.pi/(self.max_frames)) # multiple, period = max_frames
        u_offset = self.cos_func(peak, multiple, frame_index)
        if light_index <= peak:
            u = u_offset 
        else:
            u = 2*peak - u_offset
        brightness = self.Normal_distribution_calculate(u, sig, A, light_index, 0)
        return list([max(0, int(c * brightness)) for c in color])

    def listen(self, frame_index, light_index, color='pink', A=2.5, sig=1):
        """
        listen style, from middle to left, then from left to right, finally from right to middle

        """
        # https://www.geogebra.org/calculator/gwbrzrkt
        color = [i*self.brightness for i in color]
        peak = self.light_num-1
        multiple = float(2*math.pi/(self.max_frames)) # multiple, period = max_frames
        offset = math.pi/2 # offset left pi/2
        u = self.cos_func(peak, multiple, frame_index, offset)
        brightness = self.Normal_distribution_calculate(u, sig, A, light_index, 0)
        return list([max(0, int(c * brightness)) for c in color])

    # set mode
    # =================================================================
    def colorConvertor(self, color):
        """"
        Unify color values to [r, g, b]
        
        :param color: color value
        :type color: str , 1*3 list, tuple, eg: "white", "WHITE", "#a2c20c", 0xa2c20c, [168, 192, 203], (168, 192, 203) 
        :return: list of r,g,b values
        :rtype: list
        """
        try:
            if isinstance(color, str):
                if color.lower() in self.COLORS:
                    return self.COLORS[color.lower()]
                elif color.startswith('#') and len(color) == 7:
                    return [int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)]
                else:
                    raise # trigger exception
            elif isinstance(color, list) or isinstance(color, tuple):
                return [color[0], color[1], color[2]]
            elif isinstance(color, int):
                return [color >> 16, color >> 8 & 0xff, color & 0xff]
        except:
            raise ValueError('\033[0;31m%s\033[0m'%("Invalid color value."))

    def set_mode(self, style='breath', color='white', bps=1, brightness=1):
        """
        Set the display mode of the rgb strip

        :param style: rgb display style
        :type style: str
        :param color: rgb display color
        :type color: str , 1*3 list, tuple, eg: "white", "WHITE", "#a2c20c", 0xa2c20c, [168, 192, 203], (168, 192, 203)
        :param bps: beats per second, this number of style actions executed per second
        :type bps: float or int
        :param brightness: rgb display brightness
        :type brightness: float or int
        """
        if style in self.STYLES:
            self.style = style
        else:
            self.style = None
            raise ValueError("Invalid style value.")

        color = self.colorConvertor(color)
        self.color = color

        if isinstance(bps, int) or isinstance(bps, float):
            self.bps = bps
        else:
            raise ValueError("Invalid bps value.")

        if isinstance(brightness, int) or isinstance(brightness, float):
            self.brightness = brightness
        else:
            raise ValueError("Invalid brightness value.")

        self.is_changed = True
        

    # calulate and display frames
    # =================================================================
    def calulate_data(self, frame_index, light_index):
        if self.style == "monochromatic":
            return self.monochromatic(color=self.color)
        elif self.style == 'breath':
            return self.breath(frame_index, light_index, color=self.color)
        elif self.style == 'boom':
            return self.boom(frame_index, light_index, color=self.color)
        elif self.style == 'bark':
            return self.bark(frame_index, light_index, color=self.color)
        elif self.style == 'speak':
            return self.speak(frame_index, light_index, color=self.color)
        elif self.style == 'listen':
            return self.listen(frame_index, light_index, color=self.color)

    def show(self):
        if self.style is None:
            if self.is_changed:
                self.is_changed = False
                self.display([[0, 0, 0]]*self.light_num)
            time.sleep(self.MIN_DELAY)
            return
        else:
            # if changed, calulate frames
            if self.is_changed:
                self.is_changed = False
                self.frames.clear()
                self.max_frames = int(1/self.bps/self.MIN_DELAY)
                for frame_index in range(self.max_frames):
                    frame = [] # 11*[r, g ,b]
                    for light_index in range(self.light_num):
                        _data = self.calulate_data(frame_index, light_index)
                        frame.append(_data)
                    if __name__ == '__main__':
                        print(f"{frame_index}:{frame}")
                    self.frames.append(frame)
            # dispaly frame-by-frame, to quickly change mode or close 
            if self.current_frame >= self.max_frames:
                self.current_frame = 0
            self.display(self.frames[self.current_frame])
            self.current_frame += 1
            time.sleep(self.MIN_DELAY)

    def close(self):
        self.style = None
        self.is_changed = True

if __name__ == '__main__':
    rgb = RGBStrip(0X74, 11)
    # rgb.set_mode(style="monochromatic", color="white", bps=5, brightness=1)
    # rgb.set_mode(style="breath", color="pink", bps=1.5, brightness=1)
    # rgb.set_mode(style="boom", color="yellow", bps=2.5, brightness=1)
    # rgb.set_mode(style="bark", color="red", bps=2.5, brightness=1)
    # rgb.set_mode(style="speak", color="magenta", bps=1, brightness=1)
    rgb.set_mode(style="listen", color="cyan", bps=0.5, brightness=1)
    try:
        while True:
            rgb.show()
    finally:
        rgb.close()
        rgb.show()
        print("close while exiting.")

