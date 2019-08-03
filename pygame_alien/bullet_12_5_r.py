import pygame
from pygame.sprite import Sprite

class BulletRight(Sprite):
    """管理飞船发射子弹"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处位置创建一个子弹对象"""
        super(BulletRight, self).__init__()
        self.screen = screen

        # 在（0,0）处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_height, ai_settings.bullet_width)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

        # 储存用小数表示的子弹位置
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.x += self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.x = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
