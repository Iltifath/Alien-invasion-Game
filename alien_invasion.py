import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #This will initialize game and create a screen obbject.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    #This will make play button on the screen.
    play_button = Button(ai_settings, screen, "Play")

    #This will create an instance to store game statistics.
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)

    #To make a group to store bullets in.
    bullets = Group()
    aliens = Group()

    #This will create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #main loop for the game.
    while True:

        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen,stats, ship, aliens, bullets, play_button)
        
run_game()
