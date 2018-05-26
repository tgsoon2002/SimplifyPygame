
import pygame
from globalData import *
import SpriteSheet


class BaseObject:
    colliderType = COLLIDERTYPE_RECT
    animated = False
    animationDuration = 0
    spriteSheet = []
    fps = 0

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

    def DrawSprite(self):

        if self.animated:
            pass
        else:
            currentRect = self.sprite.get_rect()
            correctX = self.x - (self.rect[2]/2) - \
                (currentRect[2] - self.rect[2])/2
            correctY = self.y - (self.rect[3]/2) - \
                (currentRect[3] - self.rect[3])/2
            if self.sprite:
                self.mainScreen.blit(self.sprite, (correctX, correctY))

    def Collision_Check(self, className):
        targets = FindObjects(className)
        result = []
        for obj in targets:
            if self.colliderType == COLLIDERTYPE_RECT and obj.colliderType == COLLIDERTYPE_RECT:
                if ColCheckRectToRect(self, obj):
                    result.append(obj)
            elif self.colliderType == COLLIDERTYPE_RECT and obj.colliderType == COLLIDERTYPE_CIRCLE:
                if ColCheckRectToCircle(self, obj):
                    pass
            elif self.colliderType == COLLIDERTYPE_CIRCLE and obj.colliderType == COLLIDERTYPE_RECT:
                if ColCheckRectToCircle(obj, self):
                    pass
        return result

    def SetSrpite(self, spriteName):
        ss = SpriteSheet.spritesheet('Sprite/'+spriteName)
        # self.basesprite = ss.image_at((5, 5, 30, 30))
        self.basesprite = ss.get_image()
        self.basesprite = pygame.transform.scale(self.basesprite, (self.rect))
        self.sprite = self.basesprite
        self.rect = self.sprite.get_rect()

    def MoveObjectBy(self, xdiff, ydiff):
        self.x += xdiff
        self.y += ydiff

    def MoveObjectTo(self, xdiff, ydiff):
        self.x = xdiff
        self.y = ydiff

    def RotateObject(self, angle):
        self.sprite = pygame.transform.rotate(self.basesprite, angle)
        # self.sprite = pygame.transform.scale(
        #     self.sprite, (self.rect[2], self.rect[3]))
        # print(angle)
        # print(self.sprite.get_rect())

    def SetAnimation(self, rects, fps, ):
        self.spriteSheet = rects
        self.fps = fps
        self.animationDuration = len(rects) * (1000/fps)
