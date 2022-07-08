

import matplotlib.pyplot as plt
import numpy as np
from walk_cal_5_step import cal_walk_coords
from turn_left_cal import cal_turn_left_coords
from turn_right_cal_2 import cal_turn_right_coords
from backward_cal import cal_backward_coords
from new_walk3 import Walk
import readchar 

# 窗口设置
fig = plt.figure(figsize=(14, 5)) # inch
# fig.canvas.set_window_title('Walk')
fig.canvas.manager.set_window_title('Walk')
plt.title('Walk',fontsize=18)
plt.xlabel('x (mm)', fontsize=14)
plt.ylabel('y (mm)', fontsize=14)
plt.xticks(np.arange(-300, 400, step=10)) 
plt.yticks(np.arange(-100, 240, step=10))
plt.plot([-100, 240, 240, -100, -100], [-20, -20, 120, 120, -20], '-', color='blue')
plt.ion() # interactive mode

x1_o=0;x2_o=0;x3_o=0;x4_o=0;h1_o=0;h2_o=0;h3_o=0;h4_o=0
x1_s=0;x2_s=0;x3_s=0;x4_s=0;y1_s=0;y2_s=0;y3_s=0;y4_s=0

# 结构：
# 粗略测量 重心距离后腿舵盘 70 mm, 身体+头部 全长等效为 140mm 

body_l = 105 # 前后两舵盘中心的垂直距离
body_w = 95 # 躯干的宽
crotch_l = 20 # 足尖到躯干边缘的垂直距离， (105 - 65)/2 = 20
center_of_gravity = 14 # 重心离身体重心距离 
# 设：
head_w = 40  # 头部等效的body延长

stand = 80

# 躯干：
#  [3]=========[1]
#  |             |
#  |             |
#  [4]=========[2]

# 则：
# 躯干固定位置
x1 = body_l / 2
y1 = body_w / 2
x2 = body_l / 2
y2 = -body_w / 2
x3 = -body_l / 2
y3 = body_w / 2
x4 = -body_l / 2
y4 = -body_w / 2

# 画出躯干重心示意图
body_xs = [x1, x2, x4, x3, x1, x4, x3, x2]
body_ys = [y1, y2, y4, y3, y1, y4, y3, y2]
foot_ys = [y1 + crotch_l, y2-crotch_l, y3+crotch_l, y4-crotch_l]

# plt.plot(bx_o, bh_o, 'o', color='red',ls = ':')
# plt.plot([x1_o, x2_o], [h1_o, h2_o] ,color='red',ls = ':')


print('\n load forward_data ...')
# walk_datas = cal_walk_coords()
# walk_datas = cal_turn_left_coords()
# walk_datas = cal_turn_right_coords()
# walk_datas = cal_backward_coords()

forward = Walk(fb=Walk.FORWARD, lr=Walk.STRAIGHT)
backward = Walk(fb=Walk.BACKWARD, lr=Walk.STRAIGHT)
forward_left = Walk(fb=Walk.FORWARD, lr=Walk.LEFT)
forward_right = Walk(fb=Walk.FORWARD, lr=Walk.RIGHT)
walk_datas = forward.get_coords()

print('datas_len:',len(walk_datas))
print(walk_datas)


while True:
    for coords in walk_datas:

        key = readchar.readkey()
        if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            import sys
            print('')
            sys.exit(0)  
        print(coords)

        x1 = body_l / 2 - coords[0][0]
        x2 = body_l / 2 - coords[1][0]
        x3 = -body_l / 2 - coords[2][0]
        x4 = -body_l / 2 - coords[3][0]

        xs = [x1, x2, x3, x4]
        ys = [coords[0][1], coords[1][1], coords[2][1], coords[3][1]]
        plot_xs = []
        plot_ys = []
        for i in (0,1,3,2):  
            if ys[i] == stand:
                plot_xs.append(xs[i])
                plot_ys.append(foot_ys[i])
        plot_xs.append(plot_xs[0])
        plot_ys.append(plot_ys[0])

        plt.clf()
        # 定款，防止画面乱动
        plt.plot([-150, 150], [-100, -100], 'o', color='yellow', ls = '-')
        # 躯干
        plt.plot(body_xs, body_ys, 'o', color='red',ls = ':')
        # 重心
        plt.plot([center_of_gravity], [0], 'o', color='green',ls = ':')
        # 步态
        plt.plot(plot_xs, plot_ys, 'o', color='blue', ls = '-.')

        plt.gca().set_aspect('equal', adjustable='box')
        plt.pause(0.05)
        





# plt.show()

# %%
