import sys
import pygame


def check_event(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.move_right = True
            if event.key == pygame.K_LEFT:
                ship.move_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right = False
            if event.key == pygame.K_LEFT:
                ship.move_left = False


def update_screen(setting, screen, ship):
    screen.fill(setting.bg_color)
    ship.blitme()

    pygame.display.flip()
