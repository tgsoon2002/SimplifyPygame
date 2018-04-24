
import pygame


class BaseObject(pygame.sprite.Sprite):
    x = 0
    y = 0
    sprite = {}
    spriteRect = (100, 100)
    mainScreen = {}

    def __init__(self, screen, width=100, height=100):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.mainScreen = screen
        x = 0
        y = 0
        self.Start()

    def Start(self):
        pass

    def Update(self):
        pass
