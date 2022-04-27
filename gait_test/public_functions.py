#!/usr/bin/env python3
import os
from time import sleep,time
from robot_hat import Robot, utils
from math import pi, sin, cos, sqrt, acos, atan2, atan
import numpy as np
import readchar 

# user and User home directory
User = os.popen('echo ${SUDO_USER:-$LOGNAME}').readline().strip()
UserHome = os.popen('getent passwd %s | cut -d: -f 6'%User).readline().strip()
# print(User)  # pi
# print(UserHome) # /home/pi
config_file = '%s/.config/pidog/pidog.conf'%UserHome


utils.reset_mcu()
sleep(0.5)

feet = Robot(pin_list=[1, 2, 3, 4, 5, 6, 7, 8],
            name='feet',
            init_angles=[45, 0, -45, 0, 45, 0, -45, 0],
            db=config_file)

head = Robot(pin_list=[9, 10, 11], # yaw, roll, pitch
            name='head',
            init_angles=[-0, 0, 0], 
            db=config_file)

leg = 43
foot = 70
b = 105
width = 105
length = 95

def feet_simple_move(angles, delay=0.001):
    tt = time()

    rel_angles = []
    for i in range(len(angles)):
        rel_angles.append(angles[i] + feet.offset[i])
    feet.angle_list(rel_angles) 

    tt2 = time() - tt
    delay2 = 0.001*len(angles) - tt2
    # print('\r time: %s    '%delay2,end='')

    if delay2 < -delay:
        delay2 = -delay
    sleep(delay + delay2)


def coord2polar(coord):
    x, z = coord
    # print('x,z:%s,%s'%(x,z))
    u = sqrt(pow(x,2) + pow(z,2))
    # print('u: %s' % u)
    cos_angle1 = (foot**2 + leg**2 - u**2) / (2 * foot * leg)
    beta = acos(cos_angle1)
    # print('beta: %s' % beta)

    angle1 = atan2(x, z)
    # print("angle1:",angle1)
    angle2 = acos((leg**2 + u**2 - foot**2)/(2*leg*u))
    alpha = angle2 + angle1

    alpha = alpha / pi * 180 
    beta = beta / pi * 180 

    # alpha =  round(alpha, 2)
    # beta = round(beta, 2) 

    # print('alpha,beta :%s, %s'%(alpha, beta))
    return alpha, beta

    
def angle_calculation(coords):
    translate_list = []
    # print(coords)
    for i,coord in enumerate(coords): # each servo motion
        # coord2polar   
        leg_angle, foot_angle = coord2polar(coord) 

        # The left and right sides are opposite
        leg_angle = leg_angle
        foot_angle = foot_angle-90
        if i % 2 != 0:
            leg_angle = -leg_angle
            foot_angle = -foot_angle
            
            # leg_angle =  round(leg_angle, 2)
            # foot_angle = round(foot_angle, 2) 

            
        translate_list += [leg_angle, foot_angle]

    # print('translate_list:%s'%(translate_list))

    return translate_list   

