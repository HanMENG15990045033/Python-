# # 12.4.1 创建ship类
#
# import pygame
#
# class Ship():
#
#     def __init__(self, screen):
#         """初始化飞船并设置其初始位置"""
#         self.screen = screen
#
#         # 加载飞船图像并获取其他外接矩形
#         # self.image = pygame.image.load('images/ship.bmp')
#         self.image = pygame.image.load(r'D:\PYTHON练习\pygame_alien\ship_3.png')
#         self.rect = self.image.get_rect()
#         self.screen_rect = screen.get_rect()
#
#         # 将每艘新飞船放在屏幕底部中央
#         self.rect.centerx = self.screen_rect.centerx
#         self.rect.bottom = self.screen_rect.bottom
#
#     def blitme(self):
#         """在指定的位置绘制飞船"""
#         self.screen.blit(self.image, self.rect)

# # 12.6.2 KEYDOWN，KEYUP，movint_right
#
# import pygame
#
# class Ship():
#
#     def __init__(self,screen):
#         """初始化飞船并设置其初始位置"""
#         self.screen = screen
#
#         # self.image = pygame.image.load('images/ship.bmp')
#         self.image = pygame.image.load(r'D:\PYTHON练习\pygame_alien\ship_3.png')
#         self.rect = self.image.get_rect()
#         self.screen_rect = screen.get_rect()
#
#         self.rect.centerx = self.screen_rect.centerx
#         self.rect.bottom = self.screen_rect.bottom
#
#         # 移动标志
#         self.moving_right=False
#
#     def update(self): # 加一个函数
#         """根据移动标志调整飞船的位置"""
#         if self.moving_right:
#             self.rect.centerx += 1
#
#     def blitme(self):
#
#         self.screen.blit(self.image, self.rect)

# # 12.6.3 左右移动
#
# import pygame
#
# class Ship():
#
#     def __init__(self,screen):
#         """初始化飞船并设置其初始位置"""
#         self.screen = screen
#
#         # self.image = pygame.image.load('images/ship.bmp')
#         self.image = pygame.image.load(r'D:\PYTHON练习\pygame_alien\ship_3.png')
#         self.rect = self.image.get_rect()
#         self.screen_rect = screen.get_rect()
#
#         self.rect.centerx = self.screen_rect.centerx
#         self.rect.bottom = self.screen_rect.bottom
#
#         # 移动标志
#         self.moving_right=False
#         self.moving_left=False
#
#     def update(self): # 加一个函数
#         """根据移动标志调整飞船的位置"""
#         if self.moving_right:
#             self.rect.centerx += 1
#         if self.moving_left:
#             self.rect.centerx -= 1
#
#     def blitme(self):
#
#         self.screen.blit(self.image,self.rect)
#
# # 12.6.4设置速度
#
# import pygame
#
# class Ship():
#
#     def __init__(self, ai_settings, screen):
#         """初始化飞船并设置其初始位置"""
#         self.screen = screen
#         self.ai_settings = ai_settings
#
#         # self.image = pygame.image.load('images/ship.bmp')
#         self.image = pygame.image.load(r'D:\PYTHON练习\pygame_alien\ship_3.png')
#         self.rect = self.image.get_rect()
#         self.screen_rect = screen.get_rect()
#
#         self.rect.centerx = self.screen_rect.centerx
#         self.rect.bottom = self.screen_rect.bottom
#         # 在飞船的属性中存储小数值
#         self.center = float(self.rect.centerx)
#
#         # 移动标志
#         self.moving_right = False
#         self.moving_left = False
#
#     def update(self):  # 加一个函数
#         """根据移动标志调整飞船的位置"""
#         # 更新飞船的center值而不是rect
#         if self.moving_right:
#             self.center += self.ai_settings.ship_speed_factor
#         if self.moving_left:
#             self.center -= self.ai_settings.ship_speed_factor
#
#         # 根据self.centre更新rect对象
#         self.rect.centerx = self.center
#
#     def blitme(self):
#
#         self.screen.blit(self.image, self.rect)

# 12.6.5 限制移动范围
# #self.screen_rect.rigt，x轴最左边

import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.image.load(r'D:\PYTHON练习\pygame_alien\ship_3.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):  # 加一个函数
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.centre更新rect对象
        self.rect.centerx = self.center

    def blitme(self):

        self.screen.blit(self.image, self.rect)