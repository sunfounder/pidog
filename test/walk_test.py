from robot_hat import Robot, Pin, Ultrasonic, utils, Music
from pidog.walk import Walk
from pidog import Pidog
import time
import os

# user and User home directory
User = os.popen('echo ${SUDO_USER:-$LOGNAME}').readline().strip()
UserHome = os.popen('getent passwd %s | cut -d: -f 6'%User).readline().strip()
# print(User)  # pi
# print(UserHome) # /home/pi
config_file = '%s/.config/pidog/pidog.conf'%UserHome
feet_pins=[1, 2, 3, 4, 5, 6, 7, 8]

robot = Robot(pin_list=feet_pins, db=config_file)

data = []
forward = Walk(Walk.FORWARD, Walk.STRAIGHT)
coords = forward.get_coords()
for coord in coords:
    data.append(Pidog.feet_angle_calculation(coord))
print(data)

while True:
    for coord in data:
        print(coord)
        # robot.servo_move(coord, speed=100)
        # robot.servo_move2(coord, speed=100)
        robot.servo_write_all(coord)
        time.sleep(0.1)