#!/usr/bin/env python3
import os
from time import sleep,time
from multiprocessing import Process, Manager, Value, Lock
import threading
from turtle import delay
import numpy as np
from math import pi, sin, cos, sqrt, acos, atan2, atan
from robot_hat import Robot, Pin, Ultrasonic, utils, Music
from .sh3001 import Sh3001
from .rgb_strip import RGB_Strip
from .sound_direction import Sound_direction
from .touch_sw import TouchSW

''' servos order
                     9,
                   0, '-'
                     |
              2,1 --[ ] -- 3,4
                    [ ]
              6,5 --[ ]-- 7,8
                     |
                    '='
                    / 
    thighs and calf crus shank

    feet order: 1~8
        left front leg, left front foot, 
        right front leg, right front foot,
        left hind leg, left hind foot, 
        right hind leg, right hind foot,

    head order: 9~11
        yaw,roll,pitch
    
    tail order: 12

'''

# user and User home directory
User = os.popen('echo ${SUDO_USER:-$LOGNAME}').readline().strip()
UserHome = os.popen('getent passwd %s | cut -d: -f 6'%User).readline().strip()
# print(User)  # pi
# print(UserHome) # /home/pi
config_file = '%s/.config/pidog/pidog.conf'%UserHome


class Pidog():

# structure constants
    leg = 43
    foot = 70
    b = 105
    width = 105
    length = 95

# init
    def __init__(self, feet_pins, head_pins, tail_pin,
            feet_init_angles=None, head_init_angles=None, tail_init_angle=None):


        from .actions_dictionary import ActionDict
        self.actions_dict = ActionDict()
        
        self.pos = np.mat([0.0,  0.0,  85]).T  # 目标位置向量
        self.rpy = np.array([0.0,  0.0,  0.0]) * pi / 180 # 欧拉角，化为弧度值
        self.pitch = 0
        self.roll = 0
    

        if feet_init_angles == None:
            feet_init_angles = self.actions_dict['lie'][0][0]
        if head_init_angles == None:
            # head_init_angles = [0,0,-20]
            head_init_angles =  [0]*3        
        if tail_init_angle == None:
            tail_init_angle = [0]

        self.feet = Robot(pin_list=feet_pins,name='feet', init_angles=feet_init_angles, db=config_file)
        self.head = Robot(pin_list=head_pins,name='head', init_angles=head_init_angles, db=config_file)
        self.tail = Robot(pin_list=tail_pin,name='tail', init_angles=tail_init_angle, db=config_file)

        self.feet_actions_buffer = []
        self.head_actions_buffer = []
        self.tail_actions_buffer = []

        self.feet_actions_coords_buffer = []

        self.feet_current_angle = feet_init_angles
        self.head_current_angle = head_init_angles
        self.tail_current_angle = tail_init_angle

        self.feet_speed = 90
        self.head_speed = 90
        self.tail_speed = 90
        
        self.feet_done_flag  = False
        self.head_done_flag  = False
        self.tail_done_flag  = False

        self.imu = Sh3001(db=config_file)
        self.imu_acc_offset = [0, 0, 0]
        self.imu_gyro_offset = [0, 0, 0]
        self.accData = [] # ax,ay,az
        self.gyroData = [] # gx,gy,gz

        self.rgb_strip = RGB_Strip(0X74) 
        self.rgb_strip.set_mode('breath', 'black')
        self.sensory_processes = None
        self.distance = Value('f',-1.0)
        # self.sound_direction = Value('f',-1.0)
        # from ctypes import c_char_p
        # self.touch = Manager().Value(c_char_p,'N') 
        self.sensory_lock = Lock()

        self.touch_sw = TouchSW('D2','D3')
        self.touch = 'N'

        self.ears = Sound_direction()
        self.sound_direction = -1

        # self.action_threads_start()
        # self.sensory_processes_start()
        self.exit_flag = False
        self.sensory_processes = None
        self.threads_manage_t =  threading.Thread(target=self.threads_manage)
        self.threads_manage_t.setDaemon(False)
        self.threads_manage_t.start()

        
# action related: feet,head,tail,imu,rgb_strip

    def close_all_thread(self):
        self.exit_flag = True

    def close(self):
        import signal
        import sys

        def handler(signal,frame):
            print(' please wait')
        signal.signal(signal.SIGINT, handler)
        print('\rstopping and returning to the initial position ... ')

        try:
            self.stop_and_lie()
            self.close_all_thread()
            print(' quit')
        except Exception as e:
            print('close error:',e)

        def handler(signal,frame):
            print(' quit done')
            sys.exit(0)
        signal.signal(signal.SIGINT, handler)

        sys.exit(0)  


    def threads_manage(self):
        self.action_threads_start()  # setDaemon = True
        # self.sensory_processes_start()

        while True:
            try:
                if self.exit_flag ==  True:
                    if self.sensory_processes != None:
                        self.sensory_processes.terminate()
                    break
            except Exception as e:
                print('threads_manage Exception：%s'%e)
            sleep(0.02)


    def feet_simple_move(self,angles_list, speed=90):

        tt = time()

        max_delay = 0.05
        min_delay = 0.005

        if speed > 100:
            speed = 100
        elif speed < 0:
            speed = 0
        
        delay = (100 - speed) / 100*(max_delay - min_delay) + min_delay

        rel_angles_list = []
        for i in range(len(angles_list)):
            rel_angles_list.append(angles_list[i] + self.feet.offset[i])
        self.feet.angle_list(rel_angles_list) 

        tt2 = time() - tt
        delay2 = 0.001*len(angles_list) - tt2

        if delay2 < -delay:
            delay2 = -delay
        sleep(delay + delay2)


    def feet_switch(self, flag=False):
        self.feet_sw_flag = flag

    def action_threads_start(self):
        #Immutable objects int, float, string, tuple, etc., need to be declared with global
        #Variable object lists, dicts, instances of custom classes, etc., do not need to be declared with global
        self.feet_thread = threading.Thread(name='feet_thread',target=self._feet_action_thread)
        self.head_thread = threading.Thread(name='head_thread',target=self._head_action_thread)
        self.tail_thread = threading.Thread(name='tail_thread',target=self._tail_action_thread)
        self.feet_thread.setDaemon(True)
        self.head_thread.setDaemon(True)
        self.tail_thread.setDaemon(True)  
        self.feet_thread.start()
        self.head_thread.start()
        self.tail_thread.start()    
        self.rgb_strip_thread = threading.Thread(name='rgb_strip_thread',target=self._rgb_strip_thread)
        self.imu_thread = threading.Thread(name='imu_thread',target=self._imu_thread)   
        self.rgb_strip_thread.setDaemon(True)
        self.imu_thread.setDaemon(True) 
        self.rgb_strip_thread.start()
        self.imu_thread.start() 

    # feet
    def _feet_action_thread(self):
        # print('_feet_action_thread start')
        while True:            
            try:
                if self.exit_flag == True:
                    break
                self.feet.servo_move2(self.feet_actions_buffer[0],self.feet_speed)
                self.feet_current_angle = list.copy(self.feet_actions_buffer[0])
                self.feet_actions_buffer.pop(0)

            except IndexError:
                sleep(0.1)
                pass
            except Exception as e:
                print('_feet_action_thread Exception:%s'%e)
                self.exit_flag = True
                break

    # def _feet_action_thread(self):
    #     # print('_feet_action_thread start')
    #     while True:            
    #         try:
    #             if self.exit_flag == True:
    #                 break
    #             print('_feet_action_thread:[0]',self.feet_actions_coords_buffer[0])
    #             _steps = self.feet_actions_coords_buffer[0]
    #             print('_feet_action_thread:',_steps)
    #             for i, step in enumerate(_steps) :
    #                 self.pos = np.mat([step[0], 0.0,  step[1]]).T  # 目标位置向量
    #                 coord = self.pose2coords(self.roll, self.pitch)
    #                 # print(i, coord)


    #             # self.feet.servo_move(self.feet_actions_buffer[0],self.feet_speed)
    #             # self.feet_current_angle = list.copy(self.feet_actions_buffer[0])
    #             self.feet_actions_coords_buffer.pop(0)

    #         except IndexError:
    #             sleep(0.1)
    #             pass
    #         except Exception as e:
    #             print('_feet_action_thread Exception：%s'%e)
    #             self.exit_flag = True
    #             break


    # head
    def _head_action_thread(self):
        # print('_head_action_thread start')
        while True:
            try:
                if self.exit_flag == True:
                    break
                self.head.servo_move(self.head_actions_buffer[0],self.head_speed)
                self.head_current_angle = list.copy(self.head_actions_buffer[0])
                self.head_actions_buffer.pop(0)

            except IndexError:
                sleep(0.1)
                pass
            except Exception as e:
                print('_head_action_thread Exception：%s'%e)
                self.exit_flag = True
                break
                
    # tail
    def _tail_action_thread(self):
        # print('_tail_action_thread start')
        while True:        
            try:
                if self.exit_flag == True:
                    break
                self.tail.servo_move(self.tail_actions_buffer[0],self.tail_speed)
                self.tail_current_angle = list.copy(self.tail_actions_buffer[0])
                self.tail_actions_buffer.pop(0)
            except IndexError:
                sleep(0.1)
                pass
            except Exception as e:
                print('_tail_action_thread Exception：%s'%e)
                self.exit_flag = True   
                break

    # rgb strip
    def _rgb_strip_thread(self):
        # print('_rgb_strip_thread start')
        while True:
            try:
                if self.exit_flag == True:
                    break
                self.rgb_strip.show()
            except Exception as e:
                print('_rgb_strip_thread Exception：%s'%e)
                self.exit_flag = True
                break
                

    # IMU
    def _imu_thread(self):
        # print('_imu_thread start')
        # x_last = time()

        # imu calibrate
        _ax = 0; _ay = 0; _az = 0
        _gx = 0; _gy = 0; _gz = 0
        time = 10
        for _ in range(time):
            data = self.imu._sh3001_getimudata()
            if data == False:
                print('_imu_thread imu data error')
                self.exit_flag = True
                break
            
            self.accData, self.gyroData = data
            _ax += self.accData[0]
            _ay += self.accData[1]
            _az += self.accData[2]
            _gx += self.gyroData[0]
            _gy += self.gyroData[1]
            _gz += self.gyroData[2]
            sleep(0.1)

        self.imu_acc_offset[0] = round(-16384 - _ax/time, 0)
        self.imu_acc_offset[1] = round(0 - _ay/time, 0)
        self.imu_acc_offset[2] = round(0 - _az/time, 0)
        self.imu_gyro_offset[0] = round(0 - _gx/time, 0)
        self.imu_gyro_offset[1] = round(0 - _gy/time, 0)
        self.imu_gyro_offset[2] = round(0 - _gz/time, 0)


        while not self.exit_flag:
            try:
                
                # print(time() - x_last)
                # x_last = time()
                data = self.imu._sh3001_getimudata()
                if data == False:
                    print('_imu_thread imu data error')
                    self.exit_flag = True
                    break
                self.accData, self.gyroData = data
                self.accData[0] += self.imu_acc_offset[0]
                self.accData[1] += self.imu_acc_offset[1]
                self.accData[2] += self.imu_acc_offset[2]
                self.gyroData[0] += self.imu_gyro_offset[0]
                self.gyroData[1] += self.imu_gyro_offset[1]
                self.gyroData[2] += self.imu_gyro_offset[2]
                ax = self.accData[0]
                ay = self.accData[1]
                az = self.accData[2]
    
                self.pitch = atan(ay/sqrt(ax*ax+az*az))*57.2957795
                self.roll = atan(az/sqrt(ax*ax+ay*ay))*57.2957795

                sleep(0.05)
            except Exception as e:
                print(data)
                print('_imu_thread Exception：%s'%e)
                self.exit_flag = True
                break

    # clear actions buff
    def feet_stop(self):
        self.feet_actions_buffer.clear()
        while len(self.feet_actions_buffer) > 0:
            sleep(0.001)

    def head_stop(self):
        self.head_actions_buffer.clear()
        while len(self.head_actions_buffer) > 0:
            sleep(0.001)

    def tail_stop(self):
        self.tail_actions_buffer.clear()
        while len(self.tail_actions_buffer) > 0:
            sleep(0.001)

    def body_stop(self):
        self.feet_stop()
        self.head_stop()
        self.tail_stop()
        sleep(0.5)

    # move  
    def feet_move(self,target_angles,immediately=True,speed=50):
        if immediately == True:
            self.feet_stop() 
        self.feet_speed = speed   
        self.feet_actions_buffer += target_angles

    def head_move_adjust(self,target_yrp, roll_init=0, pitch_init=0, immediately=True,speed=50): 
        if immediately == True:
            self.head_stop() 
        self.head_speed = speed
        yaw, roll, pitch = target_yrp
        signed = -1 if yaw < 0 else 1
        ratio = abs(yaw) / 90
        pitch_servo = roll * ratio  + pitch * (1-ratio) + pitch_init
        roll_servo = -(signed * (roll * (1-ratio)  + pitch * ratio) + roll_init)
        yaw_servo = yaw
        print(target_yrp, '|',  yaw_servo, roll_servo, pitch_servo )
        self.head_actions_buffer += [[yaw_servo, roll_servo, pitch_servo]]

    def head_move(self,target_angles,immediately=True,speed=50): 
        if immediately == True:
            self.head_stop() 
        self.head_speed = speed
        self.head_actions_buffer += target_angles

    def tail_move(self,target_angles,immediately=True,speed=50):
        if immediately == True:
            self.tail_stop() 
        self.tail_speed = speed   
        self.tail_actions_buffer += target_angles

# sensory_processes : ultrasonic,sound_direction
    def sensory_processes_work(self,distance_addr,sound_direction_addr,touch_addr,lock):
        ultrasonic_thread = threading.Thread(name='ultrasonic_thread',
                                    target=self._ultrasonic_thread,
                                    args=(distance_addr,lock,))
        ear_thread = threading.Thread(name='ear_thread',
                                    target=self._ear_thread,
                                    args=(sound_direction_addr,)) 
        # touch_thread = threading.Thread(name='touch_thread',
        #                             target=self._touch_thread,
        #                             args=(touch_addr,))
        ultrasonic_thread.start() 
        # ear_thread.start() 
        # touch_thread.start()

    def sensory_processes_start(self):
        if self.sensory_processes != None:
            self.sensory_processes.terminate()
        self.sensory_processes = Process(name='sensory_processes',
                                        target=self.sensory_processes_work,
                                        args=(self.distance,self.sound_direction,self.touch,self.sensory_lock))
        self.sensory_processes.start()
        # print('[process]sensory_processes start : [%s]'%self.sensory_processes.pid)

    # ultrasonic
    def _ultrasonic_thread(self,distance_addr,lock):
        # print("_ultrasonic_thread strat")    
        echo = Pin('D0')
        trig = Pin('D1')
        ultrasonic = Ultrasonic(trig,echo)
        while True: 
            try:
                with lock:
                    val = round(float(ultrasonic.read()),2)
                    # print('val',val)
                    distance_addr.value = val 
                sleep(1)
            except:
                sleep(0.1)
                print('ultrasonic_thread  except')
                break
    # ear (sound direction )
    def _ear_thread(self,sound_direction_addr):
        print('_ear_thread start')
        ears = Sound_direction()
        while True:
            try:
                if ears.isdetected():
                    sound_direction_addr.value = ears.read()
            except Exception as e:
                print("sound_direction error:%s"%e)  
                sleep(0.2)

    # touch 
    def _touch_thread(self,touch_addr):
        print("_touch_thread start")
        touch_sw = TouchSW()
        while True:
            touch_addr.value = touch_sw.is_slide()
            sleep(0.02)

# reset: stop, stop_and_lie 
    def stop_and_lie(self, speed=85):
        try:
            self.body_stop()
            self.feet_move(self.actions_dict['lie'][0],speed)
            self.head_move([[0,0,0]],speed)
            self.tail_move([[0,0,0]],speed)
            while len(self.feet_actions_buffer) > 0 or len(self.head_actions_buffer) > 0:
                sleep(0.01)
                if self.exit_flag == True:
                    break
        except Exception as e:
            print('stop_and_lie error:%s'%e)
            
            


# speak
    def speak(self, style, format='mp3'): 
        
        # _ = os.popen('pulseaudio --kill')
        # utils.run_command('pulseaudio --kill')
        status, result = utils.run_command('sudo killall pulseaudio')
        if status == 0:
            print('kill pulseaudio')

        # Music().sound_effect_play('/home/pi/pidog/sounds/'+str(style)+'.'+format)
        Music().sound_effect_threading('/home/pi/pidog/sounds/'+str(style)+'.'+format)
        

# calibration
    def feet_offset(self, cali_list):
        self.feet.set_offset(cali_list)
        self.feet.reset()
        self.feet_current_angle = [0]*8

    def head_offset(self, cali_list):
        self.head.set_offset(cali_list)
        self.head.reset()
        self.head_current_angle = [0]*3

    def tail_offset(self, cali_list):
        self.tail.set_offset(cali_list)
        self.tail.reset()
        self.tail_current_angle = [0]

# calculate angles and coords

    # pose and Euler Angle algorithm
    def pose2coords(self,roll,pitch):

        self.rpy = np.array([float(roll),  float(pitch),  0.0]) * pi / 180
        self.R = self.rpy[0]
        self.P = self.rpy[1]
        self.Y = self.rpy[2]

        # self.R = roll
        # self.P = pitch
        self.rotx = np.mat([[ 1,       0,            0          ],
                 [ 0,       cos(self.R), -sin(self.R)],
                 [ 0,       sin(self.R),  cos(self.R)]])
        self.roty = np.mat([[ cos(self.P),  0,      -sin(self.P)],
                 [ 0,            1,       0          ],
                 [ sin(self.P),  0,       cos(self.P)]])
        self.rotz = np.mat([[ cos(self.Y), -sin(self.Y),  0     ],
                 [ sin(self.Y),  cos(self.Y),  0     ],
                 [ 0,            0,            1     ]])
        self.rot_mat = self.rotx * self.roty * self.rotz
        self.body_struc = np.mat([[ self.length / 2,  self.b / 2,  0],
                       [ self.length / 2, -self.b / 2,  0],
                       [-self.length / 2,  self.b / 2,  0],
                       [-self.length / 2, -self.b / 2,  0]]).T
        self.footpoint_struc = np.mat([[ self.length / 2,  self.width / 2,  0],
                            [ self.length / 2, -self.width / 2,  0],
                            [-self.length / 2,  self.width / 2,  0],
                            [-self.length / 2, -self.width / 2,  0]]).T
        self.AB = np.mat(np.zeros((3, 4)))
        for i in range(4):
            self.AB[:, i] = - self.pos - self.rot_mat * self.body_struc[:, i] + self.footpoint_struc[:, i]
        
        # print((self.footpoint_struc - self.AB).T)

        self.body_coor_list = []
        for i in range(4):
            self.body_coor_list.append([(self.footpoint_struc - self.AB).T[i,0],(self.footpoint_struc - self.AB).T[i,1],(self.footpoint_struc - self.AB).T[i,2]])

        self.foot_coor_list = []
        for i in range(4):
            self.foot_coor_list.append([self.footpoint_struc.T[i,0],self.footpoint_struc.T[i,1],self.footpoint_struc.T[i,2]])
        
        print("body_coor_list:",self.body_coor_list)
        print("foot_coor_list:",self.foot_coor_list)
        return self.foot_coor_list

    
    def coord2polar(self, coord):
        x, z = coord
        # print('x,z:',x,z)
        u = sqrt(pow(x,2) + pow(z,2))
        # print('u: %s' % u)
        cos_angle1 = (self.foot**2 + self.leg**2 - u**2) / (2 * self.foot * self.leg)
        beta = acos(cos_angle1)
        # print('beta: %s' % beta)

        angle1 = atan2(x, z)
        # print("angle1:",angle1)
        angle2 = acos((self.leg**2 + u**2 - self.foot**2)/(2*self.leg*u))
        alpha = angle2 + angle1

        alpha = alpha / pi * 180 
        beta = beta / pi * 180 

        return alpha, beta

    def polar2coord(self, angles):
        alpha, beta, gamma = angles

        L1 = sqrt(self.A**2+self.B**2-2*self.A*self.B*cos((90+alpha)/180*pi))
        angle = acos((self.A**2+L1**2-self.B**2)/(2*self.A*L1))*180/pi
        angle = 90 - beta - angle
        L = L1*cos(angle*pi/180) + self.C

        x = L*sin((45+gamma)*pi/180)
        y = L*cos((45+gamma)*pi/180)
        z = L1*sin(angle*pi/180)
    
        return [round(x,4),round(y,4),round(z,4)]

    @classmethod 
    def feet_angle_calculation(cls,coords):  # 注意这里使用了 @classmethod 
        translate_list = []
        # print(coords)
        for i,coord in enumerate(coords): # each servo motion
            # coord2polar   
            leg_angle, foot_angle= Pidog.coord2polar(cls,coord) 
            # The left and right sides are opposite
            leg_angle = leg_angle
            foot_angle = foot_angle-90
            if i % 2 != 0:
                leg_angle = -leg_angle
                foot_angle = -foot_angle
            translate_list += [leg_angle, foot_angle]

        return translate_list        


    def pose2feet_angle(self):
        coords = []
        angles = []

        for i in range(4):
            coords.append([self.foot_coor_list[i][0]-self.body_coor_list[i][0], self.body_coor_list[i][2] - self.foot_coor_list[i][2]])

        angles = self.feet_angle_calculation(coords)

        return angles

# limit
    def limit(self,min,max,x):
        if x > max:
            return max
        elif x < min:
            return min
        else:
            return x

    # def limit_angle(self,angles):
    #     alpha, beta, gamma = angles
    #     # limit 
    #     limit_flag = False
    #     ## alpha
    #     temp = self.limit(-90,90,alpha)
    #     if temp != alpha:
    #         alpha = temp
    #         limit_flag = True
    #     ## beta
    #     temp = self.limit(-10,90,beta)
    #     if temp != beta:
    #         beta = temp
    #         limit_flag = True
    #     ## gamma
    #     temp = self.limit(-52,60,gamma)
    #     if temp != gamma:
    #         gamma = temp
    #         limit_flag = True
    #     # return
    #     return limit_flag,[alpha,beta,gamma]

# set angle
    def set_angle(self, angles_list,speed=50,israise=False):
        translate_list = []
        results = []
        for angles in angles_list:
            result, angles = self.limit_angle(angles)
            translate_list += angles
            results.append(result)
        if True in results:
            if israise == True:
                raise ValueError('\033[1;35mCoordinates out of controllable range.\033[0m')
            else:
                print('\033[1;35mCoordinates out of controllable range.\033[0m')
                coords = []
                # Calculate coordinates 
                for i in range(4):
                    coords.append(self.polar2coord([translate_list[i*3],translate_list[i*3+1],translate_list[i*3+2]]))
                self.current_coord = coords
        else:
            self.current_coord = self.coord_temp

        self.servo_move(translate_list,speed)

# do action
    def do_action(self, motion_name, step_count=1,wait=False,speed=50):

        try:
            actions,part = self.actions_dict[motion_name]
            if part == 'feet':
                if wait == True:
                    while len(self.feet_actions_buffer) > 0:
                        sleep(0.1)
                for _ in range(step_count): 
                    self.feet_move(actions,immediately=False,speed=speed)
            elif part == 'head':
                if wait == True:
                    while len(self.head_actions_buffer) > 0:
                        sleep(0.1)              
                for _ in range(step_count): 
                    self.head_move(actions,immediately=False,speed=speed)
            elif part == 'tail':
                if wait == True:
                    while len(self.tail_actions_buffer) > 0:
                        sleep(0.1)
                for _ in range(step_count): 
                    self.tail_move(actions,immediately=False,speed=speed)
        except KeyError:
            print("No such action")
        except Exception as e:
            print(e)       

    def wait_all_done(self):
        self.wait_feet_done()
        self.wait_head_done()
        self.wait_tail_done()

    def wait_feet_done(self):
        while len(self.feet_actions_buffer) > 0:
            sleep(0.01)

    def wait_head_done(self):
        while len(self.head_actions_buffer) > 0:
            sleep(0.01)

    def wait_tail_done(self):
        while len(self.tail_actions_buffer) > 0:
            sleep(0.01)




