# 16.1 CSV 这可怎么搞，上来就卡住了吗

# ## Comma Separated Values逗号分隔值
#
# # 16.1.1 分析CSV文件头 就是读一下
#
# import csv
#
# filename = 'zichuang.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     ## next()调用一次读一行，作为列表
#     print(header_row)
#
#     header_row = next(reader)
#     print(header_row)
#
#     header_row = next(reader)
#     print(header_row)
# #
# # 16.1.2 打印文件头及其位置
#
# import csv
#
# filename = 'zichuang.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     ## next()调用一次读一行，作为列表
#     print(header_row)
#
#     for index, column_header in enumerate(header_row):
#         ## 对列表调用函数，索引和元素提出来
#         print(index, column_header)

# # 16.1.3 提取并读取数据
#
# import csv
#
# filename = 'zichuang.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     ## next()调用一次读一行，作为列表
#
#     highs = []
#     for row in reader:
#         highs.append(row[1])
#
#     print(highs)

## 字符串转换为数字
#
# import csv
#
# filename = '16_2.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     ## next()调用一次读一行，作为列表
#
#     highs = []
#     for row in reader:
#         high = int(row[1])
#         highs.append(high)
#
#     print(highs)
# #
# # 16.1.4 绘制图表
# import csv
# from matplotlib import pyplot as plt
#
# ## 先获取数字
# filename = '16_2.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     ## next()调用一次读一行，作为列表
#
#     highs = []
#     for row in reader:
#         high = int(row[1])
#         highs.append(high)
#
#     print(highs)
#
# ## 绘制图像
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(highs, c='red')
#
# plt.title("Xia Da De", fontsize=40)
# plt.xlabel('', fontsize=20)
# plt.ylabel("Temperature(F)", fontsize=20)
# plt.tick_params(axis='both', which='major', labelsize=20)
# ## which 有三个参数，major显示主刻度，minor次刻度，both都显示
#
# plt.show()
#
# # 16.1.5 模块datetime，看一下strptime()的工作原理
#
# from datetime import datetime
# first_date = datetime.strptime('2019-6-3', '%Y-%m-%d')
# print(first_date)
# #
# # 16.1.6 在图表中添加日期
#
# import csv
# from matplotlib import pyplot as plt
# from datetime import datetime
#
# filename = '16_4.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     dates, highs = [], [] ## 定义两个空列表，还有这种骚操作
#     for row in reader:
#         current_date = datetime.strptime(row[0], "%Y/%m/%d")
#         dates.append(current_date) ## 把第一列提出来
#         high = int(row[1])
#         highs.append(high)
#
#
# ## 绘制图像
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red') ## 加入，dates
#
# plt.title("Xia Da De", fontsize=40)
# plt.xlabel('', fontsize=20)
#
# fig.autofmt_xdate() ## 让x轴的刻度日期斜着写
#
# plt.ylabel("Temperature(F)", fontsize=20)
# plt.tick_params(axis='both', which='major', labelsize=20)
# ## which 有三个参数，major显示主刻度，minor次刻度，both都显示
#
# plt.show()

## 涵盖更长的时间 我不搞了 没数据
#
# # 16.1.8 在加一列数呗
#
# import csv
# from matplotlib import pyplot as plt
# from datetime import datetime
#
# filename = '16_6.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     dates, highs, lows = [], [], [] ## 定义三个空列表，还有这种骚操作
#     for row in reader:
#         current_date = datetime.strptime(row[0], "%Y/%m/%d")
#         dates.append(current_date)
#
#         high = int(row[1])
#         highs.append(high)
#
#         low = int(row[2])
#         lows.append(low)
#
#
# ## 绘制图像
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red')
# plt.plot(dates, lows, c='blue') ## 在加一条线
#
# plt.title("Xia Da De", fontsize=40)
# plt.xlabel('', fontsize=20)
#
# fig.autofmt_xdate() ## 让x轴的刻度日期斜着写
#
# plt.ylabel("Temperature(F)", fontsize=20)
# plt.tick_params(axis='both', which='major', labelsize=20)
# ## which 有三个参数，major显示主刻度，minor次刻度，both都显示
#
# plt.show()
# #
# # 16.1.9 给图表区绘制颜色
#
# import csv
# from matplotlib import pyplot as plt
# from datetime import datetime
#
# filename = '16_7.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     dates, highs, lows = [], [], [] ## 定义三个空列表，还有这种骚操作
#     for row in reader:
#         current_date = datetime.strptime(row[0], "%Y/%m/%d")
#         dates.append(current_date)
#
#         high = int(row[1])
#         highs.append(high)
#
#         low = int(row[2])
#         lows.append(low)
#
#
# ## 绘制图像
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red', alpha=0.5) ## 加alpha指定透明度
# plt.plot(dates, lows, c='blue', alpha=0.5)
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#
# plt.title("Xia Da De", fontsize=40)
# plt.xlabel('', fontsize=20)
#
# fig.autofmt_xdate() ## 让x轴的刻度日期斜着写
#
# plt.ylabel("Temperature(F)", fontsize=20)
# plt.tick_params(axis='both', which='major', labelsize=20)
# ## which 有三个参数，major显示主刻度，minor次刻度，both都显示
#
# plt.show()

# 16.1.10 错误检查

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = '16_8.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], [] ## 定义三个空列表，还有这种骚操作
    for row in reader:
        # current_date = datetime.strptime(row[0], "%Y/%m/%d")
        # high = int(row[1])
        # low = int(row[2])
        #
        # dates.append(current_date)
        # highs.append(high)
        # lows.append(low)
        try:
            current_date = datetime.strptime(row[0], "%Y/%m/%d")
            high = int(row[1])
            low = int(row[2])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)



## 绘制图像
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5) ## 加alpha指定透明度
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Xia Da De", fontsize=40)
plt.xlabel('', fontsize=20)

fig.autofmt_xdate() ## 让x轴的刻度日期斜着写

plt.ylabel("Temperature(F)", fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
## which 有三个参数，major显示主刻度，minor次刻度，both都显示

plt.show()
