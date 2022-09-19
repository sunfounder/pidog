from robot_hat import Ultrasonic, Pin
import time


ultrasonic = Ultrasonic(Pin("D1"), Pin("D0"))

# Read the distance in centimeters
while True:
    distance = ultrasonic.read()
    print(f"Distance: {distance} cm")
    time.sleep(1)
