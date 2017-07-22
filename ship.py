import pygame

class Ship():
    def __init__(self, setting, screen):
        self.screen = screen
        self.setting = setting

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.setting.ship_speed
        if self.move_left and self.rect.left > 0:
            self.center -= self.setting.ship_speed
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
