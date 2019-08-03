# # 习题15-1 立方 指定颜色
# import matplotlib.pyplot as plt
#
# x_values = list(range(1, 5001))
# y_values = [x**3 for x in x_values]
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Paired, edgecolors='none', s=40)
#
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# ## 标题，xy坐标轴
#
# plt.tick_params(axis='both', which='major', labelsize=15)
# # plt.axis([0, 6, 0, 140])
# plt.axis([0, 5100, 0, 130000000000])
# plt.show()


# # 15-3 15-4
# import matplotlib.pyplot as plt
# from random import choice
#
# class RandomWalk():
#     """一个生成随机漫步数据的类"""
#
#     def __init__(self, num_points=5000):
#         """初始化随机漫步的属性"""
#         self.num_points = num_points
#
#         # 所有随机漫步都始于（0，0）
#         self.x_values = [0]
#         self.y_values = [0]
#
#     def fill_walk(self):
#         """计算随机漫步包含的所有点"""
#
#         # 不断漫步，直到列表到达指定的长度
#         while len(self.x_values) < self.num_points:
#
#             # 决定前进方向以及沿这个方向前进的距离
#             x_direction = 1
#             # x_direction = choice([1, -1])
#             x_distance = choice([0, 1, 2, 3, 4])
#             x_step = x_direction * x_distance
#
#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
#             y_step = y_direction* y_distance
#
#             # 拒绝原地踏步
#             if x_step == 0 and y_step ==0:
#                 continue
#             # 计算下一个x，y得值
#             next_x = self.x_values[-1] + x_step
#             next_y = self.y_values[-1] + y_step
#
#             self.x_values.append(next_x)
#             self.y_values.append(next_y)
#
# while True:
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     # 设置绘图窗口的尺寸
#     plt.figure(figsize=(10, 6))
#
#     point_numbers = list(range(rw.num_points))
#     plt.plot(rw.x_values, rw.y_values, c='green')
#     ## 之前c是点的颜色，现在c是点的个数，是个列表
#     #c='red',c=(0.9, 0.5, 0.7)
#
#     # 突出起点和终点
#     plt.plot(0, 0, c='green')
#     plt.plot(rw.x_values[-1], rw.y_values[-1], c='blue')
#
#     # 隐藏坐标轴
#     plt.axes().get_xaxis().set_visible(False)
#     plt.axes().get_yaxis().set_visible(False)
#
#     plt.show()
#     # plt.savefig('squares_plot.png', bbox_inches='tight')
#
#     keep_running = input("Make another walk?(y/n):")
#     if keep_running == 'n':
#         break
# #
# # 15-5 重构
# import matplotlib.pyplot as plt
# from random import choice
#
# class RandomWalk():
#     """一个生成随机漫步数据的类"""
#
#     def __init__(self, num_points=5000):
#         """初始化随机漫步的属性"""
#         self.num_points = num_points
#
#         # 所有随机漫步都始于（0，0）
#         self.x_values = [0]
#         self.y_values = [0]
#
#     def fill_walk(self):
#         """计算随机漫步包含的所有点"""
#
#         # 不断漫步，直到列表到达指定的长度
#         while len(self.x_values) < self.num_points:
#             x_step = self.get_step()
#             y_step = self.get_step()
#
#             # 拒绝原地踏步
#             if x_step == 0 and y_step ==0:
#                 continue
#             # 计算下一个x，y得值
#             next_x = self.x_values[-1] + x_step
#             next_y = self.y_values[-1] + y_step
#
#             self.x_values.append(next_x)
#             self.y_values.append(next_y)
#
#     def get_step(self):
#         direction = choice([1, -1])
#         distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
#         step = direction * distance
#         return step
#
#
# while True:
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     # 设置绘图窗口的尺寸
#     plt.figure(figsize=(10, 6))
#
#     point_numbers = list(range(rw.num_points))
#     plt.plot(rw.x_values, rw.y_values, c='green')
#     ## 之前c是点的颜色，现在c是点的个数，是个列表
#     #c='red',c=(0.9, 0.5, 0.7)
#
#     # 突出起点和终点
#     plt.plot(0, 0, c='green')
#     plt.plot(rw.x_values[-1], rw.y_values[-1], c='blue')
#
#     # 隐藏坐标轴
#     plt.axes().get_xaxis().set_visible(False)
#     plt.axes().get_yaxis().set_visible(False)
#
#     plt.show()
#     # plt.savefig('squares_plot.png', bbox_inches='tight')
#
#     keep_running = input("Make another walk?(y/n):")
#     if keep_running == 'n':
#         break


# # 15-6 自动生成标签 x值改为循环，for循环替换为列表解析
#
# # #列表解析，直接上
# # squares=[value**2 for value in range(1,11)]
# # print(squares)
#
# import pygal
# from random import randint
# class Die():
#     """表示一个骰子的类"""
#
#     def __init__(self, num_sides=6):
#         """骰子默认为6个面"""
#         self.num_sides = num_sides
#
#     def roll(self):
#         """返回一个位于1和骰子面数之间的随机值"""
#         return randint(1, self.num_sides)
#
# die_1 = Die()
# die_2 = Die(10)
# # 掷几次骰子，将结果储存在一个列表中
# # results = []
# # for roll_num in range(50000):
# #     result = die_1.roll() + die_2.roll()
# #     results.append(result)
# results = [die_1.roll()+die_2.roll() for roll_num in range(5000)]
# print(results)
#
# # 对结果进行统计
#
# max_result = die_1.num_sides + die_2.num_sides ## 6+6=12
# # for value in range(2, max_result+1):## [1, 13)
# #     frequency = results.count(value)
# #     frequencies.append(frequency)
# frequencies = [results.count(value) for value in range(2, max_result+1)]
# print(frequencies)
#
# # 对结果进行可视化
# hist = pygal.Bar()
#
# hist.title = "Results of rolling a D6 and a D10 50,000 times."
#
# hist.x_lables = []
# for x in range(2, 17):
#     hist.x_lables.append(x)
# print(hist.x_lables)
#
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"
#
# hist.add('D6 + D10', frequencies)
# hist.render_to_file('die_visual_4.svg')

# # 15-7 两个D8骰子
#
# import pygal
# from random import randint
# class Die():
#     """表示一个骰子的类"""
#
#     def __init__(self, num_sides=6):
#         """骰子默认为6个面"""
#         self.num_sides = num_sides
#
#     def roll(self):
#         """返回一个位于1和骰子面数之间的随机值"""
#         return randint(1, self.num_sides)
#
# die_1 = Die(8)
# die_2 = Die(8)
#
# results = [die_2.roll()+die_2.roll() for roll_num in range(500000)]
# print(results)
#
# max_result = die_1.num_sides + die_2.num_sides ## 8+8=16
# frequencies = [results.count(value) for value in range(2, max_result+1)]
#
#
# hist = pygal.Bar()
#
# hist.title = "Results of rolling a D6 and a D10 50,000 times."
#
# hist.x_lables = [x for x in range(2, max_result+1)]
#
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"
#
# hist.add('D8 + D8', frequencies)
# hist.render_to_file('die_visual_7.svg')

# # 15-8 三个D6
# import pygal
# from random import randint
# class Die():
#     """表示一个骰子的类"""
#
#     def __init__(self, num_sides=6):
#         """骰子默认为6个面"""
#         self.num_sides = num_sides
#
#     def roll(self):
#         """返回一个位于1和骰子面数之间的随机值"""
#         return randint(1, self.num_sides)
#
# die_1 = Die(6)
# die_2 = Die(6)
# die_3 = Die(6)
#
# results = [die_1.roll()+die_2.roll()+die_3.roll() for roll_num in range(500000)]
#
# max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides ## 6+6+6=18
# frequencies = [results.count(value) for value in range(3, max_result+1)]
#
#
# hist = pygal.Bar()
#
# hist.title = "Results of rolling a D6 and a D10 50,000 times."
#
# hist.x_lables = [x for x in range(3, max_result+1)]
#
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"
#
# hist.add('D6 + D6 + D6', frequencies)
# hist.render_to_file('die_visual_8.svg')

# # 15-9 点数相乘
# import pygal
# from random import randint
# class Die():
#     """表示一个骰子的类"""
#
#     def __init__(self, num_sides=6):
#         """骰子默认为6个面"""
#         self.num_sides = num_sides
#
#     def roll(self):
#         """返回一个位于1和骰子面数之间的随机值"""
#         return randint(1, self.num_sides)
#
# die_1 = Die(6)
# die_2 = Die(6)
#
#
# results = [die_1.roll()*die_2.roll() for roll_num in range(5000)]
# result_possible = []
# for n in range(1, die_1.num_sides+1): # [1, 7)
#     for m in range (1, die_2.num_sides+1): # [1.7)
#         if n*m not in result_possible:
#             result_possible.append(n*m)
#
# print(result_possible)
# result_possible.sort()
# print(result_possible)
#
# frequencies = [results.count(value) for value in result_possible]
#
#
# hist = pygal.Bar()
#
# hist.title = "Results of rolling a D6 and a D10 50,000 times."
#
# hist.x_lables = result_possible
#
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"
#
# hist.add('D6 * D6', frequencies)
# hist.render_to_file('die_visual_9.svg')
#
# ## 计算一下不同结果的概率
# result_possible_2 = []
# for n in range(1, die_1.num_sides+1): # [1, 7)
#     for m in range(1, die_2.num_sides+1): # [1.7)
#             result_possible_2.append(n*m)
#
# p = [result_possible_2.count(value) for value in result_possible]
# print(p)
# ## 可能的结果，总体中出现的次数，如36个可能的结果中，1出现1次，6出现4次

# 5-10 用matplotlib掷骰子，用pygal做随机漫步

## 用matplotlib做柱状图
#
# import matplotlib.pyplot as plt
# from random import randint
#
# class Die():
#     """表示一个骰子的类"""
#
#     def __init__(self, num_sides=6):
#         """骰子默认为6个面"""
#         self.num_sides = num_sides
#
#     def roll(self):
#         """返回一个位于1和骰子面数之间的随机值"""
#         return randint(1, self.num_sides)
#
# die_1 = Die()
# die_2 = Die(10)
# # 掷几次骰子，将结果储存在一个列表中
#
# results = [die_1.roll()+die_2.roll() for roll_num in range(5000)]
#
# # 对结果进行统计
# frequencies = []
#
# max_result = die_1.num_sides + die_2.num_sides ## 6+6=12
#
# frequencies = [results.count(value) for value in range(2, max_result+1)]
# print(frequencies)
#
# plt.bar(range(2, max_result+1), frequencies)
#
# plt.show()
#

## 用pygal做随机漫步

import pygal
from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=500):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于（0，0）
        self.values = []
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表到达指定的长度
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step ==0:
                continue
            # 计算下一个x，y得值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            self.values.append((next_x, next_y))

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

rw = RandomWalk()
rw.fill_walk()

sandiantu = pygal.XY(stroke=False)

sandiantu.title = "Results of random walk."

sandiantu.add('A', rw.values)
sandiantu.render_to_file('random_walk_2.svg')
print(rw.values)