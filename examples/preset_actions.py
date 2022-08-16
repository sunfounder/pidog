
from time import sleep

def scratch(my_dog):
    h2 = [[0, 40, -40]]
    f_up = [
        [30, 60, 50, 50, 80, -45, -80, 45],
    ]
    f_scratch = [
        [30, 60, 40, 40, 80, -45, -80, 45],
        [30, 60, 50, 50, 80, -45, -80, 45],
    ]

    my_dog.head_move(h2, immediately=False, speed=80)
    my_dog.feet_move(f_up, immediately=False, speed=80)
    my_dog.wait_all_done()
    for _ in range(10):
        my_dog.feet_move(f_scratch, immediately=False, speed=94)
        my_dog.wait_all_done()

    my_dog.head_move(h1, immediately=False, speed=80)
    my_dog.do_action('sit', speed=80)
    my_dog.wait_all_done()

def hand_shake(my_dog):
    f_up = [
        [30, 60, -20, 65, 80, -45, -80, 45],
    ]
    f_handshake = [
        [30, 60, 10, -25, 80, -45, -80, 45],
        [30, 60, 10, -35, 80, -45, -80, 45],
    ]
    f_withdraw = [
        [30, 60, -40, 30, 80, -45, -80, 45],
    ]

    my_dog.feet_move(f_up, immediately=False, speed=80)
    my_dog.wait_all_done()

    for _ in range(5):
        my_dog.feet_move(f_handshake, immediately=False, speed=90)
        my_dog.wait_all_done()

    my_dog.feet_move(f_withdraw, immediately=False, speed=80)
    my_dog.wait_all_done()

def high_five(my_dog):
    f_up = [
        [30, 60, 50, 30, 80, -45, -80, 45],
    ]
    f_down = [
        [30, 60, 70, -50, 80, -45, -80, 45],
    ]
    f_withdraw = [
        [30, 60, -40, 30, 80, -45, -80, 45],
    ]
    my_dog.feet_move(f_up, immediately=False, speed=80)
    my_dog.wait_all_done()

    my_dog.feet_move(f_down, immediately=False, speed=94)
    my_dog.wait_all_done()
    sleep(0.5)

    my_dog.feet_move(f_withdraw, immediately=False, speed=80)
    my_dog.wait_all_done()

def pant(my_dog, yrp=None):
    if yrp is None:
        yrp = [0, 0, -40]
    h1 = [0 + yrp[0], 0 + yrp[1], 20 + yrp[2]]
    h2 = [0 + yrp[0], 0 + yrp[1],  0 + yrp[2]]
    h = [h1] + [h2] + [h1]
    my_dog.speak('pant')
    for _ in range(10):
        my_dog.head_move(h, immediately=False, speed=92)
        my_dog.wait_head_done()

def body_twisting(my_dog):
    f1 = [-80, 70, 80, -70, -20, 64, 20, -64]
    f2 = [-70, 50, 80, -90, 10, 20, 20, -64]
    f3 = [-80, 90, 70, -50, -20, 64, -10, -20]
    f = [f2] + [f1] + [f3] + [f1]

    my_dog.feet_move(f,immediately=False,speed=50)

def bark_action(my_dog, yrp=None, speak=None):
    if yrp is None:
        yrp = [0, 0, 0]
    h1 = [0 + yrp[0], 0 + yrp[1], 20 + yrp[2]]
    h2 = [0 + yrp[0], 0 + yrp[1],  0 + yrp[2]]

    f1 = my_dog.feet_angle_calculation([[0, 100], [0, 100], [30, 90], [30, 90]])
    f2 = my_dog.feet_angle_calculation([[-20, 90], [-20, 90], [0, 90], [0, 90]])

    if speak is not None:
        my_dog.speak(speak)
    my_dog.feet_move([f1], immediately=True, speed=95)
    my_dog.head_move([h1], immediately=True, speed=95)
    my_dog.wait_all_done()
    sleep(0.01)
    my_dog.feet_move([f2], immediately=True, speed=95)
    my_dog.head_move([h2], immediately=True, speed=95)
    my_dog.wait_all_done()
    sleep(0.01)

def shake_head(my_dog, yrp=None):
    if yrp is None:
        yrp = [0, 0, -20]
    h1 = [[40 + yrp[0], 0 + yrp[1], 0 + yrp[2]]]
    h2 = [[-40 + yrp[0], 0 + yrp[1], 0 + yrp[2]]]
    h3 = [[0 + yrp[0], 0 + yrp[1], 0 + yrp[2]]]
    my_dog.head_move(h1, immediately=False, speed=92)
    my_dog.head_move(h2, immediately=False, speed=92)
    my_dog.head_move(h3, immediately=False, speed=92)
    my_dog.wait_all_done()

def bark(my_dog, yrp=None):
    if yrp is None:
        yrp = [0, 0, 0]
    head_up = [0 + yrp[0], 0 + yrp[1], 25 + yrp[2]]
    head_down = [0 + yrp[0], 0 + yrp[1],  0 + yrp[2]]
    my_dog.head_move([head_up], immediately=True, speed=100)
    my_dog.speak('single_bark_1')
    my_dog.wait_all_done()
    sleep(0.08)
    my_dog.head_move([head_down], immediately=True, speed=100)
    my_dog.wait_all_done()
    sleep(0.5)

def pushup(my_dog):
    my_dog.head_move([[0, 0, -80], [0, 0, -40]], speed=80)
    my_dog.do_action('pushup', speed=80)
    my_dog.wait_all_done()

def howling(my_dog):
    my_dog.do_action('sit', speed=95)
    my_dog.head_move([[0,0,-30]], speed=95)
    my_dog.wait_all_done()

    my_dog.rgb_strip.set_mode('breath', front_color='cyan', delay=0.08)
    my_dog.do_action('half_sit', wait=True, speed=80)
    my_dog.head_move([[0,0,-60]], speed=80)
    my_dog.wait_all_done()
    my_dog.speak('howling')
    my_dog.do_action('sit', speed=60)
    my_dog.head_move([[0,0,10]], speed=70)
    my_dog.wait_all_done()

    my_dog.do_action('sit', speed=60)
    my_dog.head_move([[0,0,10]], speed=80)
    my_dog.wait_all_done()

    sleep(2.34)


if __name__ == "__main__":
    from pidog import Pidog
    import readchar

    my_dog = Pidog(feet_pins=[1, 2, 9, 10, 3, 4, 11, 12],
        head_pins=[7, 5, 6],
        tail_pin=[8],
    )
    hand_shake(my_dog)