#!/usr/bin/env python3
from public_functions import *


def cal_trot():
    
    stride = 40
    raise_feet = 15
    stand = 85

    x1_s=0;x2_s=0;x3_s=0;x4_s=0;y1_s=0;y2_s=0;y3_s=0;y4_s=0
    Tm=0.50
    Ts=1
    step_t = 0.05

    f_center =  -20 # -35
    h_center = 0  # 5
    f_stand = stand 
    h_stand = stand 

    stride_half = stride/2
    x1_st = f_center + stride_half
    x2_st = f_center + stride_half
    x3_st = h_center + stride_half
    x4_st = h_center + stride_half 


    def cal_t(t): 
        nonlocal x1_s,x2_s,x3_s,x4_s,y1_s,y2_s,y3_s,y4_s

        if t<=Tm:  # 迈出腿2,3
            sigma = 2*pi*t/Tm
            zep = raise_feet*(1-cos(sigma))/2
            xep_up = stride*((sigma-sin(sigma))/(2*pi))
            xep_down = stride - xep_up

            # xep_up = stride*(t/Tm - sin(sigma)/(2*pi)) 
            # xep_down = stride - xep_up
            # if t < Tm/2:
            #     zep = raise_feet*((2*( t/Tm - sin(4*pi*t/Tm)/(4*pi) ) -1) + 1)

            # else:
            #     zep = raise_feet*(-(2*( t/Tm - sin(2*sigma)/(4*pi) ) -1) + 1)

            print('%s '%zep, end='')

            #输出y
            y1_s = f_stand  
            y2_s = f_stand - zep
            y3_s = h_stand - zep 
            y4_s = h_stand +5
            #输出x
            x1_s = x1_st - xep_down
            x2_s = x2_st - xep_up
            x3_s = x3_st - xep_up
            x4_s = x4_st - xep_down 
            

        elif t>Tm and t<=1: # 迈出腿2,3
            t = t-Tm
            sigma = 2*pi*t/Tm
            zep=raise_feet*(1-cos(sigma))/2
            xep_up = stride*((sigma-sin(sigma))/(2*pi))
            xep_down = stride - xep_up

            # xep_up = stride*(t/Tm - sin(sigma)/(2*pi)) 
            # xep_down = stride - xep_up
            # if t < Tm/2:
            #     zep = raise_feet*((2*( t/Tm - sin(2*sigma)/(4*pi) ) -1) + 1)
            # else:
            #     zep = raise_feet*(-(2*( t/Tm - sin(2*sigma)/(4*pi) ) -1) + 1)

            print('%s '%zep, end='')
            #输出y
            y1_s = f_stand - zep
            y2_s = f_stand 
            y3_s = h_stand + 5
            y4_s = h_stand - zep 
            #输出x
            x1_s = x1_st - xep_up
            x2_s = x2_st - xep_down
            x3_s = x3_st - xep_down
            x4_s = x4_st - xep_up

        print([x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s])
        return [[x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s]]


    date =[]
    for t in np.arange(0.0,1.001,step_t):
        t = round(t,2)
        print('t',t)
        result = cal_t(t)
        date.append(angle_calculation(result))  

    return date


def pause():
    key = readchar.readkey()
    if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
        import sys
        print('')
        sys.exit(0)


def main():

    forward_datas = cal_trot()
    datas_len = len(forward_datas)
    # print('forward_datas:',forward_datas)
    print('datas_len:',datas_len)

    print('offset:',feet.offset)

    while True:

        for angles in forward_datas:
            pause()

            tt = time()
            feet_simple_move(angles, delay=0.005)  # 0.005 ~ 0.05
            print('\r time: %s    '%(time()-tt),end='')
            # sleep(0.005)
        # sleep(0.5)


if __name__ == '__main__':
    main()