# from robot_hat import I2C
# import time

# ADDR = 0x57

# DATA_REG_ADDR = 0x00

# sonar = I2C(ADDR)
# while True:
#     sonar.write(0x01)
#     time.sleep(0.2) #wait for the echo

#     data = sonar.mem_read(3, DATA_REG_ADDR)
#     print(data)
#     time.sleep(0.2)

import smbus
import time

bus = smbus.SMBus(1)  # Rev 2 Pi uses 1
time.sleep(1) #wait here to avoid 121 IO Error

address = 0x57 #I2C address

while True:

    cmd = 1
    bus.write_byte(address, cmd)
    time.sleep(0.2) #wait for the echo  # 0.2

    data = bus.read_i2c_block_data(address, 0, 3) #read three bytes into array

    distance = (data[0] * 65535 + data[1] * 256 + data[2])/10000
    print("distance : " + format(distance, '.2f'))

