import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_right:
            self.rect.centerx += 10
        if self.move_left:
            self.rect.centerx -= 10

    def blitme(self):
        self.screen.blit(self.image, self.rect)
