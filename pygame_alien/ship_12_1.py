import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.image.load(r'D:\PYTHON练习\pygame_alien\ship_3.png')
        # self.image = pygame.image.load(r'D:\PYTHON练习\pygame_alien\ship_1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # 在飞船的属性中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):  # 加一个函数
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        # 根据self.centre更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):

        self.screen.blit(self.image, self.rect)