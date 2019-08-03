import pygame

from settings_13 import Settings
from game_stats_13 import GameStats
from ship_13 import Ship
import game_function_13 as gf
from pygame.sprite import Group

def run_game():

    ai_settings = Settings()
    pygame.init()
    pygame.display.set_caption("Alien Invasion")


    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_heigh))

    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        # 每次循环，都调用ship的update
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()

