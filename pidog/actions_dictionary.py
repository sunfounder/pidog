#!/usr/bin/env python3
from datetime import date
from .pidog import Pidog
from .walk_cal import cal_walk
from .backward_cal import cal_backward
from .turn_left_cal import cal_turn_left
from .turn_right_cal import cal_turn_right
from .trot_cal import cal_trot
from math import pi, sin, cos
import numpy as np


# ActionDict: - > angles_dict
class ActionDict(dict):

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs) 
        super().__init__()
        self.barycenter = -15
        self.height = 95

    def __getitem__(self, item):
        return eval("self.%s"%item.replace(" ", "_"))

    def set_height(self,height):
        if height in range(20,95):
            self.height = height

    def set_barycenter(self,offset):
        if offset in range(-60,60):
            self.barycenter = offset

# 站 stand
    @property
    def stand(self):
        x = self.barycenter 
        y = 105
        return [
            Pidog.feet_angle_calculation([[x,y],[x,y],[x+20,y-5],[x+20,y-5]])            
        ],'feet'
# 坐 sit
    @property
    def sit(self):
        return [     
            [30, 60, -30, -60, 80, -45, -80, 45],
            # [-20, 60, 20, -60, -80, -45, -80, 45]
        ],'feet'
# 趴 lie
    @property
    def lie(self):
        return [
            # [45,-30,-45,30,45,-45,-45,45], 
            # [52, -52, -52, 52, 45, -45, -45, 45],
            [45, -45, -45, 45, 45, -45, -45, 45]
        ],'feet'

    @property
    def lie_with_hands_out(self):
        return [
            [-60,60,60,-60,45,-45,-45,45], 
        ],'feet'

# 漫步 walk
    @property
    def walk(self):
        data = []
        coords = cal_walk()
        for coord in coords:
            data.append(Pidog.feet_angle_calculation(coord))
        return data,'feet'

# 小跑 trot
    @property
    def trot(self):
        data = []
        coords = cal_trot()
        for coord in coords:
            data.append(Pidog.feet_angle_calculation(coord))
        return data,'feet'   

# 后退 backward
    @property
    def backward(self):
        data = []
        coords = cal_backward()
        for coord in coords:
            data.append(Pidog.feet_angle_calculation(coord))
        return data,'feet'

# 左转 turn_left
    @property
    def turn_left(self):
        data = []
        coords = cal_turn_left()
        for coord in coords:
            data.append(Pidog.feet_angle_calculation(coord))
        return data,'feet'

# 右转 turn_right
    @property
    def turn_right(self):
        data = []
        coords = cal_turn_right()
        for coord in coords:
            data.append(Pidog.feet_angle_calculation(coord))
        return data,'feet'



# 伸懒腰 stretch
    @property 
    def stretch(self):
        return[
            [-80, 70, 80, -70, -20, 64, 20, -64],
        ],'feet'
# 俯卧撑 pushup
    @property 
    def pushup(self):
        return[
            [45, -25, -45, 25, 80, 70, -80, -70],
            [45, -25, -45, 25, 80, 70, -80, -70],
            [45, 25, -45, -25, 80, 70, -80, -70],
            [45, 25, -45, -25, 80, 70, -80, -70]
        ],'feet'    
# 打瞌睡 doze_off
    @property 
    def doze_off(self):
        start = -30
        am = 20
        anl_f = 0
        anl_b = 0
        angs = []   
        t = 4     
        for i in range(0,am+1,1): # up
            anl_f = start + i
            anl_b = 45 - i/2
            angs+= [[45, anl_f, -45, -anl_f, 45, -anl_b, -45, anl_b]]*t
        for _ in range(4): # stop
            anl_f = start + am
            anl_b = 45 - am/2
            angs+= [[45, anl_f, -45, -anl_f, 45, -anl_b, -45, anl_b]]*t
        for i in range(am,-1,-1): # down
            anl_f = start + i
            anl_b = 45 - i/2
            angs+= [[45, anl_f, -45, -anl_f, 45, -anl_b, -45, anl_b]]*t
        for _ in range(4): # stop
            anl_f = start 
            anl_b = 45
            angs+= [[45, anl_f, -45, -anl_f, 45, -anl_b, -45, anl_b]]*t
        
        return angs,'feet'

    @property 
    def nod_lethargy(self):
        y=0;r=0;p=30
        angs = []
        for i in range(21):
            r = round(10*sin(i*0.314),2)
            p = round(10*sin(i*0.628) - 30,2)
            if r == -10 or r == 10:
                for _ in range(10):
                    angs.append([y,r,p]) 
            angs.append([y,r,p]) 
        
        return angs,'head'
# 摇头
    @property
    def shake_head(self):
        amplitude = 60
        angs = []
        for i in range(21):
            y = round(sin(i*0.314),2)
            y1 = amplitude*sin(i*0.314) 
            angs.append([y1,0,0]) 
        return angs,'head'

# 左歪头
    @property
    def tilting_head_left(self):
        yaw = 0
        roll = -25
        pitch = 15
        return[
            [yaw,roll,pitch]
        ],'head'
# 右歪头
    @property
    def tilting_head_right(self):
        yaw = 0
        roll = 25
        pitch = 20
        return[
            [yaw,roll,pitch]
        ],'head'
# 左右歪头
    @property
    def tilting_head(self):
        yaw = 0
        roll = 22
        pitch = 20
        return [[yaw,roll,pitch]]*20 \
                + [[yaw,-roll,pitch]]*20 \
        ,'head'     
# 晕 

# 仰头吠叫 head_bark
    # @property
    # def head_bark(self):
    #     return [[0, 0, -20],
    #             [0, 0, 10],
    #             [0, 0, 10]
    #     ],'head'

    @property
    def head_bark(self):
        return [[0, 0, -40],
                [0, 0, -10],
                [0, 0, -10]
        ],'head'

# 摇尾巴 tail_wagging
    @property
    def tail_wagging(self):
        amplitude=50
        angs = []
        for i in range(21):
            a = round(sin(i*0.314),2)
            angs.append([amplitude*a])
        return angs,'tail'     

# head_up_down
    @property
    def head_up_down(self):
        # amplitude = 20
        # angs = []
        # for i in range(20):
        #     y = round(sin(i*0.314),3)
        #     y1 = amplitude*sin(i*0.314) 
        #     if y == -1 or y == 1:
        #         for _ in range(10):
        #             angs.append([0,0,y1]) 
        #     angs.append([0,0,y1]) 
        # return angs,'head'
        return[
            [0,0,20],
            [0,0,20],
            [0,0,-10]
        ],'head'

# half_sit
    @property
    def half_sit(self):
        return[
            [25, 25, -25, -25, 64, -45, -64, 45],
        ],'feet'
