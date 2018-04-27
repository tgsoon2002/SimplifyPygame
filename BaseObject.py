
import pygame
from globalData import *


class BaseObject:

    def __init__(self, screen, width=100, height=100):
        self.mainScreen = screen
        self.rect = (width, height)
        self.x = 0
        self.y = 0
        self.Start()

    def Start(self):
        pass

    def Update(self):
        pass

    def Collision_Check(self, target):
        if (self.rect[0] < target.rect[0] + target.rect[2] and
            self.rect[0] + self.rect[2] > target.rect[0] and
                self.rect[1] < target.rect[1] + target.rect[3] and
                self.rect[1] + self.rect[3] > target.rect[1]):
            print("collide")

    def SetSrpite(self, spriteName):
        self.basesprite = get_image('Sprite/'+spriteName)
        self.basesprite = pygame.transform.scale(self.basesprite, (self.rect))
        self.sprite = self.basesprite
        self.rect = self.sprite.get_rect()

    def RotatteObject(self, angle):
        self.sprite = pygame.transform.rotate(self.basesprite, angle)
        # self.sprite = pygame.transform.scale(
        #     self.sprite, (self.rect[2], self.rect[3]))
        print(self.rect)
