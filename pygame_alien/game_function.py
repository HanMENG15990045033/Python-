# # 12.5.1 退出这部分重写
# import sys
# import pygame
#
# def check_events():
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#
# # 12.5.2
#
# def update_screen(ai_settings,screen,ship):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重新绘制屏幕
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()
#
# # 12.6.1 相应按键 KEYDOWN
#
# import sys
# import pygame
#
# def check_events(ship): # 这里要加一个变量ship
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 # 向右移动飞船
#                 ship.rect.centerx += 1
#
# def update_screen(ai_settings, screen, ship):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重新绘制屏幕
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()
#
# # 12.6.2 相应按键 KEYDOWN
#
# import sys
# import pygame
#
# def check_events(ship):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = True
#
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = False
#
# def update_screen(ai_settings, screen, ship):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重新绘制屏幕
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()

# #12.6.3 相应按键 KEYDOWN
#
# import sys
# import pygame
#
# def check_events(ship):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = True
#             if event.key == pygame.K_LEFT:
#                 ship.moving_left = True
#
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = False
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left =False
#
# def update_screen(ai_settings, screen, ship):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重新绘制屏幕
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()

# # 12.6.6 重构check_events
#
# import sys
# import pygame
#
# def check_keydown_events(event,ship):
#     """键下按"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = True
#     if event.key == pygame.K_LEFT:
#         ship.moving_left = True
#
# def check_keyup_events(event,ship):
#     """按键抬起"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = False
#
#
# def check_events(ship):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         elif event.type == pygame.KEYDOWN:
#             check_keydown_events(event, ship)
#
#         elif event.type == pygame.KEYUP:
#             check_keyup_events(event, ship)
#
# def update_screen(ai_settings, screen, ship):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重新绘制屏幕
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()

# # 12.8.4 开火
#
# import sys
# import pygame
# from bullet import Bullet
#
# def check_keydown_events(event, ai_settings, screen, ship, bullets):
#     """键下按"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = True
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = True
#     elif event.key==pygame.K_SPACE:
#         #创建一个子弹，并将其加入到编组的bullets中
#         new_bullet = Bullet(ai_settings, screen, ship)
#         bullets.add(new_bullet)
#
#
# def check_keyup_events(event,ship):
#     """按键抬起"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = False
#
#
# def check_events(ai_settings, screen, ship, bullets):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         elif event.type == pygame.KEYDOWN:
#             check_keydown_events(event, ai_settings, screen, ship, bullets)
#
#         elif event.type == pygame.KEYUP:
#             check_keyup_events(event,ship)
#
# def update_screen(ai_settings, screen, ship, bullets):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重新绘制屏幕
#     screen.fill(ai_settings.bg_color)
#     # 重绘所有子弹
#     for bullet in bullets.sprites():
#         bullet.draw_bullet()
#
#     ship.blitme()
#
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()

# # 12.8.6 删除已经消失的子弹
#
# import sys
# import pygame
# from bullet import Bullet
#
# def check_keydown_events(event, ai_settings, screen, ship, bullets):
#     """键下按"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = True
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = True
#     elif event.key==pygame.K_SPACE:
#         #创建一个子弹，并将其加入到编组的bullets中
#         if len(bullets)<ai_settings.bullets_allowed:
#             new_bullet = Bullet(ai_settings,screen,ship)
#             bullets.add(new_bullet)
#
#
# def check_keyup_events(event,ship):
#     """按键抬起"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = False
#
#
# def check_events(ai_settings, screen, ship, bullets):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         elif event.type == pygame.KEYDOWN:
#             check_keydown_events(event, ai_settings, screen, ship, bullets)
#
#         elif event.type == pygame.KEYUP:
#             check_keyup_events(event,ship)
#
# def update_screen(ai_settings, screen, ship, bullets):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重新绘制屏幕
#     screen.fill(ai_settings.bg_color)
#     # 重绘所有子弹
#     for bullet in bullets.sprites():
#         bullet.draw_bullet()
#
#     ship.blitme()
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()
#
# def update_bullets(bullets):
#     """更新子弹的位置，并删除已经消失的子弹"""
#     # 更新子弹的位置
#     bullets.update()  ##这个子弹的跟新，子弹往前飞
#
#     ##删除已经消失的子弹
#     for bullet in bullets.copy():
#         if bullet.rect.bottom <= 0:
#             bullets.remove(bullet)
    # print(len(bullets)) 用于确认子弹确实消失了

# 12.8.8 fire_bullet 开火

import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """键下按"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key==pygame.K_SPACE:
        #创建一个子弹，并将其加入到编组的bullets中
        fire_bullet(ai_settings, screen, ship, bullets)



def check_keyup_events(event,ship):
    """按键抬起"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    # 更新子弹的位置
    bullets.update()  ##这个子弹的跟新，子弹往前飞

    ##删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets)) 用于确认子弹确实消失了

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没有达到到限制时，就发射子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


