import sys
import pygame


def check_keydown_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    if event.key == pygame.K_LEFT:
        ship.move_left = True


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    if event.key == pygame.K_LEFT:
        ship.move_left = False


def check_event(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(setting, screen, ship):
    screen.fill(setting.bg_color)
    ship.blitme()

    pygame.display.flip()
