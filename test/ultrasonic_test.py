from robot_hat import Ultrasonic, Pin
import time

ultrasonic = Ultrasonic(Pin("D1"), Pin("D0"))

# Read the distance in centimeters
while True:
    distance = ultrasonic.read()
    print(f"Distance: {distance} cm")
    time.sleep(1)


# from pidog import Pidog
# import time

# my_dog = Pidog()
    
# DANGER_DISTANCE = 15

# while True:
#     distance = round(my_dog.read_distance(), 2)
#     my_dog.do_action('shake_head', step_count=1, speed=80)
#     if distance < DANGER_DISTANCE:
#         print(f"\033[0;31m Distance: {distance}\033[m")
#         time.sleep(0.21)
#     else:
#         print(f"Distance: {distance}")
#     time.sleep(0.01)