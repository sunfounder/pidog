#!/usr/bin/env python3
import os
from time import sleep,time
from multiprocessing import Process, Value, Lock
import threading
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
              2,1 --[ ]-- 3,4
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
        yaw, roll, pitch
    
    tail order: 12

'''

# user and User home directory
User = os.popen('echo ${SUDO_USER:-$LOGNAME}').readline().strip()
UserHome = os.popen('getent passwd %s | cut -d: -f 6'%User).readline().strip()
config_file = '%s/.config/pidog/pidog.conf'%UserHome


class Pidog():

    # structure constants
    leg = 42
    foot = 76
    BODY_LENGTH = 117
    BODY_WIDTH = 98
    BODY_STRUCT = np.mat([
        [-BODY_WIDTH / 2, -BODY_LENGTH / 2,  0],
        [ BODY_WIDTH / 2, -BODY_LENGTH / 2,  0],
        [-BODY_WIDTH / 2,  BODY_LENGTH / 2,  0],
        [ BODY_WIDTH / 2,  BODY_LENGTH / 2,  0]]).T
    SOUND_DIR = "/home/pi/pidog/sounds/"
    # PID Constants
    KP = 0.033
    KI = 0.0
    KD = 0.0

    # init
    def __init__(self, feet_pins, head_pins, tail_pin,
            feet_init_angles=None, head_init_angles=None, tail_init_angle=None):


        from .actions_dictionary import ActionDict
        self.actions_dict = ActionDict()
        
        self.body_height = 80
        self.pose = np.mat([0.0,  0.0,  self.body_height]).T  # 目标位置向量
        self.rpy = np.array([0.0,  0.0,  0.0]) * pi / 180 # 欧拉角，化为弧度值
        self.footpoint_struc = np.mat([
            [-self.BODY_WIDTH / 2, -self.BODY_LENGTH / 2,  0],
            [ self.BODY_WIDTH / 2, -self.BODY_LENGTH / 2,  0],
            [-self.BODY_WIDTH / 2,  self.BODY_LENGTH / 2,  0],
            [ self.BODY_WIDTH / 2,  self.BODY_LENGTH / 2,  0]
        ]).T
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
        self.sensory_lock = Lock()

        self.touch_sw = TouchSW('D2','D3')
        self.touch = 'N'

        self.ears = Sound_direction()
        self.sound_direction = -1

        self.exit_flag = False
        self.sensory_processes = None
        self.action_threads_start()
        self.sensory_processes_start()
        
        self.roll_last_error = 0
        self.roll_error_integral = 0
        self.pitch_last_error = 0
        self.pitch_error_integral = 0

        self.target_rpy = [0, 0, 0]

        self.rgb_fail_count = 0
        self.imu_fail_count = 0
        self.music = Music()

    # action related: feet,head,tail,imu,rgb_strip

    def close_all_thread(self):
        self.exit_flag = True

    def close(self):
        import signal
        import sys

        def handler(signal,frame):
            print('Please wait')
        signal.signal(signal.SIGINT, handler)

        print('\rStopping and returning to the initial position ... ')

        try:
            self.stop_and_lie()
            self.close_all_thread()
            print('Quit')
        except Exception as e:
            print('Close error:',e)

        self.feet_thread.join()
        self.head_thread.join()
        self.tail_thread.join()
        self.rgb_strip_thread.join()
        self.imu_thread.join()
        if self.sensory_processes != None:
            self.sensory_processes.terminate()
        sys.exit(0)  

    def feet_simple_move(self, angles_list, speed=90):

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
        while True:            
            try:
                if self.exit_flag == True:
                    break
                self.feet.servo_move2(self.feet_actions_buffer[0], self.feet_speed)
                self.feet_current_angle = list.copy(self.feet_actions_buffer[0])
                self.feet_actions_buffer.pop(0)

            except IndexError:
                sleep(0.1)
                pass
            except Exception as e:
                print('_feet_action_thread Exception:%s'%e)
                self.exit_flag = True
                break

    # head
    def _head_action_thread(self):
        while True:
            try:
                if self.exit_flag == True:
                    break
                self.head.servo_move2(self.head_actions_buffer[0],self.head_speed)
                self.head_current_angle = list.copy(self.head_actions_buffer[0])
                self.head_actions_buffer.pop(0)

            except IndexError:
                sleep(0.1)
            except Exception as e:
                print('_head_action_thread Exception: %s'%e)
                self.exit_flag = True
                break
                
    # tail
    def _tail_action_thread(self):
        while not self.exit_flag:  
            try:
                self.tail.servo_move2(self.tail_actions_buffer[0],self.tail_speed)
                self.tail_current_angle = list.copy(self.tail_actions_buffer[0])
                self.tail_actions_buffer.pop(0)
            except IndexError:
                sleep(0.1)
                pass
            except Exception as e:
                print('_tail_action_thread Exception: %s'%e)
                self.exit_flag = True   
                break

    # rgb strip
    def _rgb_strip_thread(self):
        while not self.exit_flag:
            try:
                self.rgb_strip.show()
                self.rgb_fail_count = 0
            except Exception as e:
                print('_rgb_strip_thread Exception: %s'%e)
                self.rgb_fail_count += 1
                if self.rgb_fail_count > 10:
                    self.exit_flag = True
                    break
                

    # IMU
    def _imu_thread(self):
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
                data = self.imu._sh3001_getimudata()
                if data == False:
                    print('_imu_thread imu data error')
                    self.imu_fail_count += 1
                    if self.imu_fail_count > 10:
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

                self.imu_fail_count = 0
                sleep(0.05)
            except Exception as e:
                print(data)
                print('_imu_thread Exception: %s'%e)
                self.imu_fail_count += 1
                if self.imu_fail_count > 10:
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
    def feet_move(self, target_angles, immediately=True, speed=50):
        if immediately == True:
            self.feet_stop() 
        self.feet_speed = speed   
        self.feet_actions_buffer += target_angles

    def head_rpy_to_angle(self, target_yrp, roll_init=0, pitch_init=0):
        yaw, roll, pitch = target_yrp
        signed = -1 if yaw < 0 else 1
        ratio = abs(yaw) / 90
        pitch_servo = roll * ratio  + pitch * (1-ratio) + pitch_init
        roll_servo = -(signed * (roll * (1-ratio)  + pitch * ratio) + roll_init)
        yaw_servo = yaw
        return [yaw_servo, roll_servo, pitch_servo]

    def head_move(self, target_yrps, roll_init=0, pitch_init=0, immediately=True, speed=50): 
        if immediately == True:
            self.head_stop() 
        self.head_speed = speed
        angles = [self.head_rpy_to_angle(target_yrp, roll_init, pitch_init) for target_yrp in target_yrps]
        self.head_actions_buffer += angles

    def head_move_raw(self, target_angles, immediately=True, speed=50): 
        if immediately == True:
            self.head_stop() 
        self.head_speed = speed
        self.head_actions_buffer += target_angles

    def tail_move(self, target_angles, immediately=True, speed=50):
        if immediately == True:
            self.tail_stop() 
        self.tail_speed = speed   
        self.tail_actions_buffer += target_angles

    # sensory_processes : ultrasonic,sound_direction
    def sensory_processes_work(self,distance_addr,sound_direction_addr,touch_addr,lock):
        ultrasonic_thread = threading.Thread(name='ultrasonic_thread',
                                    target=self._ultrasonic_thread,
                                    args=(distance_addr,lock,))
        ultrasonic_thread.start() 

    def sensory_processes_start(self):
        if self.sensory_processes != None:
            self.sensory_processes.terminate()
        self.sensory_processes = Process(name='sensory_processes',
                                        target=self.sensory_processes_work,
                                        args=(self.distance,self.sound_direction,self.touch,self.sensory_lock))
        self.sensory_processes.start()

    # ultrasonic
    def _ultrasonic_thread(self,distance_addr,lock):
        echo = Pin('D0')
        trig = Pin('D1')
        ultrasonic = Ultrasonic(trig,echo)
        while True: 
            try:
                with lock:
                    val = round(float(ultrasonic.read()),2)
                    distance_addr.value = val 
                # sleep(1)
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
            self.head_move_raw([[0,0,0]],speed)
            self.tail_move([[0,0,0]],speed)
            while len(self.feet_actions_buffer) > 0 or len(self.head_actions_buffer) > 0:
                sleep(0.01)
                if self.exit_flag == True:
                    break
        except Exception as e:
            print('stop_and_lie error:%s'%e)

    # speak
    def speak(self, name): 
        status, _ = utils.run_command('sudo killall pulseaudio')
        if status == 0:
            print('kill pulseaudio')
        # Scan for all available audios, see if name matches
        for filename in os.listdir(self.SOUND_DIR):
            if filename.startswith(name):
                self.music.sound_effect_threading(self.SOUND_DIR+filename)
                break
        else:
            print('No sound found for %s'%name)
            return False

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

    def set_pose(self, x=None, y=None, z=None):
        if x != None:
            self.pose[0,0] = float(x)
        if y != None:
            self.pose[1,0] = float(y)
        if z != None:
            self.pose[2,0] = float(z)
            self.body_height = float(z)

    def set_rpy(self, roll=None, pitch=None, yaw=None, pid=False):
        if roll is None:
            roll = self.rpy[0]
        if pitch is None:
            pitch = self.rpy[1]
        if yaw is None:
            yaw = self.rpy[2]
        
        if pid:
            roll_error =  self.target_rpy[0] - self.roll
            pitch_error = self.target_rpy[1] - self.pitch

            roll_offset = self.KP * roll_error + self.KI * self.roll_error_integral + self.KD * (roll_error - self.roll_last_error)
            pitch_offset = self.KP * pitch_error + self.KI * self.pitch_error_integral + self.KD * (pitch_error - self.pitch_last_error)

            self.roll_error_integral += roll_error
            self.pitch_error_integral += pitch_error
            self.roll_last_error = roll_error
            self.pitch_last_error = pitch_error

            roll_offset = roll_offset / 180. * pi
            pitch_offset = pitch_offset / 180. * pi

            self.rpy[0] += roll_offset
            self.rpy[1] += pitch_offset
        else:
            self.rpy[0] = roll / 180. * pi
            self.rpy[1] = pitch / 180. * pi
            self.rpy[2] = yaw / 180. * pi

    def set_feet(self, feet_list):
        self.footpoint_struc = np.mat([
            [-self.BODY_WIDTH / 2, -self.BODY_LENGTH / 2 + feet_list[0][0], self.body_height - feet_list[0][1]],
            [ self.BODY_WIDTH / 2, -self.BODY_LENGTH / 2 + feet_list[1][0], self.body_height - feet_list[1][1]],
            [-self.BODY_WIDTH / 2,  self.BODY_LENGTH / 2 + feet_list[2][0], self.body_height - feet_list[2][1]],
            [ self.BODY_WIDTH / 2,  self.BODY_LENGTH / 2 + feet_list[3][0], self.body_height - feet_list[3][1]]
        ]).T

    # pose and Euler Angle algorithm
    def pose2coords(self):
        roll = self.rpy[0]
        pitch = self.rpy[1]
        yaw = self.rpy[2]

        rotx = np.mat([
            [cos(roll), 0, -sin(roll)],
            [         0, 1,           0],
            [sin(roll), 0,  cos(roll)]])
        roty = np.mat([
            [1,         0,          0],
            [0, cos(-pitch), -sin(-pitch)],
            [0, sin(-pitch),  cos(-pitch)]])
        rotz = np.mat([
            [ cos(yaw), -sin(yaw), 0],
            [ sin(yaw),  cos(yaw), 0],
            [        0,         0, 1]])
        rot_mat = rotx * roty * rotz
        AB = np.mat(np.zeros((3, 4)))
        for i in range(4):
            AB[:, i] = - self.pose - rot_mat * self.BODY_STRUCT[:, i] + self.footpoint_struc[:, i]
        
        body_coor_list = []
        for i in range(4):
            body_coor_list.append([(self.footpoint_struc - AB).T[i,0],(self.footpoint_struc - AB).T[i,1],(self.footpoint_struc - AB).T[i,2]])

        foot_coor_list = []
        for i in range(4):
            foot_coor_list.append([self.footpoint_struc.T[i,0],self.footpoint_struc.T[i,1],self.footpoint_struc.T[i,2]])
        
        return {"foot":foot_coor_list, "body":body_coor_list}

    def pose2feet_angle(self):
        data = self.pose2coords()
        foot_coor_list = data["foot"]
        body_coor_list = data["body"]
        coords = []
        angles = []

        for i in range(4):
            coords.append([foot_coor_list[i][1]-body_coor_list[i][1], body_coor_list[i][2] - foot_coor_list[i][2]])

        angles = []
        
        for i, coord in enumerate(coords):
            
            leg_angle, foot_angle= self.fieldcoord2polar(coord) 
            # The left and right sides are opposite
            leg_angle = leg_angle
            foot_angle = foot_angle-90
            if i % 2 != 0:
                leg_angle = -leg_angle
                foot_angle = -foot_angle
            angles += [leg_angle, foot_angle]

        return angles

    # Pose calculated coord is Field coord, acoord refer to field, not refer to robot
    def fieldcoord2polar(self, coord):
        y, z = coord
        u = sqrt(pow(y,2) + pow(z,2))
        cos_angle1 = (self.foot**2 + self.leg**2 - u**2) / (2 * self.foot * self.leg)
        cos_angle1 = min(max(cos_angle1, -1), 1)
        beta = acos(cos_angle1)

        angle1 = atan2(y, z)
        cos_angle2 = (self.leg**2 + u**2 - self.foot**2)/(2*self.leg*u)
        cos_angle2 = min(max(cos_angle2, -1), 1)
        angle2 = acos(cos_angle2)
        alpha = angle2 + angle1 + self.rpy[1]
  
        alpha = alpha / pi * 180 
        beta = beta / pi * 180 

        return alpha, beta
    
    def coord2polar(self, coord):
        y, z = coord
        u = sqrt(pow(y,2) + pow(z,2))
        cos_angle1 = (self.foot**2 + self.leg**2 - u**2) / (2 * self.foot * self.leg)
        cos_angle1 = min(max(cos_angle1, -1), 1)
        beta = acos(cos_angle1)

        angle1 = atan2(y, z)
        cos_angle2 = (self.leg**2 + u**2 - self.foot**2)/(2*self.leg*u)
        cos_angle2 = min(max(cos_angle2, -1), 1)
        angle2 = acos(cos_angle2)
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
    def do_action(self, motion_name, step_count=1, wait=False, speed=50):
        try:
            actions, part = self.actions_dict[motion_name]
            if part == 'feet':
                if wait == True:
                    while len(self.feet_actions_buffer) > 0:
                        sleep(0.1)
                for _ in range(step_count): 
                    self.feet_move(actions, immediately=False, speed=speed)
            elif part == 'head':
                if wait == True:
                    while len(self.head_actions_buffer) > 0:
                        sleep(0.1)              
                for _ in range(step_count): 
                    self.head_move(actions, immediately=False, speed=speed)
            elif part == 'tail':
                if wait == True:
                    while len(self.tail_actions_buffer) > 0:
                        sleep(0.1)
                for _ in range(step_count): 
                    self.tail_move(actions, immediately=False, speed=speed)
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




