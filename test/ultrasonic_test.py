from robot_hat import Ultrasonic, Pin
import time

# Create an ultrasonic sensor object
# Trigger pin is D0, echo pin is D1

ultrasonic = Ultrasonic(Pin("D0"), Pin("D1"))

# Read the distance in centimeters
while True:
    distance = ultrasonic.read()
    print(f"Distance: {distance} cm")
    time.sleep(1)
