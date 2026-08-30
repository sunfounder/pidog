from pidog import Pidog

# init
# =================================================================
my_dog = Pidog()

# rgb color
# =================================================================
rgb_colors = [
    [255,   0,   0], # 0
    [255,  69,   0], # 1
    [255, 165,   0], # 2
    [255, 255,   0], # 3
    [173, 255,  47], # 4
    [  0, 255,   0], # 5
    [  0, 128,   0], # 6
    [ 64, 224, 208], # 7
    [  0, 255, 255], # 8
    [138,  43, 226], # 9
    [255,  20, 147], # 10 	
]
# stop rgb thread
my_dog.rgb_thread_run = False
my_dog.rgb_strip_thread.join()

my_dog.rgb_strip.display(rgb_colors)

# pose
# =================================================================
f_up = [
    # [30, 60, -20, 65, 80, -45, -80, 38],  # Note 1
    [30, 60, -15, 5, 80, -45, -80, 38],
]
# f_handshake = [
#     [30, 60, 10, -25, 80, -45, -80, 38],  # Note 1
#     [30, 60, 10, -35, 80, -45, -80, 38],  # Note 1
# ]
# f_withdraw = [
#     [30, 60, -40, 30, 80, -45, -80, 38],  # Note 1
# ]
my_dog.head_move([[-25, 20, 0]], pitch_comp=-20)
my_dog.legs_move(f_up, immediately=False, speed=80)
my_dog.wait_all_done()

# for _ in range(5):
#     my_dog.legs_move(f_handshake, immediately=False, speed=90)
#     my_dog.wait_all_done()

# my_dog.legs_move(f_withdraw, immediately=False, speed=80)
# my_dog.do_action('sit', speed=80)
# my_dog.wait_all_done()