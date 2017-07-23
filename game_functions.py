import sys
import pygame
from bullet import Bullet


def check_keydown_event(event, setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    if event.key == pygame.K_LEFT:
        ship.move_left = True
    if event.key == pygame.K_UP:
        ship.move_up = True
    if event.key == pygame.K_DOWN:
        ship.move_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(setting, screen, ship, bullets)


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    if event.key == pygame.K_LEFT:
        ship.move_left = False
    if event.key == pygame.K_UP:
        ship.move_up = False
    if event.key == pygame.K_DOWN:
        ship.move_down = False


def check_event(setting, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, setting, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(setting, screen, ship, bullets):
    screen.fill(setting.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(setting, screen, ship, bullets):
    if len(bullets) < setting.bullets_allowed:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)
