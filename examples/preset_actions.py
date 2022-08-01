
from time import sleep

def pant(my_dog, yrp=None):
    if yrp is None:
        yrp = [0, 0, -40]
    h1 = [0 + yrp[0], 0 + yrp[1], 10 + yrp[2]]
    h2 = [0 + yrp[0], 0 + yrp[1],  0 + yrp[2]]
    h = [h1] + [h2] + [h1]
    my_dog.speak('pant')
    for _ in range(10):
        my_dog.head_move(h, immediately=False, speed=92)

def body_twisting(my_dog):
    f1 = [-80, 70, 80, -70, -20, 64, 20, -64]
    f2 = [-70, 50, 80, -90, 10, 20, 20, -64]
    f3 = [-80, 90, 70, -50, -20, 64, -10, -20]
    f = [f2] + [f1] + [f3] + [f1]

    h1 = [0,0,20]
    h2 = [0,30,20]
    h3 = [0,-30,20]
    h = [h2] + [h1] + [h3] + [h1]

    my_dog.feet_move(f,immediately=False,speed=50)

def bark_action(my_dog, yrp=None):
    if yrp is None:
        yrp = [0, 0, -40]
    h1 = [0 + yrp[0], 0 + yrp[1], 20 + yrp[2]]
    h2 = [0 + yrp[0], 0 + yrp[1],  0 + yrp[2]]

    f1 = my_dog.feet_angle_calculation([[0, 100], [0, 100], [30, 90], [30, 90]])
    f2 = my_dog.feet_angle_calculation([[-20, 90], [-20, 90], [0, 90], [0, 90]])

    my_dog.feet_move([f1], immediately=True, speed=95)
    my_dog.head_move([h1], immediately=True, speed=95)
    my_dog.wait_all_done()
    sleep(0.01)
    my_dog.feet_move([f2], immediately=True, speed=95)
    my_dog.head_move([h2], immediately=True, speed=95)
    my_dog.wait_all_done()
    sleep(0.01)

def shake_head(my_dog):
    my_dog.head_move([[40, 0, -20]], immediately=False, speed=92)
    my_dog.head_move([[-40, 0, -20]], immediately=False, speed=92)
    my_dog.head_move([[0, 0, -20]], immediately=False, speed=92)
    my_dog.wait_all_done()

def bark(my_dog, yrp=None):
    if yrp is None:
        yrp = [0, 0, -40]
    h1 = [0 + yrp[0], 0 + yrp[1], 20 + yrp[2]]
    h2 = [0 + yrp[0], 0 + yrp[1],  0 + yrp[2]]
    angles = [h2, h1, h1, h2]
    my_dog.head_move(angles, speed=95)
    # my_dog.do_action('head_bark', speed=95)
    sleep(0.1)
    my_dog.speak('single_bark_001')
    my_dog.wait_all_done()

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
