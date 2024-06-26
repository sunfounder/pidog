
from time import sleep
import random

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

    for _ in range(5):
        my_dog.legs_move(f_handshake, immediately=False, speed=90)
        my_dog.wait_all_done()

    my_dog.legs_move(f_withdraw, immediately=False, speed=80)
    my_dog.do_action('sit', speed=80)
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
    my_dog.do_action('sit', speed=80)
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

    my_dog.do_action('sit', speed=80)
    my_dog.head_move([[0, 0, -40]], speed=80)
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
    # leg1 =  [
    #     [40, 35, -30, -60, 80, -45, -80, 45],
    #     [40, 35, -30, -60, 80, -45, -80, 45],

    #     [30, 60, -40, -35, 80, -45, -80, 45],
    #     [30, 60, -40, -35, 80, -45, -80, 45],
    # ]
    # leg2 =  [
    #     [40, 35, -30, -60, 80, -45, -80, 45],
    #     [30, 60, -30, -60, 80, -45, -80, 45],
    # ]
    # leg3 =  [
    #     [30, 60, -40, -35, 80, -45, -80, 45],
    #     [30, 60, -30, -60, 80, -45, -80, 45],
    # ]
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

    # my_dog.do_action('sit', speed=60)
    # my_dog.head_move([[0, 0, -40]], speed=80)
    # my_dog.wait_all_done()

    for _ in range(step):
        my_dog.legs_move(legs_action, immediately=False, speed=45)
        my_dog.wait_legs_done()

    # my_dog.legs_move([current_legs], immediately=False, speed=45)
    # my_dog.wait_legs_done()

    my_dog.do_action('sit', speed=60)
    my_dog.head_move([[0, 0, -40]], speed=80)
    my_dog.wait_all_done()

    
def sit_2_stand(my_dog, speed=75):

    sit_angles = my_dog.actions_dict['sit'][0][0]
    stand_angles = my_dog.actions_dict['stand'][0][0]

    # for i, x in enumerate(sit_angles):
    #     sit_angles[i] = round(x, 2)
    # for i, x in enumerate(stand_angles):
    #     stand_angles[i] = round(x, 2)

    # print(f'sit: {sit_angles}')
    # print(f'stand: {stand_angles}')

    # sit = [30, 60, -30, -60, 80, -45, -80, 45]
    # stand = [40.61, 15.54, -40.61, -15.54, 60.28, 5.26, -60.28, -5.26]

    L1 = [25, 25, -25, -25, 70, -25, -70, 25]

    # L1 = [30, 35, -35, -35, 70, -25, -70, 25]

    legs_action = [
        # sit_angles,
        L1,
        stand_angles,
    ]
    
    my_dog.legs_move(legs_action, immediately=False, speed=speed)
    my_dog.wait_legs_done()


if __name__ == "__main__":
    from pidog import Pidog
    import readchar

    yrp = [0, 0, -40]
    my_dog = Pidog()
    my_dog.do_action('sit', speed=80)
    # scratch(my_dog)
    # my_dog.close()

    while True:
        # my_dog.do_action('lie', speed=80)
        my_dog.do_action('sit', speed=80)
        sleep(2)
        sit_2_stand(my_dog, 75)
        sleep(2)
