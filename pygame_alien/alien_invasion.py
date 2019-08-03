# # 12.1 游戏规划
# # 12.2 安装
# # 12.3.1 创建Pygame窗口，相应用户输入
# import sys
# import pygame
#
# def run_game():
#
#     pygame.init()
#     pygame.display.set_caption("Alien Invasion")
#     screen = pygame.display.set_mode((1200, 800))
#
#     while True:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         pygame.display.flip()
#
# run_game()
#
# #

# # 12.3.2 设置背景色
#
# import sys
# import pygame
#
# def run_game():
#     pygame.init()
#     screen = pygame.display.set_mode((1200, 800))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 设置背景色
#     bg_color = (230, 230, 230)
#
#     while True:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         # 每次循环时都重绘屏幕
#         screen.fill(bg_color)
#
#         pygame.display.flip()
#
# run_game()


# # 12.3.3创建设置类
#
# import sys
# import pygame
#
# from settings import Settings
#
# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width,
#          ai_settings.screen_heigh))
#
#     pygame.display.set_caption("Alien Invasion")
#
#
#     while True:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         # 每次循环时都重绘屏幕
#         screen.fill(ai_settings.bg_color)
#
#         pygame.display.flip()
#
# run_game()
#
# # 12.4 添加图像
# # 12.4.1 创建ship类
# # 12.4.2 在屏幕上绘制飞船
#
# import sys
# import pygame
#
# from settings import Settings
# # 导入ship类
# from ship import Ship
#
#
# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width,
#          ai_settings.screen_heigh))
#
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一艘飞船
#     ship = Ship(screen)
#
#     while True:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         screen.fill(ai_settings.bg_color)
#         ship.blitme()
#         # 先填充背景，后绘制飞船，确保飞船在前面
#
#         pygame.display.flip()
#
# run_game()

# # 12.5 重构，就是把while循环提出来
#
# # 12.5.1 新建game_funciton
# import pygame
#
# from settings import Settings
# from ship import Ship
# import game_function as gf
# # 导入game_funciton
#
#
# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width,
#          ai_settings.screen_heigh))
#
#     pygame.display.set_caption("Alien Invasion")
#
#
#     # 创建一艘飞船
#     ship = Ship(screen)
#
#     while True:
#
#         gf.check_events()
#
#         screen.fill(ai_settings.bg_color)
#         ship.blitme()
#         # 先填充背景，后绘制飞船，确保飞船在前面
#
#         pygame.display.flip()
#
# run_game()

# # 12.5.2 把while里更新屏幕的功能提出去
#
# import pygame
#
# from settings import Settings
# from ship import Ship
# import game_function as gf
# # 导入game_funciton
#
#
# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width,
#          ai_settings.screen_heigh))
#
#     pygame.display.set_caption("Alien Invasion")
#     bg_color = (230,230,230)
#
#     # 创建一艘飞船
#     ship = Ship(screen)
#
#     while True:
#
#         gf.check_events()
#         gf.update_screen(ai_settings,screen,ship)
#
# run_game()

# # 12.6.1 响应按键 game_function.py修改
# import pygame
#
# from settings import Settings
# from ship import Ship
# import game_function as gf
#
# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width,
#          ai_settings.screen_heigh))
#
#     pygame.display.set_caption("Alien Invasion")
#
#     ship = Ship(screen)
#
#     while True:
#         gf.check_events(ship) #添加变量ship
#         gf.update_screen(ai_settings, screen, ship)
#
# run_game()
#
# # 12.6.2 允许不断移动 改ship.py
# import pygame
#
# from settings import Settings
# from ship import Ship
# import game_function as gf
#
# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width,
#          ai_settings.screen_heigh))
#
#     pygame.display.set_caption("Alien Invasion")
#
#
#     ship = Ship(ai_settings, screen)
#
#     while True:
#         gf.check_events(ship)
#         # 每次循环，都调用ship的update
#         ship.update()
#         gf.update_screen(ai_settings,screen,ship)
#
# run_game()

## 此时运行，可以按住右键一直向右移动

#12.6.3 左右移动
## 改ship
## 改game_function,主代码不用改

# 12.6.4 调整飞船的速度
## 改settings
## 改ship
# ## 主文件加一个变量
# import pygame
#
# from settings import Settings
# from ship import Ship
# import game_function as gf
#
# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width,
#          ai_settings.screen_heigh))
#
#     pygame.display.set_caption("Alien Invasion")
#
#     ##这里加一个参数
#     ship = Ship(ai_settings,screen)
#
#     while True:
#         gf.check_events(ship)
#         # 每次循环，都调用ship的update
#         ship.update()
#         gf.update_screen(ai_settings,screen,ship)
#
# run_game()

# # 12.6.5 限制飞船的活动范围 改ship
# 12.6.6 重构check_events()


# 12.7 简单回顾总结，画个图吧，太蒙了

# 12.8.1 添加子弹设置
# #settings
# 12.8.2 创建子弹
# bullet.py 创建Bullet类
# 12.8.3 将子弹存储到编组中
#
# import pygame
#
# from settings import Settings
# from ship import Ship
# import game_function as gf
# from pygame.sprite import Group
#
# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width,
#          ai_settings.screen_heigh))
#
#     pygame.display.set_caption("Alien Invasion")
#
#     ship = Ship(ai_settings,screen)
#     bullets = Group()
#
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         # 每次循环，都调用ship的update
#         ship.update()
#         bullets.update()##这个子弹的跟新，子弹往前飞
#         gf.update_screen(ai_settings, screen, ship, bullets)
#
# run_game()
#
# # 还得改game_funciotns 才行

# # 12.8.5 删除已消失的子弹
#
# import pygame
#
# from settings import Settings
# from ship import Ship
# import game_function as gf
# from pygame.sprite import Group
#
# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width,
#          ai_settings.screen_heigh))
#
#     pygame.display.set_caption("Alien Invasion")
#     bg_color = (230,230,230)
#
#     ship = Ship(ai_settings,screen)
#
#     bullets = Group()
#
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         # 每次循环，都调用ship的update
#         ship.update()
#         bullets.update()##这个子弹的跟新，子弹往前飞
#
#         ##删除已经消失的子弹
#         for bullet in bullets.copy():
#             if bullet.rect.bottom<=0:
#                 bullets.remove(bullet)
#         # print(len(bullets)) #用于确认子弹确实消失了
#
#         gf.update_screen(ai_settings, screen, ship, bullets)
#
# run_game()

# 12.8.6 限制子弹数量
# settings
# game_function

# 12.8.7 创建函数

# 12.8.5 删除已消失的子弹
#
import pygame

from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group

def run_game():

    pygame.init()
    ai_settings = Settings()
    pygame.display.set_caption("Alien Invasion")

    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_heigh))

    ship = Ship(ai_settings,screen)

    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        # 每次循环，都调用ship的update
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()

# # 12.8.8 创建函数fire_bullet()
# # 改game_functions

