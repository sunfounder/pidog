from pidog.sh3001 import Sh3001
from time import sleep

imu = Sh3001(db="home/pi/.config/pidog/pidog.conf")

accData = []  # ax,ay,az
gyroData = []  # gx,gy,gz

imu_acc_offset = [0, 0, 0]
imu_gyro_offset = [0, 0, 0]

print("Calibrating IMU...")

_ax = 0
_ay = 0
_az = 0
_gx = 0
_gy = 0
_gz = 0
time = 10
for _ in range(time):
    data = imu._sh3001_getimudata()
    if data == False:
        print('_imu_thread imu data error')
        break

    accData, gyroData = data
    _ax += accData[0]
    _ay += accData[1]
    _az += accData[2]
    _gx += gyroData[0]
    _gy += gyroData[1]
    _gz += gyroData[2]
    sleep(0.1)

imu_acc_offset[0] = round(-16384 - _ax/time, 0)
imu_acc_offset[1] = round(0 - _ay/time, 0)
imu_acc_offset[2] = round(0 - _az/time, 0)
imu_gyro_offset[0] = round(0 - _gx/time, 0)
imu_gyro_offset[1] = round(0 - _gy/time, 0)
imu_gyro_offset[2] = round(0 - _gz/time, 0)

print("Done!")


while True:
    data = imu._sh3001_getimudata()
    if data == False:
        sleep(0.1)
        print('_imu_thread imu data error')
        break

    accData, gyroData = data
    accData = [accData[i]+imu_acc_offset[i] for i in range(3)]
    gyroData = [gyroData[i]+imu_gyro_offset[i] for i in range(3)]

    print(f"\rACC: {accData[0]:8} {accData[1]:8} {accData[2]:8} | GYRO: {gyroData[0]:8} {gyroData[1]:8} {gyroData[2]:8}",
          end="          ", flush=True)
    sleep(0.1)
