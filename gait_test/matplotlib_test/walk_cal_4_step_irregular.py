#!/usr/bin/env python3
from math import pi, sin, cos, sqrt, acos, atan2, atan
import numpy as np

def cal_walk_coords():

    # 设：
    faai = 0.24 # 单腿抬腿时间
    Ts = 5*faai # 步态时间
    step_t = 0.02 # 计时间隔

    Beta = 4/5 # 负载因子 = （Ts-faai）/Ts

    stride = 80 # 步距
    S = 3 # 稳定裕度
    Ls = stride # 机器人单腿从抬起到落地过程中，单腿相对地面的位移。通常情况下 L = A+E = stride

    # stride = Ls = 4*As + 4*S
    # Es = 3*As + 4*S <= stride
    # Beta = (3*Es + 4*S)/Ls = (3Es + 4*S)/(4Es + 4*S) >= 3/4

    As = (Ls - 4*S)/4  # 单腿步距，单腿从抬起到落地的过程中，机器人躯体相对地面的位移
    Es = 3*As + 4*S  # 单腿抬起后，机器人躯体相对地面的位移

    print('As:%s, Es:%s'%(As,Es))

    # As = (stride - 4*S)/4


    raise_feet = 30
    stand = 85

    f_center = -35
    h_center = 0


    #中间变量设定
    x1_s=0;x2_s=0;x3_s=0;x4_s=0;y1_s=0;y2_s=0;y3_s=0;y4_s=0

    f_stand = stand
    h_stand = stand 
    x_up_inc = Es*step_t/faai
    x_dn_inc = As*step_t/faai
    x_4S_inc = (4*S+20)*step_t/Ts

    x1_st = f_center - Es+2*As
    x2_st = f_center + As
    x3_st = h_center - As
    x4_st = h_center + Es-2*As

    # 1, 4-2-3-1
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
            x1_s = f_center - Es+2*As 
            x2_s = f_center + As 
            x3_s = h_center - As 
            x4_s = h_center + Es-2*As 

            print('start, ', end='')

        elif t>0 and t<faai:    #迈出腿4
            sigma=2*pi*t/(faai)
            zep=raise_feet*(1-cos(sigma))/2
            # xep=2*stride*((sigma-sin(sigma))/(2*pi))

            if t== 0:
                x4_st = x4_s
                print('x4_st',x4_st)
            if t< faai/2:
                xep=Es*((2*sigma-sin(2*sigma))/(2*pi))
                x4_s = x4_st-xep

            #输出y
            y1_s = f_stand 
            y2_s = f_stand 
            y3_s = h_stand 
            y4_s = h_stand - zep
            #输出x

            x1_s += x_dn_inc
            x2_s += x_dn_inc 
            x3_s += x_dn_inc 
            # x4_s += -x_up_inc
            # x4_s = x4_st-xep

            print('leg 4, ', end='')

        
        elif t>=faai and t<2*faai:    #迈出腿2

            t=t-faai
            sigma=2*pi*t/(faai)
            # zep=h*((sigma-sin(sigma))/(2*pi))
            xep=Es*((sigma-sin(sigma))/(2*pi))
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x2_st = x2_s
                print('x2_st',x2_st)
            # if t< faai/2:
            #     xep=2*stride*((2*sigma-sin(2*sigma))/(2*pi))
            #     x2_s = x2_st-xep

            #输出y
            y1_s = f_stand 
            y2_s = f_stand - zep
            y3_s = h_stand 
            y4_s = h_stand 
            #输出x
            x1_s += x_dn_inc
            # x2_s += -x_up_inc
            x2_s = x2_st-xep
            x3_s += x_dn_inc 
            x4_s += x_dn_inc

            print('leg 2, ', end='')


        elif t>=2*faai and t<3*faai:    #四足调整
            #输出y
            y1_s = f_stand 
            y2_s = f_stand 
            y3_s = h_stand 
            y4_s = h_stand 
            #输出x
            x1_s += x_4S_inc  
            x2_s += x_4S_inc  
            x3_s += x_4S_inc 
            x4_s += x_4S_inc          

        elif t>=3*faai and t<4*faai:    #迈出腿3
            t=t-faai*3
            sigma=2*pi*t/(faai)
            # zep=h*((sigma-sin(sigma))/(2*pi))
            # xep=2*stride*((sigma-sin(sigma))/(2*pi))
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x3_st = x3_s
                print('x3_st',x3_st)
            if t< faai/2:
                xep=Es*((2*sigma-sin(2*sigma))/(2*pi))
                x3_s = x3_st-xep


            #输出y
            y1_s = f_stand 
            y2_s = f_stand 
            y3_s = h_stand - zep
            y4_s = h_stand 
            #输出x
            x1_s += x_dn_inc
            x2_s += x_dn_inc
            # x3_s += -x_up_inc
            # x3_s = x3_st-xep
            x4_s += x_dn_inc

            print('leg 3, ', end='')

        elif t>=4*faai and t<5*faai:    #迈出腿1
            t=t-faai*4
            sigma=2*pi*t/(faai)
            xep=Es*((sigma-sin(sigma))/(2*pi))
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x1_st = x1_s
                print('x1_st',x1_st)
            # if t< faai/2:
            #     xep=2*stride*((2*sigma-sin(2*sigma))/(2*pi))
            #     x1_s = x1_st-xep


            #输出y
            y1_s = f_stand - zep
            y2_s = f_stand 
            y3_s = h_stand 
            y4_s = h_stand 
            #输出x
            # x1_s += -x_up_inc
            x1_s = x1_st-xep
            x2_s += x_dn_inc 
            x3_s += x_dn_inc 
            x4_s += x_dn_inc 

            print('leg 1, ', end='')

        else:
            return [[x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s]]

        print([x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s])
        return [[x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s]]
        # return [[x2_s,y2_s],[x1_s,y1_s],[x4_s,y4_s],[x3_s,y3_s]]


    date =[]
    for t in np.arange(0.0,1.201,step_t):
        t = round(t,2)
        print('t',t)
        result = cal_w(t)
        date.append(result)
    return date

    # date =[]
    # for t in np.arange(0.0,0.961,step_t):
    #     t = round(t,2)
    #     print('t',t)
    #     result = cal_w(t)
    #     if mode == 'angle':
    #         date.append(angle_calculation(result))  
    #     else :
    #         date.append(result)
    # return date

if __name__ == '__main__':
    cal_walk_coords()
    # print(date)