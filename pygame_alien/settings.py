# # 12.3.3创建设置类
#
# class Settings():
#     """储存游戏所有设置"""
#
#     def __init__(self):
#         """初始化游戏的设置"""
#         # 屏幕设置
#         self.screen_width = 900
#         self.screen_heigh = 600
#         self.bg_color = (230, 230, 230)

# # 12.6.4调整飞船的速度
#
# class Settings():
#     """储存游戏所有设置"""
#
#     def __init__(self):
#         """初始化游戏的设置"""
#
#         self.screen_width = 900
#         self.screen_heigh = 600
#         self.bg_color = (230, 230, 230)
#
#         # 飞船的速度
#         self.ship_speed_factor = 1.5

# # 12.8.1 添加Bullet所需要的值
#
# class Settings():
#     """储存游戏所有设置"""
#
#     def __init__(self):
#         """初始化游戏的设置"""
#
#         self.screen_width = 900
#         self.screen_heigh = 600
#         self.bg_color = (230, 230, 230)
#         self.ship_speed_factor = 2
#
#         # 子弹设置
#         self.bullet_speed_factor = 1
#         self.bullet_width = 3
#         self.bullet_height = 15
#         self.bullet_color = 60, 60, 60

# 12.8.6 添加Bullet所需要的值

class Settings():
    """储存游戏所有设置"""

    def __init__(self):
        """初始化游戏的设置"""

        self.screen_width = 900
        self.screen_heigh = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor=2

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        ## 加一条
        self.bullets_allowed = 3
