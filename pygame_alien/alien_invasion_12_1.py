import pygame

from settings_12_1 import Settings
from ship_12_1 import Ship
import game_function_12_1 as gf
from pygame.sprite import Group
def run_game():

    ai_settings = Settings()
    pygame.init()
    pygame.display.set_caption("Alien Invasion")

    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_heigh))

    ship = Ship(ai_settings,screen)

    bullets = Group()
    bullets_down = Group()
    bullets_left = Group()
    bullets_right = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets, bullets_down, bullets_left, bullets_right)
        # 每次循环，都调用ship的update
        ship.update()
        gf.update_bullets(ai_settings, bullets, bullets_down, bullets_left, bullets_right)
        gf.update_screen(ai_settings, screen, ship, bullets, bullets_down, bullets_left, bullets_right)

run_game()

