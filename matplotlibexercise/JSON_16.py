# # 16.2 JSON 先解决一下
# # http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json
# # 查看数据：打开网页 列表里面套字典
#
#
# # 16.2.1 下载数据
# ## 使用urlopen
#
# from __future__ import (absolute_import, division, print_function, unicode_literals)
# ## 导入，绝对导入和相对导入？？？？
#
# try:
#     # Python 2.x 版本
#     from urllib2 import urlopen
# except ImportError:
#     # Python 3.x 版本
#     from urllib.request import urlopen
#
# import json
#
# json_url = 'http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
#
# response = urlopen(json_url)
# ## 向GitHub服务器请求，服务器将文件发给python
# req = response.read()
# # 读取数据
# with open('btc_close_2017_urllib.json','wb') as f:
#     ## wb是什么鬼
#     f.write(req)
#     ## 将数据写入文件
#
# file_urllib = json.loads(req)
# ## 再将文件转化为python能读取的形式
# print(file_urllib)


## 用requests模块下载 报错，找不到requests目前不影响，先搁置一下

import requests
sudo python printBarcodeSex.py

json_url = 'http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
# 将数据写入文件

with open('btc_close_2017_urllib_req.json','w') as f:
    f.write(req.text)
file_requests = req.json()


#
# 16.2.2 提取相关的数据
# 16.2.3 将字符串转换为数字值
#
# ## python不能将含有小数点的字符串直接转换为整数，所以str-float-int
#
# import json
# # 将数据加载到一个列表中
#
# filename = 'btc_close_2017_urllib.json'
# with open(filename) as f:
#     btc_data = json.load(f)
#     print(btc_data)
#     for n in range(len(btc_data)):
#         print(btc_data[n])
#
# for btc_dict in btc_data:
#     date = btc_dict['date']
#     month = btc_dict['month']
#     week = btc_dict['week']
#     weekday = btc_dict['weekday']
#     # close = btc_dict['close'] ## 16.2.2 直接提取出来
#     close = int(float(btc_dict['close'])) ## 16.2.3 字符串转换为整型
#
#     print("{} is month {} week {}, {}, the close price ias {}RMB".format(date, month, week, weekday, close))


# 16.2.4 绘制收盘价折线图

import json
# 将数据加载到一个列表中

filename = 'btc_close_2017_urllib.json'
with open(filename) as f:
    btc_data = json.load(f)
    # print(btc_data)
    # for n in range(len(btc_data)):
    #     print(btc_data[n])

## 创建5个空列表
dates, months, weeks, weekdays, close = [], [], [], [], []

for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(btc_dict['month'])
    weeks.append(btc_dict['week'])
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))


## x轴y轴数据都有了，下面来绘制折线图
## 其中x轴要显示346个日期？？我也不知道几个，反正要处理一下

# import pygal
#
# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# ## 让x轴上的标签顺时针旋转20度
# ## False：不显示所有的标签
# line_chart.title = '收盘价图像(￥)'
# line_chart.x_lables = dates
# N = 20 ## x轴坐标每隔20天显示一次
# line_chart.x_lables_major = dates[::N] ## 定义好x轴
# line_chart.add('收盘价', close) ## 加入y轴和这条线的名称
# line_chart.render_to_file('收盘价折线图(￥).svg') ## 保存为文件
#
# print(dates)

###!!!! 为什么不显示y轴？？！ 谁能告诉我
#
# 16.2.5 时间序列特征初探

# import pygal
# import math ## 导入模块math
#
# ## 补充一下log10函数
# a = [10, 100, 1000, 10000, 100000] ## log10的含义
# b = [math.log10(_) for _ in a] ## 将指数增长的数据，考察其数量级上的增长
# print(b)
#
# ## 为了找到周期性，观察相似波动，使用对数处理
# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# ## 标签旋转20度 不显示所有刻度
# line_chart.title = '收盘价对数变换(￥)'
# line_chart.x_labels = dates
# N = 20
# line_chart.x_lable_major = dates[::N]
# close_log = [math.log10(_) for _ in close]
# line_chart.add('log收盘价', close_log)
# line_chart.render_to_file('收盘价对数变换折线图(￥).svg')

## 趋势trend，周期性seasonality，噪声noise，描述事实，预测未来，做出决策
## 将非线性趋势消除
## 使用对数变换，log transformation
## math.log10 semi-logarithmic
## 3、6、9出现波动，预测12月出现波动

#
#
#
# 16.2.6 收盘价均值
## 参考CSDN VPointer701的博客 https://blog.csdn.net/VPointer701/article/details/80691264
## zip groupby 见 zip_groupby.py

# 总之zip就是一个列表，每个纵列做一个元组
# groupby的功能是根据某一位元素分组，生成的是一个字典，key值是分组的元素，value是对一一组的东西
import pygal
from itertools import groupby
## 导入分组，月份、周数、周几，在计算每组的平均值

## 定义一个 求 以某段为单位的平均数 的函数
def draw_line(x_data, y_data, title, y_legend):
    ## x轴 y轴 生成文件的名称 y_legend='月平局值'这种，就是线的名称
    xy_map = []
    ## 一个空列表，以后里面装的元素也是列表
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        ## zip：
        ## 将x轴与y轴合并，对应值组成元组,如：
        ## x_data = [1, 1, 2, 2]
        ## y_data = [3, 2, 4, 6]
        ## (zip(x_data, y_data)=[(1,3), (1,2),(2,4),(2,6)]
        ## 排序：
        ## sorted(zip(x_data, y_data))
        ## [(1,2), (1,3),(2,4),(2,6)]
        ## groupby：
        ## key=lambda _: _[0] 分组按0位元素分组，得到一个字典
        ## 如 {1：[(1,2),(1,3)]，2:[(2,4),(2,6)]}
        ## for循环：
        ## x 就是字典中的key值，也就是分组的依据,x=1, x=2
        ## y就是字典中value值，也就是元组组成的这个列表
        ## y=[(1,2),(1,3)], y=[(2,4),(2,6)]
        y_list = [v for _, v in y]
        ## y里面的元素是元组(1,2),(1,3), 不要这个1，取出2,3
        ## 对于y列表里面的元素，_,对应1，v对应2，3，把v取出来
        xy_map.append([x, sum(y_list)/len(y_list)])
        ## 每一对值作为一个列表，放到xy_map中
        ## xy_map=[[1, 2.5], [2, 5]]

    x_unique, y_mean = [*zip(*xy_map)]
    ## * 解包，变成两个列表：
    ## *xy_map = [1, 2.5], [2, 5]
    ## zip 再提纵向值压缩
    ## zip(*xy_map) = [(1,2), (2.5, 5)]
    ## * 再解包
    ## *zip(*xy_map) = (1,2), (2.5, 5)
    ## 用两个值把这两个列表提取出来
    ## x_unique = (1, 2)
    ## y_mean = (2.5, 5)
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean) ## y_legend='月均值' 线的名称
    line_chart.render_to_file(title+'.svg') ## 画出来
    return line_chart

## 调用函数，求月均值
## 由于2017年12月的数据不完整，所以只取一月到十一月的数据
idx_month = dates.index('2017-12-01')
## str.index(str, beg=0, end=len(string))
## 从beg位开始，到end位结束，查找是否存在str
## 如果不设置beg，end默认0到-1
## 如果存在，返回位置索引
print(idx_month)
line_chart_month = draw_line(months[:idx_month], close[:idx_month],'收盘价月均值(￥)','月均值')
## 月份列表中切片，取从0到334
## 月份相同的会分到一组
## 收盘价列表中切片
line_chart_month
## 运行这个函数, 就会建立文件


## 2017-01-02~2017-12-10的每周均值 周一到周一

idx_week = dates.index('2017-12-11')
## 1. 按照书上做是失败的
# line_chart_week = draw_line(weeks[1:idx_week], close[1:idx_week], '收盘价周均值(￥)', '周均值')
# weeks里面的元素值字符串，sorted排序有问题

# # 2. 解决方案一: weeks里面的元素改为整型，报错
# week_int = [int(x) for x in weeks]
# line_chart_week = draw_line(week_int[1:idx_week], close[1:idx_week], '收盘价周均值(￥)', '周均值')

## 2. 解决方案二: weeks里面的元素'1'变为'01'
def sort_str_n(a):
    for x in a:
        if x == '1':
            a[a.index(x)] = '01'
        elif x == '2':
            a[a.index(x)] = '02'
        elif x == '3':
            a[a.index(x)] = '03'
        elif x == '4':
            a[a.index(x)] = '04'
        elif x == '5':
            a[a.index(x)] = '05'
        elif x == '6':
            a[a.index(x)] = '06'
        elif x == '7':
            a[a.index(x)] = '07'
        elif x == '8':
            a[a.index(x)] = '08'
        elif x == '9':
            a[a.index(x)] = '09'
sort_str_n(weeks)
# print(weeks)
line_chart_week = draw_line(weeks[1:idx_week], close[1:idx_week], '收盘价周均值(￥)', '周均值')
line_chart_month
## made！摔！终于成功了

## 星期一的均值，星期二的均值等

idx_week = dates.index('2017-12-11')
## 取值范围，从第一个周一到左后一个周日
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
# print(weekdays[1:idx_week])
# line_chart_weekday = draw_line(weekdays_int, close[1:idx_week], '收盘价星期均值(￥)', '星期均值')
## 注意这里按书上写会报错
# print(weekdays_int)
weekdays_int_str = [str(x) for x in weekdays_int]
line_chart_weekday = draw_line(weekdays_int_str, close[1:idx_week], '收盘价星期均值(￥)', '星期均值')
##
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘价星期均值(￥).svg')

# 12.6.7 dashboard 做成表盘 图表合到一起

with open('收盘价Dashboard.html','w',encoding='utf-8-sig') as html_file:
# with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><metacharset="utf-8"></head><body>\n')
    for svg in [
        '收盘价折线图(￥).svg', '收盘价对数变换折线图(￥).svg', '收盘价月均值(￥).svg', '收盘价周均值(￥).svg', '收盘价星期均值(￥).svg'
    ]:
        html_file.write('   <object type="image/svg+xml" data="{0}"height=500></object>\n'.format(svg))
        html_file.write('</body><html>')