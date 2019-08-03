class Settings():
    """储存游戏所有设置"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置
        self.screen_width = 1500
        self.screen_heigh = 900
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limit = 2

        # 子弹设置
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 100

        # 外星人设置
        self.fleet_drop_speed = 10

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.2
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 2

        self.fleet_direction = 1

        # 记分
        self.alien_points = 10

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)



