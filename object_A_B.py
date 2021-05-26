import pygame


class Object_A_B(pygame.sprite.Sprite):
    def __init__(self, color, name, X, Y):
        self.color = color
        self.name = name
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (X, Y)

    def get_poz(self):
        return self.rect

