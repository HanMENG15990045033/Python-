# # 15.2 简单的折线图
# import matplotlib.pyplot as plt
# ## 导入pyplot命名为plt
#
# squares = [1, 4, 9, 16, 25]
# ## 建个列表储存平方数,纵坐标值
# plt.plot(squares)
# ## 传递给函数plot，横坐标默认 0,1,2,3,4
# plt.show()
# ## 将图像显示出来，查看器可以缩放，可以保存

# # 15.2.1 题目横纵坐标字体格式
# import matplotlib.pyplot as plt
# ## 导入pyplot命名为plt
#
# squares = [1, 4, 9, 16, 25]
# plt.plot(squares, linewidth=5)
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# ## 标题，xy坐标轴
#
# plt.tick_params(axis='both', labelsize=15)
# ## 刻度标记的大小
#
# plt.show()
#
# # 15.2.2 x轴设定
# import matplotlib.pyplot as plt
# ## 导入pyplot命名为plt
#
# input_values = [1, 2, 3, 4, 5]
# ## 设置横坐标值
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5)
# ## 横纵坐标对应
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# ## 标题，xy坐标轴
#
# plt.tick_params(axis='both', labelsize=15)
# ## 刻度标记的大小
#
# plt.show()

# # 15.2.3 散点图一个点
# import matplotlib.pyplot as plt
#
# plt.scatter(2, 4, s=200)
# ## x=2, y=4, 型号200
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # 标题，xy坐标轴
#
# plt.tick_params(axis='both', which='major', labelsize=15)
# ## 刻度标记的大小  ？？
#
# plt.show()

# # 15.2.4 散点图多个点
# import matplotlib.pyplot as plt
#
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=200)
#
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# ## 标题，xy坐标轴
#
# plt.tick_params(axis='both', which='major', labelsize=15)
# ## 刻度标记的大小，which=major是啥意思
#
# plt.show()
#
# # 15.2.5 自动计算数据
# import matplotlib.pyplot as plt
#
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, s=40)
# ## 还是散点图，绘制1000个点
#
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# ## 标题，xy坐标轴
#
# plt.tick_params(axis='both', which='major', labelsize=15)
# ## 刻度标记的大小，which=major是啥意思
#
# plt.axis([0, 1100, 0, 1100000])
# ## xy取值区间
#
# plt.show()

# # 15.2.6 删除据点的轮廓
# import matplotlib.pyplot as plt
#
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, edgecolors='none', s=40)
# ## 设置轮廓为无，这没看出来有啥作用，就变细了一点点
#
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# ## 标题，xy坐标轴
#
# plt.tick_params(axis='both', which='major', labelsize=15)
# ## 刻度标记的大小，which=major是啥意思
#
# plt.axis([0, 1100, 0, 1100000])
# ## xy取值区间
#
# plt.show()
#
# # 15.2.7 自定义点的颜色
# import matplotlib.pyplot as plt
#
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# # plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
# plt.scatter(x_values, y_values, c=(0.9, 0.5, 0.7), edgecolors='none', s=40)
# ## 颜色设置，注意0-1之间的小数
#
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# ## 标题，xy坐标轴
#
# plt.tick_params(axis='both', which='major', labelsize=15)
# ## 刻度标记的大小，which=major是啥意思
#
# plt.axis([0, 1100, 0, 1100000])
# ## xy取值区间
#
# plt.show()

# # # 15.2.8 使用颜色映射
# import matplotlib.pyplot as plt
#
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# # plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, edgecolors='none', s=40)
# ## 颜色设置，注意0-1之间的小数
#
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# ## 标题，xy坐标轴
#
# plt.tick_params(axis='both', which='major', labelsize=15)
# ## 刻度标记的大小，which=major是啥意思
#
# plt.axis([0, 1100, 0, 1100000])
# ## xy取值区间

# plt.show()

## http://matplotlib.org/
#
#
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# cmaps = [('Perceptually Uniform Sequential', [
#             'viridis', 'plasma', 'inferno', 'magma', 'cividis']),
#          ('Sequential', [
#             'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
#             'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
#             'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
#          ('Sequential (2)', [
#             'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
#             'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
#             'hot', 'afmhot', 'gist_heat', 'copper']),
#          ('Diverging', [
#             'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
#             'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
#          ('Cyclic', ['twilight', 'twilight_shifted', 'hsv']),
#          ('Qualitative', [
#             'Pastel1', 'Pastel2', 'Paired', 'Accent',
#             'Dark2', 'Set1', 'Set2', 'Set3',
#             'tab10', 'tab20', 'tab20b', 'tab20c']),
#          ('Miscellaneous', [
#             'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
#             'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
#             'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'])]
#
#
# gradient = np.linspace(0, 1, 256)
# gradient = np.vstack((gradient, gradient))
#
#
# def plot_color_gradients(cmap_category, cmap_list):
#     # Create figure and adjust figure height to number of colormaps
#     nrows = len(cmap_list)
#     figh = 0.35 + 0.15 + (nrows + (nrows-1)*0.1)*0.22
#     fig, axes = plt.subplots(nrows=nrows, figsize=(6.4, figh))
#     fig.subplots_adjust(top=1-.35/figh, bottom=.15/figh, left=0.2, right=0.99)
#
#     axes[0].set_title(cmap_category + ' colormaps', fontsize=14)
#
#     for ax, name in zip(axes, cmap_list):
#         ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
#         ax.text(-.01, .5, name, va='center', ha='right', fontsize=10,
#                 transform=ax.transAxes)
#
#     # Turn off *all* ticks & spines, not just the ones with colormaps.
#     for ax in axes:
#         ax.set_axis_off()
#
#
# for cmap_category, cmap_list in cmaps:
#     plot_color_gradients(cmap_category, cmap_list)
#
# plt.show()

# 15.2.9 自动保存列表

# plt.show 替换为
# plt.savefig('squares_plot.png', bbox_inches='tight')
# 保存位置：py文件所在目录，名字格式，去掉周围空白区域

# 15.3 随机漫步 模拟现实中的很多情形
import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=500):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表到达指定的长度
        while len(self.x_values) < self.num_points:

            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction* y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step ==0:
                continue
            # 计算下一个x，y得值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.spring, edgecolors='none', s=1)
    ## 之前c是点的颜色，现在c是点的个数，是个列表
    #c='red',c=(0.9, 0.5, 0.7)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=150)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=150)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    # plt.savefig('squares_plot.png', bbox_inches='tight')

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
