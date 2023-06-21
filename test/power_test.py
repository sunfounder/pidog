from pidog import Pidog
from time import sleep
import threading



my_dog = Pidog()

SPEED = 100

try:
    active_threads = threading.active_count()
    print(f"active_threads: {active_threads}")
    for thread in threading.enumerate():
        print(f"{thread.name}")

    my_dog.rgb_strip.set_mode("boom", "red")
    while True:
        # my_dog.do_action("stand", speed=SPEED)
        # sleep(2)
        # my_dog.do_action("lie", speed=SPEED)
        # sleep(2)
        # my_dog.do_action("push_up", speed=SPEED)
        # sleep(2)
        # my_dog.do_action("lie", speed=SPEED)
        # sleep(2)
        # print(len(my_dog.legs_action_buffer))
        my_dog.do_action("trot", step_count=1, speed=SPEED)
        my_dog.do_action("wag_tail", step_count=10, speed=SPEED)
        my_dog.do_action("shake_head", step_count=2, speed=SPEED)
        # print(f"{my_dog.accData, my_dog.ultrasonic.read_distance()}")
        sleep(0.1)
except KeyboardInterrupt:
    my_dog.close()

# from robot_hat import Servo
# from time import sleep

# s0 = Servo(9)

# while True:
#     for i in range(-90, 90, 5):
#         s0.angle(i)
#         sleep(0.001)
#     sleep(0.2)
#     for i in range(90, -90, -5):
#         s0.angle(i)
#         sleep(0.001)
#     sleep(0.2)