#!/usr/bin/env python3

import numpy as np
from math import sin, cos, pi

def cal_turn_left():
    
    stride_L = 10
    stride_R = 40

    raise_feet = 25
    stand = 85

    # Middle vriable setting
    x1_s=0;x2_s=0;x3_s=0;x4_s=0;y1_s=0;y2_s=0;y3_s=0;y4_s=0
    faai=0.24
    Ts=0.96
    step_t = 0.02

    fl_center = -15
    hl_center = -10
    fr_center = -15
    hr_center = 5

    xl_dn_inc = step_t*2*stride_L/(Ts-Ts*faai)
    xr_dn_inc = step_t*2*stride_R/(Ts-Ts*faai)

    x1_st = fl_center + 1/3*stride_L
    x2_st = fr_center - stride_R
    x3_st = hl_center + stride_L  
    x4_st = hr_center - 1/3*stride_R

    # 1, 4-2-3-1
    def cal_w(t):   

        nonlocal x1_s,x2_s,x3_s,x4_s,y1_s,y2_s,y3_s,y4_s
        nonlocal x1_st,x2_st,x3_st,x4_st
        # Start Action calculation

        if t == 0: # Step foot 1

            # Output y
            y1_s = stand
            y2_s = stand
            y3_s = stand
            y4_s = stand

            # Output x
            x1_s = fl_center + 1/3*stride_L
            x2_s = fr_center - stride_R
            x3_s = hl_center + stride_L  
            x4_s = hr_center - 1/3*stride_R

        elif t>0 and t<faai:    # Step foot 3
            sigma=2*pi*t/(faai)
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x3_st = x3_s
            if t< 0.25/2:
                xep=2*stride_L*((2*sigma-sin(2*sigma))/(2*pi))
                x3_s = x3_st-xep

            # Output y
            y1_s = stand +2
            y2_s = stand -2
            y3_s = stand - zep
            y4_s = stand -2
            # Output x
            x1_s += xl_dn_inc
            x2_s += xr_dn_inc
            x4_s += xr_dn_inc
        
        elif t>=faai and t<2*faai:    # Step foot 1
            t=t-faai
            sigma=2*pi*t/(faai)
            xep=2*stride_L*((sigma-sin(sigma))/(2*pi))
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x1_st = x1_s

            # Output y
            y1_s = stand - zep
            y2_s = stand +2
            y3_s = stand +2
            y4_s = stand -3
            # Output x
            x1_s = x1_st-xep
            x2_s += xr_dn_inc 
            x3_s += xl_dn_inc 
            x4_s += xr_dn_inc 

        elif t>=2*faai and t<3*faai:    # Step foot 4
            t=t-faai*2
            sigma=2*pi*t/(faai)
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x4_st = x4_s
            if t< 0.25/2:
                xep=2*stride_R*((2*sigma-sin(2*sigma))/(2*pi))
                x4_s = x4_st-xep

            # Output y
            y1_s = stand -3
            y2_s = stand +2
            y3_s = stand +2
            y4_s = stand - zep
            # Output x
            x1_s += xl_dn_inc
            x2_s += xr_dn_inc 
            x3_s += xl_dn_inc 

        elif t>=3*faai and t<4*faai:    # Step foot 2
            t=t-faai*3
            sigma=2*pi*t/(faai)
            xep=2*stride_R*((sigma-sin(sigma))/(2*pi))
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x2_st = x2_s

            # Output y
            y1_s = stand + 2
            y2_s = stand - zep
            y3_s = stand - 3
            y4_s = stand + 2
            # Output x
            x1_s += xl_dn_inc
            x2_s = x2_st-xep
            x3_s += xl_dn_inc 
            x4_s += xr_dn_inc

        else:
            return [[x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s]]

        return [[x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s]]

    data =[]
    for t in np.arange(0.0,Ts+0.001,step_t):
        t = round(t,2)
        result = cal_w(t)
        data.append(result)
    return data
