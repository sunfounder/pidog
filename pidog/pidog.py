#!/usr/bin/env python3
import os
import sys
from time import sleep, time
from multiprocessing import Process, Value, Lock
import threading
import numpy as np
from math import pi, sin, cos, sqrt, acos, atan2, atan
from robot_hat import Robot, Pin, Ultrasonic, utils, Music
from .sh3001 import Sh3001
from .rgb_strip import RGBStrip
from .sound_direction import SoundDirection
from .dual_touch import DualTouch
import warnings
warnings.filterwarnings("ignore") # ignore warnings for pygame

''' servos order
                     4,
                   5, '6'
                     |
              3,2 --[ ]-- 7,8
                    [ ]
              1,0 --[ ]-- 10,11
                     |
                    '9'
                    /

    legs pins: [2, 3, 7, 8, 0, 1, 10, 11]
        left front leg, left front leg
        right front leg, right front leg
        left hind leg, left hind leg,
        right hind leg, right hind leg,

    head pins: [4, 6, 5]
        yaw, roll, pitch

    tail pin: [9]

'''

# user and User home directory
User = os.popen('echo ${SUDO_USER:-$LOGNAME}').readline().strip()
UserHome = os.popen('getent passwd %s | cut -d: -f 6' %User).readline().strip()
config_file = '%s/.config/pidog/pidog.conf' % UserHome

# color:
# https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007
# 1;30:gray 31:red, 32:green, 33:yellow, 34:blue, 35:purple, 36:dark green, 37:white
GRAY = '1;30'
RED = '0;31'
GREEN = '0;32'
YELLOW = '0;33'
BLUE = '0;34'
PURPLE = '0;35'
DARK_GREEN = '0;36'
WHITE = '0;37'

def print_color(msg, end='\n', file=sys.stdout, flush=False, color=''):
    print('\033[%sm%s\033[0m'%(color, msg), end=end, file=file, flush=flush)

def info(msg, end='\n', file=sys.stdout, flush=False):
    print_color('\033[%sm%s\033[0m'%(WHITE, msg), end=end, file=file, flush=flush)

def debug(msg, end='\n', file=sys.stdout, flush=False):
    print_color('\033[%sm%s\033[0m'%(GRAY, msg), end=end, file=file, flush=flush)

def warn(msg, end='\n', file=sys.stdout, flush=False):
    print_color('\033[%sm%s\033[0m'%(YELLOW, msg), end=end, file=file, flush=flush)

def error(msg, end='\n', file=sys.stdout, flush=False):
    print_color('\033[%sm%s\033[0m'%(RED, msg), end=end, file=file, flush=flush)


class MyUltrasonic(Ultrasonic):
    def __init__(self, tring, echo):
        super().__init__(tring, echo)
        self.distance = Value('f', -1.0)

    def read_distance(self):
        return self.distance.value

class Pidog():

    # structure constants
    LEG = 42
    FOOT = 76
    BODY_LENGTH = 117
    BODY_WIDTH = 98
    BODY_STRUCT = np.mat([
        [-BODY_WIDTH / 2, -BODY_LENGTH / 2,  0],
        [BODY_WIDTH / 2, -BODY_LENGTH / 2,  0],
        [-BODY_WIDTH / 2,  BODY_LENGTH / 2,  0],
        [BODY_WIDTH / 2,  BODY_LENGTH / 2,  0]]).T
    SOUND_DIR = f"{UserHome}/pidog/sounds/"
    # Servo Speed
    HEAD_DPS = 300
    LEGS_DPS = 350
    TAIL_DPS = 500
    # PID Constants
    KP = 0.033
    KI = 0.0
    KD = 0.0
    # Left Front Leg, Left Front Leg, Right Front Leg, Right Front Leg, Left Hind Leg, Left Hind Leg, Right Hind Leg, Right Hind Leg
    DEFAULT_LEGS_PINS = [2, 3, 7, 8, 0, 1, 10, 11]
    # Head Yaw, Roll, Pitch
    DEFAULT_HEAD_PINS = [4, 6, 5]
    DEFAULT_TAIL_PIN = [9]

    HEAD_PITCH_OFFSET = 45

    HEAD_YAW_MIN = -90
    HEAD_YAW_MAX = 90
    HEAD_ROLL_MIN = -70
    HEAD_ROLL_MAX = 70
    HEAD_PITCH_MIN = -45
    HEAD_PITCH_MAX = 30

    # init
    def __init__(self, leg_pins=DEFAULT_LEGS_PINS, head_pins=DEFAULT_HEAD_PINS, tail_pin=DEFAULT_TAIL_PIN,
                 leg_init_angles=None, head_init_angles=None, tail_init_angle=None):

        from .actions_dictionary import ActionDict
        self.actions_dict = ActionDict()

        self.body_height = 80
        self.pose = np.mat([0.0,  0.0,  self.body_height]).T  # target position vector
        self.rpy = np.array([0.0,  0.0,  0.0]) * pi / 180  # Euler angle, converted to radian value
        self.leg_point_struc = np.mat([
            [-self.BODY_WIDTH / 2, -self.BODY_LENGTH / 2,  0],
            [self.BODY_WIDTH / 2, -self.BODY_LENGTH / 2,  0],
            [-self.BODY_WIDTH / 2,  self.BODY_LENGTH / 2,  0],
            [self.BODY_WIDTH / 2,  self.BODY_LENGTH / 2,  0]
        ]).T
        self.pitch = 0
        self.roll = 0

        self.roll_last_error = 0
        self.roll_error_integral = 0
        self.pitch_last_error = 0
        self.pitch_error_integral = 0
        self.target_rpy = [0, 0, 0]

        if leg_init_angles == None:
            leg_init_angles = self.actions_dict['lie'][0][0]
        if head_init_angles == None:
            head_init_angles = [0, 0, self.HEAD_PITCH_OFFSET]
        else:
            head_init_angles[2] += self.HEAD_PITCH_OFFSET
            # head_init_angles = [0]*3
        if tail_init_angle == None:
            tail_init_angle = [0]

        self.thread_list = []

        try:
            debug(f"config_file: {config_file}")
            debug("robot_hat init ... ", end='', flush=True)
            self.legs = Robot(pin_list=leg_pins, name='legs', init_angles=leg_init_angles, init_order=[
                            0, 2, 4, 6, 1, 3, 5, 7], db=config_file)
            self.head = Robot(pin_list=head_pins, name='head',
                            init_angles=head_init_angles, db=config_file)
            self.tail = Robot(pin_list=tail_pin, name='tail',
                            init_angles=tail_init_angle, db=config_file)
            # add thread
            self.thread_list.extend(["legs", "head", "tail"])
            # via
            self.legs.max_dps = self.LEGS_DPS
            self.head.max_dps = self.HEAD_DPS
            self.tail.max_dps = self.TAIL_DPS

            self.legs_action_buffer = []
            self.head_action_buffer = []
            self.tail_action_buffer = []

            self.legs_thread_lock = threading.Lock()
            self.head_thread_lock = threading.Lock()
            self.tail_thread_lock = threading.Lock()

            self.legs_actions_coords_buffer = []

            self.leg_current_angles = leg_init_angles
            self.head_current_angles = head_init_angles
            self.tail_current_angles = tail_init_angle

            self.legs_speed = 90
            self.head_speed = 90
            self.tail_speed = 90

            # done
            debug("done")
        except OSError:
            error("fail")
            raise OSError("rotbot_hat I2C init failed. Please try again.")

        try:
            debug("imu_sh3001 init ... ", end='', flush=True)
            self.imu = Sh3001(db=config_file)
            self.imu_acc_offset = [0, 0, 0]
            self.imu_gyro_offset = [0, 0, 0]
            self.accData = []  # ax,ay,az
            self.gyroData = []  # gx,gy,gz
            self.imu_fail_count = 0
            # add imu thread
            self.thread_list.append("imu")
            debug("done")
        except OSError:
            error("fail")

        try:
            debug("rgb_strip init ... ", end='', flush=True)
            self.rgb_strip = RGBStrip(0X74)
            self.rgb_strip.set_mode('breath', 'black')
            self.rgb_fail_count = 0
            # add rgb thread
            self.thread_list.append("rgb")
            debug("done")
        except OSError:
            error("fail")

        try:
            debug("ultrasonic init ... ", end='', flush=True)
            echo = Pin('D0')
            trig = Pin('D1')
            self.ultrasonic = MyUltrasonic(trig, echo)
            # add ultrasonic thread
            self.thread_list.append("ultrasonic")
            debug("done")
        except Exception as e:
            error("fail")
            raise ValueRrror(e)

        try:
            debug("dual_touch init ... ", end='', flush=True)
            self.dual_touch = DualTouch('D2', 'D3')
            self.touch = 'N'
            debug("done")
        except:
            error("fail")

        try:
            debug("sound_direction init ... ", end='', flush=True)
            self.ears = SoundDirection()
            # self.sound_direction = -1
            debug("done")
        except:
            error("fail")

        try:
            debug("sound_effect init ... ", end='', flush=True)
            self.music = Music()
            debug("done")
        except:
            error("fail")


        self.sensory_processes = None
        self.sensory_lock = Lock()

        self.exit_flag = False
        self.action_threads_start()
        self.sensory_processes_start()

    # class PidogUltrasonic(Ultrasonic):
    #     def __init__(self,

    # action related: legs,head,tail,imu,rgb_strip
    def close_all_thread(self):
        self.exit_flag = True

    def close(self):
        import signal
        import sys


        def handler(signal, frame):
            info('Please wait')
        signal.signal(signal.SIGINT, handler)

        def _handle_timeout(signum, frame):
            raise TimeoutError('function timeout')

        timeout_sec = 5
        signal.signal(signal.SIGALRM, _handle_timeout)
        signal.alarm(timeout_sec)

        info('\rStopping and returning to the initial position ... ')

        try:
            if self.exit_flag == True:
                self.exit_flag = False
                self.action_threads_start()
            self.stop_and_lie()
            self.close_all_thread()

            self.legs_thread.join()
            self.head_thread.join()
            self.tail_thread.join()

            if 'rgb' in self.thread_list:
                self.rgb_strip_thread.join()
            if 'imu' in self.thread_list:
                self.imu_thread.join()
            if self.sensory_processes != None:
                self.sensory_processes.terminate()

            info('Quit')
        except Exception as e:
            error(f'Close error: {e}')
        finally:
            signal.alarm(0)
            sys.exit(0)

    def legs_simple_move(self, angles_list, speed=90):

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
            rel_angles_list.append(angles_list[i] + self.legs.offset[i])
        self.legs.servo_write_raw(rel_angles_list)

        tt2 = time() - tt
        delay2 = 0.001*len(angles_list) - tt2

        if delay2 < -delay:
            delay2 = -delay
        sleep(delay + delay2)

    def legs_switch(self, flag=False):
        self.legs_sw_flag = flag

    def action_threads_start(self):
        # Immutable objects int, float, string, tuple, etc., need to be declared with global
        # Variable object lists, dicts, instances of custom classes, etc., do not need to be declared with global
        if 'legs' in self.thread_list:
            self.legs_thread = threading.Thread(name='legs_thread', target=self._legs_action_thread)
            self.legs_thread.setDaemon(True)
            self.legs_thread.start()
        if 'head' in self.thread_list:
            self.head_thread = threading.Thread(name='head_thread', target=self._head_action_thread)
            self.head_thread.setDaemon(True)
            self.head_thread.start()
        if 'tail' in self.thread_list:
            self.tail_thread = threading.Thread(name='tail_thread', target=self._tail_action_thread)
            self.tail_thread.setDaemon(True)
            self.tail_thread.start()
        if 'rgb' in self.thread_list:
            self.rgb_strip_thread = threading.Thread(name='rgb_strip_thread', target=self._rgb_strip_thread)
            self.rgb_strip_thread.setDaemon(True)
            self.rgb_strip_thread.start()
        if 'imu' in self.thread_list:
            self.imu_thread = threading.Thread(name='imu_thread', target=self._imu_thread)
            self.imu_thread.setDaemon(True)
            self.imu_thread.start()

    # legs
    def _legs_action_thread(self):
        while not self.exit_flag:
            try:
                with self.legs_thread_lock:
                    self.leg_current_angles = list.copy(self.legs_action_buffer[0])
                # Release lock after copying data before the next operations
                self.legs.servo_move(self.leg_current_angles, self.legs_speed)
                self.legs_action_buffer.pop(0)
            except IndexError:
                sleep(0.001)
            except Exception as e:
                error(f'\r_legs_action_thread Exception:{e}')
                break

    # head
    def _head_action_thread(self):
        while not self.exit_flag:
            try:
                with self.head_thread_lock:
                    self.head_current_angles = list.copy(self.head_action_buffer[0])
                # Release lock after copying data before the next operations
                _angles = list.copy(self.head_current_angles)
                _angles[0] = self.limit(self.HEAD_YAW_MIN, self.HEAD_YAW_MAX, _angles[0])
                _angles[1] = self.limit(self.HEAD_ROLL_MIN, self.HEAD_ROLL_MAX, _angles[1])
                _angles[2] = self.limit(self.HEAD_PITCH_MIN, self.HEAD_PITCH_MAX, _angles[2])
                _angles[2] += self.HEAD_PITCH_OFFSET
                self.head.servo_move(_angles, self.head_speed)
                self.head_action_buffer.pop(0)
            except IndexError:
                sleep(0.001)
            except Exception as e:
                error(f'\r_head_action_thread Exception:{e}')
                break

    # tail
    def _tail_action_thread(self):
        while not self.exit_flag:
            try:
                with self.tail_thread_lock:
                    self.tail_current_angles = list.copy(self.tail_action_buffer[0])
                # Release lock after copying data before the next operations
                self.tail.servo_move(self.tail_current_angles, self.tail_speed)
                self.tail_action_buffer.pop(0)
            except IndexError:
                sleep(0.001)
            except Exception as e:
                error(f'\r_tail_action_thread Exception:{e}')
                break

    # rgb strip
    def _rgb_strip_thread(self):
        while not self.exit_flag:
            try:
                self.rgb_strip.show()
                self.rgb_fail_count = 0
            except Exception as e:
                self.rgb_fail_count += 1
                sleep(0.001)
                if self.rgb_fail_count > 10:
                    error(f'\r_rgb_strip_thread Exception:{e}')
                    break

    # IMU

    def _imu_thread(self):
        # imu calibrate
        _ax = 0
        _ay = 0
        _az = 0
        _gx = 0
        _gy = 0
        _gz = 0
        time = 10
        for _ in range(time):
            data = self.imu._sh3001_getimudata()
            if data == False:
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
                    self.imu_fail_count += 1
                    if self.imu_fail_count > 10:
                        error('\r_imu_thread imu data error')
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
                ay = -ay
                az = -az

                self.pitch = atan(ay/sqrt(ax*ax+az*az))*57.2957795
                self.roll = atan(az/sqrt(ax*ax+ay*ay))*57.2957795

                self.imu_fail_count = 0
                sleep(0.05)
            except Exception as e:
                self.imu_fail_count += 1
                sleep(0.001)
                if self.imu_fail_count > 10:
                    error(f'\r_imu_thread Exception:{e}')
                    self.exit_flag = True
                    break

    # clear actions buff
    def legs_stop(self):
        with self.legs_thread_lock:
            self.legs_action_buffer.clear()
        self.wait_legs_done()

    def head_stop(self):
        with self.head_thread_lock:
            self.head_action_buffer.clear()
        self.wait_head_done()

    def tail_stop(self):
        with self.tail_thread_lock:
            self.tail_action_buffer.clear()
        self.wait_tail_done()

    def body_stop(self):
        self.legs_stop()
        self.head_stop()
        self.tail_stop()

    # move
    def legs_move(self, target_angles, immediately=True, speed=50):
        if immediately == True:
            self.legs_stop()
        self.legs_speed = speed
        with self.legs_thread_lock:
            self.legs_action_buffer += target_angles

    def head_rpy_to_angle(self, target_yrp, roll_comp=0, pitch_comp=0):
        yaw, roll, pitch = target_yrp
        signed = -1 if yaw < 0 else 1
        ratio = abs(yaw) / 90
        pitch_servo = roll * ratio + pitch * (1-ratio) + pitch_comp
        roll_servo = -(signed * (roll * (1-ratio) + pitch * ratio) + roll_comp)
        yaw_servo = yaw
        return [yaw_servo, roll_servo, pitch_servo]

    def head_move(self, target_yrps, roll_comp=0, pitch_comp=0, immediately=True, speed=50):
        if immediately == True:
            self.head_stop()
        self.head_speed = speed
        
        angles = [self.head_rpy_to_angle(
            target_yrp, roll_comp, pitch_comp) for target_yrp in target_yrps]

        with self.head_thread_lock:
            self.head_action_buffer += angles

    def head_move_raw(self, target_angles, immediately=True, speed=50):
        if immediately == True:
            self.head_stop()
        self.head_speed = speed
        with self.head_thread_lock:
            self.head_action_buffer += target_angles
        

    def tail_move(self, target_angles, immediately=True, speed=50):
        if immediately == True:
            self.tail_stop()
        self.tail_speed = speed
        with self.tail_thread_lock:
            self.tail_action_buffer += target_angles
        

    # ultrasonic
    def _ultrasonic_thread(self, distance_addr, lock):
        while True:
            try:
                with lock:
                    val = round(float(self.ultrasonic.read()), 2)
                    distance_addr.value = val
                # sleep(1)
            except Exception as e:
                sleep(0.1)
                error(f'\rultrasonic_thread  except: {e}')
                break

    # sensory_processes : ultrasonic
    def sensory_processes_work(self, distance_addr, lock):
        if 'ultrasonic' in self.thread_list:
            ultrasonic_thread = threading.Thread(name='ultrasonic_thread',
                                             target=self._ultrasonic_thread,
                                             args=(distance_addr, lock,))
            # ultrasonic_thread.setDaemon(True)
            ultrasonic_thread.start()

    def sensory_processes_start(self):
        if self.sensory_processes != None:
            self.sensory_processes.terminate()
        self.sensory_processes = Process(name='sensory_processes',
                                         target=self.sensory_processes_work,
                                         args=(self.ultrasonic.distance, self.sensory_lock))
        self.sensory_processes.start()

    # reset: stop, stop_and_lie
    def stop_and_lie(self, speed=85):
        try:
            self.body_stop()
            self.legs_move(self.actions_dict['lie'][0], speed)
            self.head_move_raw([[0, 0, 0]], speed)
            self.tail_move([[0, 0, 0]], speed)
            self.wait_all_done()
            sleep(0.1)
        except Exception as e:
            error(f'\rstop_and_lie error:{e}')

    # speak
    def speak(self, name):
        status, _ = utils.run_command('sudo killall pulseaudio') # Solve the problem that there is no sound when running in the vnc environment
        for filename in os.listdir(self.SOUND_DIR):
            if filename.startswith(name):
                self.music.sound_play_threading(self.SOUND_DIR+filename)
                break
        else:
            warn(f'No sound found for {name}')
            return False

    # calibration
    def leg_offsets(self, cali_list):
        self.legs.set_offset(cali_list)
        self.legs.reset()
        self.leg_current_angles = [0]*8

    def head_offset(self, cali_list):
        self.head.set_offset(cali_list)
        #self.head.reset()
        self.head_move([[0]*3], immediately=True, speed=80)
        self.head_current_angles = [0]*3

    def tail_offset(self, cali_list):
        self.tail.set_offset(cali_list)
        self.tail.reset()
        self.tail_current_angles = [0]

    # calculate angles and coords

    def set_pose(self, x=None, y=None, z=None):
        if x != None:
            self.pose[0, 0] = float(x)
        if y != None:
            self.pose[1, 0] = float(y)
        if z != None:
            self.pose[2, 0] = float(z)

    def set_rpy(self, roll=None, pitch=None, yaw=None, pid=False):
        if roll is None:
            roll = self.rpy[0]
        if pitch is None:
            pitch = self.rpy[1]
        if yaw is None:
            yaw = self.rpy[2]

        if pid:
            roll_error = self.target_rpy[0] - self.roll
            pitch_error = self.target_rpy[1] - self.pitch

            roll_offset = self.KP * roll_error + self.KI * self.roll_error_integral + \
                self.KD * (roll_error - self.roll_last_error)
            pitch_offset = self.KP * pitch_error + self.KI * self.pitch_error_integral + \
                self.KD * (pitch_error - self.pitch_last_error)

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

    def set_legs(self, legs_list):
        self.legpoint_struc = np.mat([
            [-self.BODY_WIDTH / 2, -self.BODY_LENGTH / 2 +
                legs_list[0][0], self.body_height - legs_list[0][1]],
            [self.BODY_WIDTH / 2, -self.BODY_LENGTH / 2 +
                legs_list[1][0], self.body_height - legs_list[1][1]],
            [-self.BODY_WIDTH / 2,  self.BODY_LENGTH / 2 +
                legs_list[2][0], self.body_height - legs_list[2][1]],
            [self.BODY_WIDTH / 2,  self.BODY_LENGTH / 2 +
                legs_list[3][0], self.body_height - legs_list[3][1]]
        ]).T

    # pose and Euler Angle algorithm
    def pose2coords(self):
        roll = self.rpy[0]
        pitch = self.rpy[1]
        yaw = self.rpy[2]

        rotx = np.mat([
            [cos(roll), 0, -sin(roll)],
            [0, 1,           0],
            [sin(roll), 0,  cos(roll)]])
        roty = np.mat([
            [1,         0,          0],
            [0, cos(-pitch), -sin(-pitch)],
            [0, sin(-pitch),  cos(-pitch)]])
        rotz = np.mat([
            [cos(yaw), -sin(yaw), 0],
            [sin(yaw),  cos(yaw), 0],
            [0,         0, 1]])
        rot_mat = rotx * roty * rotz
        AB = np.mat(np.zeros((3, 4)))
        for i in range(4):
            AB[:, i] = - self.pose - rot_mat * \
                self.BODY_STRUCT[:, i] + self.legpoint_struc[:, i]

        body_coor_list = []
        for i in range(4):
            body_coor_list.append([(self.legpoint_struc - AB).T[i, 0],
                                  (self.legpoint_struc - AB).T[i, 1], (self.legpoint_struc - AB).T[i, 2]])

        leg_coor_list = []
        for i in range(4):
            leg_coor_list.append(
                [self.legpoint_struc.T[i, 0], self.legpoint_struc.T[i, 1], self.legpoint_struc.T[i, 2]])

        return {"leg": leg_coor_list, "body": body_coor_list}

    def pose2legs_angle(self):
        data = self.pose2coords()
        leg_coor_list = data["leg"]
        body_coor_list = data["body"]
        coords = []
        angles = []

        for i in range(4):
            coords.append([
                leg_coor_list[i][1] - body_coor_list[i][1],
                body_coor_list[i][2] - leg_coor_list[i][2]])

        angles = []

        for i, coord in enumerate(coords):

            leg_angle, foot_angle = self.fieldcoord2polar(coord)
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
        u = sqrt(pow(y, 2) + pow(z, 2))
        cos_angle1 = (self.FOOT**2 + self.LEG**2 - u**2) / \
            (2 * self.FOOT * self.LEG)
        cos_angle1 = min(max(cos_angle1, -1), 1)
        beta = acos(cos_angle1)

        angle1 = atan2(y, z)
        cos_angle2 = (self.LEG**2 + u**2 - self.FOOT**2)/(2*self.LEG*u)
        cos_angle2 = min(max(cos_angle2, -1), 1)
        angle2 = acos(cos_angle2)
        alpha = angle2 + angle1 + self.rpy[1]

        alpha = alpha / pi * 180
        beta = beta / pi * 180

        return alpha, beta

    def coord2polar(self, coord):
        y, z = coord
        u = sqrt(pow(y, 2) + pow(z, 2))
        cos_angle1 = (self.FOOT**2 + self.LEG**2 - u**2) / \
            (2 * self.FOOT * self.LEG)
        cos_angle1 = min(max(cos_angle1, -1), 1)
        beta = acos(cos_angle1)

        angle1 = atan2(y, z)
        cos_angle2 = (self.LEG**2 + u**2 - self.FOOT**2)/(2*self.LEG*u)
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

        return [round(x, 4), round(y, 4), round(z, 4)]

    @classmethod
    def legs_angle_calculation(cls, coords):  # 注意这里使用了 @classmethod
        translate_list = []
        for i, coord in enumerate(coords):  # each servo motion
            # coord2polar
            leg_angle, foot_angle = Pidog.coord2polar(cls, coord)
            # The left and right sides are opposite
            leg_angle = leg_angle
            foot_angle = foot_angle-90
            if i % 2 != 0:
                leg_angle = -leg_angle
                foot_angle = -foot_angle
            translate_list += [leg_angle, foot_angle]

        return translate_list

    # limit
    def limit(self, min, max, x):
        if x > max:
            return max
        elif x < min:
            return min
        else:
            return x

    # set angle
    def set_angle(self, angles_list, speed=50, israise=False):
        translate_list = []
        results = []
        for angles in angles_list:
            result, angles = self.limit_angle(angles)
            translate_list += angles
            results.append(result)
        if True in results:
            if israise == True:
                raise ValueError(
                    '\033[1;35mCoordinates out of controllable range.\033[0m')
            else:
                print('\033[1;35mCoordinates out of controllable range.\033[0m')
                coords = []
                # Calculate coordinates
                for i in range(4):
                    coords.append(self.polar2coord(
                        [translate_list[i*3], translate_list[i*3+1], translate_list[i*3+2]]))
                self.current_coord = coords
        else:
            self.current_coord = self.coord_temp

        self.servo_move(translate_list, speed)

    # do action
    def do_action(self, action_name, step_count=1, speed=50):
        try:
            actions, part = self.actions_dict[action_name]
            if part == 'legs':
                for _ in range(step_count):
                    self.legs_move(actions, immediately=False, speed=speed)
            elif part == 'head':
                for _ in range(step_count):
                    self.head_move(actions, immediately=False, speed=speed)
            elif part == 'tail':
                for _ in range(step_count):
                    self.tail_move(actions, immediately=False, speed=speed)
        except KeyError:
            error("do_action: No such action")
        except Exception as e:
            error(f"do_action:{e}")

    def wait_legs_done(self):
        while not self.is_legs_done():
            sleep(0.001)

    def wait_head_done(self):
        while not self.is_head_done():
            sleep(0.001)

    def wait_tail_done(self):
        while not self.is_tail_done():
            sleep(0.001)

    def wait_all_done(self):
        self.wait_legs_done()
        self.wait_head_done()
        self.wait_tail_done()

    def is_legs_done(self):
        return not bool(len(self.legs_action_buffer) > 0)

    def is_head_done(self):
        return not bool(len(self.head_action_buffer) > 0)

    def is_tail_done(self):
        return not bool(len(self.tail_action_buffer) > 0)

    def is_all_done(self):
        return self.is_legs_done() and self.is_head_done() and self.is_tail_done()
