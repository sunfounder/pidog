from pidog import Pidog
import time
import threading



my_dog = Pidog()

SPEED = 100

try:
    active_threads = threading.active_count()
    print(f"active_threads: {active_threads}")
    for thread in threading.enumerate():
        print(f"{thread.name}")

    my_dog.rgb_strip.set_mode("boom", "red")

    my_dog.do_action("stand", step_count=54, speed=SPEED)
    # my_dog.head_move([[0, 0, 0]], pitch_comp=-30)

    # my_dog.rgb_strip.set_mode("boom", "red")
    st = time.time()
    while True:
        # my_dog.do_action("stand", speed=SPEED)
        # time.sleep(1.5)
        # my_dog.do_action("lie", speed=SPEED)
        # time.sleep(1.5)
        # my_dog.do_action("push_up", speed=SPEED)
        # time.sleep(1.5)
        # my_dog.do_action("lie", speed=SPEED)
        # time.sleep(1.5)
        # print(len(my_dog.legs_action_buffer))
        my_dog.do_action("trot", step_count=2, speed=SPEED)
        my_dog.do_action("wag_tail", step_count=10, speed=SPEED)
        my_dog.do_action("shake_head", step_count=5, pitch_comp=-10, speed=SPEED)
        # print(f"{my_dog.accData, my_dog.ultrasonic.read_distance()}")
        # if time.time() - st > 60:
        #     my_dog.body_stop()
        #     time.sleep(3)
        #     st = time.time()
        
        time.sleep(1)


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