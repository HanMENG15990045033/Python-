# # 15.4 Pygal 矢量图
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
# die = Die()
# # 掷几次骰子，将结果储存在一个列表中
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
#
# print(results)
#
# # 对结果进行统计
# frequencies = []
# for value in range(1, die.num_sides+1):## [1, 7)
#     frequency = results.count(value)
#     ## count, 查results这个列表里有多少个value
#     frequencies.append(frequency)
# # print(frequencies)
#
# # 对结果进行可视化
# hist = pygal.Bar()
#
# hist.title = "Results of rolling one D6 1000 times."
# hist.x_lables = ['1', '2', '3', '4', '5', '6']
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"
#
# hist.add('D6', frequencies)
# hist.render_to_file('die_visual_2.svg')
# ## 生成svg格式的文件，用网页浏览器打开

# # 15.4.7 同时掷两个
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
# die_2 = Die()
# # 掷几次骰子，将结果储存在一个列表中
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
#
#
# # 对结果进行统计
# frequencies = []
#
# max_result = die_1.num_sides + die_2.num_sides ## 6+6=12
# for value in range(2, max_result+1):## [2, 13)
#     frequency = results.count(value)
#     frequencies.append(frequency)
# # print(frequencies)
#
# # 对结果进行可视化
# hist = pygal.Bar()
#
# hist.title = "Results of rolling two D6 1000 times."
# hist.x_lables = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"
#
# hist.add('D6 + D6', frequencies) ##y轴列表加进去
# hist.render_to_file('die_visual_3.svg')
## 生成svg格式的文件，用网页浏览器打开

# 15.4.8 同时掷两个面数不同的骰子

import pygal
from random import randint
class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认为6个面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)

die_1 = Die()
die_2 = Die(10)
# 掷几次骰子，将结果储存在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# 对结果进行统计
frequencies = []

max_result = die_1.num_sides + die_2.num_sides ## 6+6=12
for value in range(2, max_result+1):## [1, 13)
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_lables = ['2', '3', '4', '5', '6', '7', '8', '9',
                 '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual_4.svg')
## 生成svg格式的文件，用网页浏览器打开