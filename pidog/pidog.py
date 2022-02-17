#!/usr/bin/env python3
import os
from time import sleep
from multiprocessing import Process, Manager, Value, Lock
import threading
import numpy as np
from math import pi, sin, cos, sqrt, acos, atan2
from robot_hat import Robot, Pin, Ultrasonic, utils, Music
from .sh3001 import Sh3001
from .rgb_strip import RGB_Strip
from .sound_direction import Sound_direction
from .touch_sw import TouchSW

''' servos order
                    head
                  9,10,11
                     +
              2,1 -- | -- 3,4
                    | |
                    | |
              6,5 -- | -- 7,8
                     12
                     |
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
    def __init__(self,feet_pins,head_pins,tail_pin,feet_init_angles=None,head_init_angles=None,tail_init_angle=None):

        utils.reset_mcu()
        sleep(0.5)

        self.pos = np.mat([0.0,  0.0,  85]).T  # 目标位置向量
        self.rpy = np.array([0.0,  0.0,  0.0]) * pi / 180 # 欧拉角，化为弧度值
 
        self.actions_dict = self.ActionDict()
        # t = time.time()
        if feet_init_angles == None:
            # feet_init_angles = self.actions_dict['sit'][0][0]
            feet_init_angles = self.actions_dict['lie'][0][0]
        if head_init_angles == None:
            # head_init_angles = [0,0,-20]
            head_init_angles =  [0]*3        
        if tail_init_angle == None:
            tail_init_angle = [0]
        self.feet = Robot(pin_list=feet_pins,name='feet', init_angles=feet_init_angles, db=config_file)
        self.head = Robot(pin_list=head_pins,name='head', init_angles=head_init_angles, db=config_file)
        self.tail = Robot(pin_list=tail_pin,name='tail', init_angles=tail_init_angle, db=config_file)
        # print('servo init:',time.time()-t)
        self.feet_actions_buffer = []
        self.head_actions_buffer = []
        self.tail_actions_buffer = []

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
        self.imu_offset_x = 0
        self.imu_offset_y = 0 
        self.imu_offset_z = 0
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

        self.stop_and_lie()
        self.close_all_thread()
        print(' quit')

        def handler(signal,frame):
            print(' quit done')
            sys.exit(0)
        signal.signal(signal.SIGINT, handler)

        sys.exit(0)  


    def threads_manage(self):
        self.action_threads_start()
        self.sensory_processes_start()

        while True:
            try:
                if self.exit_flag ==  True:
                    if self.sensory_processes != None:
                        self.sensory_processes.terminate()
                    break
            except Exception as e:
                print('threads_manage Exception：%s'%e)
            sleep(0.02)

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
                self.feet.servo_move(self.feet_actions_buffer[0],self.feet_speed)
                self.feet_current_angle = list.copy(self.feet_actions_buffer[0])
                self.feet_actions_buffer.pop(0)
            except IndexError:
                sleep(0.1)
                pass
            except Exception as e:
                print('feet_action_thread  except: %s'%e)
                break

    # head
    def _head_action_thread(self):
        # print('_head_action_thread start')
        while True:
            try:
                self.head.servo_move(self.head_actions_buffer[0],self.head_speed)
                self.head_current_angle = list.copy(self.head_actions_buffer[0])
                self.head_actions_buffer.pop(0)
            except IndexError:
                sleep(0.1)
                pass
            except Exception as e:
                print('head_action_thread  except: %s'%e)
                break
                
    # tail
    def _tail_action_thread(self):
        # print('_tail_action_thread start')
        while True:        
            try:
                self.tail.servo_move(self.tail_actions_buffer[0],self.tail_speed)
                self.tail_current_angle = list.copy(self.tail_actions_buffer[0])
                self.tail_actions_buffer.pop(0)
            except IndexError:
                sleep(0.1)
                pass
            except Exception as e:
                print('tail_action_thread  except: %s'%e)
                break
    # rgb strip
    def _rgb_strip_thread(self):
        # print('_rgb_strip_thread start')
        while True:
            try:
                self.rgb_strip.show()
            except :
                sleep(0.1)
                print('rgb_strip_thread  except')
                pass

    # IMU
    def _imu_thread(self):
        # print('_imu_thread start')
        while True:
            try:
                self.accData, self.gyroData = self.imu._sh3001_getimudata()
                self.accData[0] += self.imu_offset_x
                self.accData[1] += self.imu_offset_y
                self.accData[2] += self.imu_offset_z
                sleep(0.05)
            except :
                sleep(0.1)
                print('imu_thread  except')
                pass

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
        self.body_stop()
        self.feet_move(self.actions_dict['lie'][0],speed)
        self.head_move([[0,0,0]],speed)
        self.tail_move([[0,0,0]],speed)
        while len(self.feet_actions_buffer) > 0 or len(self.head_actions_buffer) > 0:
            sleep(0.01)


# speak
    def speak(self, style, format='mp3'):     
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
        
        # print("body_coor_list:",self.body_coor_list)
        # print("foot_coor_list:",self.foot_coor_list)
        # return self.body_coor_list

    
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
    def feet_angle_calculation(cls,coords):
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

# custom action

# do step
    # def do_step(self,step_list,speed=50):
       
    #     translate_list = []
    #     for i,coord in enumerate(step_list): # each servo motion
    #         # coord2polar
    #         leg_angle, foot_angle= self.coord2polar(coord)
    #         # The left and right sides are opposite
    #         leg_angle = leg_angle
    #         foot_angle = foot_angle-90
    #         if i % 2 != 0:
    #             leg_angle = -leg_angle
    #             foot_angle = -foot_angle
    #         translate_list += [leg_angle, foot_angle]

    #     # print('translate_list :',translate_list)
    #     # foot_move
    #     self.foot_move(translate_list,speed)

    #     return list(translate_list)

# ActionDict:
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
    # 侧对步 pack
    # 漫步 walk
        @property
        def walk(self):

            center = -20
            stride = -20 
            stride_q1 = stride/4
            stride_q2 = stride_q1*2
            stride_q3 = stride_q1*3

            outter_x1 = stride_q1 + center
            outter_x2 = stride_q2 + center
            outter_x3 = stride_q3 + center  
            outter_x4 = stride + center

            inner_x1 = center 
            inner_x2 = -stride*0.5 + center
            inner_x3 = -stride*1 + center
            inner_x4 = -stride*1.5 + center

            raise_feet = 15
            step_dn_y = self.height - 5
            step_dn_y2 = self.height 
            step_dn_y3 = self.height -10
            step_up_y = step_dn_y - raise_feet

          # 三角支撑
            return[

                # 右后 3/4 up，其它后2/4 
                Pidog.feet_angle_calculation([[outter_x3, step_dn_y], [inner_x3, step_dn_y], [inner_x1, step_dn_y], [outter_x1, step_up_y]]),  
                # Pidog.feet_angle_calculation([[outter_x4, step_dn_y], [inner_x3, step_dn_y], [inner_x2, step_dn_y], [outter_x3, step_up_y]]),  
                # 右后 4/4 up，其它后4/4 
                Pidog.feet_angle_calculation([[outter_x2, step_dn_y], [inner_x4, step_dn_y], [inner_x2, step_dn_y], [outter_x4, step_dn_y]]), 

                # 右前 3/4 up，其它后2/4 
                Pidog.feet_angle_calculation([[outter_x1, step_dn_y], [outter_x3, step_up_y], [inner_x4, step_dn_y], [outter_x3, step_dn_y]]),  
                # 右前 4/4 up，其它后4/4 
                Pidog.feet_angle_calculation([[inner_x1, step_dn_y], [outter_x4, step_dn_y], [inner_x4, step_dn_y], [inner_x3, step_dn_y]]), 

                # # 左后 3/4 up，其它后2/4 
                Pidog.feet_angle_calculation([[inner_x2, step_dn_y], [outter_x3, step_dn_y], [inner_x1, step_up_y], [inner_x2, step_dn_y]]),  
                # # 左后 4/4 up，其它后4/4 
                Pidog.feet_angle_calculation([[inner_x3, step_dn_y], [outter_x2, step_dn_y], [outter_x4, step_dn_y], [inner_x3, step_dn_y]]), 

                # # 左前 3/4 up，其它后2/4 
                Pidog.feet_angle_calculation([[inner_x4, step_up_y], [inner_x1, step_dn_y], [outter_x3, step_dn_y], [inner_x4, step_dn_y]]),  
                # # 左前 4/4 up，其它后4/4 
                Pidog.feet_angle_calculation([[outter_x4, step_dn_y], [inner_x3, step_dn_y], [outter_x1, step_dn_y], [inner_x3, step_dn_y]]),  


            ],'feet'
    # 漫步 walk2
        @property
        def walk2(self):
            from math import pi,cos,sin
            center = -20
            stride = 30
            raise_feet = 15
            stand = 95
            #中间变量设定
            x1_s=0;x2_s=0;x3_s=0;x4_s=0;y1_s=0;y2_s=0;y3_s=0;y4_s=0
            xs=0
            faai=0.5
            Ts=1
            t=0
            walk_speed=0.015
            
            def cal_w(t,xf,h):   #WALK步态主计算函数，相序 1-2-3-4
                nonlocal x1_s,x2_s,x3_s,x4_s,y1_s,y2_s,y3_s,y4_s
                
                #开始步态计算
                if t<Ts*faai:    #迈出腿1
                    #print("腿1")
                    t=t+walk_speed
                    sigma=2*pi*t/(faai*Ts)
                    zep=h*(1-cos(sigma))/2
                    xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
                    #输出y
                    y1=-zep+stand
                    y2=stand
                    y3=stand
                    y4=stand
                    #输出x
                    x1=-xep_b + center
                    x2=center
                    x3=center
                    x4=center
                    x1_s=x1;x2_s=x2;x3_s=x3;x4_s=x4;y1_s=y1;y2_s=y2;y3_s=y3;y4_s=y4
                    return [[x1_s,y1_s],[x2_s,y2_s],[x4_s,y4_s],[x3_s,y3_s]]

                if t>=Ts*faai and t<2*Ts*faai:    #迈出腿2
                    #print("腿2")
                    t=t+walk_speed
                    t=t-faai*Ts
                    sigma=2*pi*t/(faai*Ts)
                    zep=h*(1-cos(sigma))/2
                    xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
                    #输出y
                    y1=stand
                    y2=-zep+stand
                    y3=stand
                    y4=stand
                    #输出x
                    x1=-xf+center
                    x2=-xep_b+center
                    x3=center
                    x4=center
                    x1_s=x1;x2_s=x2;x3_s=x3;x4_s=x4;y1_s=y1;y2_s=y2;y3_s=y3;y4_s=y4
                    return [[x1_s,y1_s],[x2_s,y2_s],[x4_s,y4_s],[x3_s,y3_s]]
                if t>=2*Ts*faai and t<3*Ts*faai:    #迈出腿3
                    #print("腿3")
                    t=t+walk_speed
                    t=t-faai*Ts*2
                    sigma=2*pi*t/(faai*Ts)
                    zep=h*(1-cos(sigma))/2
                    xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
                    #输出y
                    y1=stand
                    y2=stand
                    y3=-zep+stand
                    y4=stand
                    #输出x
                    x1=-xf+center
                    x2=-xf+center
                    x3=-xep_b+center
                    x4=center
                    x1_s=x1;x2_s=x2;x3_s=x3;x4_s=x4;y1_s=y1;y2_s=y2;y3_s=y3;y4_s=y4
                    return [[x1_s,y1_s],[x2_s,y2_s],[x4_s,y4_s],[x3_s,y3_s]]

                if t>=3*Ts*faai and t<4*Ts*faai:    #迈出腿4
                    #print("腿4")
                    t=t+walk_speed
                    t=t-faai*Ts*3
                    sigma=2*pi*t/(faai*Ts)
                    zep=h*(1-cos(sigma))/2
                    xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
                    #输出y
                    y1=stand
                    y2=stand
                    y3=stand
                    y4=-zep+stand
                    #输出x
                    x1=-xf+center
                    x2=-xf+center
                    x3=-xf+center
                    x4=-xep_b+center
                    x1_s=x1;x2_s=x2;x3_s=x3;x4_s=x4;y1_s=y1;y2_s=y2;y3_s=y3;y4_s=y4
                    return [[x1_s,y1_s],[x2_s,y2_s],[x4_s,y4_s],[x3_s,y3_s]]

                if t>=4*Ts*faai:    #足端坐标归零
                    if x1_s>0:
                        x1_s=x1_s-x1_s*0.1
                    elif x1_s<0:
                        x1_s=x1_s+x1_s*0.1
                    x2_s=x1_s;x3_s=x1_s;x4_s=x1_s
                    return [[x1_s,y1_s],[x2_s,y2_s],[x4_s,y4_s],[x3_s,y3_s]]

            date =[]
            # for _ in raise
            for t in np.arange(0.1,2.1,0.05):
                t = round(t,2)
                result = cal_w(t,xf=stride,h=raise_feet)
                # date.append(result)
                date.append(Pidog.feet_angle_calculation(result))  
            # print(date)
            return date,'feet'
    # 漫步 walk3
        @property
        def walk3(self):

            center = -58
            step = 3
            stride = 80
            stride_q1 = stride/(step*4-3)

            raise_feet = 20
            default_y = self.height - 10

            result = []
            legs = [9, 3, 0, 6]
            for i in range(step*4):
                temp = []
                for j, leg in enumerate(legs):
                    legs[j] += 1
                    if legs[j] > step*4-1:
                        legs[j] = 0
                    if leg == step*4-2:
                        y = raise_feet
                        x = 6 * stride_q1 + center
                    elif leg == step*4-1:
                        y = raise_feet
                        x = 0 * stride_q1 + center 
                    else:
                        y = 0
                        x = leg * stride_q1 + center 
                    y = default_y - y
                    temp.append([x, y])
                # print(temp)
                result.append(Pidog.feet_angle_calculation(temp))
            # result = [[coord[0] * stride_q1 + center, y] for coord in result]
            # print(result)
            return result, 'feet'
    # 小跑 trot
        @property
        def trot(self):
            from math import pi,cos,sin
            faai=0.5
            Ts=1
            center = -36
            stride = 40
            raise_feet = 12
            stand = self.height

            #  t: time
            # xs: x_start
            # xf: x_final
            #  h: raise_height
            def cal_t(t,xs,xf,h):   
                if t<=Ts*faai:
                    sigma=2*pi*t/(faai*Ts)
                    zep=h*(1-cos(sigma))/2
                    xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
                    xep_z=(xs-xf)*((sigma-sin(sigma))/(2*pi))+xf
                    #输出y
                    y1=-zep + stand
                    y2=stand 
                    y3=-zep + stand 
                    y4=stand
                    #输出x
                    x1=xep_z + center #-10
                    x2=xep_b + center ##-10
                    x3=xep_z + center
                    x4=xep_b + center
                    return [[x1,y1],[x2,y2],[x4,y4],[x3,y3]]

                elif t>Ts*faai and t<=Ts:
                    sigma=2*pi*(t-Ts*faai)/(faai*Ts)
                    zep=h*(1-cos(sigma))/2
                    xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
                    xep_z=(xs-xf)*((sigma-sin(sigma))/(2*pi))+xf
                    #输出y
                    y1=stand 
                    y2=-zep + stand 
                    y3=stand 
                    y4=-zep + stand
                    #输出x
                    x1=xep_b + center #-6
                    x2=xep_z + center #-6
                    x3=xep_b + center
                    x4=xep_z + center
                    return [[x1,y1],[x2,y2],[x4,y4],[x3,y3]]

            date =[]
            for t in np.arange(0.1,1.01,0.05):
                t = round(t,3)
                result = cal_t(t,xs=0,xf=stride,h=raise_feet)
                date.append(Pidog.feet_angle_calculation(result))  
            return date,'feet'   
    # 后退 backward
        @property
        def move_back(self):
            # Center of gravity Offset
            outter_x = -20 + self.barycenter
            middle_x = -0 + self.barycenter
            # inner_x = 40 + self.barycenter

            step_dn_y = self.height
            raise_feet = 0
            step_up_y = self.height - raise_feet

            # 对角同步 ，重心前移（腿部后移）
            return[
                Pidog.feet_angle_calculation([[middle_x, step_up_y], [middle_x, step_dn_y], [middle_x, step_dn_y], [middle_x, step_up_y]]),                
                Pidog.feet_angle_calculation([[outter_x, step_dn_y], [middle_x, step_dn_y], [middle_x, step_dn_y], [outter_x, step_dn_y]]),            
                Pidog.feet_angle_calculation([[middle_x, step_dn_y], [middle_x, step_up_y], [middle_x, step_up_y], [middle_x, step_dn_y]]),
                Pidog.feet_angle_calculation([[middle_x, step_dn_y], [outter_x, step_dn_y], [outter_x, step_dn_y], [middle_x, step_dn_y]]),
            ],'feet'
    # 后退 backward2
        @property
        def backward(self):
            from math import pi,cos,sin
            faai=0.5
            Ts=1
            center = -20
            raise_feet = 10
            stand = 95
            def cal_t(t,xs,xf,h):    #小跑步态执行函数
                if t<=Ts*faai:
                    sigma=2*pi*t/(faai*Ts)
                    zep=h*(1-cos(sigma))/2
                    xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
                    xep_z=(xs-xf)*((sigma-sin(sigma))/(2*pi))+xf
                    #输出y
                    y1=-zep + stand
                    y2=stand + 1
                    y3=-zep + stand 
                    y4=stand
                    #输出x
                    x1=xep_z + center 
                    x2=xep_b + center 
                    x3=xep_z + center + 10
                    x4=xep_b + center + 10
                    return [[x1,y1],[x2,y2],[x4,y4],[x3,y3]]

                elif t>Ts*faai and t<=Ts:
                    sigma=2*pi*(t-Ts*faai)/(faai*Ts)
                    zep=h*(1-cos(sigma))/2
                    xep_b=(xf-xs)*((sigma-sin(sigma))/(2*pi))+xs
                    xep_z=(xs-xf)*((sigma-sin(sigma))/(2*pi))+xf
                    #输出y
                    y1=stand 
                    y2=-zep + stand 
                    y3=stand + 1
                    y4=-zep + stand
                    #输出x
                    x1=xep_b + center 
                    x2=xep_z + center 
                    x3=xep_b + center + 10
                    x4=xep_z + center + 10
                    return [[x1,y1],[x2,y2],[x4,y4],[x3,y3]]

            date =[]
            for t in np.arange(0.1,1.01,0.05):
                t = round(t,2)
                result = cal_t(t,xs=0,xf=-20,h=raise_feet)
                date.append(Pidog.feet_angle_calculation(result))  
            return date,'feet'
     # 握手

    # 后退 backward3
        @property
        def backward3(self):

            center = 0
            step = 3
            stride = 40
            stride_q1 = -stride/(step*4-3)

            raise_feet = 15
            default_y = self.height

            result = []
            legs = [9, 3, 0, 6]
            for i in range(step*4):
                temp = []
                for j, leg in enumerate(legs):
                    legs[j] += 1
                    if legs[j] > step*4-1:
                        legs[j] = 0
                    if leg == step*4-2:
                        y = raise_feet
                        x = 6 * stride_q1 + center
                    elif leg == step*4-1:
                        y = raise_feet
                        x = 0 * stride_q1 + center 
                    else:
                        y = 0
                        x = leg * stride_q1 + center 
                    y = default_y - y
                    temp.append([x, y])
                # print(temp)
                result.append(Pidog.feet_angle_calculation(temp))
            # result = [[coord[0] * stride_q1 + center, y] for coord in result]
            # print(result)
            return result, 'feet'

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
        def doze_off2(self):
            start = -30
            am = 20
            angs = []         
            for i in range(0,am+1,1):
                anl = start + i
                angs.append([45, anl, -45, -anl, 45, -45, -45, 45])  
            for _ in range(1):
                anl = start + am
                angs.append([45, anl, -45, -anl, 45, -45, -45, 45])    
            for i in range(am,-1,-1):
                anl = start + i
                angs.append([45, anl, -45, -anl, 45, -45, -45, 45]) 
            for _ in range(1):
                anl = start 
                angs.append([45, anl, -45, -anl, 45, -45, -45, 45]) 
            
            return angs,'feet'

        @property 
        def doze_off(self):
            start = -30
            am = 20
            angs = []   
            t = 4     
            for i in range(0,am+1,1):
                anl = start + i
                angs += [[45, anl, -45, -anl, 45, -45, -45, 45]]*t 
            for _ in range(4):
                anl = start + am
                angs += [[45, anl, -45, -anl, 45, -45, -45, 45]]*t   
            for i in range(am,-1,-1):
                anl = start + i
                angs += [[45, anl, -45, -anl, 45, -45, -45, 45]]*t
            for _ in range(4):
                anl = start 
                angs += [[45, anl, -45, -anl, 45, -45, -45, 45]]*t
            
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


def test():
    my_pidog = Pidog(feet_pins=[1,2,3,4,5,6,7,8],
            head_pins=[9,10,11],tail_pin=[12],
            # feet_init_angles=[45,0,-45,0,45,0,-45,0],
            # head_init_angles=[0,0,0],
            tail_init_angle=[0])
    sleep(0.5)  
 
    # def offset(cali_list):
    #     my_pidog.feet.set_offset(cali_list)
    #     my_pidog.feet.reset()

    # offset([-5, 4, -10, 0, 0,0, 0, 0])

    
    while True:
        # print(round(my_pidog.distance.value,2),my_pidog.sound_direction.value,my_pidog.touch.value)
        # print(my_pidog.accData,my_pidog.gyroData)
       
        # my_pidog.do_action('doze_off',step_count=150,wait=False,speed=50)
        #
        my_pidog.do_action('trot',step_count=150,wait=False,speed=90)
        # 
        # my_pidog.head_move([[0,0,30]],speed=80) 
        # my_pidog.do_action('pushup',step_count=150,wait=False,speed=60)
        # sleep(8)
        # my_pidog.do_action('head_up_down',step_count=150,wait=False,speed=60)
        # 
        # my_pidog.do_action('stretch',step_count=150,wait=False,speed=90)
        # my_pidog.head_move([[0,0,30]],speed=50)
        # #

        sleep(20)

if __name__ == "__main__":
    test()

