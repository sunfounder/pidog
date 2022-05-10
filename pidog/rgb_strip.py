#!/usr/bin/env python3
import time
from smbus import SMBus
import numpy as np
import math
# from PIL import Image


class RGB_Strip():

# color define
    colors_dict = {
        'white': [255,255,255],
        'black': [  0,  0,  0],
        'red':   [255,  0,  0],
        'green': [  0,255,  0],
        'blue':  [  0,  0,255],
        'yellow':[255,255,  0],
        'pink':  [255,192,203]
    }

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

    MSKSTD1 = (0x3<<0)	
    MSKSTD2 = (0x3<<2)
    MSKSTD3 = (0x3<<4)	
    MSKSTD4 = (0x3<<6)
    CONST_STD_GROUP1 = 0x00		
    CONST_STD_GROUP2 = 0x55	
    CONST_STD_GROUP3 = 0xAA		
    CONST_STD_GROUP4 = 0xFF

    MSKVAF1 = (0x4<<0) 
    MSKVAF2 = (0x4<<4)
    MSKVAF3 = (0x4<<0)
    MSKFORCEVAFTIME_CONST= (0x0<<3)
    MSKFORCEVAFCTL_ALWAYSON = (0x0<<6)
    MSKFORCEVAFCTL_DISABLE = (0x2<<6)
    MSKCURRENT_CTL_EN = (0x1<<7)
    CONST_CURRENT_STEP_20mA = (0x19<<0)
    mskBLINK_FRAME_300 = (0x0<<6)
    mskBLINK_EN = (0x1<<3)
    mskBLINK_DIS = (0x0<<3)
    mskBLINK_PERIOD_TIME_CONST = (0x7<<0)

    Type3Vaf = [
    #Frame 1
	0x50, 0x55, 0x55, 0x55, #C1-A ~ C1-P
	0x00, 0x00, 0x00, 0x00, #C2-A ~ C2-P
	0x00, 0x00, 0x00, 0x00, #C3-A ~ C3-P  
	0x15, 0x54, 0x55, 0x55, #C4-A ~ C4-P 
	0x00, 0x00, 0x00, 0x00, #C5-A ~ C5-P  
	0x00, 0x00, 0x00, 0x00, #C6-A ~ C6-P 
	0x55, 0x05, 0x55, 0x55, #C7-A ~ C7-P  
	0x00, 0x00, 0x00, 0x00, #C8-A ~ C8-P
	#Frame 2
	0x00, 0x00, 0x00, 0x00, #C9-A ~ C9-P 
	0x55, 0x55, 0x41, 0x55, #C10-A ~ C10-P 
	0x00, 0x00, 0x00, 0x00, #C11-A ~ C11-P  
	0x00, 0x00, 0x00, 0x00, #C12-A ~ C12-P 
	0x55, 0x55, 0x55, 0x50, #C13-A ~ C13-P  
	0x00, 0x00, 0x00, 0x00, #C14-A ~ C14-P 
	0x00, 0x00, 0x00, 0x00, #C15-A ~ C15-P 
	0x00, 0x00, 0x00, 0x00, #C16-A ~ C16-P 
    ]

# endregion constants

# region init
    def __init__(self, addr):

        self.light_num = 11

        self.style = 'breath', 
        self.font_color = 'white', 
        self.back_color = 'black',
        self.brightness = 1, 
        self.delay = 0.1

        self.bus = SMBus(1)
        self.addr = addr

        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FUNCTION_PAGE)  #Setting SLED1735 Ram Page to Function Page
        self.write_cmd(self.SW_SHUT_DOWN_REG, 0x0)  #System must go to SW shutdowm mode when initialization
        self.write_cmd(self.PICTURE_DISPLAY_REG, 0x10)  #Setting Matrix Type = Type3
        self.write_cmd(self.STAGGERED_DELAY_REG, ((self.MSKSTD4 & self.CONST_STD_GROUP4)|(self.MSKSTD3 & self.CONST_STD_GROUP3)|(self.MSKSTD2 & self.CONST_STD_GROUP2)|(self.MSKSTD1 & self.CONST_STD_GROUP1)))  #Setting Staggered Delay
        self.write_cmd(self.SLEW_RATE_CTL_REG, 0x1)  #Enable Slew Rate control
        self.write_cmd(self.VAF_CTL_REG, (self.MSKVAF2 | self.MSKVAF1))  #VAF Control settings base on the LED type.
        self.write_cmd(self.VAF_CTL_REG2, (self.MSKFORCEVAFCTL_DISABLE | self.MSKFORCEVAFTIME_CONST | self.MSKVAF3))
        self.write_cmd(self.CURRENT_CTL_REG, (self.MSKCURRENT_CTL_EN | self.CONST_CURRENT_STEP_20mA))  #Setting LED driving current = 20mA and Enable current control
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME1_PAGE)  #Init Frame1Page(Clear all Ram) Setting SLED1735 Ram Page to Frame 1 Page
        self.write_Ndata(0x00, 0X00, 0XB3)  #send 0xB3 bytes length Data From address 0x00
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME2_PAGE)  #Clear Type3 Frame 2 Page 
        self.write_Ndata(0x00, 0X00, 0XB3)  #send 0xB3 bytes length Data From address 0x00
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.LED_VAF_PAGE)
        self.write_Ndata(0X00, self.Type3Vaf, 0X40)
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FUNCTION_PAGE)
        self.write_cmd(self.SW_SHUT_DOWN_REG, 0x1)  #After initialization , system back to SW Normal mode.
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME1_PAGE)
        self.write_Ndata(0X00, 0XFF, 0X10)  #Clear LED CTL Registers (Frame1Page)
        self.write_Ndata(0x20, 0x00, 0X80)
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME2_PAGE)
        self.write_Ndata(0X00, 0XFF, 0X10)  #Clear LED CTL Registers (Frame1Page)
        self.write_Ndata(0x20, 0x00, 0X80)

# endregion init

# i2c communicate
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
  
# image should be a 3-column two-digit array
    def display(self, image):

        reds = list(map(lambda x: x[0], image))     # 'lambda x: x[0]'  same as  'fun(x): return x[0]'
        greens = list(map(lambda x: x[1], image))
        blues = list(map(lambda x: x[2], image))
        revert_image = [reds, greens, blues]

        reg = 0x20  #一页的寄存器起始地址
        empty = 0  #寄存器地址空缺的位置（写入的数据需要补0）
        pos = 0  #数据列表需要写入的数据所对应的索引

        for i in range(3):
            if i == 0:
                # print("Write Page 1")
                self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME1_PAGE)  #设置写入的页
            elif reg == 0x20:
                # print("Write Page 2")
                self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME2_PAGE)

            color = i % 3
            data = revert_image[color][pos*14:(pos+1)*14]
            data.insert(empty,0)  #写入的数据补0
            data.insert(empty + 1, 0)

            self.bus.write_i2c_block_data(self.addr, reg, data)
            if color == 2:
                empty += 3
                pos += 1
            reg += 0x10
            if reg == 0xA0:
                reg = 0x20

# styles
    def monochromatic(self,color='white'): 
           
        data = [ color ]*self.light_num
        data.reverse()
        self.display(data)


    def increase(self,direction='low',font_color='white',back_color='black',delay=0.1):
        background = self.colors_dict[back_color]* self.light_num
        data=[]
        for i in range(self.light_num):
            data[i] = self.colors_dict[font_color]
        self.display(data)


    def Normal_distribution_calculate(self,u,sig,a,x,offset):
        y = a*np.exp(-(x-u)**2/(2*sig**2))/(math.sqrt(2*math.pi)*sig) + offset
        return y

    def cosine_calculate(self,x):
        return math.sin(x) 

    def Normal_distribution_display(self,u, sig, a, offset, color):
        data = []
        for x in range(self.light_num):
            brightness = self.Normal_distribution_calculate(u, sig, a, x, offset)
            # print(brightness)
            data.append(list([max(0, int(c * brightness)) for c in color]))
        # print(data)
        self.display(data)

    def cos_func(self,max, a, x):
        return max/2 * math.cos(a*x) + max/2

    def drop_move_back_forth(self,color='yellow',
        delay=0.1,
        a=5,
        sig = 2):

        u = 0
        offset = 0
        start = int(-(self.light_num/2))
        end = int(self.light_num *1.5)


        while True:
            for u in range(start, end, 1):
                self.Normal_distribution_display(u, sig, a, offset, color)
                time.sleep(delay)
            for u in range(end, start, -1):
                self.Normal_distribution_display(u, sig, a, offset, color)
                time.sleep(delay)

    # def breath(color=Pink,frequency_min=)
    def drop_move_breath(self,color='pink',
        delay=0.1,
        a=5,
        sig = 2):

         
        u = 5
        start = int(-(self.light_num/2))
        end = int(self.light_num *1.5)

        def loop(u, sig, a, offset):
            data = []
            for x in range(self.light_num):
                brightness = self.Normal_distribution_calculate(u, sig, a, x, offset)
                print(brightness)
                data.append(list([max(0, int(c * brightness)) for c in color]))
            print(data)
            self.display(data)
            time.sleep(delay)


        while True:
            for x in range(0, 32, 1):
                offset = -self.cos_func(1, 20, x / 100)
                self.Normal_distribution_display(u, sig, a, offset, color)
                time.sleep(delay)
            for x in range(0, 32, 1):
                offset = -self.cos_func(0.7, 20, x / 100)
                self.Normal_distribution_display(u, sig, a, offset, color)
                time.sleep(delay)
            time.sleep(delay*260)


    # 


   
    
    # def breath_once(self,color='pink',delay=0.1,hold=0.1,a=5,sig = 2):
    #     u = 5
    #     color = [i*self.brightness for i in color]
    #     for x in range(0, 15, 1):
    #         offset = -self.cos_func(1, 20, x / 100)
    #         self.Normal_distribution_display(u, sig, a, offset, color)
    #         time.sleep(delay)
    #     time.sleep(hold) 
    #     for x in range(16, 32, 1):
    #         offset = -self.cos_func(1, 20, x / 100)
    #         self.Normal_distribution_display(u, sig, a, offset, color)
    #         time.sleep(delay)
    #     time.sleep(hold)

    def breath_once(self,color='pink',a=5,sig = 2, frame=None, i=None):
        u = 5
        color = [i*self.brightness for i in color]
        
        offset = -self.cos_func(1, 20, frame/100)
        brightness = self.Normal_distribution_calculate(u, sig, a, i, offset)
        return list([max(0, int(c * brightness)) for c in color])

    def boom(self,color='pink',a=5,sig = 2, frame=None, i=None):
        u = 5
        color = [i*self.brightness for i in color]
        
        offset = -self.cos_func(1, 40, frame/100)
        brightness = self.Normal_distribution_calculate(u, sig, a, i, offset)
        return list([max(0, int(c * brightness)) for c in color])

    def bark(self,color='pink',
        a=5,
        sig = 2, frame=None, i=None):

        u = 5
        color = [i*self.brightness for i in color]
        
        offset = -self.cos_func(1, 20, frame/100)
        brightness = self.Normal_distribution_calculate(u, sig, a, i, offset)
        return list([max(0, int(c * brightness)) for c in color])

    def mode(self, frame, i):
        if self.style == 'breath':
            return self.breath_once(color=self.font_color, frame=frame, i=i)
        elif self.style == 'boom':
            return self.boom(color=self.font_color, frame=frame, i=i)
        elif self.style == 'bark':
            return self.bark(color=self.font_color, frame=frame, i=i)
        

    

    def set_mode(self, style='breath', font_color='white', back_color='black',brightness=1, delay=0.01):
        color = self.colors_dict[font_color]
        try: 
            font_color = self.colors_dict[font_color]
            back_color = self.colors_dict[back_color]
        except KeyError:
            raise KeyError('Without this color !')
        except Exception as e:
            print(e)    

        self.style = style 
        self.font_color = font_color
        self.back_color = back_color
        self.brightness = brightness
        self.delay = delay

         
    def show(self):
        if self.style != None:
            for frame in range(0, 32, 1):
                
                datas = []
                for i in range(self.light_num):
                    data = self.mode(frame, i)
                    datas.append(data)
                self.display(datas)
                time.sleep(self.delay)



    

if __name__=='__main__':
    strip = RGB_Strip(0X74)
    strip.set_mode('bark','yellow')
    while True:
        strip.show()