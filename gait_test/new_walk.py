#!/usr/bin/env python3
from pidog import Pidog
from time import time, sleep
import readchar
import numpy as np
from math import pi, sin, cos

dog = Pidog(feet_pins=[1, 2, 3, 4, 5, 6, 7, 8],
    head_pins=[9, 10, 11], tail_pin=[12],
    )

def cal_walk():
    
    stride = 40
    raise_feet = 30
    stand = 70
    pitch_angle = 0
    roll_angle = 0
    y_offset = -5

    #中间变量设定
    x1_s=0;x2_s=0;x3_s=0;x4_s=0;y1_s=0;y2_s=0;y3_s=0;y4_s=0
    faai=0.24
    Ts=0.96
    step_t = 0.02

    f_center = -35
    h_center = 5
    f_stand = stand 
    h_stand = stand 
    x_dn_inc = step_t*2*stride/(Ts-faai)

    x1_st = f_center - stride
    x2_st = f_center + 1/3*stride
    x3_st = h_center - 1/3*stride
    x4_st = h_center + stride  

    # 1, 4-2-3-1
    def cal_w(t):   

        pose = {"y": 0, "z": stand}
        rpy = {"pitch": 0, "roll": 0,}

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
            x3_s = h_center - 1/3*stride
            x4_s = h_center + stride 

            print('start, ', end='')

        elif t>0 and t<faai:    #迈出腿4
            sigma=2*pi*t/(faai)
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x4_st = x4_s
                print('x4_st',x4_st)
            if t< 0.25/2:
                xep=2*stride*((2*sigma-sin(2*sigma))/(2*pi))
                x4_s = x4_st-xep

            #输出y
            y1_s = f_stand# -1
            y2_s = f_stand# +1
            y3_s = h_stand# -1
            y4_s = h_stand - zep
            #输出x

            x1_s += x_dn_inc
            x2_s += x_dn_inc 
            x3_s += x_dn_inc 

            print('leg 4, ', end='')
            pose["y"] = y_offset
            rpy["pitch"] = -pitch_angle
            rpy["roll"] = roll_angle

        
        elif t>=faai and t<2*faai:    #迈出腿2

            t=t-faai
            sigma=2*pi*t/(faai)
            xep=2*stride*((sigma-sin(sigma))/(2*pi))
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x2_st = x2_s
                print('x2_st',x2_st)

            #输出y
            y1_s = f_stand# + 3
            y2_s = f_stand - zep
            y3_s = h_stand# - 5*t/0.24
            y4_s = h_stand# + 2
            #输出x
            x1_s += x_dn_inc
            x2_s = x2_st-xep
            x3_s += x_dn_inc 
            x4_s += x_dn_inc

            print('leg 2, ', end='')
            pose["y"] = -y_offset
            rpy["pitch"] = pitch_angle
            rpy["roll"] = roll_angle


        elif t>=2*faai and t<3*faai:    #迈出腿3
            t=t-faai*2
            sigma=2*pi*t/(faai)
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x3_st = x3_s
                print('x3_st',x3_st)
            if t< 0.25/2:
                xep=2*stride*((2*sigma-sin(2*sigma))/(2*pi))
                x3_s = x3_st-xep


            #输出y
            y1_s = f_stand# +1
            y2_s = f_stand# -1
            y3_s = h_stand - zep
            y4_s = h_stand# -1
            #输出x
            x1_s += x_dn_inc
            x2_s += x_dn_inc
            x4_s += x_dn_inc

            print('leg 3, ', end='')
            pose["y"] = y_offset
            rpy["pitch"] = -pitch_angle
            rpy["roll"] = -roll_angle

        elif t>=3*faai and t<4*faai:    #迈出腿1
            t=t-faai*3
            sigma=2*pi*t/(faai)
            xep=2*stride*((sigma-sin(sigma))/(2*pi))
            zep=raise_feet*(1-cos(sigma))/2

            if t== 0:
                x1_st = x1_s
                print('x1_st',x1_st)

            #输出y
            y1_s = f_stand - zep
            y2_s = f_stand# +3
            y3_s = h_stand# +2
            y4_s = h_stand# -5*t/0.24
            #输出x
            x1_s = x1_st-xep
            x2_s += x_dn_inc 
            x3_s += x_dn_inc 
            x4_s += x_dn_inc 

            print('leg 1, ', end='')
            pose["y"] = -y_offset
            rpy["pitch"] = pitch_angle
            rpy["roll"] = -roll_angle

        print([x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s])
        return [[x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s]], pose, rpy

    data =[]
    for t in np.arange(0.0,0.961,step_t):
        t = round(t,2)
        print('t',t)
        data.append(cal_w(t))
    return data


def feet_simple_move(angles, delay=0.001):
    tt = time()

    rel_angles = []
    for i in range(len(angles)):
        rel_angles.append(angles[i] + dog.feet.offset[i])
    dog.feet.angle_list(rel_angles) 

    tt2 = time() - tt
    delay2 = 0.001*len(angles) - tt2
    # print('\r time: %s    '%delay2,end='')

    if delay2 < -delay:
        delay2 = -delay
    sleep(delay + delay2)

def main():

    forward_datas = cal_walk()
    datas_len = len(forward_datas)
    # print('forward_datas:',forward_datas)
    # print('datas_len:',datas_len)
    # print(forward_datas)

    while True:
        for data in forward_datas:
            foot_coords, pose, rpy = data
            dog.set_feet(foot_coords)
            dog.set_pose(**pose)
            dog.set_rpy(**rpy)
            # dog.set_feet([[0, 80], [0, 80], [0, 80], [0, 80]])
            angle_list = dog.pose2feet_angle()
            key = readchar.readkey()
            # print(foot_coords)
            if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
                import sys
                print('')
                sys.exit(0)
            # tt = time()
            
            feet_simple_move(angle_list, delay=0.01)  # 0.005 ~ 0.05
            # feet.servo_move2(angles,100 )
            # print('\r time: %s    '%(time()-tt),end='')
            # sleep(0.001)
        # sleep(0.5)

if __name__ == '__main__':
    main()