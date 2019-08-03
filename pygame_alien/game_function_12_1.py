import sys
import pygame
from bullet_12_1 import Bullet
from bullet_12_5 import BulletDown
from bullet_12_5_w import BulletLeft
from bullet_12_5_r import BulletRight

def check_keydown_events(event, ai_settings, screen, ship, bullets, bullets_down, bullets_left, bullets_right):
    """键下按"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_e:
        fire_bullet_down(ai_settings, screen, ship, bullets_down)
    elif event.key == pygame.K_w:
        fire_bullet_left(ai_settings, screen, ship, bullets_left)
    elif event.key == pygame.K_r:
        fire_bullet_right(ai_settings, screen, ship, bullets_right)



def check_keyup_events(event,ship):
    """按键抬起"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets, bullets_down, bullets_left, bullets_right):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, bullets_down,bullets_left, bullets_right)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets, bullets_down,
                  bullets_left, bullets_right):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in bullets_down.sprites():
        bullet.draw_bullet()
    for bullet in bullets_left.sprites():
        bullet.draw_bullet()
    for bullet in bullets_right.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings, bullets, bullets_down, bullets_left, bullets_right):
    """更新子弹的位置，并删除已经消失的子弹"""

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets)) 用于确认子弹确实消失了

    bullets_down.update()
    for bullet_down in bullets_down.copy():
        if bullet_down.rect.top >= ai_settings.screen_heigh:
            bullets_down.remove(bullet_down)
    # print(len(bullets_down))

    bullets_left.update()
    for bullet_left in bullets_left.copy():
        if bullet_left.rect.right <=0:
            bullets_left.remove(bullet_left)

    bullets_right.update()
    for bullet_right in bullets_right.copy():
        if bullet_right.rect.left >= ai_settings.screen_width:
            bullets_right.remove(bullet_right)

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没有达到到限制时，就发射子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def fire_bullet_down(ai_settings, screen, ship, bullets_down):
    """如果没有达到到限制时，就发射子弹"""
    if len(bullets_down) < ai_settings.bullets_allowed:
        new_bullet_down = BulletDown(ai_settings, screen, ship)
        bullets_down.add(new_bullet_down)

def fire_bullet_left(ai_settings, screen, ship, bullets_left):
    """如果没有达到到限制时，就发射子弹"""
    if len(bullets_left) < ai_settings.bullets_allowed:
        new_bullet_left = BulletLeft(ai_settings, screen, ship)
        bullets_left.add(new_bullet_left)

def fire_bullet_right(ai_settings, screen, ship, bullets_right):
    """如果没有达到到限制时，就发射子弹"""
    if len(bullets_right) < ai_settings.bullets_allowed:
        new_bullet_right = BulletRight(ai_settings, screen, ship)
        bullets_right.add(new_bullet_right)



