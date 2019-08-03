import pygame

from settings_14 import Settings
from game_stats_14 import GameStats
from scoreboard_14 import Scoreboard
from button_14 import Button
from ship_14 import Ship
import game_function_14 as gf
from pygame.sprite import Group

def run_game():

    ai_settings = Settings()
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_heigh))

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建储存游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        # 每次循环，都调用ship的update
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()

