#!/usr/bin/env python3
from math import pi, sin, cos, sqrt, acos, atan2, atan
import numpy as np

def cal_backward_coords():
    
    stride = 30
    raise_feet = 20
    stand = 85

    #中间变量设定
    x1_s=0;x2_s=0;x3_s=0;x4_s=0;y1_s=0;y2_s=0;y3_s=0;y4_s=0
    faai=0.24
    Ts=0.96
    step_t = 0.02

    f_center = -30
    h_center = -5
    f_stand = stand 
    h_stand = stand 
    x_up_inc = step_t*2*stride/(faai)
    x_dn_inc = step_t*2*stride/(Ts-faai)
    x_up_inc = step_t*2*stride/(faai)
    x_dn_inc = -x_dn_inc

    x1_st = f_center - stride
    x2_st = f_center + 1/3*stride
    x3_st = h_center - 1/3*stride
    x4_st = h_center + stride  

    # backward, 4-2-3-1
    def cal_w(t):   

        nonlocal x1_s,x2_s,x3_s,x4_s,y1_s,y2_s,y3_s,y4_s
        nonlocal x1_st,x2_st,x3_st,x4_st
            #开始步态计算s

        if t == 0: #迈出腿1

            #输出y
            y1_s = f_stand
            y2_s = f_stand
            y3_s = h_stand
            y4_s = h_stand

            #输出x
            x1_s = f_center - stride
            x2_s = f_center + 1/3*stride
            x3_s = h_center -1/3*stride
            x4_s = h_center + stride 

            print('start, ', end='')

        elif t>0 and t<faai:    #迈出腿1
            sigma=2*pi*t/(faai)
            zep=raise_feet*(1-cos(sigma))/2
            # xep=2*stride*((sigma-sin(sigma))/(2*pi))

            if t== 0:
                x1_st = x1_s
                print('x1_st',x1_st)
            if t< 0.25/2:
                xep=2*stride*((2*sigma-sin(2*sigma))/(2*pi))
                xep = -xep
                x1_s = x1_st-xep

            #输出y
            y1_s = f_stand - zep
            y2_s = f_stand 
            y3_s = h_stand 
            y4_s = h_stand 
            #输出x

            # x1_s += -x_up_inc
            # x1_s = x1_st-xep
            x2_s += x_dn_inc 
            x3_s += x_dn_inc 
            x4_s += x_dn_inc 

            print('leg 1, ', end='')

        
        elif t>=faai and t<2*faai:    #迈出腿3

            t=t-faai
            sigma=2*pi*t/(faai)
            # zep=h*((sigma-sin(sigma))/(2*pi))
            xep=2*stride*((sigma-sin(sigma))/(2*pi))
            xep = -xep
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x3_st = x3_s
                print('x3_st',x3_st)
            # if t< 0.25/2:
            #     xep=2*stride*((2*sigma-sin(2*sigma))/(2*pi))
            #     x2_s = x2_st-xep

            #输出y
            y1_s = f_stand 
            y2_s = f_stand 
            y3_s = h_stand - zep
            y4_s = h_stand 
            #输出x
            x1_s += x_dn_inc
            x2_s += x_dn_inc 
            x3_s = x3_st-xep
            x4_s += x_dn_inc

            print('leg 3, ', end='')


        elif t>=2*faai and t<3*faai:    #迈出腿2
            t=t-faai*2
            sigma=2*pi*t/(faai)
            # zep=h*((sigma-sin(sigma))/(2*pi))
            # xep=2*stride*((sigma-sin(sigma))/(2*pi))
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x2_st = x2_s
                print('x2_st',x2_st)
            if t< 0.25/2:
                xep=2*stride*((2*sigma-sin(2*sigma))/(2*pi))
                xep = -xep
                x2_s = x2_st-xep


            #输出y
            y1_s = f_stand 
            y2_s = f_stand - zep 
            y3_s = h_stand 
            y4_s = h_stand 
            #输出x
            x1_s += x_dn_inc
            # x2_s += x_dn_inc
            x3_s += x_dn_inc
            x4_s += x_dn_inc

            print('leg 2, ', end='')

        elif t>=3*faai and t<4*faai:    #迈出腿4
            t=t-faai*3
            sigma=2*pi*t/(faai)
            xep=2*stride*((sigma-sin(sigma))/(2*pi))
            xep = -xep
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x4_st = x4_s
                print('x4_st',x4_st)
            # if t< 0.25/2:
            #     xep=2*stride*((2*sigma-sin(2*sigma))/(2*pi))
            #     x1_s = x1_st-xep


            #输出y
            y1_s = f_stand 
            y2_s = f_stand 
            y3_s = h_stand 
            y4_s = h_stand - zep
            #输出x
            # x1_
            x1_s += x_dn_inc
            x2_s += x_dn_inc 
            x3_s += x_dn_inc 
            x4_s = x4_st-xep 

            print('leg 4, ', end='')

        else:
            return [[x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s]]

        print([x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s])
        return [[x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s]]
        # return [[x2_s,y2_s],[x1_s,y1_s],[x4_s,y4_s],[x3_s,y3_s]]


    date =[]
    for t in np.arange(0.0,0.961,step_t):
        t = round(t,2)
        print('t',t)
        result = cal_w(t)
        date.append(result)
    return date
