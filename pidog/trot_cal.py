#!/usr/bin/env python3
from math import pi, sin, cos
import numpy as np


def cal_trot():
    
    stride = 45
    raise_feet = 12
    stand = 85

    #中间变量设定
    x1_s=0;x2_s=0;x3_s=0;x4_s=0;y1_s=0;y2_s=0;y3_s=0;y4_s=0
    faai=0.50
    Ts=1
    step_t = 0.02

    f_center = -35
    h_center = 5
    f_stand = stand 
    h_stand = stand 
    x_up_inc = step_t*2*stride/(faai)
    x_dn_inc = step_t*2*stride/(Ts-faai)

    x1_st = f_center - stride
    x2_st = f_center + 1/3*stride
    x3_st = h_center - 1/3*stride
    x4_st = h_center + stride  

    def cal_t(t):   
        if t<=Ts*faai:  # 迈出腿1,4
            sigma=2*pi*t/(faai*Ts)
            zep=raise_feet*(1-cos(sigma))/2
            xep_b=stride*((sigma-sin(sigma))/(2*pi))
            xep_z=-stride*((sigma-sin(sigma))/(2*pi))+stride
            #输出y
            y1_s=-zep + stand
            y2_s=stand 
            y3_s=stand
            y4_s=-zep + stand
            #输出x
            x1_s=xep_z + f_center 
            x2_s=xep_b + f_center 
            x3_s=xep_b + h_center
            x4_s=xep_z + h_center

        elif t>Ts*faai and t<=Ts: # 迈出腿2,3
            sigma=2*pi*(t-Ts*faai)/(faai*Ts)
            zep=raise_feet*(1-cos(sigma))/2
            xep_b=stride*((sigma-sin(sigma))/(2*pi))
            xep_z=-stride*((sigma-sin(sigma))/(2*pi))+stride
            #输出y
            y1_s=stand 
            y2_s=-zep + stand 
            y3_s=-zep + stand 
            y4_s=stand
            #输出x
            x1_s=xep_b + f_center #-6
            x2_s=xep_z + f_center #-6
            x3_s=xep_z + h_center
            x4_s=xep_b + h_center

        # print([x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s])
        return [[x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s]]


    date =[]
    for t in np.arange(0.0,1.001,step_t):
        t = round(t,2)
        # print('t',t)
        result = cal_t(t)
        date.append(result)
    return date


