class Settings():
    """储存游戏所有设置"""

    def __init__(self):
        """初始化游戏的设置"""

        # 飞船设置
        self.screen_width = 1456
        self.screen_heigh = 900
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 2
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        ## 加一条
        self.bullets_allowed=100

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        # 方向参数，1表示向右移动，-1表示向左移动
        self.fleet_direction = 1

