#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from math import sin
from preset_actions import bark_action


my_dog = Pidog()
sleep(0.1)


def lean_forward():
    my_dog.speak('angry')
    bark_action(my_dog)
    sleep(0.2)
    bark_action(my_dog)
    sleep(0.8)
    bark_action(my_dog)


def head_nod(step):
    y = 0
    r = 0
    p = 30
    angs = []
    for i in range(20):
        r = round(10*sin(i*0.314), 2)
        p = round(20*sin(i*0.314) + 10, 2)
        angs.append([y, r, p])

    my_dog.head_move(angs*step, immediately=False, speed=80)


def alert():
    my_dog.do_action('stand', step_count=1, speed=90)
    my_dog.rgb_strip.set_mode(
        'breath', color='pink', brightness=0.8, delay=0.08)
    while True:
        print(
            f'distance.value: {round(my_dog.ultrasonic.read_distance(), 2)} cm, touch {my_dog.dual_touch.read()}')
        # alert
        if my_dog.ultrasonic.read_distance() < 15 and my_dog.ultrasonic.read_distance() > 1:
            my_dog.head_move([[0, 0, 0]], immediately=True, speed=90)
            my_dog.tail_move([[0]], immediately=True, speed=90)
            my_dog.rgb_strip.set_mode(
                'boom', color='red', brightness=0.8, delay=0.001)
            my_dog.do_action('backward', step_count=1, speed=98)
            my_dog.wait_all_done()
            lean_forward()
            while len(my_dog.legs_action_buffer) > 0:
                sleep(0.1)
            my_dog.do_action('stand', step_count=1, speed=90)
            sleep(0.5)
        else:
            my_dog.rgb_strip.set_mode(
                'breath', color='pink', brightness=0.8, delay=0.08)
        # relax
        if my_dog.dual_touch.read() != 'N':
            if len(my_dog.head_action_buffer) < 2:
                head_nod(1)
                my_dog.do_action('wag_tail', step_count=20, speed=100)
                my_dog.rgb_strip.set_mode(
                    'breath', color='pink', brightness=0.8, delay=0.08)
        else:
            my_dog.tail_stop()
        sleep(0.2)


if __name__ == "__main__":
    try:
        alert()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        my_dog.close()

