# 17.1.2 网址输入IE
# github https://github.com/explore 看一眼
# http://api.github.com/search/repositories?q=language:python&sort=stars
## http://api.github.com/ 请求发送
## search/repositories 让API搜索GitHub上所有的仓库
## ? 传递一个实参
## q= 查询
## language:python 主语言为python的仓库信息
## &sort=stars 指定项目按星级排序

# # 17.1.3 安装requests
#
# # 17.1.4 处理API响应
#
# import requests
# ## 导入模块
#
# url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# ## 用requests的get进行调用
# print("Status code:",r.status_code)
# ## 属性，打印status_code, 如果返回200，说明调用成功
#
# response_dict = r.json()
# ## 将API响应存储在一个变量中
# ## 方法json将信息转换为一个python字典
#
# print(response_dict.keys())
# ## 打印出字典中的key值
# ## 一共三个，items的内容巨长无比


#
# # 17.1.5 处理响应字典
#
# import requests
#
# url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:",r.status_code)
#
# response_dict = r.json()
# print("Total repositories:", response_dict['total_count'])
# ## 字典中total_count里面对应的值
#
# repo_dicts = response_dict['items']
# print("Repositories returned:",len(repo_dicts))
# ## item是取出来是一个列表，看一下这个列表的长度
#
# repo_dict = repo_dicts[0]
# ## 取出列表中第一个元素，是一个字典
# print("\nKeys:", len(repo_dict))
# ## 字典的长度，也就是key值的个数
# # for key in sorted(repo_dict.keys()):
# #     print(key)
# ## 把key值取出来，并打印
# ## 可以看一下第一个字典中大概的信息
#
# print("Selected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])

# # 17.1.6 多个库 做一个for循环
#
# import requests
#
# url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:",r.status_code)
#
# response_dict = r.json()
# print("Total repositories:", response_dict['total_count'])
#
# repo_dicts = response_dict['items']
# print("Repositories returned:",len(repo_dicts))
#
# print("Selected information about each repository:")
#
# for repo_dict in repo_dicts:
#     print('\n\nName:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Updated:', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])

# 17.1.7 监视API的速率限制
# http://api.github.com/rate_limit
# search每分钟的限制

# 17.2 使用Paygal可视化
#
# # 目标：项目，获得多少颗星，点击条形图可以进入项目在GitHub上的主页
#
# import requests
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#
#
# url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:",r.status_code)
#
# response_dict = r.json()
# print("Total repositories:", response_dict['total_count'])
#
# repo_dicts = response_dict['items']
#
# names, stars = [], []
# ## 两个空列表，很明显x轴项目名，y轴几颗星
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# my_style = LS('#333366', base_style=LCS)
# ## 定义样式，LS类，深蓝色，基本风格使用LCS
# chart = pygal.Bar(style=my_style,
#                   x_label_rotation=45
#                   ,
#                   show_legend=False)
# ## Bar创建条形图，x轴倾斜45度，隐藏图例，因为只画一套图
# chart.title = 'Most-Starred Python Projects on GitHub'
# chart.x_labels = names
#
# chart.add('', stars)
# ## 不需要标签，故为空，加入y轴数据
# chart.render_to_file('python_repos.svg')

# # 17.2.1 改进图表
# import requests
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#
#
# url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:",r.status_code)
#
# response_dict = r.json()
# print("Total repositories:", response_dict['total_count'])
#
# repo_dicts = response_dict['items']
#
# names, stars = [], []
# ## 两个
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# my_style = LS('#333366', base_style=LCS)
#
# ## 图表的个性化设置先做好
# my_config = pygal.Config()
# ## 类Config，创建一个实例
# ## 通过修改类里面的设置，可以定制图表的外观
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.title_font_size = 24
# ## 标题
# my_config.lable_font_size = 14
# ## 副标签
# my_config.major_label_font_size = 18
# ## 主标签，y轴上5000整数倍的刻度
# my_config.truncate_label = 15
# ## 较长的名目缩短为15个字符
# my_config.show_y_guides = False
# ## 隐藏图表中的水平线
# my_config.width = 1000
# ## 自定义宽度
#
# chart = pygal.Bar(my_config, style=my_style)
# chart.title = 'Most-Starred Python Projects on GitHub'
# chart.x_labels = names
#
# chart.add('', stars)
# chart.render_to_file('python_repos_2.svg')

# # 17.2.2 自定义互动
# # 就是鼠标指着条形图时，会有数字出来
# # 我们加入设置，同时显示描述
#
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#
# my_style = LS('#333366', base_style=LCS)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
#
# chart.title = 'Python Projects'
# chart.x_labels = ['heepie', 'django', 'flask']
#
# plot_dicts = [
#     {'value':16101, 'label':'Description of heepie.'},
#     {'value':15028, 'label':'Description of django'},
#     {'value':14798, 'label':'Description of flask'},
# ]
#
# chart.add('', plot_dicts)
# chart.render_to_file('bar_descriptions.svg')

# # 17.2.3 改进图表
# # 17.2.4 在图表中添加可单击的链接
# import requests
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#
#
# url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:",r.status_code)
#
# response_dict = r.json()
# print("Total repositories:", response_dict['total_count'])
#
# repo_dicts = response_dict['items']
#
# names, plot_dicts = [], []
# ## x轴还是names，y轴列表里面要装字典
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#
#     plot_dict = {
#         'value': repo_dict['stargazers_count'],
#         'label': repo_dict['description'],
#         'xlink': repo_dict['html_url'],
#     }
#     plot_dicts.append(plot_dict)
#
# my_style = LS('#333366', base_style=LCS)
#
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.title_font_size = 24
# my_config.lable_font_size = 14
# my_config.major_label_font_size = 18
# my_config.truncate_label = 15
# my_config.show_y_guides = False
# my_config.width = 1000
#
# chart = pygal.Bar(my_config, style=my_style)
# chart.title = 'Most-Starred Python Projects on GitHub'
# chart.x_labels = names
#
# chart.add('', plot_dicts) ## 这里，y轴的值改一下
# chart.render_to_file('python_repos_3.svg')
#
# print(plot_dicts)



# 17.3 Hacker News API
# http://hacker-news.firebaseio.com/v0/item/9884165.json

import requests
from operator import itemgetter

# 执行API调用并存储响应
url = 'http://hacker-news.firebaseio.com/v0/item/9884165.json'
r = requests.get(url)
print('Status code:', r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # 对于每篇文章，都执行一个API调用
    url = ('http://hacker-news.firebaseio.com/v0/item'+str(submission_id)+'.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title':response_dict['title'],
        'link':'http://news.ycombinator.com/item?id='
               + str(submission_id),
        'comments':response_dict.get('descendants',0)
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    print('\nTitle:', submission_dict['title'])
    print('Discussion link:', submission_dict['link'])
    print('Comments:', submission_dict['comments'])



