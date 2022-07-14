#!/usr/bin/env python3
from public_functions import *


def cal_turn_left(mode:'angle or coord'='angle'):
    
    stride = 40
    stride_L = 10
    stride_R = 40

    raise_feet = 25
    raise_right= 10
    stand = 85

    #中间变量设定
    x1_s=0;x2_s=0;x3_s=0;x4_s=0;y1_s=0;y2_s=0;y3_s=0;y4_s=0
    faai=0.24
    Ts=0.96
    step_t = 0.02

    f_center = -35
    h_center = 5

    fl_center = -15
    hl_center = -10
    fr_center = -15
    hr_center = 5

    xl_up_inc = step_t*2*stride_L/(Ts*faai)
    xl_dn_inc = step_t*2*stride_L/(Ts-Ts*faai)
    xr_up_inc = step_t*2*stride_R/(Ts*faai)
    xr_dn_inc = step_t*2*stride_R/(Ts-Ts*faai)

    x1_st = fl_center + 1/3*stride_L
    x2_st = fr_center - stride_R
    x3_st = hl_center + stride_L  
    x4_st = hr_center - 1/3*stride_R

    # 1, 4-2-3-1
    def cal_w(t):   

        nonlocal x1_s,x2_s,x3_s,x4_s,y1_s,y2_s,y3_s,y4_s
        nonlocal x1_st,x2_st,x3_st,x4_st
            #开始步态计算s

        if t == 0: #迈出腿1

            #输出y
            y1_s = stand
            y2_s = stand
            y3_s = stand
            y4_s = stand

            #输出x
            x1_s = fl_center + 1/3*stride_L
            x2_s = fr_center - stride_R
            x3_s = hl_center + stride_L  
            x4_s = hr_center - 1/3*stride_R

            print('start, ', end='')

        elif t>0 and t<faai:    #迈出腿3
            sigma=2*pi*t/(faai)
            # zep=h*((sigma-sin(sigma))/(2*pi))
            # xep=2*stride*((sigma-sin(sigma))/(2*pi))
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x3_st = x3_s
                print('x3_st',x3_st)
            if t< 0.25/2:
                xep=2*stride_L*((2*sigma-sin(2*sigma))/(2*pi))
                x3_s = x3_st-xep


            #输出y
            y1_s = stand +2
            y2_s = stand -2
            y3_s = stand - zep
            y4_s = stand -2
            #输出x
            x1_s += xl_dn_inc
            x2_s += xr_dn_inc
            # x3_s += -x_up_inc
            # x3_s = x3_st-xep
            x4_s += xr_dn_inc

            print('leg 3, ', end='')

        
        elif t>=faai and t<2*faai:    #迈出腿1
            t=t-faai
            sigma=2*pi*t/(faai)
            xep=2*stride_L*((sigma-sin(sigma))/(2*pi))
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x1_st = x1_s
                print('x1_st',x1_st)
            # if t< 0.25/2:
            #     xep=2*stride*((2*sigma-sin(2*sigma))/(2*pi))
            #     x1_s = x1_st-xep


            #输出y
            y1_s = stand - zep
            y2_s = stand +2
            y3_s = stand +2
            y4_s = stand -3
            #输出x
            # x1_s += -x_up_inc
            x1_s = x1_st-xep
            x2_s += xr_dn_inc 
            x3_s += xl_dn_inc 
            x4_s += xr_dn_inc 

            print('leg 1, ', end='')


        elif t>=2*faai and t<3*faai:    #迈出腿4
            t=t-faai*2
            sigma=2*pi*t/(faai)
            zep=raise_feet*(1-cos(sigma))/2
            # xep=2*stride*((sigma-sin(sigma))/(2*pi))

            if t== 0:
                x4_st = x4_s
                print('x4_st',x4_st)
            if t< 0.25/2:
                xep=2*stride_R*((2*sigma-sin(2*sigma))/(2*pi))
                x4_s = x4_st-xep

            #输出y
            y1_s = stand -3
            y2_s = stand +2
            y3_s = stand +2
            y4_s = stand - zep
            #输出x

            x1_s += xl_dn_inc
            x2_s += xr_dn_inc 
            x3_s += xl_dn_inc 
            # x4_s += -x_up_inc
            # x4_s = x4_st-xep

            print('leg 4, ', end='')

        elif t>=3*faai and t<4*faai:    #迈出腿2
            t=t-faai*3
            sigma=2*pi*t/(faai)
            # zep=h*((sigma-sin(sigma))/(2*pi))
            xep=2*stride_R*((sigma-sin(sigma))/(2*pi))
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x2_st = x2_s
                print('x2_st',x2_st)
            # if t< 0.25/2:
            #     xep=2*stride*((2*sigma-sin(2*sigma))/(2*pi))
            #     x2_s = x2_st-xep

            #输出y
            y1_s = stand + 2
            y2_s = stand - zep
            y3_s = stand - 3
            y4_s = stand + 2
            #输出x
            x1_s += xl_dn_inc
            # x2_s += -x_up_inc
            x2_s = x2_st-xep
            x3_s += xl_dn_inc 
            x4_s += xr_dn_inc

            print('leg 2, ', end='')

        else:
            return [[x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s]]

        print([x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s])
        return [[x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s]]
        # return [[x2_s,y2_s],[x1_s,y1_s],[x4_s,y4_s],[x3_s,y3_s]]


    data =[]
    for t in np.arange(0.0,Ts+0.001,step_t):
        t = round(t,2)
        print('t',t)
        result = cal_w(t)
        if mode == 'angle':
            data.append(angle_calculation(result))  
        else :
            data.append(result)
    return data

def pause():
    key = readchar.readkey()
    if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
        import sys
        print('')
        sys.exit(0)

def main():

    forward_datas = cal_turn_left()
    datas_len = len(forward_datas)
    # print('forward_datas:',forward_datas)
    print('datas_len:',datas_len)

    print('offset:',feet.offset)

    while True:
        # pause()
        for angles in forward_datas:
            # pause()
            tt = time()
            
            feet_simple_move(angles, delay=0.01)  # 0.005 ~ 0.05
            # feet.servo_move2(angles,100 )
            print('\r time: %s    '%(time()-tt),end='')
            # sleep(0.005)
        # sleep(0.5)

if __name__ == '__main__':
    main()