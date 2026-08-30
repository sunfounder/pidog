
from time import sleep
import random
from math import sin, cos, pi


def scratch(my_dog):
    h1 = [[0, 0, -40]]
    h2 = [[30, 70, -10]]
    f_up = [
        [30, 60, 50, 50, 80, -45, -80, 38],  # Note 1
    ]
    f_scratch = [
        [30, 60, 40, 40, 80, -45, -80, 38],  # Note 1
        [30, 60, 50, 50, 80, -45, -80, 38],  # Note 1
    ]
    my_dog.do_action('sit', speed=80)
    my_dog.head_move(h2, immediately=False, speed=80)
    my_dog.legs_move(f_up, immediately=False, speed=80)
    my_dog.wait_all_done()
    for _ in range(10):
        my_dog.legs_move(f_scratch, immediately=False, speed=94)
        my_dog.wait_all_done()

    my_dog.head_move(h1, immediately=False, speed=80)
    my_dog.do_action('sit', speed=80)
    my_dog.wait_all_done()
# Note 1: Last servo(4th legs) original value is 45, change to 40 to push down alittle bit to support the rasing legs, prevent the dog from falling down.


def hand_shake(my_dog):
    f_up = [
        [30, 60, -20, 65, 80, -45, -80, 38],  # Note 1
    ]
    f_handshake = [
        [30, 60, 10, -25, 80, -45, -80, 38],  # Note 1
        [30, 60, 10, -35, 80, -45, -80, 38],  # Note 1
    ]
    f_withdraw = [
        [30, 60, -40, 30, 80, -45, -80, 38],  # Note 1
    ]

    my_dog.legs_move(f_up, immediately=False, speed=80)
    my_dog.wait_all_done()
    sleep(0.1)

    for _ in range(8):
        my_dog.legs_move(f_handshake, immediately=False, speed=90)
        my_dog.wait_all_done()

    my_dog.legs_move(f_withdraw, immediately=False, speed=80)

    hand_down_angs = [
        [30, 60, -30, -40, 80, -45, -80, 45],
        [30, 60, -30, -50, 80, -45, -80, 45],
        [30, 60, -30, -58, 80, -45, -80, 45],
        [30, 60, -30, -60, 80, -45, -80, 45],
    ]

    my_dog.legs_move(hand_down_angs, immediately=False, speed=80)
    my_dog.head_move([[0, 0, -35]], speed=80)
    my_dog.wait_all_done()


def high_five(my_dog):
    f_up = [
        [30, 60, 50, 30, 80, -45, -80, 38],  # Note 1
    ]
    f_down = [
        [30, 60, 70, -50, 80, -45, -80, 38],  # Note 1
    ]
    f_withdraw = [
        [30, 60, -40, 30, 80, -45, -80, 38],  # Note 1
    ]
    my_dog.legs_move(f_up, immediately=False, speed=80)
    my_dog.wait_all_done()

    my_dog.legs_move(f_down, immediately=False, speed=94)
    my_dog.wait_all_done()
    sleep(0.5)

    my_dog.legs_move(f_withdraw, immediately=False, speed=80)

    hand_down_angs = [
        [30, 60, -30, -40, 80, -45, -80, 45],
        [30, 60, -30, -50, 80, -45, -80, 45],
        [30, 60, -30, -58, 80, -45, -80, 45],
        [30, 60, -30, -60, 80, -45, -80, 45],
    ]

    my_dog.legs_move(hand_down_angs, immediately=False, speed=80)
    my_dog.head_move([[0, 0, -35]], speed=80)
    my_dog.wait_all_done()


def pant(my_dog, yrp=None, pitch_comp=0, speed=80, volume=100):
    if yrp is None:
        yrp = [0, 0, 0]
    h1 = [0 + yrp[0], 0 + yrp[1],   0 + yrp[2]]
    h2 = [0 + yrp[0], 0 + yrp[1], -10 + yrp[2]]
    h = [h1] + [h2] + [h1]
    my_dog.speak('pant', volume)
    sleep(0.01)
    for _ in range(6):
        my_dog.head_move(h, pitch_comp=pitch_comp, immediately=False, speed=speed)
        my_dog.wait_head_done()


def body_twisting(my_dog):
    f1 = [-80, 70, 80, -70, -20, 64, 20, -64]
    f2 = [-70, 50, 80, -90, 10, 20, 20, -64]
    f3 = [-80, 90, 70, -50, -20, 64, -10, -20]
    f = [f2] + [f1] + [f3] + [f1]

    my_dog.legs_move(f, immediately=False, speed=50)
    my_dog.wait_all_done()
    sleep(.3)
    _2_sit_angs = [
        [40, 35, -40, -35, 60, 5, -60, -5],
        [30, 60, -30, -60, 80, -45, -80, 45]
    ]
    my_dog.legs_move(_2_sit_angs, immediately=False, speed=68)
    my_dog.head_move_raw([[0, 0, -35]], immediately=False, speed=68)
    my_dog.wait_all_done()


def bark_action(my_dog, yrp=None, speak=None, volume=100):
    if yrp is None:
        yrp = [0, 0, 0]
    h1 = [0 + yrp[0], 0 + yrp[1], 20 + yrp[2]]
    h2 = [0 + yrp[0], 0 + yrp[1],  0 + yrp[2]]

    f1 = my_dog.legs_angle_calculation(
        [[0, 100], [0, 100], [30, 90], [30, 90]])
    f2 = my_dog.legs_angle_calculation(
        [[-20, 90], [-20, 90], [0, 90], [0, 90]])

    if speak is not None:
        my_dog.speak(speak, volume)
    my_dog.legs_move([f1], immediately=True, speed=85)
    my_dog.head_move([h1], immediately=True, speed=85)
    my_dog.wait_all_done()
    sleep(0.01)
    my_dog.legs_move([f2], immediately=True, speed=85)
    my_dog.head_move([h2], immediately=True, speed=85)
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


def shake_head_smooth(my_dog, pitch_comp=0, amplitude=40, speed=90):
    y = 0
    r = 0
    p = 0
    angs = []

    for i in range(0, 31, 2):
        y = round(amplitude*sin(pi/10*i), 2)
        r = 0
        p = pitch_comp
        angs.append([y, r, p])

    my_dog.head_move_raw(angs, speed=speed)
    my_dog.wait_all_done()


def bark(my_dog, yrp=None, pitch_comp=0, roll_comp=0, volume=100):
    if yrp is None:
        yrp = [0, 0, 0]
    head_up = [0 + yrp[0], 0 + yrp[1], 25 + yrp[2]]
    head_down = [0 + yrp[0], 0 + yrp[1],  0 + yrp[2]]
    my_dog.wait_head_done()
    my_dog.head_move([head_up], pitch_comp=pitch_comp,
                     roll_comp=roll_comp, immediately=True, speed=100)
    my_dog.speak('single_bark_1', volume)
    my_dog.wait_head_done()
    sleep(0.08)
    my_dog.head_move([head_down], pitch_comp=pitch_comp,
                     roll_comp=roll_comp, immediately=True, speed=100)
    my_dog.wait_head_done()
    sleep(0.5)


def push_up(my_dog, speed=80):
    my_dog.head_move([[0, 0, -80], [0, 0, -40]], speed=speed-10)
    my_dog.do_action('push_up', speed=speed)
    my_dog.wait_all_done()


def howling(my_dog, volume=100):
    my_dog.do_action('sit', speed=80)
    my_dog.head_move([[0, 0, -30]], speed=95)
    my_dog.wait_all_done()

    my_dog.rgb_strip.set_mode('speak', color='cyan', bps=0.6)
    my_dog.do_action('half_sit', speed=80)
    my_dog.head_move([[0, 0, -60]], speed=80)
    my_dog.wait_all_done()
    my_dog.speak('howling', volume)
    my_dog.do_action('sit', speed=60)
    my_dog.head_move([[0, 0, 10]], speed=70)
    my_dog.wait_all_done()

    my_dog.do_action('sit', speed=60)
    my_dog.head_move([[0, 0, 10]], speed=80)
    my_dog.wait_all_done()

    sleep(2.34)
    my_dog.do_action('sit', speed=80)
    my_dog.head_move([[0, 0, -40]], speed=80)
    my_dog.wait_all_done()


def attack_posture(my_dog):
    f2 = my_dog.legs_angle_calculation(
        [[-20, 90], [-20, 90], [0, 90], [0, 90]]
        )
    my_dog.legs_move([f2], immediately=True, speed=85)
    my_dog.wait_legs_done()
    sleep(0.01)


def lick_hand(my_dog):
    leg1 =  [
        [30, 45, 70, -32, 80, -55, -80, 45]
    ]
    head1 = [
        [-22, -23, -45],
        [-22, -23, -35],
    ]
    leg2 =  [
        [30, 45, 70, -32, 80, -55, -80, 45],
        [30, 45, 66, -36, 80, -55, -80, 45]
    ]
    
    my_dog.do_action('sit', speed=80)
    my_dog.head_move([[0, 0, -40]], immediately=True, speed=70)
    my_dog.wait_head_done()
    my_dog.wait_legs_done()

    my_dog.legs_move(leg1, immediately=False, speed=80)
    my_dog.head_move(head1, immediately=False, speed=70)
    my_dog.wait_head_done()
    my_dog.wait_legs_done()
    for _ in range(3):
        my_dog.legs_move(leg2, immediately=False, speed=90)
        my_dog.head_move(head1, immediately=False, speed=80)
        my_dog.wait_head_done()
        my_dog.wait_legs_done()

    hand_down_angs = [
        [30, 60, -30, -40, 80, -45, -80, 45],
        [30, 60, -30, -50, 80, -45, -80, 45],
        [30, 60, -30, -58, 80, -45, -80, 45],
        [30, 60, -30, -60, 80, -45, -80, 45],
    ]

    my_dog.legs_move(hand_down_angs, immediately=False, speed=80)
    my_dog.head_move([[0, 0, -35]], speed=80)
    my_dog.wait_all_done()

def waiting(my_dog, pitch_comp):
    global last_wait
    p0 =  [0, 7, pitch_comp+5]
    p1 =  [0, -7, pitch_comp+5]
    p2 =  [0, 7, pitch_comp-5]
    p3 =  [0, -7, pitch_comp-5]
    p = [p0, p1, p2, p3]
    weights = [1, 1, 1, 1]
    choice = random.choices(p, weights)[0]
    my_dog.head_move([choice], immediately=False, speed=5)
    my_dog.wait_head_done()

def feet_shake(my_dog, step=None):
    current_legs = list.copy(my_dog.leg_current_angles)

    L1 = list.copy(current_legs)
    L2 = list.copy(current_legs)
    L1[0] += 10
    L1[1] -= 25
    L2[2] -= 10
    L2[3] += 25

    leg1 = [
        L1,
        L1,
        L2,
        L2,
    ]
    leg2 =  [
        L1,
        current_legs,
    ]
    leg3 =  [
        L2,
        current_legs,
    ]

    legs_actions = [ leg1, leg2, leg3]
    weights = [1, 1, 1]
    legs_action = random.choices(legs_actions, weights)[0]

    if step == None:
        step = random.randint(1, 2)

    for _ in range(step):
        my_dog.legs_move(legs_action, immediately=False, speed=45)
        my_dog.wait_legs_done()

    my_dog.do_action('sit', speed=60)
    my_dog.head_move([[0, 0, -40]], speed=80)
    my_dog.wait_all_done()

    
def sit_2_stand(my_dog, speed=75):

    sit_angles = my_dog.actions_dict['sit'][0][0]
    stand_angles = my_dog.actions_dict['stand'][0][0]

    L1 = [25, 25, -25, -25, 70, -25, -70, 25]

    legs_action = [
        # sit_angles,
        L1,
        stand_angles,
    ]
    
    my_dog.legs_move(legs_action, immediately=False, speed=speed)
    my_dog.wait_legs_done()

def relax_neck(my_dog, pitch_comp=-35):

    y_ang = 0
    r_ang = 0
    p_ang = 0
    turn_neck_angs = []

    for i in range(21):
        y_ang = round(10*sin(pi/10*i), 2)
        r_ang = round(45*sin(pi/10*i), 2)
        p_ang = round(20*sin(pi/10*i-pi/2) + pitch_comp, 2)
        turn_neck_angs.append([y_ang, r_ang, p_ang])

    my_dog.head_move_raw(turn_neck_angs, speed=80)
    
    my_dog.wait_all_done()
    sleep(0.3)

    stretch_neck_angs = [
        [0, 0, 5+pitch_comp],
        # [0, 35, 5+pitch_comp],
        [0, 45, 5+pitch_comp],
        [0, 25, 5+pitch_comp],
        [0, 45, 5+pitch_comp],
        [0, 25, 5+pitch_comp],

        [0, 0, 5+pitch_comp],
        [0, 0, 5+pitch_comp],

        [0, 0, 5+pitch_comp],
        # [0, -35, 5+pitch_comp],
        [0, -45, 5+pitch_comp],
        [0, -25, 5+pitch_comp],
        [0, -45, 5+pitch_comp],
        [0, -25, 5+pitch_comp],
        [0, 0, pitch_comp],
    ]


    # my_dog.head_move(stretch_neck_angs, speed=80, pitch_comp=-35)
    my_dog.head_move_raw(stretch_neck_angs, speed=80)

    my_dog.wait_all_done()


def nod(my_dog, pitch_comp=-35, amplitude=20, step=2, speed=90):
    y = 0
    r = 0
    p = 0
    angs = []

    for i in range(0, 20*step+1, 2):
        y = 0
        r = 0
        p = round(amplitude*cos(pi/10*i) - amplitude + pitch_comp, 2)
        angs.append([y, r, p])

    my_dog.head_move_raw(angs, speed=speed)
    my_dog.wait_all_done()

def think(my_dog, pitch_comp=0):
    h_l = [
        [20, -15, 15+pitch_comp]
    ]

    my_dog.head_move_raw(h_l, speed=80)
    my_dog.wait_all_done()


def recall(my_dog, pitch_comp=0):
    h_l = [
        [-20, 15, 15+pitch_comp]
    ]

    my_dog.head_move_raw(h_l, speed=80)
    my_dog.wait_all_done()


def head_down_left(my_dog, pitch_comp=0):
    h_l = [
        [25, 0, -35+pitch_comp]
    ]

    my_dog.head_move_raw(h_l, speed=80)
    my_dog.wait_all_done()


def head_down_right(my_dog, pitch_comp=0):
    h_l = [
        [-25, 0, -35+pitch_comp]
    ]

    my_dog.head_move_raw(h_l, speed=80)
    my_dog.wait_all_done()

def fluster(my_dog, pitch_comp=0):
    h_l = [
        [-10, 0, pitch_comp],
        [0, 0, pitch_comp],
        [10, 0, pitch_comp],
        [0, 0, pitch_comp],
    ]

    # current_legs = list.copy(my_dog.leg_current_angles)
    current_legs = [30, 60, -30, -60, 80, -45, -80, 45]
    L1 = list.copy(current_legs)
    L2 = list.copy(current_legs)
    L1[0] += 10
    L1[1] -= 25
    L2[2] -= 10

    leg1 = [
        L1,
        L1,
        L2,
        L2,
    ]

    for _ in range(5):
        # my_dog.legs_move(leg1, immediately=False, speed=100)
        my_dog.head_move_raw(h_l, speed=100)
        my_dog.wait_all_done()

def alert(my_dog, pitch_comp=0):
    legs_angs = [
        [30, 50, -30, -50, 80, -45, -80, 45],
        [30, 60, -30, -60, 88, -45, -88, 45],
    ]
    head_angs = [
        [0, 0, -5+pitch_comp],
        [0, 0, 10+pitch_comp]
    ]
    my_dog.legs_move(legs_angs, immediately=False, speed=100)
    my_dog.head_move_raw(head_angs, immediately=False, speed=100)
    my_dog.wait_all_done()

    my_dog.head_move_raw([[30, 0, pitch_comp]], speed=100)
    my_dog.wait_all_done()
    sleep(1)
    my_dog.head_move_raw([[-30, 0, pitch_comp]], speed=100)
    my_dog.wait_all_done()
    sleep(1)

    my_dog.head_move_raw([[0, 0, pitch_comp]], speed=100)
    my_dog.wait_all_done()


def surprise(my_dog, pitch_comp=0, status='sit'):
    if status == 'sit':
        legs_angs = [
            [30, 50, -30, -50, 80, -45, -80, 45],
            [30, 80, -30, -80, 88, -45, -88, 45],
        ]
        head_angs = [
            [0, 0, -5+pitch_comp],
            [0, 0, 10+pitch_comp]
        ]
        my_dog.legs_move(legs_angs, immediately=False, speed=100)
        my_dog.head_move_raw(head_angs, immediately=False, speed=100)
        my_dog.wait_all_done()

        sleep(1)

        my_dog.legs_move([[30, 60, -30, -60, 80, -45, -80, 45]], immediately=False, speed=80)
        my_dog.head_move_raw([[0, 0, pitch_comp]], immediately=False, speed=80)
        my_dog.wait_all_done()

    elif status == 'stand':
        legs_angs = [
            [40, 10, -40, -10, 60, -5, -60, 5],
            [40, 25, -40, -25, 60, 0, -60, 0],
        ]
        head_angs = [
            [0, 0, pitch_comp],
            [0, 0, 10+pitch_comp]
        ]
        my_dog.legs_move(legs_angs, immediately=False, speed=80)
        my_dog.head_move_raw(head_angs, immediately=False, speed=80)
        my_dog.wait_all_done()

        sleep(1)

        my_dog.legs_move([[40, 15, -40, -15, 60, 5, -60, -5]], immediately=False, speed=80)
        my_dog.head_move_raw([[0, 0, pitch_comp]], immediately=False, speed=80)
        my_dog.wait_all_done()


def stretch(my_dog):

    head_angs = [
        [0, 0, 25],
    ]
    leg_angs = [
        [-80, 70, 80, -70, -20, 64, 20, -64],
        [-80, 70, 80, -70, -20, 64, 20, -64],
        [-65, 70, 65, -70, -20, 64, 20, -64],
        [-80, 70, 80, -70, -20, 64, 20, -64],
        [-65, 70, 65, -70, -20, 64, 20, -64],
    ]

    my_dog.legs_move(leg_angs, immediately=False, speed=55)
    my_dog.head_move_raw(head_angs, immediately=False, speed=55)
    my_dog.wait_all_done()
    sleep(.3)
    _2_sit_angs = [
        [40, 35, -40, -35, 60, 5, -60, -5],
        [30, 60, -30, -60, 80, -45, -80, 45]
    ]
    my_dog.legs_move(_2_sit_angs, immediately=False, speed=68)
    my_dog.head_move_raw([[0, 0, -35]], immediately=False, speed=68)
    my_dog.wait_all_done()

if __name__ == "__main__":
    from pidog import Pidog
    import readchar

    yrp = [0, 0, -40]
    my_dog = Pidog()
    my_dog.rgb_strip.set_mode('listen', 'cyan', 1)
    my_dog.do_action('sit', speed=80)
    my_dog.head_move_raw([[0, 0, -25]], immediately=False, speed=68)
    my_dog.wait_all_done()
    sleep(.5)
    
    # scratch(my_dog)
    # my_dog.close()

    # while True:
    #     # my_dog.do_action('lie', speed=80)
    #     my_dog.do_action('sit', speed=80)
    #     sleep(2)
    #     sit_2_stand(my_dog, 75)
    #     sleep(2)

    # # --- nod ---
    # while True:
    #     nod(my_dog, pitch_comp=-35, amplitude=30, step=2, speed=95)
    #     # break
    #     sleep(2)

    # # --- think ---
    # while True:
    #     # my_dog.do_action('tilting_head_left', speed=50)
    #     think(my_dog, -30)
    #     # break
    #     sleep(2)

    # # --- recall ---
    # while True:
    #     # my_dog.do_action('tilting_head_left', speed=50)
    #     recall(my_dog, -30)
    #     # break
    #     sleep(2)


    # # --- head_down_left ---
    # while True:
    #     # my_dog.do_action('tilting_head_left', speed=50)
    #     head_down_left(my_dog, -30)
    #     # break
    #     sleep(2)

    # # --- head_down_right---
    # while True:
    #     # my_dog.do_action('tilting_head_left', speed=50)
    #     head_down_right(my_dog, -30)
    #     # break
    #     sleep(2)

    # # --- shake_head ---
    # while True:
    #     # my_dog.do_action('shake_head', speed=50)
    #     # shake_head(my_dog)
    #     shake_head_smooth(my_dog, pitch_comp=-35, amplitude=20, speed=95)
    #     # break
    #     sleep(2)

    # --- relax_neck ---
    # while True:
    #     # my_dog.do_action('nod_lethargy', speed=50)
    #     relax_neck(my_dog)
    #     # break
    #     sleep(2)


    # # --- fluster ---
    # while True:
    #     # my_dog.do_action('nod_lethargy', speed=50)
    #     fluster(my_dog, pitch_comp=-35)
    #     # break
    #     sleep(2)

    # --- surprise ---
    # while True:
    #     # my_dog.do_action('nod_lethargy', speed=50)
    #     # surprise(my_dog, pitch_comp=-35, status='sit')
    #     surprise(my_dog, pitch_comp=0, status='stand')
    #     # break
    #     sleep(2)


    # # --- stretch ---
    # while True:
    #     stretch(my_dog)
    #     # break
    #     sleep(2)

    # --- alert ---
    # while True:
    #     alert(my_dog, pitch_comp=-35)
    #     # break
    #     sleep(2)


